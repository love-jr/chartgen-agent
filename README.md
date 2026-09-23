# ChartGen-Agent

**A Three-Stage Framework for Automated High-Quality Chart Generation**

本仓库是论文的实验代码，发表于 ADMA 2025（LNCS 16200, pp. 19–32）。DOI: [10.1007/978-981-95-3462-3_2](https://doi.org/10.1007/978-981-95-3462-3_2)

---

## 三阶段框架

把「从主题到成图」拆成三个阶段，每个阶段独立可替换：

| 阶段 | 做什么 | 代码位置 |
|---|---|---|
| ① 数据生成 | 依据主题与图表类型，生成符合现实逻辑的图表数据 | `src/*/data_generator.py` |
| ② 代码生成 | 把数据转成 R/ggplot2 绘图代码 | `src/*/code_generator.py` |
| ③ 评估与优化 | 对成图打分；低于阈值则依据评语优化代码并重新出图 | `src/code_optimazation/` |

```
主题 + 图表类型
   ↓ ① 数据生成
   图表数据(JSON)
   ↓ ② 代码生成
   ggplot2 代码
   ↓ Rscript 出图
   成图 → ③ 评估打分 ──低于阈值──→ 优化代码 ──→ 重新出图
                └──达到阈值──→ 输出
```

阶段 ③ 每项 0–2 分共 10 分，五个维度分别依据 Cleveland 认知感知理论、Tufte 数据墨水比、Web 内容无障碍指南、孟塞尔色彩体系与 UI 设计规范。提示词见 `config/prompts/eval_chart*.txt`、`last_optimazation*.txt`。

## 环境准备

**Python**
```bash
pip install -r requirements.txt
```

**R 环境**（阶段 ② 的产物是 R 代码，必需）
```r
install.packages(c("ggplot2", "ggrepel", "hrbrthemes", "bbplot",
                   "ggsci", "ggthemes", "dplyr"))
```

**API 密钥**（通过环境变量提供，可复制 `.env.example` 为 `.env`：

| 环境变量 | 服务 | 对应模型 |
|---|---|---|
| `IFOPEN_API_KEY` | beta.ifopen.ai | GPT-4o / GPT-4 / o1 |
| `AIGCBEST_API_KEY` | aigcbest.top | Claude 3.7 Sonnet |
| `ARK_API_KEY` | 火山引擎方舟 | DeepSeek-V3、DouBao、GLM3 等 |
| `QIANFAN_API_KEY` | 百度千帆 | ERNIE、QwQ-32B、DeepSeek-R1-Distill 系列 |

**输出目录**：默认写到项目根的 `output/`（已 gitignore），可用 `CHARTGEN_OUTPUT_DIR` 改到别处。

## 运行

```bash
# 单条生成（需在对应子目录下运行）
cd src/code_withTemplate    && python main.py    # 带模板
cd src/code_withoutTemplate && python main.py    # 不带模板

# 实验
cd src/eval && python experiment1.py
```

首次试跑请先把 `main.py` 里的 `NUM_ITERATIONS` 调小。

辅助脚本（会改动文件系统，务必先加 `--dry-run`）：
```bash
python src/eval/count.py [目录]                 # 统计子文件夹数
python src/eval/delete.py <目录> --dry-run       # 列出缺少 R/png/json 的目录
python src/eval/chage_name.py <目录> --dry-run   # 按序重命名为 chart_0001…
```

## 实验

框架支持两条路线，用于对比「是否给定参考模板」的影响：带模板用 `code_generation_template.txt`（模板取自 `config/list.py`），不带模板用 `code_generation.txt`。

| 脚本 | 内容 |
|---|---|
| `experiment1.py` | 带模板路线：多模型批量生成 + 评估 |
| `experiment3.py` | 不带模板路线：多模型批量生成 + 评估 |
| `experiment2.py` | 对已生成结果批量评估 |
| `experiment4.py` | 优化前后得分对比 |
| `generate_datasets.py` | 数据集批量生成 |

参与对比的模型：GPT-4o、Claude 3.7 Sonnet、DeepSeek-V3、DouBao、ERNIE、QwQ-32B，经 API 部署的开源模型（R1-Distill-Llama-70B、R1-Distill-Qwen-32B/7B、GLM3、Mistral-7B、Moonshot），以及本地推理的 Qwen2.5-7B/1.5B/0.5B-Instruct。

生成规模：9 种图表类型、15 种主题、24 种配色、395 个选题、13 套提示词模板。原始得分见 `src/eval/results.txt`、`result4.txt`。

## 目录结构

```
config/
  list.py                图表类型、主题、配色、模板定义
  prompts/               提示词模板（中英双语）
src/
  code_withTemplate/     带模板路线
  code_withoutTemplate/  不带模板路线
  code_optimazation/     阶段 ③：评分与代码优化
  eval/                  多模型对比与消融实验
  utils/                 API 客户端、配置与输出路径解析
```

## 说明

仓库内的 `*.png`、`Rplots.pdf`、`*.log`、`*_scores.json` 为历史实验产物，运行不需要。`src/eval/ex4/` 是论文之外的早期探索代码，一并保留供参考。
