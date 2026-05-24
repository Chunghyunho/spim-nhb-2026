"""V-Dem v16으로 E(제도탄성) 재측정 + 회귀 재실행"""
import pandas as pd, numpy as np, sys, os
sys.stdout.reconfigure(encoding='utf-8')

VDEM = r"C:\Users\21ckj\인토피아 Dropbox\1. 학문연구\2. 수강신청\1. 수업자료\3. 하반기_3교시 과학저널리즘특강3_과학적 사고와 이론화의 기초 + 현상을 개념으로 _김정남\4주차_과제제출\Is Path Integral and Rocket Model Fit for Social Change_\_papers\_data\VDem_extracted\V-Dem-CY-Full+Others-v16.csv"
OUT = r"C:\Users\21ckj\AppData\Local\Temp\social_pi"
PANEL = os.path.join(OUT, 'panel_data.csv')

print("Loading V-Dem (large file)...")
# E 변수 합성에 사용할 핵심 8개 + 식별 컬럼
E_VARS = ['v2x_polyarchy','v2x_libdem','v2x_jucon','v2xlg_legcon',
          'v2x_corr','v2xcl_rol','v2x_freexp_altinf','v2x_frassoc_thick']
cols = ['country_text_id','year'] + E_VARS
vdem = pd.read_csv(VDEM, usecols=cols, low_memory=False)
print(f"  rows={len(vdem)}, cols={len(vdem.columns)}")

# 우리 29국으로 필터
COUNTRIES = ['KOR','JPN','DEU','FRA','GBR','SWE','NOR','DNK',
             'USA','CAN','AUS','NLD','CHE','FIN','AUT','BEL',
             'RUS','VEN','SYR','EGY','TUN','LBY',
             'BRA','ARG','ZAF','TUR','MEX','IDN','IND','POL']
vdem = vdem[vdem['country_text_id'].isin(COUNTRIES) & vdem['year'].between(2000,2022)]
vdem = vdem.rename(columns={'country_text_id':'country'})
print(f"  filtered: {len(vdem)} obs, {vdem['country'].nunique()} countries")
print(f"  E vars coverage: ")
for v in E_VARS:
    print(f"    {v}: {vdem[v].notna().sum()}/{len(vdem)}")

# v2x_corr는 부패지수(높을수록 부패) → 역수
vdem['v2x_corr_inv'] = 1 - vdem['v2x_corr']

# 정규화 0-10
def norm(s):
    mn, mx = s.min(), s.max()
    if mx == mn: return pd.Series(5.0, index=s.index)
    return (s - mn)/(mx - mn)*10

E_USE = ['v2x_polyarchy','v2x_libdem','v2x_jucon','v2xlg_legcon',
         'v2x_corr_inv','v2xcl_rol','v2x_freexp_altinf','v2x_frassoc_thick']
for v in E_USE:
    vdem[f'E_{v}'] = norm(vdem[v])

vdem['E_vdem'] = vdem[[f'E_{v}' for v in E_USE]].mean(axis=1)
print(f"\nE_vdem: mean={vdem['E_vdem'].mean():.2f}, std={vdem['E_vdem'].std():.2f}, n={vdem['E_vdem'].notna().sum()}")

# 기존 패널과 병합 (E를 V-Dem 기반으로 교체)
panel = pd.read_csv(PANEL)
print(f"\nExisting panel: {len(panel)} obs")
merged = panel.merge(vdem[['country','year','E_vdem']], on=['country','year'], how='left')
merged['E_orig'] = merged['E']
merged['E'] = merged['E_vdem']
merged = merged.dropna(subset=['S','E','H','R_proxy'])
merged = merged[(merged[['S','E','H','R_proxy']] > 0).all(axis=1)]
print(f"After V-Dem merge: {len(merged)} obs ({merged['country'].nunique()} countries)")
print(merged[['S','E','H','R_proxy']].describe().round(3))

# 저장
out_path = os.path.join(OUT, 'panel_vdem.csv')
merged.to_csv(out_path, index=False)
print(f"\nSaved -> {out_path}")

# 회귀 재실행
import statsmodels.api as sm
import warnings; warnings.filterwarnings('ignore')
EPS = 0.1
merged['ln_R'] = np.log(merged['R_proxy'] + EPS)
merged['ln_S'] = np.log(merged['S'] + EPS)
merged['ln_E'] = np.log(merged['E'] + EPS)
merged['ln_H'] = np.log(merged['H'] + EPS)

print("\n=== OLS (V-Dem E) ===")
m = sm.OLS(merged['ln_R'], sm.add_constant(merged[['ln_S','ln_E','ln_H']])).fit(cov_type='HC3')
a, b, e = m.params['ln_S'], -m.params['ln_E'], -m.params['ln_H']
ci = m.conf_int()
print(f"  alpha = {a:.3f}  CI [{ci.loc['ln_S',0]:.3f}, {ci.loc['ln_S',1]:.3f}]")
print(f"  beta  = {b:.3f}  CI [{-ci.loc['ln_E',1]:.3f}, {-ci.loc['ln_E',0]:.3f}]")
print(f"  eta   = {e:.3f}  CI [{-ci.loc['ln_H',1]:.3f}, {-ci.loc['ln_H',0]:.3f}]")
print(f"  R2 = {m.rsquared:.3f}, N = {len(merged)}")

# FE
df2 = merged.copy()
for c in ['ln_R','ln_S','ln_E','ln_H']:
    df2[c+'_dm'] = df2[c] - df2.groupby('country')[c].transform('mean')
fe = sm.OLS(df2['ln_R_dm'], sm.add_constant(df2[['ln_S_dm','ln_E_dm','ln_H_dm']])).fit(cov_type='HC3')
print(f"\n=== FE (within) ===")
print(f"  alpha = {fe.params['ln_S_dm']:.3f}")
print(f"  beta  = {-fe.params['ln_E_dm']:.3f}")
print(f"  eta   = {-fe.params['ln_H_dm']:.3f}")
print(f"  R2 = {fe.rsquared:.3f}")
