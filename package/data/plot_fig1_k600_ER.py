"""
图1: 气体交换系数(K600)与生态系统呼吸(ER)的关系

本脚本复现原始研究中的Figure 1，展示：
- K600 (气体交换系数) 与 ER (生态系统呼吸) 的散点图
- 线性回归关系及相关系数
- 数据点用红色表示，回归线用红色实线
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
fig, ax = plt.subplots(figsize=(5.5, 5.5))

# 绘制散点图
x = -dat['ER.mle']  # ER在原始数据中是负值
y = dat['K600_hyd']
scatter = ax.scatter(x, y, c='red', alpha=0.7, s=50, edgecolors='black', linewidth=0.5)

# 线性回归
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
x_line = np.linspace(0, x.max(), 100)
ax.plot(x_line, intercept + slope * x_line, 'red', linewidth=2, label=f'r = {r_value:.2f}')

# 设置标签和标题
ax.set_xlabel(r'Gas exchange coefficient ($k_{600}$, m d$^{-1}$)', fontsize=12)
ax.set_ylabel(r'Ecosystem respiration (mmol C m$^{-2}$ d$^{-1}$)', fontsize=12)
ax.set_title('Relationship between gas exchange and respiration', fontsize=13, fontweight='bold')

# 添加文本说明
ax.text(0.75, 0.90, f'r = {r_value:.2f}\np < 0.001', transform=ax.transAxes,
        fontsize=11, verticalalignment='top', fontweight='bold',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 添加网格
ax.grid(True, alpha=0.3, linestyle='--')

# 设置坐标轴范围
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

# 保存图表
output_path = os.path.join(output_dir, 'fig1_rel_k600_ER.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图1已保存: {output_path}")
print(f"统计结果: r = {r_value:.4f}, p = {p_value:.4e}")

# 简要说明
print("\n📊 图表说明:")
print("  - 展示河流生态系统中，气体交换效率与呼吸强度的关系")
print("  - x轴: k600 (m/d) - CO2气体交换系数")
print("  - y轴: ER (mmol C/m²/d) - 生态系统呼吸")
print("  - 红色点: 每个站点的观测值")
print("  - 红色线: 线性回归拟合线")
