# ChartGen Agent

用大模型生成 R/ggplot2 图表代码的 Agent：模型先生成数据，再生成绘图代码，最后本地执行 `Rscript` 出图。支持多轮"评分 → 优化"迭代，并在多模型间做对比实验。

## 工作流程

```
主题 → 选图表类型 → LLM 生成数据(JSON) → LLM 生成 ggplot2 代码
     → Rscript 执行出图 → LLM 评分 → 低于阈值则优化代码 → 重新出图
```

- **数据生成**：`src/code_withTemplate/data_generator.py`
- **代码生成**：`src/code_withTemplate/code_generator.py`（带模板）／`src/code_withoutTemplate/`（不带模板）
- **执行出图**：`code_executor.py` 用 `subprocess` 调 `Rscript`，并自动补 `library()` 声明
- **评分与优化**：`src/code_optimazation/eval_chart.py`、`optimize_code.py`
- **对比实验**：`src/eval/experiment1..4.py`、`generate_datasets.py`

## 环境准备

### 1. Python 依赖

```bash
pip install -r requirements.txt
```

### 2. R 环境（必需）

生成的代码是 R 代码，需要本机有 `Rscript` 以及以下 R 包：

```r
install.packages(c("ggplot2", "ggrepel", "hrbrthemes", "bbplot",
                   "ggsci", "ggthemes", "dplyr"))
```

### 3. API 密钥（**不要写进源码**）

密钥通过环境变量提供。项目根目录放一个 `.env`（已 gitignore）即可：

```
ARK_API_KEY=你的火山引擎方舟密钥
QIANFAN_API_KEY=你的百度千帆密钥
IFOPEN_API_KEY=你的 ifopen 密钥
AIGCBEST_API_KEY=你的 aigcbest 密钥
```

各变量对应的服务：

| 环境变量 | 服务 | 用途 |
|---|---|---|
| `IFOPEN_API_KEY` | beta.ifopen.ai | gpt-4o / gpt-4 / o1 |
| `AIGCBEST_API_KEY` | aigcbest.top | claude-3-7-sonnet |
| `ARK_API_KEY` | 火山引擎方舟 | deepseek-v3、doubao-vision、GLM3 等 |
| `QIANFAN_API_KEY` | 百度千帆 | ernie-x1-32k、qwq-32b、deepseek-r1-distill-llama-70b |

> 也可以直接 `export ARK_API_KEY=xxx` 而不建 `.env`。

## 目录结构

```
config/
  list.py                图表主题、类型、配色、模板定义
  prompts/               提示词模板（中英双语）
src/
  code_withTemplate/     带模板的生成流程
  code_withoutTemplate/  不带模板的生成流程
  code_optimazation/     评分 + 代码优化流程
  eval/                  多模型对比实验
  utils/                 API 客户端与配置
```

## 运行

```bash
# 带模板生成（在 src/code_withTemplate 目录下运行）
cd src/code_withTemplate && python main.py

# 不带模板生成
cd src/code_withoutTemplate && python main.py

# 对比实验
cd src/eval && python experiment1.py
```

> 生成脚本内部用 `ThreadPoolExecutor` 并发，默认迭代次数较高（如 3500）。首次试跑请先把 `num_iterations` 调小。

## 说明

- 仓库内附带的 `*.png`、`Rplots.pdf`、`*.log`、`*_scores.json` 是历史实验产物，不是运行必需。
- 本仓库原本把密钥硬编码在 `src/utils/api_config*.py` 中，现已全部改为读取环境变量。
