"""
图6: 关键变量的相关性热图

本脚本展示原始研究中主要变量的Pearson相关系数矩阵。
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

# 设置绘图风格
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# 选择相关分析
corr_vars = ['din', 'tmean', 'discharge', 'GPP.mle', 'ER.mle', 'pCO2', 'pCH4']
corr_labels = ['DIN', 'Temp', 'Discharge', 'GPP', 'ER', 'pCO$_2$', 'pCH$_4$']
corr_matrix = dat[corr_vars].corr()

# 创建图表
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制热图
im = ax.imshow(corr_matrix.values, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')

# 设置轴标签
ax.set_xticks(range(len(corr_labels)))
ax.set_yticks(range(len(corr_labels)))
ax.set_xticklabels(corr_labels, fontsize=11, rotation=45, ha='right')
ax.set_yticklabels(corr_labels, fontsize=11)

# 添加数值标签
for i in range(len(corr_labels)):
    for j in range(len(corr_labels)):
        value = corr_matrix.iloc[i, j]
        color = 'white' if abs(value) > 0.5 else 'black'
        ax.text(j, i, f'{value:.2f}', ha='center', va='center',
                fontsize=10, color=color, fontweight='bold')

# 添加颜色条
cbar = plt.colorbar(im, ax=ax, shrink=0.8)
cbar.set_label('Pearson Correlation Coefficient', fontsize=11)

# 设置标题
ax.set_title('Correlation Matrix of Key Variables', fontsize=14, fontweight='bold', pad=20)

# 保存图表
output_path = os.path.join(output_dir, 'fig6_correlation_heatmap.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图6已保存: {output_path}")

print("\n📊 强相关关系 (|r| > 0.5):")
for i, var1 in enumerate(corr_labels):
    for j, var2 in enumerate(corr_labels):
        if i < j:
            value = corr_matrix.iloc[i, j]
            if abs(value) > 0.5:
                sign = '正' if value > 0 else '负'
                print(f"  {var1} vs {var2}: r = {value:.2f} ({sign}相关)")

print("\n📊 图表说明:")
print("  - 红色表示正相关，蓝色表示负相关")
print("  - 颜色越深，相关系数的绝对值越大")
print("  - GPP与ER强正相关，反映生态系统代谢耦合")
print("  - DIN与两种温室气体都呈正相关")
