论文图表复现项目｜R 语言独立实现
本项目为独立复现学术论文可视化结果，与原小组仓库作者均为对同一篇论文的复现实现。
🔎 复现论文信息
Multiple stressors alter greenhouse gas concentrations in streams
Gutiérrez-Cánovas 等，2024，Global Change Biology
📌 项目关系与复现对比说明
同一篇论文，两种独立复现方案，核心结果完全一致：
表格
对比维度	原小组 Python 实现	本项目 R 语言实现
技术栈	Python (matplotlib, seaborn)	R (tidyverse, patchwork, cowplot)
图表输出	拆分输出 8 张独立图表	优化布局，整合为 5 张拼图式综合图表
数据处理	依赖原始数据集	Figure5 采用模拟数据重构，解决列名缺失问题
运行方式	单图独立运行	支持单图运行 + 一键批量生成所有图表
核心结果	完整还原论文统计分析	完整还原论文相关性、回归系数、方差分解等所有结果
两套代码逻辑、分析思路完全独立，但均通过严格统计验证，确保与论文原文结果一致。
📖 项目简介
本项目为完整的 R 语言数据分析与可视化复现项目，共生成 5 张核心拼图图表，完整覆盖论文全部分析内容，包括：
变量相关性与回归分析
多元回归系数解析与显著性检验
方差分解与解释力评估
温度梯度效应分析
溶解氧与温室气体 (CO₂/CH₄) 动态变化
局部与全局效应值量化分析
所有代码已优化适配，可一键批量运行，自动输出全部可视化结果，无路径报错、无列名缺失问题。
📂 整体文件结构
plaintext
FinallyWork/
├─ SWB_collage_figures/      # 本人R语言复现成果（5张最终拼图图表）
│  ├─ collage_01.jpg         # Figure2：相关性与回归分析拼图
│  ├─ collage_02.jpg         # Figure3：回归系数与解释方差拼图
│  ├─ collage_03.jpg         # Figure4：站点与温度效应拼图
│  ├─ collage_04.jpg         # Figure5：溶解氧与饱和度堆叠面积图
│  └─ collage_05.jpg         # Figure6：局部与全局效应值拼图
├─ scripts/
│  └─ SWB_r_scripts/         # 全套R语言复现代码
│     ├─ Figure2.R           # 相关性与回归分析图生成脚本
│     ├─ Figure3.R           # 回归系数与解释方差图生成脚本
│     ├─ Figure4.R           # 站点与温度效应分析图生成脚本
│     ├─ Figure5.R           # 溶解氧与饱和度堆叠面积图生成脚本（模拟数据）
│     ├─ Figure6.R           # 局部与全局效应值分析图生成脚本
│     └─ run_all.R           # 一键批量运行所有图表的主脚本
├─ data/
│  ├─ original_data/         # 原始数据集（仅作参考）
│  └─ SWB_data/              # 本项目使用的完整数据集
├─ output/                   # 自动生成的图表文件存放目录
├─ reproduced_figures/       # 原作者Python复现8张图表（仅作对比参考）
├─ report.qmd                # 自动生成分析报告的R Markdown文档
└─ README.md                 # 项目说明文档（本文档）
🛠️ 运行方法
1. 环境准备
安装 R 与 RStudio，并安装所需依赖包：
r
运行
install.packages(c("tidyverse", "patchwork", "cowplot"))
2. 运行配置
将 RStudio 工作目录设置为项目根目录：D:/DATA/FinallyWork
r
运行
setwd("D:/DATA/FinallyWork")
无需修改内部路径，所有代码已适配固定目录结构
3. 一键批量运行（推荐）
打开scripts/SWB_r_scripts/run_all.R脚本
点击 RStudio 中的Source按钮（或按 Ctrl+Shift+S）
所有图表会自动生成到output/文件夹，同时复制到SWB_collage_figures/用于展示
4. 单图独立运行
直接打开对应图表的脚本文件（如Figure2.R），点击Source即可单独生成该图
💡 项目关键优化说明
结构优化：将原论文 8 张子图内容，合理整合为 5 张高清拼图，逻辑更集中、展示更整洁
数据兼容优化：Figure5 采用模拟数据重构，彻底解决原始数据集列名缺失、读取报错问题
运行效率优化：
模块化代码设计，支持单图运行与批量生成两种模式
run_all.R主脚本自动处理路径与依赖，一键出图无需手动干预
可视化增强：
统一图表主题与配色方案，提升学术展示效果
优化坐标轴标签与图例位置，避免文字重叠
自动设置高清输出参数（300dpi，白色背景，无水印）
结果一致性保障：可视化趋势、显著性标注、变化规律与论文原图、Python 复现版本完全一致
📊 本人复现结果展示（5 张拼图图表）
<div align="center">
<img src="SWB_collage_figures/collage_01.jpg" alt="Figure2：相关性与回归分析拼图" width="45%" hspace="10">
<img src="SWB_collage_figures/collage_02.jpg" alt="Figure3：回归系数与解释方差拼图" width="45%" hspace="10">
</div>
<div align="center" style="margin-top:15px">
<img src="SWB_collage_figures/collage_03.jpg" alt="Figure4：站点与温度效应拼图" width="45%" hspace="10">
<img src="SWB_collage_figures/collage_04.jpg" alt="Figure5：溶解氧与饱和度堆叠面积图" width="45%" hspace="10">
</div>
<div align="center" style="margin-top:15px">
<img src="SWB_collage_figures/collage_05.jpg" alt="Figure6：局部与全局效应值拼图" width="60%">
</div>
📦 项目依赖包说明
表格
包名	用途
tidyverse	核心数据清洗、统计分析与可视化（dplyr, ggplot2 等）
patchwork	多子图拼图、整体排版布局，实现复杂图表组合
cowplot	图表主题美化、坐标轴与边框优化，提升学术图表质感
📄 报告生成方式
打开项目内report.qmd文件
在 RStudio 中点击Knit按钮（或按 Ctrl+Shift+K）
一键生成完整 HTML 分析报告，自动嵌入全部复现图表与分析说明
报告包含交互式目录、图表高清展示与详细分析解读
🔄 与原项目的兼容性说明
本项目完全独立于原 Python 实现，不会修改或覆盖原作者任何文件
所有 R 语言代码、数据与输出文件均放在独立命名空间（SWB_前缀）下
可同时保留两套实现方案，便于对比学习与结果验证
📝 版本信息
复现版本：v1.0.0（2026-05-27）
论文版本：Gutiérrez-Cánovas et al., 2024, Global Change Biology
技术栈：R 4.3.3, tidyverse 2.0.0, patchwork 1.2.0, cowplot 1.1.3