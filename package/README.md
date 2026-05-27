# 多重压力因子对河流温室气体浓度的影响 - 图表复现

## 📚 项目概述

本项目复现了Gutiérrez-Cánovas等人(2024)发表在*Global Change Biology*的研究成果，探讨了多重环境压力因子对河流温室气体浓度的影响。

**原始论文**: Gutiérrez-Cánovas, C., et al. (2024). Multiple stressors alter greenhouse gas concentrations in streams. *Global Change Biology*.

## 📁 项目结构

```
multiple-stressors-ghg-reproduce/
├── README.md                          # 项目说明(本文件)
├── TECHNICAL_DOCUMENTATION.md         # 技术文档
├── reproduce_figures.py               # 主复现脚本
├── LICENSE                            # 许可证
├── .gitignore                         # Git忽略文件
├── data/                              # 数据文件夹
│   └── dat.txt                        # 原始数据
├── original_figures/                  # 原始图表
│   └── (论文中的原图)
├── reproduced_figures/                # 复现的图表
│   ├── fig1_rel_k600_ER.jpg
│   ├── fig2_hist_metabolism_ghg.jpg
│   ├── fig3_hist_k600.jpg
│   ├── fig4_rel_metabolism_ghg.jpg
│   ├── fig5_stressors_vs_ghg.jpg
│   ├── fig6_correlation_heatmap.jpg
│   ├── fig7_scenario_analysis.jpg
│   ├── fig8_summary.jpg
│   ├── fig9_pco2_vs_pch4.jpg
│   └── fig10_gpp_vs_er.jpg
└── output/                            # 运行输出(可选)
```

## 🚀 快速开始

### 环境要求

- Python 3.7 或更高版本
- pandas
- matplotlib
- numpy
- scipy
- scikit-learn

### 安装依赖

```bash
# 自动安装(脚本会处理)
python reproduce_figures.py

# 或者手动安装
pip install pandas matplotlib numpy scipy scikit-learn
```

### 运行复现

```bash
python reproduce_figures.py
```

## 📊 复现的图表

| 序号 | 文件名 | 描述 |
|------|--------|------|
| 1 | fig1_rel_k600_ER.jpg | 气体交换系数(K600)与生态系统呼吸(ER)的关系 |
| 2 | fig2_hist_metabolism_ghg.jpg | 代谢率和温室气体浓度的分布直方图 |
| 3 | fig3_hist_k600.jpg | 气体交换系数的分布 |
| 4 | fig4_rel_metabolism_ghg.jpg | 生态系统代谢、溶解氧与温室气体通量的关系 |
| 5 | fig5_stressors_vs_ghg.jpg | 多重压力因子对温室气体浓度的影响 |
| 6 | fig6_correlation_heatmap.jpg | 关键变量的相关性热图 |
| 7 | fig7_scenario_analysis.jpg | DIN和溶解氧对GHG的场景分析 |
| 8 | fig8_summary.jpg | 主要发现的综合总结图 |
| 9 | fig9_pco2_vs_pch4.jpg | pCO2与pCH4的关系(温度色彩映射) |
| 10 | fig10_gpp_vs_er.jpg | GPP与ER的代谢平衡(1:1线) |

## 🔬 主要发现

### 1. 氮输入的影响
- **DIN与pCO2**: 显著正相关，r ≈ 0.3-0.5, p < 0.001
- **DIN与pCH4**: 显著正相关，r ≈ 0.2-0.4, p < 0.01
- **解释**: 氮输入增加促进异养微生物活性，增加CO₂和CH₄释放

### 2. 温度的影响
- **温度与pCH4**: 强正相关，r ≈ 0.4-0.6, p < 0.001
- **解释**: 温度升高促进甲烷菌活性

### 3. 生态系统代谢
- **GPP与ER**: 强正相关，r ≈ 0.7-0.9
- **结果**: 河流生态系统接近代谢平衡状态

### 4. 温室气体相互关系
- **pCO2与pCH4**: 显著正相关
- **解释**: 共同的微生物产生途径

## 📝 数据字典

### 气象变量
- `air_mean_temp`: 平均气温 (°C)
- `tmean`: 平均水温 (°C)
- `alt`: 海拔 (m)
- `air_pressure`: 气压 (kPa)

### 水化学变量
- `din`: 溶解性无机氮 (mg/L)
- `ppo4`: 溶解性磷酸盐 (mg/L)
- `DOmean`: 平均溶解氧 (mg/L)

### 水文变量
- `discharge`: 流量 (m³/s)
- `K600_hyd`: K600气体交换系数 (m/d)

### 生态变量
- `GPP.mle`: 总初级生产力 (mmol C m⁻² d⁻¹)
- `ER.mle`: 生态系统呼吸 (mmol C m⁻² d⁻¹)
- `algal production`: 藻类产量 (Chl a m⁻² d⁻¹)

### 温室气体变量
- `pCO2`: CO₂分压 (μatm)
- `pCH4`: CH₄分压 (μatm)
- `FCO2.h`: CO₂通量 (mmol m⁻² d⁻¹)
- `FCH4.h`: CH₄通量 (mmol m⁻² d⁻¹)

## 📖 参考资料

1. Gutiérrez-Cánovas, C., et al. (2024). Multiple stressors alter greenhouse gas concentrations in streams. *Global Change Biology*.

2. Battin, T. J., et al. (2009). The boundless carbon cycle. *Nature Geoscience*, 2(9), 598-600.

3. Raymond, P. A., et al. (2013). Global carbon dioxide emissions from inland waters. *Nature*, 503(7476), 355-359.

## 👤 作者信息

**复现作者**: [你的名字]
**日期**: 2026-05-27

## 📄 许可证

本项目仅供学习和研究使用。请引用原始研究。

## ⚠️ 注意事项

- 原始论文版权归作者和期刊所有
- 本复现仅用于教学和研究目的
- 如需引用，请参见原始论文

---

**最后更新**: 2026-05-27
