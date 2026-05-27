"""
图8: 主要发现的综合总结图

本脚本提供一个总览性的图表，总结原始研究的关键发现。
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
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# 图8a: GHG浓度箱线图
ax = axes[0, 0]
bp = ax.boxplot([dat['pCO2'], dat['pCH4']], tick_labels=['pCO$_2$', 'pCH$_4$'], patch_artist=True)
bp['boxes'][0].set_facecolor('#3498db')
bp['boxes'][1].set_facecolor('#27ae60')
ax.set_ylabel('Concentration ($\mu$atm)', fontsize=11)
ax.set_yscale('log')
ax.set_title('(a) GHG Concentrations', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# 图8b: 代谢率箱线图
ax = axes[0, 1]
bp = ax.boxplot([dat['GPP.mle'], -dat['ER.mle'], dat['NEP']],
                tick_labels=['GPP', 'ER', 'NEP'], patch_artist=True)
bp['boxes'][0].set_facecolor('#e74c3c')
bp['boxes'][1].set_facecolor('#e74c3c')
bp['boxes'][2].set_facecolor('#e74c3c')
ax.set_ylabel('Rate (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.axhline(0, color='gray', linestyle='--', linewidth=1)
ax.set_title('(b) Metabolic Rates', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# 图8c: DIN效应散点图
ax = axes[0, 2]
ax.scatter(np.log(dat['din']), np.log(dat['pCO2']), c='#3498db', alpha=0.6, s=50, label='pCO$_2$')
ax.scatter(np.log(dat['din']), np.log(dat['pCH4']), c='#27ae60', alpha=0.6, s=50, label='pCH$_4$')
ax.set_xlabel('log(DIN)', fontsize=11)
ax.set_ylabel('log(GHG)', fontsize=11)
ax.set_title('(c) DIN Effects', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, linestyle='--')

# 图8d: 温度效应
ax = axes[1, 0]
ax.scatter(dat['tmean'], np.log(dat['pCH4']), c='#f39c12', alpha=0.6, s=50)
z = np.polyfit(dat['tmean'], np.log(dat['pCH4']), 1)
p = np.poly1d(z)
x_range = np.linspace(dat['tmean'].min(), dat['tmean'].max(), 100)
ax.plot(x_range, p(x_range), 'red', linewidth=2)
ax.set_xlabel('Temperature (°C)', fontsize=11)
ax.set_ylabel('log(pCH$_4$)', fontsize=11)
ax.set_title('(d) Temperature Effect', fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3, linestyle='--')

# 图8e: 浓度与通量
ax = axes[1, 1]
ax.scatter(dat['pCO2'], dat['FCO2.h'], c='#3498db', alpha=0.6, s=50, label='CO$_2$')
ax.scatter(dat['pCH4'], dat['FCH4.h'], c='#27ae60', alpha=0.6, s=50, label='CH$_4$')
ax.axhline(0, color='gray', linestyle='--', linewidth=1)
ax.set_xlabel('Concentration ($\mu$atm)', fontsize=11)
ax.set_ylabel('Flux (mmol m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_title('(e) Concentration vs Flux', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, linestyle='--')

# 图8f: 代谢平衡
ax = axes[1, 2]
ax.scatter(dat['GPP.mle'], -dat['ER.mle'], c='#9b59b6', alpha=0.6, s=50)
max_val = max(dat['GPP.mle'].max(), (-dat['ER.mle']).max())
ax.plot([0, max_val], [0, max_val], 'black', '--', linewidth=1.5, alpha=0.7, label='1:1 line')
ax.set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_ylabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
ax.set_title('(f) Metabolic Balance', fontsize=12, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3, linestyle='--')

# 总标题
plt.suptitle('Summary: Multiple stressors and greenhouse gases in streams',
             fontsize=14, fontweight='bold', y=1.02)

# 保存图表
output_path = os.path.join(output_dir, 'fig8_summary.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图8已保存: {output_path}")

print("\n📊 综合发现总结:")
print("  1. 河流通常是CO2和CH4的来源")
print("  2. DIN输入与两种温室气体正相关")
print("  3. 温度对CH4的影响大于对CO2的影响")
print("  4. 生态系统代谢接近平衡状态(GPP ≈ ER)")
