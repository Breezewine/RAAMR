# RAAMR 公开仓库上传说明

这个文件用于说明哪些内容适合上传到 GitHub，哪些内容不建议公开。

## 建议上传的内容

- `README.md`：说明论文任务、仓库用途、数据格式、评价方式和代码开放范围。
- `requirements.txt`：列出运行评价和预处理脚本所需依赖。
- `configs/example_config.yaml`：只保留占位路径，避免暴露服务器目录、私有数据路径和真实患者信息。
- `raamr/preprocessing.py`：图像读取、灰度归一化、CLAHE、等比例缩放和 padding 等通用预处理。
- `raamr/data_schema.py`：患者级 CSV 和结构化文本 JSON 的格式检查。
- `examples/`：只放合成示例，不放真实病例。

## 不建议上传的内容

- `train_multiview_dbt_metanet_controlled.py` 原始完整文件。
- `ControlledDBTMetaNetModel` 的完整实现。
- Meta-Net、自适应提示、可学习上下文向量、DBT gate、top-K patch 检索、跨模态注意力融合等核心创新代码。
- 真实结构化报告 JSON 文件。
- 私有 FFDM、DBT、C-view 图像。
- 模型权重、checkpoint、训练日志、包含真实 patient_id 的预测文件。
- 服务器路径、医院路径、医生标注文件和原始报告文本。

## 对外表述建议

可以在 README 中说明：公开仓库提供数据格式、预处理、评价协议和复核脚本；完整模型代码和权重由于论文仍在审稿、涉及知识产权保护和临床数据治理，暂不公开。这样的表述比直接说“核心算法不公开，防止被窃取”更适合论文投稿和 GitHub 页面。

## 后续投稿时的写法

论文中可以写：

“We provide a public verification repository containing data-format specifications, preprocessing utilities, evaluation scripts, and configuration templates. The complete training implementation and model weights will be released after publication subject to institutional data-governance approval.”

如果审稿阶段要求匿名，GitHub 仓库需要匿名化。可以使用匿名 GitHub 账号，避免 README、commit、路径和文件中出现作者姓名、单位、医院名称或真实数据路径。
