"""
图3: 气体交换系数(K600)的分布

本脚本展示K600 (气体交换系数) 在所有站点中的分布情况。
"""

import pandas as pd
import matplotlib.pyplot as plt
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
fig, ax = plt.subplots(figsize=(5, 4))

# 绘制直方图
ax.hist(dat['K600_hyd'], bins=20, color='#3498db', edgecolor='black', alpha=0.8)

# 添加均值线
mean_k600 = dat['K600_hyd'].mean()
ax.axvline(mean_k600, color='red', linestyle='--', linewidth=2,
           label=f'Mean = {mean_k600:.1f} m/d')

# 添加中值线
median_k600 = dat['K600_hyd'].median()
ax.axvline(median_k600, color='orange', linestyle=':', linewidth=2,
           label=f'Median = {median_k600:.1f} m/d')

# 设置标签和标题
ax.set_xlabel(r'Gas exchange coefficient ($k_{600}$, m d$^{-1}$)', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)
ax.set_title('Distribution of gas exchange coefficients', fontsize=13, fontweight='bold')

# 添加图例
ax.legend(fontsize=10)

# 添加网格
ax.grid(True, alpha=0.3, axis='y', linestyle='--')

# 保存图表
output_path = os.path.join(output_dir, 'fig3_hist_k600.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图3已保存: {output_path}")

# 统计信息
print("\n📊 K600统计:")
print(f"  均值:   {dat['K600_hyd'].mean():.2f} m/d")
print(f"  中位数: {dat['K600_hyd'].median():.2f} m/d")
print(f"  标准差: {dat['K600_hyd'].std():.2f} m/d")
print(f"  最小值: {dat['K600_hyd'].min():.2f} m/d")
print(f"  最大值: {dat['K600_hyd'].max():.2f} m/d")

print("\n📊 图表说明:")
print("  - 蓝色柱: K600的分布直方图")
print("  - 红色虚线: 平均值")
print("  - 橙色点线: 中位数")
print("  - K600表示CO2在水气界面的交换速率")
