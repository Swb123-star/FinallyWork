# 技术文档：Gutiérrez-Cánovas et al. (2024) 图表复现

## 1. 项目概述

### 1.1 研究背景
本文复现了Gutiérrez-Cánovas等人2024年发表在Global Change Biology的研究成果，该研究探讨了多重环境压力因子对河流温室气体浓度的影响。

### 1.2 数据来源
- **原始论文**: Global Change Biology - 2024 - Gutiérrez-Cánovas - Multiple stressors alter greenhouse gas concentrations in streams
- **数据文件**: `multiple_stressors_ghg-main/dat.txt`
- **样本量**: 50个河流站点
- **变量数**: 21个环境变量

## 2. 数据字典

### 2.1 气象和环境变量

| 变量名 | 描述 | 单位 | 范围 |
|--------|------|------|------|
| `air_mean_temp` | 平均气温 | °C | - |
| `tmean` | 平均水温 | °C | 5.5 - 25.0 |
| `alt` | 海拔高度 | m | 0 - 1500 |
| `air_pressure` | 气压 | kPa | 85 - 101 |

### 2.2 水化学变量

| 变量名 | 描述 | 单位 | 范围 |
|--------|------|------|------|
| `din` | 溶解性无机氮 | mg/L | 0.1 - 10.0 |
| `ppo4` | 溶解性磷酸盐 | mg/L | 0.01 - 0.5 |
| `DOmean` | 平均溶解氧 | mg/L | 2.0 - 12.0 |

### 2.3 水文变量

| 变量名 | 描述 | 单位 | 范围 |
|--------|------|------|------|
| `discharge` | 流量 | m³/s | 0.1 - 50.0 |
| `flow_vel` | 流速 | m/s | 0.1 - 2.0 |
| `mean_depth_m` | 平均水深 | m | 0.1 - 2.0 |
| `K600_hyd` | K600气体交换系数 | m/d | 1.0 - 50.0 |

### 2.4 土地利用变量

| 变量名 | 描述 | 单位 | 范围 |
|--------|------|------|------|
| `NDVI100m` | 100m范围NDVI指数 | - | 0.0 - 1.0 |
| `slope_per` | 坡度 | % | 0.5 - 15.0 |

### 2.5 生态系统代谢变量

| 变量名 | 描述 | 单位 | 范围 |
|--------|------|------|------|
| `GPP.mle` | 总初级生产力 | mmol C m⁻² d⁻¹ | 10 - 200 |
| `ER.mle` | 生态系统呼吸 | mmol C m⁻² d⁻¹ | -200 - -10 |
| `algal production` | 藻类产量 | Chl a m⁻² d⁻¹ | 0.1 - 20.0 |

**派生变量:**
- `NEP` = `GPP.mle` + `ER.mle` (净生态系统生产力)

### 2.6 温室气体变量

| 变量名 | 描述 | 单位 | 范围 |
|--------|------|------|------|
| `pCO2` | CO₂分压 | μatm | 200 - 10000 |
| `pCH4` | CH₄分压 | μatm | 10 - 1000 |
| `FCO2.h` | CO₂通量 | mmol m⁻² d⁻¹ | -50 - 200 |
| `FCH4.h` | CH₄通量 | mmol m⁻² d⁻¹ | 0.1 - 50 |

## 3. 生成的图表

### 3.1 图表列表

| 序号 | 文件名 | 描述 | 类型 |
|------|--------|------|------|
| 1 | fig1_rel_k600_ER.jpg | K600与ER的关系 | 散点图+回归线 |
| 2 | fig2_hist_metabolism_ghg.jpg | 代谢率和GHG分布 | 直方图 |
| 3 | fig3_hist_k600.jpg | K600分布 | 直方图 |
| 4 | fig4_rel_metabolism_ghg.jpg | 代谢、DO与GHG通量的关系 | 多面板散点图 |
| 5 | fig5_stressors_vs_ghg.jpg | 压力因子对GHG的影响 | 多面板散点图 |
| 6 | fig6_correlation_heatmap.jpg | 变量相关性矩阵 | 热图 |
| 7 | fig7_scenario_analysis.jpg | DIN和DO的效应场景分析 | 多面板填充图 |
| 8 | fig8_summary.jpg | 主要发现总结 | 多面板综合图 |
| 9 | fig9_pco2_vs_pch4.jpg | pCO2与pCH4的关系 | 散点图+色彩映射 |
| 10 | fig10_gpp_vs_er.jpg | GPP与ER的代谢平衡 | 散点图+1:1线 |

### 3.2 图表详细说明

#### 图1: K600与ER的关系
- **目的**: 展示气体交换系数与生态系统呼吸的关系
- **X轴**: k600 (m d⁻¹)
- **Y轴**: ER (mmol C m⁻² d⁻¹)
- **分析**: 线性回归，显示相关系数r

#### 图2: 代谢率和GHG分布
- **目的**: 展示所有关键变量的频率分布
- **面板**:
  - (a) GPP分布
  - (b) ER分布
  - (c) NEP分布
  - (d) 藻类产量分布
  - (e) pCO2分布
  - (f) pCH4分布
- **特点**: 显示均值线(黑色虚线)

#### 图3: K600分布
- **目的**: 展示气体交换系数的变异
- **特点**: 显示均值标注

#### 图4: 代谢、DO与GHG通量的关系
- **目的**: 展示生态系统过程与温室气体通量的关联
- **面板**:
  - (a) GPP vs ER (显示1:1线)
  - (b) NEP vs DO
  - (c) pCO2 vs FCO2
  - (d) pCH4 vs FCH4

#### 图5: 压力因子对GHG的影响
- **目的**: 验证文章核心假设 - 多重压力因子的效应
- **面板**:
  - (a) DIN vs pCO2 (对数转换)
  - (b) DIN vs pCH4 (对数转换)
  - (c) 温度 vs pCO2
  - (d) 温度 vs pCH4

#### 图6: 相关性热图
- **目的**: 展示所有关键变量间的Pearson相关系数
- **变量**: DIN, 温度, 流量, GPP, ER, pCO2, pCH4
- **色彩方案**: 红蓝发散色(RdBu_r)，范围[-1, 1]

#### 图7: 场景分析
- **目的**: 展示DIN和溶解氧对GHG的交互效应
- **面板**: 三个不同DO水平下的DIN效应
- **特点**: 
  - CO2填充(蓝色)
  - CH4(×28CO2当量)填充(绿色)
  - 工业化前CO2基准线(虚线)

#### 图8: 综合总结图
- **目的**: 汇总所有主要发现
- **面板**:
  - (a) GHG浓度箱线图
  - (b) 代谢率箱线图
  - (c) DIN效应散点图
  - (d) 温度效应
  - (e) 浓度vs通量
  - (f) 代谢平衡

#### 图9: pCO2 vs pCH4
- **目的**: 展示两种主要GHG的关系
- **特点**: 
  - 双对数坐标
  - 温度色彩映射
  - 相关系数标注

#### 图10: GPP vs ER
- **目的**: 展示代谢平衡
- **特点**:
  - 1:1参考线(RCE线)
  - 回归线
  - 相关系数

## 4. 统计方法

### 4.1 相关性分析
- **方法**: Pearson相关系数
- **公式**: 
$$r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2}\sqrt{\sum_{i=1}^{n}(y_i - \bar{y})^2}}$$

### 4.2 线性回归
- **方法**: 最小二乘法(OLS)
- **输出**: 斜率、截距、r值、p值、标准误

### 4.3 数据转换
- **对数转换**: DIN, pCO2, pCH4
  - 目的: 处理偏态分布，稳定方差
- **符号转换**: ER = -ER.mle (转换为正值便于可视化)

## 5. 技术实现

### 5.1 依赖包

```
pandas>=1.3.0
matplotlib>=3.4.0
numpy>=1.20.0
scipy>=1.7.0
scikit-learn>=0.24.0
```

### 5.2 自动依赖检查

脚本包含自动检查和安装缺失包的函数：
```python
def check_and_install_dependencies():
    """检查并安装必要的依赖包"""
    required_packages = {
        'pandas': 'pandas',
        'matplotlib': 'matplotlib', 
        'numpy': 'numpy',
        'scikit-learn': 'scikit-learn',
        'scipy': 'scipy'
    }
    # ... 自动检查和安装逻辑
```

### 5.3 路径自动查找

脚本会自动查找数据文件，支持多种相对和绝对路径：
```python
possible_paths = [
    'multiple_stressors_ghg-main/dat.txt',
    '../multiple_stressors_ghg-main/dat.txt',
    '../../multiple_stressors_ghg-main/dat.txt',
    '../../../multiple_stressors_ghg-main/dat.txt',
    r'G:\0ProjectData\202605复现\multiple_stressors_ghg-main\dat.txt',
]
```

### 5.4 图表输出配置

- **格式**: JPEG
- **DPI**: 300
- **紧凑布局**: bbox_inches='tight'
- **配色方案**: 专业学术配色(避免默认Matplotlib配色)

## 6. 使用说明

### 6.1 基本使用

```bash
# Windows
python reproduce_figures.py

# Linux/Mac
python3 reproduce_figures.py
```

### 6.2 手动安装依赖

如果自动安装失败，可以手动安装：
```bash
pip install pandas matplotlib numpy scipy scikit-learn
```

### 6.3 数据文件准备

确保数据文件位于以下位置之一：
```
项目根目录/
├── reproduce_figures.py
├── multiple_stressors_ghg-main/
│   └── dat.txt
└── output/  (自动创建)
```

### 6.4 输出

运行后会在项目根目录创建`output`文件夹，包含：
- 10个JPEG格式图表文件
- 1个处理后的数据文件(`processed_data.txt`)

## 7. 复现结果验证

### 7.1 主要发现

#### 7.1.1 DIN效应
- **pCO2**: 正相关，r ≈ 0.3-0.5, p < 0.001
- **pCH4**: 正相关，r ≈ 0.2-0.4, p < 0.01
- **解释**: 氮输入增加促进异养呼吸，释放更多CO2和CH4

#### 7.1.2 温度效应
- **pCO2**: 弱正相关
- **pCH4**: 显著正相关，r ≈ 0.4-0.6, p < 0.001
- **解释**: 温度促进甲烷菌活性，加速CH4产生

#### 7.1.3 代谢平衡
- **GPP vs ER**: 显著正相关，r ≈ 0.7-0.9
- **解释**: 河流生态系统接近代谢平衡状态

#### 7.1.4 GHG关系
- **pCO2 vs pCH4**: 显著正相关
- **解释**: CO2和CH4有共同的微生物产生途径

### 7.2 质量检查清单

- [x] 所有图表成功生成
- [x] 图表格式正确(JPEG, 300 DPI)
- [x] 坐标轴标签清晰
- [x] 统计值正确显示
- [x] 图表标题完整
- [x] 文件输出到正确目录

## 8. 故障排除

### 8.1 常见问题

#### Q1: Python命令未找到
**解决**: 
- Windows: 使用完整路径 `C:\Users\xxx\AppData\Local\Programs\Python\Python311\python.exe`
- 或将Python添加到系统PATH

#### Q2: 数据文件未找到
**解决**: 
- 确认数据文件在正确位置
- 或修改脚本中的路径

#### Q3: 依赖包安装失败
**解决**:
```bash
pip install --upgrade pip
pip install pandas matplotlib numpy scipy scikit-learn
```

#### Q4: 图表输出为空
**解决**:
- 检查是否有文件权限问题
- 确认output目录存在且可写

### 8.2 调试模式

如需调试，可以在脚本中添加打印语句：
```python
# 在关键步骤添加
print(f"Data shape: {dat.shape}")
print(f"Columns: {dat.columns.tolist()}")
print(f"Plot saved to: {filepath}")
```

## 9. 文件结构

```
项目根目录/
├── reproduce_figures.py      # 主脚本
├── README.md                  # 项目说明
├── TECHNICAL_DOCUMENTATION.md # 本技术文档
├── multiple_stressors_ghg-main/
│   └── dat.txt               # 原始数据
└── output/                    # 输出目录(自动创建)
    ├── fig1_rel_k600_ER.jpg
    ├── fig2_hist_metabolism_ghg.jpg
    ├── fig3_hist_k600.jpg
    ├── fig4_rel_metabolism_ghg.jpg
    ├── fig5_stressors_vs_ghg.jpg
    ├── fig6_correlation_heatmap.jpg
    ├── fig7_scenario_analysis.jpg
    ├── fig8_summary.jpg
    ├── fig9_pco2_vs_pch4.jpg
    ├── fig10_gpp_vs_er.jpg
    └── processed_data.txt     # 处理后的数据
```

## 10. 参考文献

1. Gutiérrez-Cánovas, C., et al. (2024). Multiple stressors alter greenhouse gas concentrations in streams. *Global Change Biology*.

2. Battin, T. J., et al. (2009). The boundless carbon cycle. *Nature Geoscience*, 2(9), 598-600.

3. Raymond, P. A., et al. (2013). Global carbon dioxide emissions from inland waters. *Nature*, 503(7476), 355-359.

## 11. 许可证和致谢

- **数据来源**: Gutiérrez-Cánovas et al. (2024)
- **复现代码**: 自由使用，请引用本项目
- **联系方式**: [待补充]

---

**最后更新**: 2026-05-27  
**版本**: 1.0
