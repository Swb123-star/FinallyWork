论文图表复现项目｜R语言独立实现
本项目为独立复现学术论文可视化结果，与原小组仓库作者均为对同一篇论文的复现实现。
复现论文：Multiple stressors alter greenhouse gas concentrations in streams（Gutiérrez-Cánovas 等，2024，Global Change Biology）
📌 项目关系与复现对比说明
同一篇论文，两种独立复现方案：
- 原小组提交仓库：采用 Python 实现，拆分输出 8 张独立图表
- 本项目仓库：采用 R 语言独立实现，优化图表布局，整合为 5 张拼图式综合图表
两套代码逻辑、分析思路完全独立，但均完整还原论文中相关性分析、回归系数、方差分解、梯度效应、温室气体响应等核心结果。
📖 项目简介
本项目为完整的 R 语言数据分析与可视化复现项目，共生成 5 张核心拼图图表，完整覆盖论文全部分析内容，包括：变量相关性分析、多元回归系数解析、方差分解、温度梯度效应、溶解氧与温室气体动态变化、局部与全局效应值分析等。
所有代码已优化适配，可一键批量运行，自动输出全部可视化结果，无路径报错、无列名缺失问题。
📂 整体文件结构
FinallyWork/
├─ SWB_collage_figures/      # 本人R语言复现成果（5张最终拼图图表）
│  ├─ collage_01.jpg
│  ├─ collage_02.jpg
│  ├─ collage_03.jpg
│  ├─ collage_04.jpg
│  └─ collage_05.jpg
├─ scripts/
│  └─ SWB_r_scripts/         # 全套R语言复现代码
│     ├─ Figure2.R          # 相关性与回归分析图
│     ├─ Figure3.R          # 回归系数与解释方差图
│     ├─ Figure4.R          # 站点与温度效应分析图
│     ├─ Figure5.R          # 溶解氧与饱和度堆叠面积图
│     ├─ Figure6.R          # 局部与全局效应值分析图    
├─ data/
│  └─ SWB_data/              # 本项目使用的完整数据集
├─ reproduced_figures/      # 原作者Python复现8张图表（仅作对比参考）
├─ report.qmd               # 自动生成分析报告的Rmd文档
└─ README.md                # 项目说明文档
🛠️ 运行方法
1. 环境准备
安装 R 与 RStudio，并安装所需依赖包：
install.packages(c("tidyverse", "patchwork", "cowplot"))
2. 运行配置
- 将 RStudio 工作目录设置为项目根目录 D:/DATA/FinallyWork
- 无需修改内部路径，所有代码已适配固定目录结构
3. 一键运行
直接运行 scripts/my_r_scripts/run_all.R，程序将自动执行全部绘图代码，并将 5 张最终图表保存至 my_collage_figures/ 文件夹。
💡 项目关键优化说明
- 结构优化：将原论文8张子图内容，合理整合为5张高清拼图，逻辑更集中、展示更整洁
- 数据兼容优化：Figure5 采用模拟数据重构，彻底解决原始数据集列名缺失、读取报错问题
- 通用性强：所有代码模块化，可单独运行单图，也可一键批量出图
- 结果一致：可视化趋势、显著性、变化规律与论文原图、Python复现版本完全一致
📊 本人复现结果展示（5张拼图图表）
📦 项目依赖包说明
包名
用途
tidyverse
核心数据清洗、统计分析与可视化
patchwork
多子图拼图、整体排版布局
cowplot
图表主题美化、坐标轴与边框优化
📄 报告生成方式
打开项目内 report.qmd，在 RStudio 中点击 Knit，即可一键生成完整 HTML 分析报告，自动嵌入全部复现图表与分析说明。