"""
主运行脚本 - 运行所有图表的复现

此脚本将依次运行10个图表的生成程序。
"""

import os
import sys

# 设置基础目录
base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"工作目录: {base_dir}")
print("="*60)

# 图表脚本列表
plot_scripts = [
    ('图1: K600与ER关系', 'plot_fig1_k600_ER.py'),
    ('图2: 代谢和GHG分布', 'plot_fig2_histograms.py'),
    ('图3: K600分布', 'plot_fig3_k600_dist.py'),
    ('图4: 代谢与GHG关系', 'plot_fig4_metabolism_ghg.py'),
    ('图5: 压力因子与GHG', 'plot_fig5_stressors_ghg.py'),
    ('图6: 相关性热图', 'plot_fig6_correlation.py'),
    ('图7: 场景分析', 'plot_fig7_scenario.py'),
    ('图8: 综合总结', 'plot_fig8_summary.py'),
    ('图9: pCO2与pCH4', 'plot_fig9_pco2_pch4.py'),
    ('图10: GPP与ER', 'plot_fig10_gpp_er.py'),
]

# 运行每个脚本
print("开始运行图表复现...\n")
success_count = 0

for name, script in plot_scripts:
    print(f"正在运行: {name}")
    script_path = os.path.join(base_dir, script)
    try:
        result = os.system(f'"{sys.executable}" "{script_path}"')
        if result == 0:
            success_count += 1
            print(f"✓ 完成: {name}")
        else:
            print(f"✗ 错误: {name}")
    except Exception as e:
        print(f"✗ 异常: {name}, {e}")
    print()

print("="*60)
print(f"运行完成! {success_count}/{len(plot_scripts)} 成功")
print(f"图表已保存到: {os.path.join(base_dir, '..', 'reproduced_figures')}")
print("="*60)

# 提供单独运行的说明
print("\n💡 提示: 也可以单独运行每个脚本")
print("  例如: python plot_fig1_k600_ER.py")
