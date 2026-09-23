# ChartGen Agent

用大模型生成 R/ggplot2 图表代码的 Agent。模型先生成贴合主题的数据，再生成绘图代码，由本地 `Rscript` 实际执行出图；成图经模型自动评分，低于阈值则回炉优化重出。内置多模型对比实验，用于评测不同模型画图的能力差异。

## 工作流程

```
主题 → 选图表类型 → 生成数据(JSON) → 生成 ggplot2 代码
     → Rscript 执行出图 → 自动评分 → 低于阈值则优化代码重出
```

各环节对应的代码位置：

| 环节 | 位置 |
|---|---|
| 数据生成 | `src/code_withTemplate/data_generator.py` |
| 代码生成 | `src/code_withTemplate/code_generator.py`（带模板）、`src/code_withoutTemplate/`（不带模板） |
| 执行出图 | `code_executor.py`：`subprocess` 调 `Rscript`，并自动补全缺失的 `library()` |
| 评分与优化 | `src/code_optimazation/eval_chart.py`、`optimize_code.py` |
| 对比实验 | `src/eval/experiment1..4.py`、`generate_datasets.py` |

## 环境准备

**Python 依赖**

```bash
pip install -r requirements.txt
```

**R 环境**（生成的代码是 R 代码，必需）

本机需有 `Rscript` 及以下 R 包：

```r
install.packages(c("ggplot2", "ggrepel", "hrbrthemes", "bbplot",
                   "ggsci", "ggthemes", "dplyr"))
```

**API 密钥**

密钥通过环境变量提供，不写进源码。可复制 `.env.example` 为 `.env` 填入，也可直接 `export`。

| 环境变量 | 服务 | 对应模型 |
|---|---|---|
| `IFOPEN_API_KEY` | beta.ifopen.ai | GPT-4o / GPT-4 / o1 |
| `AIGCBEST_API_KEY` | aigcbest.top | Claude 3.7 Sonnet |
| `ARK_API_KEY` | 火山引擎方舟 | DeepSeek-V3、DouBao、GLM3 等 |
| `QIANFAN_API_KEY` | 百度千帆 | ERNIE、QwQ-32B、DeepSeek-R1-Distill 系列 |

**输出目录**

生成的图表和数据默认写到项目根目录的 `output/` 下（已 gitignore）。如需改到别处，设置 `CHARTGEN_OUTPUT_DIR`：

```bash
export CHARTGEN_OUTPUT_DIR=/your/output/path
```

## 运行

```bash
# 生成（需在对应子目录下运行）
cd src/code_withTemplate    && python main.py    # 带模板
cd src/code_withoutTemplate && python main.py    # 不带模板

# 多模型对比实验
cd src/eval && python experiment1.py
```

生成脚本用 `ThreadPoolExecutor` 并发，默认迭代次数较高（带模板流程为 3500）。首次试跑请先把 `main.py` 里的 `NUM_ITERATIONS` 调小。

辅助脚本：

```bash
python src/eval/count.py [目录]           # 统计输出目录下的子文件夹数
python src/eval/delete.py <目录> --dry-run # 列出缺少 R/png/json 的目录
python src/eval/chage_name.py <目录> --dry-run  # 按序重命名为 chart_0001…
```

> `delete.py` 与 `chage_name.py` 会改动文件系统，**务必先加 `--dry-run` 确认**。

## 目录结构

```
config/
  list.py                图表主题、类型、配色、模板定义
  prompts/               提示词模板（中英双语）
src/
  code_withTemplate/     带模板的生成流程
  code_withoutTemplate/  不带模板的生成流程
  code_optimazation/     评分与代码优化
  eval/                  多模型对比实验
  utils/                 API 客户端与配置
```

## 项目规模

| 指标 | 数值 |
|---|---|
| Python 代码 | 39 个文件，约 7,300 行 |
| 图表类型 | 9 种，搭配 15 种主题、24 种配色 |
| 选题库 | 395 个跨领域主题（政治、社会文化、经济科技、媒体传播） |
| 提示词模板 | 13 套（中英双语） |
| 模型配置 | 14 个 |
| 实验产物 | 40 张生成图表及评分记录（`src/eval/results.txt`） |

## 自动评分维度

每项 0–2 分，评分依据取自可视化领域的既有准则：

| 维度 | 依据 |
|---|---|
| 信息表达直观性 | Cleveland 的认知感知理论 |
| 整体美观度 | Tufte 的数据墨水比 |
| 内容可读性 | Web 内容无障碍指南（字号、数据点重叠率、坐标轴设置） |
| 色彩协调性 | 孟塞尔色彩体系 |
| 布局合理性 | UI 设计规范（元素间距、图层冗余） |

## 说明

仓库内的 `*.png`、`Rplots.pdf`、`*.log`、`*_scores.json` 为历史实验产物，运行不需要。
