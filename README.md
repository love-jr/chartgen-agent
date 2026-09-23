# ChartGen-Agent

**A Three-Stage Framework for Automated High-Quality Chart Generation**

本仓库是该论文的实验代码实现：一套自动生成高质量图表的 Agent 框架，以及配套的多模型对比与消融实验脚本。

---

## 三阶段框架

框架把「从主题到成图」拆成三个阶段，每个阶段独立可替换：

| 阶段 | 做什么 | 代码位置 |
|---|---|---|
| **① 数据生成** | 依据主题与图表类型，生成符合现实逻辑的图表数据 | `src/*/data_generator.py` |
| **② 代码生成** | 把数据转成 R/ggplot2 绘图代码 | `src/*/code_generator.py` |
| **③ 评估与优化** | 对渲染出的成图打分；低于阈值则依据评语优化代码并重新出图 | `src/code_optimazation/` |

整体流程：

```
主题 + 图表类型
   ↓ ① 数据生成
   图表数据(JSON)
   ↓ ② 代码生成
   ggplot2 代码
   ↓ 执行 Rscript 出图
   成图 → ③ 评估打分 ──低于阈值──→ 优化代码 ──→ 重新出图
                └──达到阈值──→ 输出
```

### 阶段 ③ 的评分维度

每项 0–2 分，共 10 分，评分依据取自可视化领域的既有准则：

| 维度 | 依据 |
|---|---|
| 信息表达直观性（Expression） | Cleveland 的认知感知理论 |
| 整体美观度（Aesthetic） | Tufte 的数据墨水比 |
| 内容可读性（Readability） | Web 内容无障碍指南（字号、数据点重叠率、坐标轴设置） |
| 色彩协调性（Color） | 孟塞尔色彩体系 |
| 布局合理性（Layout） | UI 设计规范（元素间距、图层冗余） |

评分与优化提示词见 `config/prompts/eval_chart*.txt`、`last_optimazation*.txt`。

## 实验代码

### 两种生成路线（消融维度）

框架支持两条路线，用于对比「是否给定参考模板」对成图质量的影响：

| 路线 | 目录 | 使用的提示词 |
|---|---|---|
| 带模板 | `src/code_withTemplate/` | `config/prompts/code_generation_template.txt`，模板取自 `config/list.py` |
| 不带模板 | `src/code_withoutTemplate/` | `config/prompts/code_generation.txt` |

### 实验脚本

| 脚本 | 内容 |
|---|---|
| `src/eval/experiment1.py` | 带模板路线：多模型批量生成 + 评估 |
| `src/eval/experiment3.py` | 不带模板路线：多模型批量生成 + 评估 |
| `src/eval/experiment2.py` | 对已生成结果批量评估 |
| `src/eval/experiment4.py` | 优化前后对比（同一批图表优化前后的得分变化） |
| `src/eval/generate_datasets.py` | 数据集批量生成 |

### 对比的模型

实验脚本中配置了以下模型（密钥按服务商分组，见下方环境准备）：

- **闭源/商用**：GPT-4o、Claude 3.7 Sonnet、DeepSeek-V3、DouBao、ERNIE、QwQ-32B
- **开源（经 API 部署）**：DeepSeek-R1-Distill-Llama-70B、DeepSeek-R1-Distill-Qwen-32B/7B、GLM3、Mistral-7B、Moonshot
- **本地推理**：Qwen2.5-7B / 1.5B / 0.5B-Instruct（`LocalModelClient`）

### 生成规模

| 项目 | 规模 |
|---|---|
| 图表类型 | 9 种（折线 / 饼图 / 柱状 / 分组条形等） |
| 主题风格 | 15 种（`theme_*`） |
| 配色方案 | 24 种（`scale_color_*`） |
| 选题库 | 395 个跨领域主题 |
| 提示词模板 | 13 套（中英双语） |

实验原始得分记录在 `src/eval/results.txt`、`result4.txt` 等文件中。

---

## 环境准备

**Python 依赖**

```bash
pip install -r requirements.txt
```

**R 环境**（阶段 ② 的产物是 R 代码，必需）

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

生成的图表与数据默认写到项目根目录的 `output/`（已 gitignore）。可用环境变量改到别处：

```bash
export CHARTGEN_OUTPUT_DIR=/your/output/path
```

## 运行

```bash
# 单条生成（需在对应子目录下运行）
cd src/code_withTemplate    && python main.py    # 带模板
cd src/code_withoutTemplate && python main.py    # 不带模板

# 实验
cd src/eval && python experiment1.py
```

生成脚本用 `ThreadPoolExecutor` 并发，迭代次数定义在 `main.py` 的 `NUM_ITERATIONS`，首次试跑请先调小。

辅助脚本：

```bash
python src/eval/count.py [目录]                    # 统计输出目录下的子文件夹数
python src/eval/delete.py <目录> --dry-run          # 列出缺少 R/png/json 的目录
python src/eval/chage_name.py <目录> --dry-run      # 按序重命名为 chart_0001…
```

> `delete.py` 与 `chage_name.py` 会改动文件系统，**务必先加 `--dry-run` 确认**。

## 目录结构

```
config/
  list.py                图表类型、主题、配色、模板定义
  prompts/               提示词模板（中英双语）
src/
  code_withTemplate/     带模板路线（数据生成 → 代码生成 → 出图）
  code_withoutTemplate/  不带模板路线
  code_optimazation/     阶段 ③：评分与代码优化
  eval/                  多模型对比与消融实验
  utils/                 API 客户端、配置与输出路径解析
```

各生成脚本通过 `sys.path` 引用项目根目录，请在对应子目录下运行。

## 引用

如果本工作对你有帮助，欢迎引用：

```bibtex
@article{chartgenagent,
  title   = {ChartGen-Agent: A Three-Stage Framework for Automated High-Quality Chart Generation},
  author  = {TO BE FILLED},
  journal = {TO BE FILLED},
  year    = {TO BE FILLED}
}
```

> 作者、发表信息与 DOI 请在论文正式发表后补全。

## 说明

- 仓库内的 `*.png`、`Rplots.pdf`、`*.log`、`*_scores.json` 为历史实验产物，运行不需要。
- 论文未包含的内容（如 `src/eval/ex4/` 下的早期探索代码）也一并保留，供复现参考。
