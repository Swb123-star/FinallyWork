"""
图4: 生态系统代谢、溶解氧与温室气体通量的关系

本脚本复现原始研究中的Figure 4，展示：
- (a) GPP与ER的关系(包含1:1线)
- (b) NEP与溶解氧(DO)的关系
- (c) pCO2与CO2通量的关系
- (d) pCH4与CH4通量的关系
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# 设置路径
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '..', 'data', 'dat.txt')
output_dir = os.path.join(base_dir, '..', 'reproduced_figures')
os.makedirs(output_dir, exist_ok=True)

# 加载数据
print("加载数据...")
dat = pd.read_csv(data_path, sep='\t')
dat['NEP'] = dat['GPP.mle'] + dat['ER.mle']
print(f"数据加载成功: {dat.shape[0]} 个站点")

# 设置绘图风格
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(12, 11))

# 图4a: GPP vs ER
ax = axes[0, 0]
x = dat['GPP.mle']
y = -dat['ER.mle']
ax.scatter(x, y, c='#e74c3c', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
slope, intercept, r, p, _ = stats.linregress(x, y)
x_range = np.linspace(x.min(), x.max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'red', linewidth=2)
ax.plot([0, x.max()], [0, x.max()], 'black', '--', linewidth=1, alpha=0.5, label='1:1 line')
ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes,
        fontsize=12, fontweight='bold', verticalalignment='top')
ax.set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_ylabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_title('(a) GPP vs ER', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, linestyle='--')

# 图4b: NEP vs DO
ax = axes[0, 1]
ax.scatter(dat['NEP'], dat['DOmean'], c='#3498db', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
ax.set_xlabel(r'NEP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_ylabel(r'Dissolved oxygen (mg L$^{-1}$)', fontsize=11)
ax.set_title('(b) NEP vs Dissolved Oxygen', fontsize=12, fontweight='bold')
ax.axvline(0, color='gray', linestyle='--', linewidth=1)
ax.grid(True, alpha=0.3, linestyle='--')

# 图4c: pCO2 vs FCO2
ax = axes[1, 0]
colors = ['#3498db' if val >= 0 else '#f39c12' for val in dat['FCO2.h']]
ax.scatter(dat['pCO2'], dat['FCO2.h'], c=colors, alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
ax.axhline(0, color='black', linestyle='--', linewidth=1)
slope, intercept, r, p, _ = stats.linregress(dat['pCO2'], dat['FCO2.h'])
x_range = np.linspace(dat['pCO2'].min(), dat['pCO2'].max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'blue', linewidth=2)
ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes,
        fontsize=12, fontweight='bold', verticalalignment='top')
ax.set_xlabel(r'pCO$_2$ ($\mu$atm)', fontsize=11)
ax.set_ylabel(r'CO$_2$ flux (mmol m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_title('(c) pCO$_2$ vs CO$_2$ Flux', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 图4d: pCH4 vs FCH4
ax = axes[1, 1]
ax.scatter(dat['pCH4'], dat['FCH4.h'], c='#27ae60', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
slope, intercept, r, p, _ = stats.linregress(dat['pCH4'], dat['FCH4.h'])
x_range = np.linspace(dat['pCH4'].min(), dat['pCH4'].max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'green', linewidth=2)
ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes,
        fontsize=12, fontweight='bold', verticalalignment='top')
ax.set_xlabel(r'pCH$_4$ ($\mu$atm)', fontsize=11)
ax.set_ylabel(r'CH$_4$ flux (mmol m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_title('(d) pCH$_4$ vs CH$_4$ Flux', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 总标题
plt.suptitle('Relationships between metabolism, DO, and GHG fluxes',
             fontsize=14, fontweight='bold', y=1.02)

# 保存图表
output_path = os.path.join(output_dir, 'fig4_rel_metabolism_ghg.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图4已保存: {output_path}")

print("\n📊 图表说明:")
print("  (a) GPP vs ER: 红色点表示生态系统代谢，1:1线表示收支平衡")
print("  (b) NEP vs DO: 蓝色点显示净生产力与溶解氧的关系")
print("  (c) pCO2 vs FCO2: 蓝色表示CO2释放，橙色表示吸收，黑色线表示0通量")
print("  (d) pCH4 vs FCH4: 绿色点表示甲烷浓度与通量的关系")
