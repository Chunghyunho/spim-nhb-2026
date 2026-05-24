"""사회 경로적분 모델 - 완전 패널 구성 (WGI 없이)"""
import requests, pandas as pd, numpy as np, os

OUT = r"C:\Users\21ckj\AppData\Local\Temp\social_pi"
os.makedirs(OUT, exist_ok=True)

COUNTRIES = [
    'KOR','JPN','DEU','FRA','GBR','SWE','NOR','DNK',
    'USA','CAN','AUS','NLD','CHE','FIN','AUT','BEL',
    'RUS','VEN','SYR','EGY','TUN','LBY',
    'BRA','ARG','ZAF','TUR','MEX','IDN','IND','POL',
]
YEARS = list(range(2000, 2023))

INDICATORS = {
    'SI.POV.GINI':       'gini',
    'SL.UEM.TOTL.ZS':    'unemployment',
    'NY.GDP.PCAP.KD.ZG': 'gdp_growth',
    'SE.XPD.TOTL.GD.ZS': 'edu_spending',
    'SH.XPD.CHEX.GD.ZS': 'health_spending',
    'SP.DYN.LE00.IN':    'life_expectancy',
    'VC.IHR.PSRC.P5':    'homicide_rate',
    'SP.DYN.TFRT.IN':    'tfr',           # 합계출산율 (H 보강)
    'NY.GDP.PCAP.PP.KD': 'gdp_per_capita',# 1인당 GDP PPP (E 보강)
}

def fetch_wb(indicator):
    url = (f"https://api.worldbank.org/v2/country/{';'.join(COUNTRIES)}"
           f"/indicator/{indicator}?date={min(YEARS)}:{max(YEARS)}&format=json&per_page=10000")
    try:
        data = requests.get(url, timeout=30).json()
        if len(data) < 2 or data[1] is None: return pd.DataFrame()
        return pd.DataFrame([{'country': i['countryiso3code'], 'year': int(i['date']), 'value': float(i['value'])}
                             for i in data[1] if i.get('value') is not None])
    except: return pd.DataFrame()

print("데이터 수집...")
raw = {}
for code, name in INDICATORS.items():
    df = fetch_wb(code)
    if not df.empty:
        raw[name] = df.rename(columns={'value': name})
        print(f"  OK: {name} ({len(df)}건)")
    else:
        print(f"  SKIP: {name}")

# 전체 패널 구성
idx = pd.MultiIndex.from_product([COUNTRIES, YEARS], names=['country','year'])
panel = pd.DataFrame(index=idx).reset_index()
for name, df in raw.items():
    panel = panel.merge(df[['country','year',name]], on=['country','year'], how='left')

# 보간
for col in [c for c in panel.columns if c not in ['country','year']]:
    panel[col] = panel.groupby('country')[col].transform(
        lambda x: x.interpolate(method='linear', limit_direction='both'))

def norm(s, inv=False):
    mn, mx = s.min(), s.max()
    if mx == mn: return pd.Series(5.0, index=s.index)
    r = (s - mn)/(mx - mn)*10
    return 10 - r if inv else r

# S: 지니 + 실업 + GDP역성장
s_parts = []
if 'gini' in panel.columns:        s_parts.append(('gini', 0.4, False))
if 'unemployment' in panel.columns: s_parts.append(('unemployment', 0.35, False))
if 'gdp_growth' in panel.columns:   s_parts.append(('gdp_growth', 0.25, True))
if s_parts:
    total_w = sum(w for _,w,_ in s_parts)
    panel['S'] = sum(norm(panel[c], inv=inv) * w/total_w for c,w,inv in s_parts)
else:
    panel['S'] = 5.0

# E: 교육지출 + 보건지출 + 1인당GDP (WGI 대체)
e_parts = [c for c in ['edu_spending','health_spending','gdp_per_capita'] if c in panel.columns]
if e_parts:
    panel['E'] = pd.concat([norm(panel[c]) for c in e_parts], axis=1).mean(axis=1)
    print(f"E (WGI 대체): 평균={panel['E'].mean():.2f} 표준편차={panel['E'].std():.2f}")
else:
    panel['E'] = 5.0

# H: 기대수명 + 교육지출 + 합계출산율(역)
h_parts = [(c, inv) for c, inv in [('life_expectancy',False),('edu_spending',False),('tfr',True)]
           if c in panel.columns]
if h_parts:
    panel['H'] = pd.concat([norm(panel[c], inv=inv) for c,inv in h_parts], axis=1).mean(axis=1)
else:
    panel['H'] = 5.0

# R_proxy: 살인율
if 'homicide_rate' in panel.columns:
    panel['R_proxy'] = norm(panel['homicide_rate'])
else:
    panel['R_proxy'] = 5.0

out = panel[['country','year','S','E','H','R_proxy']].dropna()
out = out[(out[['S','E','H','R_proxy']] > 0).all(axis=1)]
path = os.path.join(OUT, 'panel_data.csv')
out.to_csv(path, index=False)
print(f"\nOK: {len(out)} obs ({out['country'].nunique()} countries) -> {path}")
print(out[['S','E','H','R_proxy']].describe().round(3))
