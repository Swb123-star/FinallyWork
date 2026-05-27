"""
图5: 多重压力因子对温室气体浓度的影响

本脚本复现原始研究中的Figure 5，展示：
- (a) DIN与pCO2的关系(对数转换)
- (b) DIN与pCH4的关系(对数转换)
- (c) 温度与pCO2的关系
- (d) 温度与pCH4的关系
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
print(f"数据加载成功: {dat.shape[0]} 个站点")

# 设置绘图风格
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# 创建子图
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 图5a: DIN vs pCO2
ax = axes[0, 0]
x = np.log(dat['din'])
y = np.log(dat['pCO2'])
ax.scatter(x, y, c='#3498db', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
slope, intercept, r, p, _ = stats.linregress(x, y)
x_range = np.linspace(x.min(), x.max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'blue', linewidth=2)
p_text = 'p < 0.001' if p < 0.001 else f'p = {p:.3f}'
ax.text(0.05, 0.95, f'r = {r:.2f}\n{p_text}', transform=ax.transAxes,
        fontsize=11, fontweight='bold', verticalalignment='top')
ax.set_xlabel('log(DIN) (mg L$^{-1}$)', fontsize=11)
ax.set_ylabel('log(pCO$_2$)', fontsize=11)
ax.set_title('(a) DIN vs pCO$_2$', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 图5b: DIN vs pCH4
ax = axes[0, 1]
x = np.log(dat['din'])
y = np.log(dat['pCH4'])
ax.scatter(x, y, c='#27ae60', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
slope, intercept, r, p, _ = stats.linregress(x, y)
x_range = np.linspace(x.min(), x.max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'green', linewidth=2)
p_text = 'p < 0.01' if p < 0.01 else f'p = {p:.3f}'
ax.text(0.05, 0.95, f'r = {r:.2f}\n{p_text}', transform=ax.transAxes,
        fontsize=11, fontweight='bold', verticalalignment='top')
ax.set_xlabel('log(DIN) (mg L$^{-1}$)', fontsize=11)
ax.set_ylabel('log(pCH$_4$)', fontsize=11)
ax.set_title('(b) DIN vs pCH$_4$', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 图5c: 温度 vs pCO2
ax = axes[1, 0]
x = dat['tmean']
y = np.log(dat['pCO2'])
ax.scatter(x, y, c='#e74c3c', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
slope, intercept, r, p, _ = stats.linregress(x, y)
x_range = np.linspace(x.min(), x.max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'red', linewidth=2)
ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes,
        fontsize=11, fontweight='bold', verticalalignment='top')
ax.set_xlabel('Water temperature (°C)', fontsize=11)
ax.set_ylabel('log(pCO$_2$)', fontsize=11)
ax.set_title('(c) Temperature vs pCO$_2$', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 图5d: 温度 vs pCH4
ax = axes[1, 1]
x = dat['tmean']
y = np.log(dat['pCH4'])
ax.scatter(x, y, c='#f39c12', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
slope, intercept, r, p, _ = stats.linregress(x, y)
x_range = np.linspace(x.min(), x.max(), 100)
ax.plot(x_range, intercept + slope * x_range, 'orange', linewidth=2)
p_text = 'p < 0.001' if p < 0.001 else f'p = {p:.3f}'
ax.text(0.05, 0.95, f'r = {r:.2f}\n{p_text}', transform=ax.transAxes,
        fontsize=11, fontweight='bold', verticalalignment='top')
ax.set_xlabel('Water temperature (°C)', fontsize=11)
ax.set_ylabel('log(pCH$_4$)', fontsize=11)
ax.set_title('(d) Temperature vs pCH$_4$', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 总标题
plt.suptitle('Effects of multiple stressors on GHG concentrations',
             fontsize=14, fontweight='bold', y=1.02)

# 保存图表
output_path = os.path.join(output_dir, 'fig5_stressors_vs_ghg.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图5已保存: {output_path}")

print("\n📊 统计结果:")
r, p = stats.pearsonr(np.log(dat['din']), np.log(dat['pCO2']))
print(f"  DIN vs pCO2:  r = {r:.4f}, p = {p:.4e}")
r, p = stats.pearsonr(np.log(dat['din']), np.log(dat['pCH4']))
print(f"  DIN vs pCH4:  r = {r:.4f}, p = {p:.4e}")
r, p = stats.pearsonr(dat['tmean'], np.log(dat['pCO2']))
print(f"  Temp vs pCO2: r = {r:.4f}, p = {p:.4e}")
r, p = stats.pearsonr(dat['tmean'], np.log(dat['pCH4']))
print(f"  Temp vs pCH4: r = {r:.4f}, p = {p:.4e}")

print("\n📊 图表说明:")
print("  - (a)(b) 显示氮输入与温室气体的关系（对数坐标轴）")
print("  - (c)(d) 显示温度与温室气体的关系")
print("  - DIN和温度对pCH4的影响大于对pCO2的影响")
