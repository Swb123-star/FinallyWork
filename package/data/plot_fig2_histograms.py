"""
图2: 代谢率和温室气体浓度的分布直方图

本脚本复现原始研究中的Figure 2，展示：
- GPP (总初级生产力) 的分布
- ER (生态系统呼吸) 的分布
- NEP (净生态系统生产力) 的分布
- 藻类产量的分布
- pCO2 (CO2分压) 的分布
- pCH4 (CH4分压) 的分布
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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

# 计算NEP
dat['NEP'] = dat['GPP.mle'] + dat['ER.mle']

# 设置绘图风格
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# 创建子图
fig, axes = plt.subplots(2, 3, figsize=(12, 8))
axes = axes.ravel()

# 图2a: GPP
ax = axes[0]
ax.hist(dat['GPP.mle'], bins=15, color='#e74c3c', edgecolor='black', alpha=0.8)
ax.set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('(a) Gross Primary Production', fontsize=11, fontweight='bold')
ax.axvline(dat['GPP.mle'].mean(), color='black', linestyle='--', linewidth=2,
           label=f'Mean = {dat["GPP.mle"].mean():.1f}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2, axis='y')

# 图2b: ER
ax = axes[1]
ax.hist(-dat['ER.mle'], bins=15, color='#e74c3c', edgecolor='black', alpha=0.8)
ax.set_xlabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('(b) Ecosystem Respiration', fontsize=11, fontweight='bold')
ax.axvline((-dat['ER.mle']).mean(), color='black', linestyle='--', linewidth=2,
           label=f'Mean = {(-dat["ER.mle"]).mean():.1f}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2, axis='y')

# 图2c: NEP
ax = axes[2]
ax.hist(dat['NEP'], bins=15, color='#e74c3c', edgecolor='black', alpha=0.8)
ax.set_xlabel(r'NEP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('(c) Net Ecosystem Production', fontsize=11, fontweight='bold')
ax.axvline(dat['NEP'].mean(), color='black', linestyle='--', linewidth=2,
           label=f'Mean = {dat["NEP"].mean():.1f}')
ax.axvline(0, color='gray', linestyle='-', linewidth=1)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2, axis='y')

# 图2d: 藻类产量
ax = axes[3]
ax.hist(dat['algal production'], bins=15, color='#f39c12', edgecolor='black', alpha=0.8)
ax.set_xlabel(r'Algal production (Chl a m$^{-2}$ d$^{-1}$)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('(d) Algal Production', fontsize=11, fontweight='bold')
ax.axvline(dat['algal production'].mean(), color='black', linestyle='--', linewidth=2,
           label=f'Mean = {dat["algal production"].mean():.1f}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2, axis='y')

# 图2e: pCO2
ax = axes[4]
ax.hist(dat['pCO2'], bins=15, color='#3498db', edgecolor='black', alpha=0.8)
ax.set_xlabel(r'pCO$_2$ ($\mu$atm)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('(e) CO$_2$ Partial Pressure', fontsize=11, fontweight='bold')
ax.axvline(dat['pCO2'].mean(), color='black', linestyle='--', linewidth=2,
           label=f'Mean = {dat["pCO2"].mean():.0f}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2, axis='y')

# 图2f: pCH4
ax = axes[5]
ax.hist(dat['pCH4'], bins=15, color='#27ae60', edgecolor='black', alpha=0.8)
ax.set_xlabel(r'pCH$_4$ ($\mu$atm)', fontsize=10)
ax.set_ylabel('Frequency', fontsize=10)
ax.set_title('(f) CH$_4$ Partial Pressure', fontsize=11, fontweight='bold')
ax.axvline(dat['pCH4'].mean(), color='black', linestyle='--', linewidth=2,
           label=f'Mean = {dat["pCH4"].mean():.0f}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.2, axis='y')

# 总标题
plt.suptitle('Distributions of metabolic rates and GHG concentrations',
             fontsize=14, fontweight='bold', y=1.02)

# 保存图表
output_path = os.path.join(output_dir, 'fig2_hist_metabolism_ghg.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图2已保存: {output_path}")

# 统计摘要
print("\n📊 统计摘要:")
print(f"  GPP: 均值 = {dat['GPP.mle'].mean():.1f}, 范围 = {dat['GPP.mle'].min():.1f} - {dat['GPP.mle'].max():.1f}")
print(f"  ER:  均值 = {(-dat['ER.mle']).mean():.1f}, 范围 = {(-dat['ER.mle']).min():.1f} - {(-dat['ER.mle']).max():.1f}")
print(f"  NEP: 均值 = {dat['NEP'].mean():.1f}, 范围 = {dat['NEP'].min():.1f} - {dat['NEP'].max():.1f}")
print(f"  pCO2: 均值 = {dat['pCO2'].mean():.0f}, 范围 = {dat['pCO2'].min():.0f} - {dat['pCO2'].max():.0f}")
print(f"  pCH4: 均值 = {dat['pCH4'].mean():.0f}, 范围 = {dat['pCH4'].min():.0f} - {dat['pCH4'].max():.0f}")

print("\n📊 图表说明:")
print("  - 红色: 生态系统代谢率(GPP, ER, NEP)")
print("  - 橙色: 藻类产量")
print("  - 蓝色: CO2浓度")
print("  - 绿色: CH4浓度")
print("  - 黑色虚线: 均值")
print("  - NEP图中的灰色线: 0值线(自养/异养平衡)")
