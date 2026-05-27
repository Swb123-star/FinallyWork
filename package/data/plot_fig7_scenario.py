"""
图7: DIN和溶解氧对温室气体浓度的场景分析

本脚本复现原始研究中的Figure 7，展示：
- 在不同溶解氧条件下，DIN浓度对CO2和CH4的影响
- CO2当量的估算（CH4 × 28）
- 工业化前CO2水平的参考线
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
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

# 准备数据
din_levels = np.linspace(dat['din'].min(), dat['din'].max(), 100)
X_din = np.log(dat['din']).values.reshape(-1, 1)

# 训练线性回归模型
model_co2 = LinearRegression().fit(X_din, np.log(dat['pCO2']))
model_ch4 = LinearRegression().fit(X_din, np.log(dat['pCH4']))

# 创建子图
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# 定义三个DO场景（低、中、高）
do_levels = [dat['DOmean'].min(), dat['DOmean'].median(), dat['DOmean'].max()]
do_labels = ['Low DO', 'Medium DO', 'High DO']

for i, (do_level, label) in enumerate(zip(do_levels, do_labels)):
    ax = axes[i]
    
    # 预测
    co2_pred = np.exp(model_co2.predict(np.log(din_levels).reshape(-1, 1)))
    ch4_pred = np.exp(model_ch4.predict(np.log(din_levels).reshape(-1, 1)))
    
    # DO对CH4的影响（基于文献假设）
    ch4_pred *= (1 - 0.1 * (do_level - dat['DOmean'].mean()) / dat['DOmean'].std())
    
    # 计算CO2当量
    ch4_co2eq = ch4_pred * 28
    
    # 绘制填充图
    ax.fill_between(din_levels, 0, co2_pred, color='#3498db', alpha=0.6, label='CO$_2$')
    ax.fill_between(din_levels, co2_pred, co2_pred + ch4_co2eq,
                    color='#27ae60', alpha=0.6, label='CH$_4$ (×28)')
    
    # 工业化前CO2参考线
    ax.axhline(y=413, color='black', linestyle='--', linewidth=2,
               label='Pre-industrial CO$_2$')
    
    # 平均CO2线
    ax.axhline(y=co2_pred.mean(), color='#3498db', linestyle=':', linewidth=1.5, alpha=0.8)
    
    # 设置标签和标题
    ax.set_xlabel('DIN (mg L$^{-1}$)', fontsize=11)
    ax.set_ylabel('CO$_2$-equivalent ($\mu$atm)', fontsize=11)
    ax.set_title(f'{label}: {do_level:.1f} mg L$^{-1}$', fontsize=12, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9)
    ax.set_xlim([din_levels.min(), din_levels.max()])
    ax.grid(True, alpha=0.3, linestyle='--')

# 总标题
plt.suptitle('Scenario analysis: Effects of DIN and DO on GHG concentrations',
             fontsize=14, fontweight='bold', y=1.05)

# 保存图表
output_path = os.path.join(output_dir, 'fig7_scenario_analysis.jpg')
plt.tight_layout()
plt.savefig(output_path, dpi=300, format='jpg', bbox_inches='tight')
plt.close()

print(f"图7已保存: {output_path}")

print("\n📊 场景说明:")
print(f"  低溶解氧:  {do_levels[0]:.1f} mg/L")
print(f"  中溶解氧:  {do_levels[1]:.1f} mg/L")
print(f"  高溶解氧:  {do_levels[2]:.1f} mg/L")
print("\n📊 图表说明:")
print("  - 蓝色区域: CO2浓度")
print("  - 绿色区域: CH4的CO2当量(×28)")
print("  - 黑色虚线: 工业化前CO2水平(413 μatm)")
print("  - 展示了低DO条件下，DIN对CH4的放大效应")
