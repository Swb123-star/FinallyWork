"""
图9: pCO2与pCH4的关系(温度色彩映射)

本脚本展示两种主要温室气体浓度的关系，并用水温给数据点着色。
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

# 绘制散点图(温度着色)
scatter = ax.scatter(dat['pCO2'], dat['pCH4'], c=dat['tmean'],
                     cmap='YlOrRd', alpha=0.7, s=80, edgecolors='black', linewidth=0.5)

# 添加颜色条
cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
cbar.set_label('Water temperature (°C)', fontsize=11)

# 计算相关系数
r, p = stats.pearsonr(np.log(dat['pCO2']), np.log(dat['pCH4']))

# 添加文本说明
p_text = 'p < 0.001' if p < 0.001 else f'p = {p:.3f}'
ax.text(0.05, 0.95, f'r = {r:.2f}\n{p_text}', transform=ax.transAxes,
        fontsize=12, fontweight='bold', verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# 设置坐标轴(对数刻度)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'CO$_2$ partial pressure ($\mu$atm)', fontsize=12)
ax.set_ylabel(r'CH$_4$ partial pressure ($\mu$atm)', fontsize=12)
ax.set_title('Relationship between CO$_2$ and CH$_4$ concentrations',
             fontsize=13, fontweight='bold')

# 添加网格
ax.grid(True, alpha=0.3, which='both', linestyle='--')

# 保存图表
output_path = os.path.join(output_dir, 'fig9_pco2_vs_pch4.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图9已保存: {output_path}")

print("\n📊 统计结果:")
print(f"  pCO2 范围: {dat['pCO2'].min():.0f} - {dat['pCO2'].max():.0f} μatm")
print(f"  pCH4 范围: {dat['pCH4'].min():.0f} - {dat['pCH4'].max():.0f} μatm")
print(f"  温度范围: {dat['tmean'].min():.1f} - {dat['tmean'].max():.1f} °C")
print(f"  相关系数: r = {r:.4f}, p = {p:.4e}")

print("\n📊 图表说明:")
print("  - 点的颜色表示水温(黄色到红色: 低温到高温)")
print("  - x轴和y轴为对数刻度")
print("  - pCO2和pCH4有正相关关系")
print("  - 高温站点(红色点)通常有较高的CH4浓度")
