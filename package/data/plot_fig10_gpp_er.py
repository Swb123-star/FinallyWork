"""
图10: GPP与ER的代谢平衡(1:1线)

本脚本详细展示河流生态系统中总初级生产力(GPP)与生态系统呼吸(ER)的关系。
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

# 创建图表
fig, ax = plt.subplots(figsize=(8, 7))

# 绘制散点图
x = dat['GPP.mle']
y = -dat['ER.mle']
ax.scatter(x, y, c='#e74c3c', alpha=0.7, s=80, edgecolors='black', linewidth=0.5)

# 计算统计
slope, intercept, r, p, _ = stats.linregress(x, y)

# 绘制回归线
x_range = np.linspace(0, max(x.max(), y.max()), 100)
ax.plot(x_range, intercept + slope * x_range, 'blue', linewidth=2,
        label=f'Regression (r = {r:.2f})')

# 绘制1:1线
max_val = max(x.max(), y.max())
ax.plot([0, max_val], [0, max_val], 'black', '--', linewidth=2,
        label='1:1 line', alpha=0.7)

# 计算在1:1线上方/下方的点数量
above = sum(y > x)
below = sum(y < x)
equal = sum(y == x)

# 添加文本说明
p_text = 'p < 0.001' if p < 0.001 else f'p = {p:.3f}'
ax.text(0.05, 0.95, f'r = {r:.2f}\n{p_text}\n\nER > GPP: {above} sites\nER < GPP: {below} sites',
          transform=ax.transAxes,
          fontsize=11, verticalalignment='top',
          bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 设置标签和标题
ax.set_xlabel(r'Gross Primary Production (mmol C m$^{-2}$ d$^{-1}$)', fontsize=12)
ax.set_ylabel(r'Ecosystem Respiration (mmol C m$^{-2}$ d$^{-1}$)', fontsize=12)
ax.set_title('Metabolic balance: GPP vs ER', fontsize=14, fontweight='bold')

# 设置坐标轴
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

# 添加图例
ax.legend(loc='upper left', fontsize=10)

# 添加网格
ax.grid(True, alpha=0.3, linestyle='--')

# 保存图表
output_path = os.path.join(output_dir, 'fig10_gpp_vs_er.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图10已保存: {output_path}")

print("\n📊 代谢平衡分析:")
print(f"  整体GPP: 均值 = {x.mean():.1f}, ER: 均值 = {y.mean():.1f}")
print(f"  NEP 均值: {dat['GPP.mle'].mean() + dat['ER.mle'].mean():.1f}")
print(f"  ER > GPP: {above} 站点 (异养型)")
print(f"  ER < GPP: {below} 站点 (自养型)")
print(f"  ER = GPP: {equal} 站点 (平衡)")

print("\n📊 图表说明:")
print("  - 红色点: 各站点的GPP和ER")
print("  - 蓝色线: 线性回归拟合线")
print("  - 黑色虚线: 1:1线(GPP = ER)")
print("  - 1:1线上方表示呼吸>光合作用(异养)")
print("  - 1:1线下方表示光合作用>呼吸(自养)")
print("  - 大多数河流生态系统接近平衡状态")
