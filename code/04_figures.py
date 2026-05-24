"""NHB Perspective Figure 1·2 생성"""
import pandas as pd, numpy as np, sys, os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
sys.stdout.reconfigure(encoding='utf-8')

OUT = r"C:\Users\21ckj\AppData\Local\Temp\social_pi"
FIG_DIR = r"C:\Users\21ckj\인토피아 Dropbox\1. 학문연구\2. 수강신청\1. 수업자료\3. 하반기_3교시 과학저널리즘특강3_과학적 사고와 이론화의 기초 + 현상을 개념으로 _김정남\4주차_과제제출\Is Path Integral and Rocket Model Fit for Social Change_\_research_notes\figures"
os.makedirs(FIG_DIR, exist_ok=True)

df = pd.read_csv(os.path.join(OUT, 'panel_100.csv'))
print(f"Loaded: {len(df)} obs, {df['country'].nunique()} countries")

# NHB 스타일 설정
plt.rcParams.update({
    'font.family': 'serif',
    'font.size': 9,
    'axes.linewidth': 0.8,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.dpi': 100,
    'savefig.dpi': 300,
})

# =====================================================================
# Figure 1: Three-panel — β·α·η scatter with fitted line
# =====================================================================
EPS = 0.1
for c in ['R','S','E','H']:
    df[f'ln_{c}'] = np.log(df[c] + EPS)

import statsmodels.api as sm
m = sm.OLS(df['ln_R'], sm.add_constant(df[['ln_S','ln_E','ln_H']])).fit()

# Partial residual plots
def partial_residual(target, others):
    """ln_R에서 others 효과를 제거한 후 target 효과"""
    X_others = sm.add_constant(df[others])
    res_R = sm.OLS(df['ln_R'], X_others).fit().resid
    res_T = sm.OLS(df[target], X_others).fit().resid
    return res_T.values, res_R.values

fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))

panels = [
    ('ln_S', ['ln_E','ln_H'], 'Social stress (log S)', f'α = {m.params["ln_S"]:+.2f}', '#c4451c'),
    ('ln_E', ['ln_S','ln_H'], 'Institutional elasticity (log E)', f'-β = {m.params["ln_E"]:+.2f}', '#1a73a8'),
    ('ln_H', ['ln_S','ln_E'], 'Future expectation (log H)', f'-η = {m.params["ln_H"]:+.2f}', '#5b8c5a'),
]

for ax, (tgt, oth, xlabel, coef_label, color) in zip(axes, panels):
    x, y = partial_residual(tgt, oth)
    ax.scatter(x, y, s=6, alpha=0.18, color=color, edgecolors='none')
    # Fitted line
    coef = np.polyfit(x, y, 1)
    xs = np.linspace(x.min(), x.max(), 100)
    ax.plot(xs, np.polyval(coef, xs), color='black', lw=1.5, alpha=0.85)
    ax.set_xlabel(f'{xlabel}\n(partial residual)', fontsize=9)
    ax.set_ylabel('Civil liberties repression (log R)\n(partial residual)' if ax is axes[0] else '', fontsize=9)
    ax.text(0.03, 0.97, coef_label, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.9))
    ax.grid(alpha=0.2, linewidth=0.5)

plt.suptitle('Figure 1. Path-weighted determinants of civil liberties repression across 93 countries (2000–2022, N = 2,136)',
             fontsize=10, y=1.02, fontweight='bold')
plt.tight_layout()
fig1_path = os.path.join(FIG_DIR, 'Figure_1_three_coefficients.png')
plt.savefig(fig1_path, bbox_inches='tight', facecolor='white')
plt.close()
print(f"OK Figure 1 -> {fig1_path}")

# =====================================================================
# Figure 2: Korea time series 1990-2024 (이미 보유 데이터)
# =====================================================================
kor = df[df['country']=='KOR'].sort_values('year').copy()
print(f"Korea years: {kor['year'].min()}~{kor['year'].max()}, n={len(kor)}")

fig, ax = plt.subplots(figsize=(9, 4.5))
ax2 = ax.twinx()

# 4 변수 정규화 시계열
colors = {'S':'#c4451c', 'E':'#1a73a8', 'H':'#5b8c5a', 'R':'#7b2c8c'}
labels = {'S':'Social stress (S)', 'E':'Institutional elasticity (E)',
          'H':'Future expectation (H)', 'R':'Civil liberties repression (R)'}

for var in ['S','E','H']:
    ax.plot(kor['year'], kor[var], marker='o', ms=3.5, lw=1.5,
            label=labels[var], color=colors[var])

ax2.plot(kor['year'], kor['R'], marker='s', ms=4, lw=2,
         label=labels['R'], color=colors['R'], linestyle='--')

# 주요 사건 annotations
events = [
    (2008, 'Global financial crisis'),
    (2017, 'Presidential impeachment'),
    (2020, 'COVID-19 + fertility collapse'),
]
for yr, txt in events:
    if kor['year'].min() <= yr <= kor['year'].max():
        ax.axvline(yr, color='gray', linestyle=':', alpha=0.5, lw=0.8)
        ax.text(yr, 9.8, txt, rotation=90, va='top', ha='right',
                fontsize=7, color='gray', alpha=0.8)

ax.set_xlabel('Year', fontsize=10)
ax.set_ylabel('S, E, H (normalized 0–10)', fontsize=10)
ax2.set_ylabel('R: Civil liberties repression (0–10)', fontsize=10, color=colors['R'])
ax2.tick_params(axis='y', labelcolor=colors['R'])
ax.set_ylim(0, 10)
ax2.set_ylim(0, 10)

lines1, labs1 = ax.get_legend_handles_labels()
lines2, labs2 = ax2.get_legend_handles_labels()
ax.legend(lines1+lines2, labs1+labs2, loc='lower left', frameon=True, framealpha=0.9, fontsize=8)

ax.set_title('Figure 2. South Korea state-space trajectory, 2000–2022',
             fontsize=11, fontweight='bold', pad=10)
ax.grid(alpha=0.2)

plt.tight_layout()
fig2_path = os.path.join(FIG_DIR, 'Figure_2_Korea_trajectory.png')
plt.savefig(fig2_path, bbox_inches='tight', facecolor='white')
plt.close()
print(f"OK Figure 2 -> {fig2_path}")

# =====================================================================
# Figure 3: Coefficients comparison (현재 결과 vs 기존 통념)
# =====================================================================
fig, ax = plt.subplots(figsize=(7, 4))

coefs = ['α (Social stress)', 'β (Institutional resilience)', 'η (Future expectation)']
our_vals = [0.631, 1.665, 0.732]
our_lo = [0.529, 1.593, 0.657]
our_hi = [0.732, 1.736, 0.808]

# 기존 SDT 통념 (Turchin류): α만 큰 효과, β·η 무시
sdt_vals = [2.0, 0.3, 0.2]  # 예시 (Turchin 류 가정 효과 크기)

x = np.arange(len(coefs))
width = 0.35

# Our results with CI
ax.bar(x - width/2, our_vals, width,
       yerr=[np.array(our_vals)-np.array(our_lo), np.array(our_hi)-np.array(our_vals)],
       capsize=4, color='#1a73a8', edgecolor='black', linewidth=0.8,
       label='Our path-weighted estimate (93 countries, 2000–2022)')
ax.bar(x + width/2, sdt_vals, width, color='#c4451c', alpha=0.6, edgecolor='black',
       linewidth=0.8, hatch='//',
       label='SDT-implied dominance (stylized)')

ax.axhline(0, color='black', lw=0.6)
ax.set_xticks(x)
ax.set_xticklabels(coefs, fontsize=9)
ax.set_ylabel('Coefficient magnitude', fontsize=10)
ax.set_title('Figure 3. β-dominance: institutional resilience exceeds stress sensitivity by 2.6×',
             fontsize=10, fontweight='bold', pad=10)
ax.legend(loc='upper right', fontsize=8, frameon=True, framealpha=0.95)
ax.grid(axis='y', alpha=0.2)

plt.tight_layout()
fig3_path = os.path.join(FIG_DIR, 'Figure_3_beta_dominance.png')
plt.savefig(fig3_path, bbox_inches='tight', facecolor='white')
plt.close()
print(f"OK Figure 3 -> {fig3_path}")

print(f"\n3 figures saved in: {FIG_DIR}")
