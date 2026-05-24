"""100국 패널로 확장 — World Bank + V-Dem 전면 활용"""
import requests, pandas as pd, numpy as np, sys, os
import statsmodels.api as sm
import warnings; warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

OUT = r"C:\Users\21ckj\AppData\Local\Temp\social_pi"
VDEM = r"C:\Users\21ckj\인토피아 Dropbox\1. 학문연구\2. 수강신청\1. 수업자료\3. 하반기_3교시 과학저널리즘특강3_과학적 사고와 이론화의 기초 + 현상을 개념으로 _김정남\4주차_과제제출\Is Path Integral and Rocket Model Fit for Social Change_\_papers\_data\VDem_extracted\V-Dem-CY-Full+Others-v16.csv"

# 100국 선정 — 5개 권역 × 20개국, 다양한 체제 포함
COUNTRIES_100 = [
    # 서유럽·북미·오세아니아 안정 민주주의 (24)
    'USA','CAN','GBR','FRA','DEU','ITA','ESP','PRT','NLD','BEL','LUX','CHE','AUT',
    'SWE','NOR','DNK','FIN','ISL','IRL','GRC','AUS','NZL','JPN','KOR',
    # 중동부유럽 (12)
    'POL','CZE','SVK','HUN','ROU','BGR','HRV','SVN','EST','LVA','LTU','RUS',
    # 라틴아메리카 (15)
    'BRA','MEX','ARG','CHL','COL','PER','VEN','URY','ECU','BOL','PRY','GTM','CRI','PAN','DOM',
    # 중동·북아프리카 (12)
    'TUR','EGY','TUN','LBY','DZA','MAR','SAU','ARE','ISR','IRN','IRQ','JOR',
    # 사하라이남 아프리카 (15)
    'ZAF','NGA','KEN','ETH','GHA','SEN','CMR','UGA','TZA','MOZ','AGO','ZMB','RWA','CIV','MDG',
    # 동·동남아시아·남아시아 (16)
    'CHN','TWN','HKG','SGP','MYS','THA','PHL','IDN','VNM','IND','PAK','BGD','LKA','NPL','MMR','KHM',
    # 중앙아시아·코카서스 (6)
    'KAZ','UZB','UKR','BLR','GEO','ARM',
]
print(f"Total countries: {len(COUNTRIES_100)}")
YEARS = list(range(2000, 2023))

# === 1. 세계은행 데이터 수집 ===
INDICATORS = {
    'SI.POV.GINI':       'gini',
    'SL.UEM.TOTL.ZS':    'unemployment',
    'NY.GDP.PCAP.KD.ZG': 'gdp_growth',
    'SE.XPD.TOTL.GD.ZS': 'edu_spending',
    'SH.XPD.CHEX.GD.ZS': 'health_spending',
    'SP.DYN.LE00.IN':    'life_expectancy',
    'SP.DYN.TFRT.IN':    'tfr',
}

def fetch_wb(indicator, countries):
    url = (f"https://api.worldbank.org/v2/country/{';'.join(countries)}"
           f"/indicator/{indicator}?date={min(YEARS)}:{max(YEARS)}&format=json&per_page=10000")
    try:
        data = requests.get(url, timeout=60).json()
        if len(data) < 2 or data[1] is None: return pd.DataFrame()
        return pd.DataFrame([{'country': i['countryiso3code'], 'year': int(i['date']), 'value': float(i['value'])}
                             for i in data[1] if i.get('value') is not None])
    except Exception as e:
        print(f"  ERR: {e}"); return pd.DataFrame()

print("\nWorld Bank fetch...")
raw = {}
for code, name in INDICATORS.items():
    df = fetch_wb(code, COUNTRIES_100)
    if not df.empty:
        raw[name] = df.rename(columns={'value': name})
        print(f"  {name}: {len(df)}")

idx = pd.MultiIndex.from_product([COUNTRIES_100, YEARS], names=['country','year'])
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

# S = 지니·실업·GDP역성장
s_parts = [('gini',0.4,False),('unemployment',0.35,False),('gdp_growth',0.25,True)]
panel['S'] = sum(norm(panel[c], inv=inv)*w for c,w,inv in s_parts if c in panel.columns)
# H = 교육+보건+기대수명+합계출산율(역)
h_parts = [('life_expectancy',False),('edu_spending',False),('tfr',True)]
panel['H'] = pd.concat([norm(panel[c],inv=inv) for c,inv in h_parts if c in panel.columns], axis=1).mean(axis=1)

# === 2. V-Dem E 변수 + R 변수 (v2x_civlib) ===
print("\nV-Dem load...")
E_VARS = ['v2x_polyarchy','v2x_libdem','v2x_jucon','v2xlg_legcon','v2x_corr','v2xcl_rol','v2x_freexp_altinf','v2x_frassoc_thick']
R_VAR = 'v2x_civlib'
cols = ['country_text_id','year'] + E_VARS + [R_VAR]
vdem = pd.read_csv(VDEM, usecols=cols, low_memory=False)
vdem = vdem.rename(columns={'country_text_id':'country'})
vdem = vdem[vdem['country'].isin(COUNTRIES_100) & vdem['year'].between(2000,2022)]

vdem['v2x_corr_inv'] = 1 - vdem['v2x_corr']
E_USE = ['v2x_polyarchy','v2x_libdem','v2x_jucon','v2xlg_legcon','v2x_corr_inv','v2xcl_rol','v2x_freexp_altinf','v2x_frassoc_thick']
for v in E_USE:
    vdem[f'E_{v}'] = norm(vdem[v])
vdem['E'] = vdem[[f'E_{v}' for v in E_USE]].mean(axis=1)
vdem['R'] = norm(vdem[R_VAR], inv=True)  # civil liberties → repression

merged = panel.merge(vdem[['country','year','E','R']], on=['country','year'], how='left')
final = merged[['country','year','S','E','H','R']].dropna()
final = final[(final[['S','E','H','R']] > 0).all(axis=1)]
print(f"\n=== Final panel: {len(final)} obs, {final['country'].nunique()} countries ===")
print(final[['S','E','H','R']].describe().round(3))

final.to_csv(os.path.join(OUT,'panel_100.csv'), index=False)

# === 3. 회귀 ===
EPS = 0.1
for c in ['R','S','E','H']:
    final[f'ln_{c}'] = np.log(final[c] + EPS)

print("\n=== OLS (100국, V-Dem E, v2x_civlib R) ===")
m = sm.OLS(final['ln_R'], sm.add_constant(final[['ln_S','ln_E','ln_H']])).fit(cov_type='HC3')
ci = m.conf_int()
print(f"  alpha = {m.params['ln_S']:>+7.3f}  CI [{ci.loc['ln_S',0]:+.3f}, {ci.loc['ln_S',1]:+.3f}]")
print(f"  beta  = {-m.params['ln_E']:>+7.3f}  CI [{-ci.loc['ln_E',1]:+.3f}, {-ci.loc['ln_E',0]:+.3f}]")
print(f"  eta   = {-m.params['ln_H']:>+7.3f}  CI [{-ci.loc['ln_H',1]:+.3f}, {-ci.loc['ln_H',0]:+.3f}]")
print(f"  R2 = {m.rsquared:.3f}, N = {len(final)}, K = {final['country'].nunique()}")

print("\n=== Panel FE ===")
df2 = final.copy()
for c in ['ln_R','ln_S','ln_E','ln_H']:
    df2[c+'_dm'] = df2[c] - df2.groupby('country')[c].transform('mean')
fe = sm.OLS(df2['ln_R_dm'], sm.add_constant(df2[['ln_S_dm','ln_E_dm','ln_H_dm']])).fit(cov_type='HC3')
print(f"  alpha = {fe.params['ln_S_dm']:>+7.3f}")
print(f"  beta  = {-fe.params['ln_E_dm']:>+7.3f}")
print(f"  eta   = {-fe.params['ln_H_dm']:>+7.3f}")
print(f"  R2 (within) = {fe.rsquared:.3f}")

# Bootstrap
np.random.seed(42)
boots = {'a':[],'b':[],'e':[]}
for _ in range(1000):
    idx = np.random.choice(len(final), len(final), replace=True)
    db = final.iloc[idx]
    try:
        mb = sm.OLS(db['ln_R'], sm.add_constant(db[['ln_S','ln_E','ln_H']])).fit()
        boots['a'].append(mb.params['ln_S'])
        boots['b'].append(-mb.params['ln_E'])
        boots['e'].append(-mb.params['ln_H'])
    except: pass
print(f"\n=== Bootstrap N=1000 ===")
for k,v in [('alpha','a'),('beta','b'),('eta','e')]:
    arr = np.array(boots[v])
    print(f"  {k}: mean={np.mean(arr):+.3f}, 95% CI [{np.percentile(arr,2.5):+.3f}, {np.percentile(arr,97.5):+.3f}]")
