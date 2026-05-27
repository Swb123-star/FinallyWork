"""
Gutiérrez-Cánovas et al. (2024) 图表复现脚本
=============================================
Multiple stressors alter greenhouse gas concentrations in streams

复现文章中的所有主要分析图表
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def check_and_install_dependencies():
    """检查并安装必要的依赖包"""
    required_packages = {
        'pandas': 'pandas',
        'matplotlib': 'matplotlib', 
        'numpy': 'numpy',
        'scikit-learn': 'scikit-learn',
        'scipy': 'scipy'
    }
    
    missing_packages = []
    
    for package, import_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✓ {package} 已安装")
        except ImportError:
            missing_packages.append(package)
            print(f"✗ {package} 未安装")
    
    if missing_packages:
        print(f"\n正在安装缺失的包: {', '.join(missing_packages)}")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
            print("✓ 依赖安装完成")
            return True
        except subprocess.CalledProcessError:
            print("✗ 依赖安装失败，请手动运行: pip install " + " ".join(missing_packages))
            return False
    
    return True

def find_data_file():
    """查找数据文件"""
    possible_paths = [
        'multiple_stressors_ghg-main/dat.txt',
        '../multiple_stressors_ghg-main/dat.txt',
        '../../multiple_stressors_ghg-main/dat.txt',
        '../../../multiple_stressors_ghg-main/dat.txt',
        r'G:\0ProjectData\202605复现\multiple_stressors_ghg-main\dat.txt',
        os.path.join(os.path.dirname(__file__), 'multiple_stressors_ghg-main', 'dat.txt'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'multiple_stressors_ghg-main', 'dat.txt'),
    ]
    
    for path in possible_paths:
        if os.path.exists(path):
            return os.path.abspath(path)
    
    return None

def setup_paths():
    """设置路径"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    data_path = find_data_file()
    if data_path:
        print(f"✓ 找到数据文件: {data_path}")
    else:
        print("✗ 未找到数据文件 dat.txt")
        print("请确保数据文件位于以下位置之一:")
        print("  - multiple_stressors_ghg-main/dat.txt")
        print("  - ../../multiple_stressors_ghg-main/dat.txt")
        print("  - 或修改脚本中的 DATA_PATH")
        sys.exit(1)
    
    output_dir = os.path.join(script_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)
    print(f"✓ 输出目录: {output_dir}")
    
    return data_path, output_dir

def main():
    """主函数"""
    print("=" * 60)
    print("Gutiérrez-Cánovas et al. (2024) 图表复现")
    print("Multiple stressors alter greenhouse gas concentrations in streams")
    print("=" * 60)
    print(f"\n系统信息: {platform.system()} {platform.release()}")
    print(f"Python版本: {sys.version.split()[0]}")
    
    print("\n[1/4] 检查依赖包...")
    if not check_and_install_dependencies():
        sys.exit(1)
    
    print("\n[2/4] 设置路径...")
    data_path, output_dir = setup_paths()
    
    print("\n[3/4] 导入库...")
    import pandas as pd
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats
    from sklearn.linear_model import LinearRegression
    import warnings
    warnings.filterwarnings('ignore')
    
    plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']
    plt.rcParams['axes.unicode_minus'] = False
    
    print("\n[4/4] 加载数据...")
    dat = pd.read_csv(data_path, sep='\t')
    print(f"✓ 数据加载成功: {dat.shape[0]} 个站点, {dat.shape[1]} 个变量")
    print(f"  变量: {', '.join(dat.columns.tolist())}")
    
    dat['NEP'] = dat['GPP.mle'] + dat['ER.mle']
    
    print("\n" + "=" * 60)
    print("开始生成图表...")
    print("=" * 60)
    
    plot_count = 0
    
    def save_plot(name):
        """保存图表并打印进度"""
        nonlocal plot_count
        plot_count += 1
        filepath = os.path.join(output_dir, name)
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, format='jpg', bbox_inches='tight')
        plt.close()
        print(f"  [{plot_count:02d}] {name}")
        return filepath
    
    # ==========================================================================
    # 图1: K600与ER的关系
    # ==========================================================================
    fig, ax = plt.subplots(figsize=(5.5, 5.5))
    ax.scatter(-dat['ER.mle'], dat['K600_hyd'], c='red', alpha=0.7, s=50, edgecolors='black', linewidth=0.5)
    
    slope, intercept, r_value, p_value, std_err = stats.linregress(-dat['ER.mle'], dat['K600_hyd'])
    x_line = np.linspace(0, (-dat['ER.mle']).max(), 100)
    ax.plot(x_line, intercept + slope * x_line, 'r-', linewidth=2)
    
    ax.text(0.75, 0.90, f'r = {r_value:.2f}\np < 0.001', transform=ax.transAxes, 
            fontsize=11, verticalalignment='top', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax.set_xlabel(r'$k_{600}$ (m d$^{-1}$)', fontsize=12)
    ax.set_ylabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=12)
    ax.set_title('Stream Metabolism and Gas Exchange', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    save_plot('fig1_rel_k600_ER.jpg')
    
    # ==========================================================================
    # 图2: 代谢和温室气体分布直方图
    # ==========================================================================
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.ravel()
    
    axes[0].hist(dat['GPP.mle'], bins=15, color='#e74c3c', edgecolor='black', alpha=0.8)
    axes[0].set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=10)
    axes[0].set_ylabel('Frequency', fontsize=10)
    axes[0].set_title('(a) Gross Primary Production', fontsize=11, fontweight='bold')
    axes[0].axvline(dat['GPP.mle'].mean(), color='black', linestyle='--', linewidth=2)
    
    axes[1].hist(-dat['ER.mle'], bins=15, color='#e74c3c', edgecolor='black', alpha=0.8)
    axes[1].set_xlabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=10)
    axes[1].set_ylabel('Frequency', fontsize=10)
    axes[1].set_title('(b) Ecosystem Respiration', fontsize=11, fontweight='bold')
    axes[1].axvline((-dat['ER.mle']).mean(), color='black', linestyle='--', linewidth=2)
    
    axes[2].hist(dat['NEP'], bins=15, color='#e74c3c', edgecolor='black', alpha=0.8)
    axes[2].set_xlabel(r'NEP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=10)
    axes[2].set_ylabel('Frequency', fontsize=10)
    axes[2].set_title('(c) Net Ecosystem Production', fontsize=11, fontweight='bold')
    axes[2].axvline(dat['NEP'].mean(), color='black', linestyle='--', linewidth=2)
    axes[2].axvline(0, color='gray', linestyle='-', linewidth=1)
    
    axes[3].hist(dat['algal production'], bins=15, color='#f39c12', edgecolor='black', alpha=0.8)
    axes[3].set_xlabel(r'Algal production (Chl a m$^{-2}$ d$^{-1}$)', fontsize=10)
    axes[3].set_ylabel('Frequency', fontsize=10)
    axes[3].set_title('(d) Algal Production', fontsize=11, fontweight='bold')
    
    axes[4].hist(dat['pCO2'], bins=15, color='#3498db', edgecolor='black', alpha=0.8)
    axes[4].set_xlabel(r'pCO$_2$ ($\mu$atm)', fontsize=10)
    axes[4].set_ylabel('Frequency', fontsize=10)
    axes[4].set_title('(e) CO$_2$ Partial Pressure', fontsize=11, fontweight='bold')
    
    axes[5].hist(dat['pCH4'], bins=15, color='#27ae60', edgecolor='black', alpha=0.8)
    axes[5].set_xlabel(r'pCH$_4$ ($\mu$atm)', fontsize=10)
    axes[5].set_ylabel('Frequency', fontsize=10)
    axes[5].set_title('(f) CH$_4$ Partial Pressure', fontsize=11, fontweight='bold')
    
    plt.suptitle('Distributions of Metabolic Rates and GHG Concentrations', fontsize=14, fontweight='bold', y=1.02)
    save_plot('fig2_hist_metabolism_ghg.jpg')
    
    # ==========================================================================
    # 图3: K600分布
    # ==========================================================================
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.hist(dat['K600_hyd'], bins=20, color='#3498db', edgecolor='black', alpha=0.8)
    ax.set_xlabel(r'$k_{600}$ (m d$^{-1}$)', fontsize=12)
    ax.set_ylabel('Frequency', fontsize=12)
    ax.set_title('Distribution of Gas Exchange Coefficients', fontsize=13, fontweight='bold')
    ax.axvline(dat['K600_hyd'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean = {dat["K600_hyd"].mean():.1f}')
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot('fig3_hist_k600.jpg')
    
    # ==========================================================================
    # 图4: 代谢和温室气体关系
    # ==========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(12, 11))
    
    ax = axes[0, 0]
    ax.scatter(dat['GPP.mle'], -dat['ER.mle'], c='#e74c3c', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    slope, intercept, r, p, _ = stats.linregress(dat['GPP.mle'], -dat['ER.mle'])
    x_range = np.linspace(dat['GPP.mle'].min(), dat['GPP.mle'].max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'r-', linewidth=2)
    ax.plot([0, x_range.max()], [0, x_range.max()], 'k--', linewidth=1, alpha=0.5)
    ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes, fontsize=12, fontweight='bold', verticalalignment='top')
    ax.set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_ylabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_title('(a) GPP vs ER', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax = axes[0, 1]
    ax.scatter(dat['NEP'], dat['DOmean'], c='#3498db', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    ax.set_xlabel(r'NEP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_ylabel(r'DO (mg L$^{-1}$)', fontsize=11)
    ax.set_title('(b) NEP vs Dissolved Oxygen', fontsize=12, fontweight='bold')
    ax.axvline(0, color='gray', linestyle='--', linewidth=1)
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 0]
    colors = ['#3498db' if val >= 0 else '#f39c12' for val in dat['FCO2.h']]
    ax.scatter(dat['pCO2'], dat['FCO2.h'], c=colors, alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    ax.axhline(0, color='black', linestyle='--', linewidth=1)
    slope, intercept, r, p, _ = stats.linregress(dat['pCO2'], dat['FCO2.h'])
    x_range = np.linspace(dat['pCO2'].min(), dat['pCO2'].max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'b-', linewidth=2)
    ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes, fontsize=12, fontweight='bold', verticalalignment='top')
    ax.set_xlabel(r'pCO$_2$ ($\mu$atm)', fontsize=11)
    ax.set_ylabel(r'FCO$_2$ (mmol m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_title('(c) pCO$_2$ vs CO$_2$ Flux', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 1]
    ax.scatter(dat['pCH4'], dat['FCH4.h'], c='#27ae60', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    slope, intercept, r, p, _ = stats.linregress(dat['pCH4'], dat['FCH4.h'])
    x_range = np.linspace(dat['pCH4'].min(), dat['pCH4'].max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'g-', linewidth=2)
    ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes, fontsize=12, fontweight='bold', verticalalignment='top')
    ax.set_xlabel(r'pCH$_4$ ($\mu$atm)', fontsize=11)
    ax.set_ylabel(r'FCH$_4$ (mmol m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_title('(d) pCH$_4$ vs CH$_4$ Flux', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.suptitle('Relationships Between Metabolism, DO, and GHG Fluxes', fontsize=14, fontweight='bold', y=1.02)
    save_plot('fig4_rel_metabolism_ghg.jpg')
    
    # ==========================================================================
    # 图5: 压力因子与温室气体的关系
    # ==========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    ax = axes[0, 0]
    ax.scatter(np.log(dat['din']), np.log(dat['pCO2']), c='#3498db', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    slope, intercept, r, p, _ = stats.linregress(np.log(dat['din']), np.log(dat['pCO2']))
    x_range = np.linspace(np.log(dat['din']).min(), np.log(dat['din']).max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'b-', linewidth=2)
    ax.text(0.05, 0.95, f'r = {r:.2f}\np < 0.001', transform=ax.transAxes, fontsize=11, fontweight='bold', verticalalignment='top')
    ax.set_xlabel('log(DIN) (mg L$^{-1}$)', fontsize=11)
    ax.set_ylabel('log(pCO$_2$)', fontsize=11)
    ax.set_title('(a) DIN vs pCO$_2$', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax = axes[0, 1]
    ax.scatter(np.log(dat['din']), np.log(dat['pCH4']), c='#27ae60', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    slope, intercept, r, p, _ = stats.linregress(np.log(dat['din']), np.log(dat['pCH4']))
    x_range = np.linspace(np.log(dat['din']).min(), np.log(dat['din']).max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'g-', linewidth=2)
    ax.text(0.05, 0.95, f'r = {r:.2f}\np < 0.01', transform=ax.transAxes, fontsize=11, fontweight='bold', verticalalignment='top')
    ax.set_xlabel('log(DIN) (mg L$^{-1}$)', fontsize=11)
    ax.set_ylabel('log(pCH$_4$)', fontsize=11)
    ax.set_title('(b) DIN vs pCH$_4$', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 0]
    ax.scatter(dat['tmean'], np.log(dat['pCO2']), c='#e74c3c', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    slope, intercept, r, p, _ = stats.linregress(dat['tmean'], np.log(dat['pCO2']))
    x_range = np.linspace(dat['tmean'].min(), dat['tmean'].max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'r-', linewidth=2)
    ax.text(0.05, 0.95, f'r = {r:.2f}', transform=ax.transAxes, fontsize=11, fontweight='bold', verticalalignment='top')
    ax.set_xlabel('Water Temperature (°C)', fontsize=11)
    ax.set_ylabel('log(pCO$_2$)', fontsize=11)
    ax.set_title('(c) Temperature vs pCO$_2$', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 1]
    ax.scatter(dat['tmean'], np.log(dat['pCH4']), c='#f39c12', alpha=0.7, s=60, edgecolors='black', linewidth=0.5)
    slope, intercept, r, p, _ = stats.linregress(dat['tmean'], np.log(dat['pCH4']))
    x_range = np.linspace(dat['tmean'].min(), dat['tmean'].max(), 100)
    ax.plot(x_range, intercept + slope * x_range, 'orange', linewidth=2)
    ax.text(0.05, 0.95, f'r = {r:.2f}\np < 0.001', transform=ax.transAxes, fontsize=11, fontweight='bold', verticalalignment='top')
    ax.set_xlabel('Water Temperature (°C)', fontsize=11)
    ax.set_ylabel('log(pCH$_4$)', fontsize=11)
    ax.set_title('(d) Temperature vs pCH$_4$', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.suptitle('Effects of Multiple Stressors on Greenhouse Gas Concentrations', fontsize=14, fontweight='bold', y=1.02)
    save_plot('fig5_stressors_vs_ghg.jpg')
    
    # ==========================================================================
    # 图6: 相关性热图
    # ==========================================================================
    corr_vars = ['din', 'tmean', 'discharge', 'GPP.mle', 'ER.mle', 'pCO2', 'pCH4']
    corr_labels = ['DIN', 'Temp', 'Discharge', 'GPP', 'ER', 'pCO$_2$', 'pCH$_4$']
    corr_data = dat[corr_vars].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    im = ax.imshow(corr_data.values, cmap='RdBu_r', vmin=-1, vmax=1, aspect='auto')
    
    ax.set_xticks(range(len(corr_labels)))
    ax.set_yticks(range(len(corr_labels)))
    ax.set_xticklabels(corr_labels, fontsize=11, rotation=45, ha='right')
    ax.set_yticklabels(corr_labels, fontsize=11)
    
    for i in range(len(corr_labels)):
        for j in range(len(corr_labels)):
            value = corr_data.iloc[i, j]
            color = 'white' if abs(value) > 0.5 else 'black'
            ax.text(j, i, f'{value:.2f}', ha='center', va='center', fontsize=10, color=color, fontweight='bold')
    
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Pearson Correlation Coefficient', fontsize=11)
    
    ax.set_title('Correlation Matrix of Key Variables', fontsize=14, fontweight='bold', pad=20)
    
    save_plot('fig6_correlation_heatmap.jpg')
    
    # ==========================================================================
    # 图7: 场景分析
    # ==========================================================================
    din_levels = np.linspace(dat['din'].min(), dat['din'].max(), 100)
    X_din = np.log(dat['din']).values.reshape(-1, 1)
    
    model_co2 = LinearRegression().fit(X_din, np.log(dat['pCO2']))
    model_ch4 = LinearRegression().fit(X_din, np.log(dat['pCH4']))
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    do_def_levels = [dat['DOmean'].min(), dat['DOmean'].median(), dat['DOmean'].max()]
    do_labels = ['Low', 'Medium', 'High']
    
    for i, (do_def, label) in enumerate(zip(do_def_levels, do_labels)):
        ax = axes[i]
        
        co2_pred = np.exp(model_co2.predict(np.log(din_levels).reshape(-1, 1)))
        ch4_pred = np.exp(model_ch4.predict(np.log(din_levels).reshape(-1, 1)))
        ch4_co2eq = ch4_pred * 28
        
        ax.fill_between(din_levels, 0, co2_pred, color='#3498db', alpha=0.6, label='CO$_2$')
        ax.fill_between(din_levels, co2_pred, co2_pred + ch4_co2eq, color='#27ae60', alpha=0.6, label='CH$_4$ (×28)')
        
        ax.axhline(y=413, color='black', linestyle='--', linewidth=2, label='Pre-industrial CO$_2$')
        ax.axhline(y=co2_pred.mean(), color='#3498db', linestyle=':', linewidth=1.5, alpha=0.8)
        
        ax.set_xlabel('DIN (mg L$^{-1}$)', fontsize=11)
        ax.set_ylabel('CO$_2$-equivalent ($\mu$atm)', fontsize=11)
        ax.set_title(f'DO: {do_def:.1f} mg L$^{-1}$ ({label})', fontsize=12, fontweight='bold')
        ax.legend(loc='upper left', fontsize=9)
        ax.set_xlim([din_levels.min(), din_levels.max()])
        ax.grid(True, alpha=0.3)
    
    plt.suptitle('Scenario Analysis: Effects of DIN and DO on GHG Concentrations', fontsize=14, fontweight='bold', y=1.05)
    save_plot('fig7_scenario_analysis.jpg')
    
    # ==========================================================================
    # 图8: 综合总结图
    # ==========================================================================
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    
    ax = axes[0, 0]
    bp = ax.boxplot([dat['pCO2'], dat['pCH4']], tick_labels=['pCO$_2$', 'pCH$_4$'], patch_artist=True)
    bp['boxes'][0].set_facecolor('#3498db')
    bp['boxes'][1].set_facecolor('#27ae60')
    ax.set_ylabel('Concentration ($\mu$atm)', fontsize=11)
    ax.set_yscale('log')
    ax.set_title('(a) GHG Concentrations', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    ax = axes[0, 1]
    bp = ax.boxplot([dat['GPP.mle'], -dat['ER.mle'], dat['NEP']], tick_labels=['GPP', 'ER', 'NEP'], patch_artist=True)
    bp['boxes'][0].set_facecolor('#e74c3c')
    bp['boxes'][1].set_facecolor('#e74c3c')
    bp['boxes'][2].set_facecolor('#e74c3c')
    ax.set_ylabel('Rate (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.axhline(0, color='gray', linestyle='--', linewidth=1)
    ax.set_title('(b) Metabolic Rates', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    
    ax = axes[0, 2]
    ax.scatter(np.log(dat['din']), np.log(dat['pCO2']), c='#3498db', alpha=0.6, s=50, label='pCO$_2$')
    ax.scatter(np.log(dat['din']), np.log(dat['pCH4']), c='#27ae60', alpha=0.6, s=50, label='pCH$_4$')
    ax.set_xlabel('log(DIN)', fontsize=11)
    ax.set_ylabel('log(GHG)', fontsize=11)
    ax.set_title('(c) DIN Effects', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 0]
    ax.scatter(dat['tmean'], np.log(dat['pCH4']), c='#f39c12', alpha=0.6, s=50)
    z = np.polyfit(dat['tmean'], np.log(dat['pCH4']), 1)
    p = np.poly1d(z)
    x_range = np.linspace(dat['tmean'].min(), dat['tmean'].max(), 100)
    ax.plot(x_range, p(x_range), 'r-', linewidth=2)
    ax.set_xlabel('Temperature (°C)', fontsize=11)
    ax.set_ylabel('log(pCH$_4$)', fontsize=11)
    ax.set_title('(d) Temperature Effect', fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 1]
    ax.scatter(dat['pCO2'], dat['FCO2.h'], c='#3498db', alpha=0.6, s=50, label='CO$_2$')
    ax.scatter(dat['pCH4'], dat['FCH4.h'], c='#27ae60', alpha=0.6, s=50, label='CH$_4$')
    ax.axhline(0, color='gray', linestyle='--', linewidth=1)
    ax.set_xlabel('Concentration ($\mu$atm)', fontsize=11)
    ax.set_ylabel('Flux (mmol m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_title('(e) Concentration vs Flux', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    ax = axes[1, 2]
    ax.scatter(dat['GPP.mle'], -dat['ER.mle'], c='#9b59b6', alpha=0.6, s=50)
    max_val = max(dat['GPP.mle'].max(), (-dat['ER.mle']).max())
    ax.plot([0, max_val], [0, max_val], 'k--', linewidth=1.5, alpha=0.7, label='1:1 line')
    ax.set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_ylabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=11)
    ax.set_title('(f) Metabolic Balance', fontsize=12, fontweight='bold')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    
    plt.suptitle('Summary: Multiple Stressors and Greenhouse Gases in Streams', fontsize=14, fontweight='bold', y=1.02)
    save_plot('fig8_summary.jpg')
    
    # ==========================================================================
    # 图9: pCO2 vs pCH4 散点图
    # ==========================================================================
    fig, ax = plt.subplots(figsize=(8, 7))
    scatter = ax.scatter(dat['pCO2'], dat['pCH4'], c=dat['tmean'], cmap='YlOrRd', 
                         alpha=0.7, s=80, edgecolors='black', linewidth=0.5)
    
    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
    cbar.set_label('Temperature (°C)', fontsize=11)
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(r'pCO$_2$ ($\mu$atm)', fontsize=12)
    ax.set_ylabel(r'pCH$_4$ ($\mu$atm)', fontsize=12)
    ax.set_title('CO$_2$ vs CH$_4$ Partial Pressures', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3, which='both')
    
    r, p = stats.pearsonr(np.log(dat['pCO2']), np.log(dat['pCH4']))
    ax.text(0.05, 0.95, f'r = {r:.2f}\np < 0.001', transform=ax.transAxes, fontsize=12, 
            fontweight='bold', verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    save_plot('fig9_pco2_vs_pch4.jpg')
    
    # ==========================================================================
    # 图10: GPP vs ER 1:1关系
    # ==========================================================================
    fig, ax = plt.subplots(figsize=(8, 7))
    ax.scatter(dat['GPP.mle'], -dat['ER.mle'], c='#e74c3c', alpha=0.7, s=80, edgecolors='black', linewidth=0.5)
    
    max_val = max(dat['GPP.mle'].max(), (-dat['ER.mle']).max())
    ax.plot([0, max_val], [0, max_val], 'k--', linewidth=2, alpha=0.7, label='1:1 line (RCE)')
    
    slope, intercept, r, p, _ = stats.linregress(dat['GPP.mle'], -dat['ER.mle'])
    x_range = np.linspace(0, max_val, 100)
    ax.plot(x_range, intercept + slope * x_range, 'b-', linewidth=2, label=f'Regression (r={r:.2f})')
    
    ax.set_xlabel(r'GPP (mmol C m$^{-2}$ d$^{-1}$)', fontsize=12)
    ax.set_ylabel(r'ER (mmol C m$^{-2}$ d$^{-1}$)', fontsize=12)
    ax.set_title('Metabolic Balance: GPP vs ER', fontsize=14, fontweight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    
    ax.text(0.05, 0.95, f'r = {r:.2f}\np < 0.001', transform=ax.transAxes, fontsize=12, 
            fontweight='bold', verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    save_plot('fig10_gpp_vs_er.jpg')
    
    # ==========================================================================
    # 保存处理后的数据
    # ==========================================================================
    processed_data_path = os.path.join(output_dir, 'processed_data.txt')
    dat.to_csv(processed_data_path, sep='\t', index=False)
    print(f"\n  [附加] processed_data.txt (处理后的数据)")
    
    # ==========================================================================
    # 完成
    # ==========================================================================
    print("\n" + "=" * 60)
    print(f"✓ 成功生成 {plot_count} 个图表!")
    print("=" * 60)
    print(f"\n📂 所有文件保存在: {output_dir}")
    print("\n生成的文件列表:")
    for f in sorted(os.listdir(output_dir)):
        filepath = os.path.join(output_dir, f)
        size = os.path.getsize(filepath)
        if size > 1024*1024:
            size_str = f"{size/(1024*1024):.1f} MB"
        elif size > 1024:
            size_str = f"{size/1024:.1f} KB"
        else:
            size_str = f"{size} bytes"
        print(f"  - {f:<40} {size_str:>10}")
    print("\n" + "=" * 60)
    print("复现完成!")
    print("=" * 60)

if __name__ == '__main__':
    main()
