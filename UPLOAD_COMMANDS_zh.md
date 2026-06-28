# GitHub 上传步骤

以下命令在 PowerShell 中执行。

## 1. 进入公开仓库目录

```powershell
cd "path\to\RAAMR_public_release"
```

## 2. 初始化 Git 仓库

```powershell
git init
git add .
git commit -m "Initial public verification release"
```

如果本机没有配置 Git 用户名和邮箱，可以先执行：

```powershell
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

AAAI 匿名审稿阶段建议使用不暴露真实姓名和单位的账号。

## 3. 在 GitHub 创建仓库

建议仓库名：

```text
RAAMR
```

如果需要匿名投稿，可以使用匿名账号创建公开仓库，或者先建 private 仓库，等投稿版本确认后再公开。

## 4. 绑定远程仓库并推送

把下面的地址替换成你自己的 GitHub 仓库地址：

```powershell
git remote add origin https://github.com/<your-account>/RAAMR.git
git branch -M main
git push -u origin main
```

## 5. 上传前检查

上传前请再次确认不要包含以下内容：

- 原始完整训练脚本。
- 模型 checkpoint 或预训练权重。
- 私有 FFDM、DBT、C-view 图像。
- 真实结构化报告 JSON。
- 真实 patient_id、医院名称、服务器路径。
- 训练日志、预测 CSV、可追溯到患者的可视化图。

当前目录已经配置 `.gitignore`，但仍建议在 `git add .` 后执行：

```powershell
git status
```

确认暂存文件只包含公开模板和工具脚本。
