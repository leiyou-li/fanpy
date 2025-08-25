# 🚀 GitHub 上传和工作流测试指南

## 📁 需要上传的文件

以下是需要上传到你的GitHub仓库的所有文件：

### 1. GitHub Actions 工作流文件
```
.github/
├── workflows/
│   ├── sync-upstream.yml              # 基础上游同步工作流
│   ├── sync-upstream-advanced.yml     # 高级上游同步工作流（推荐）
│   └── sync-sites.yml                 # 独立的sites配置同步工作流
├── README.md                          # 工作流使用说明
└── sync-config.yml                    # 配置文件说明
```

### 2. 同步脚本
```
scripts/
└── sync_sites.py                      # Sites配置同步脚本
```

### 3. 配置文件（如果还没有）
```
spider.json                            # 源配置文件
moyun.json                             # 目标配置文件
```

## 🔧 上传步骤

### 方法1: 通过GitHub网页界面
1. 访问你的fork仓库页面
2. 点击 "Add file" → "Upload files"
3. 将以下文件夹和文件拖拽上传：
   - `.github/` 整个文件夹
   - `scripts/` 整个文件夹
   - `UPLOAD_GUIDE.md`（本文件）

### 方法2: 通过Git命令（如果你有本地Git环境）
```bash
# 添加所有文件
git add .github/ scripts/ UPLOAD_GUIDE.md

# 提交变更
git commit -m "🔧 Add automated sync workflows and sites sync functionality

- Add upstream sync workflows (basic & advanced)
- Add sites configuration sync script
- Add comprehensive documentation
- Support for automatic sites sync from spider.json to moyun.json"

# 推送到GitHub
git push origin main
```

## 🧪 测试工作流

### 1. 测试Sites同步工作流
上传完成后，可以立即测试sites同步功能：

1. 访问你的仓库 → **Actions** 页面
2. 选择 "**Sync Sites Configuration**" 工作流
3. 点击 "**Run workflow**" 按钮
4. 选择预览模式进行测试：
   - ✅ 勾选 "预览模式（不实际修改文件）"
   - 点击 "Run workflow"

### 2. 测试上游同步工作流
测试与上游仓库的同步：

1. 在Actions页面选择 "**Advanced Upstream Sync**"
2. 点击 "**Run workflow**"
3. 可选择是否强制同步
4. 观察运行结果

## 📊 工作流功能说明

### 🔄 上游同步功能
- **自动运行**: 每天北京时间08:00
- **手动触发**: 随时在Actions页面手动运行
- **安全备份**: 同步前自动创建备份分支
- **智能合并**: 优先尝试合并，冲突时安全重置
- **详细报告**: 提供完整的同步状态和变更信息

### 🔧 Sites配置同步功能
- **自动触发**: 当`spider.json`文件发生变化时
- **定时运行**: 每天北京时间08:30额外运行
- **预览模式**: 支持预览变更而不实际修改文件
- **数据验证**: 自动验证配置项的完整性
- **备份保护**: 修改前自动创建备份文件

## 🎯 预期结果

### Sites同步成功后：
1. `moyun.json` 中的 `sites` 数组将包含 `spider.json` 中的所有sites配置
2. 配置会保持JSON格式的正确性
3. 原有的 `parses`、`flags`、`lives` 等配置保持不变
4. 生成详细的同步报告和统计信息

### 上游同步成功后：
1. 你的fork仓库将包含上游的最新内容
2. Sites配置会自动从更新的 `spider.json` 同步到 `moyun.json`
3. 生成完整的同步报告
4. 创建备份分支以保护你的修改

## 🔍 验证同步结果

### 检查sites同步：
1. 查看 `moyun.json` 文件的 `sites` 数组
2. 确认sites数量和内容与 `spider.json` 一致
3. 检查是否有 `sync_info` 字段记录同步信息

### 检查工作流状态：
1. 在Actions页面查看运行历史
2. 查看详细的运行日志
3. 检查生成的摘要报告

## 🚨 故障排除

### 常见问题：
1. **权限问题**: 确保仓库设置中启用了Actions并具有写权限
2. **文件格式**: 确保JSON文件格式正确
3. **路径问题**: 文件需要在仓库根目录

### 调试方法：
1. 使用预览模式测试sites同步
2. 查看Actions页面的详细日志
3. 检查是否有自动创建的Issue（失败通知）

## 📈 后续优化

成功运行后，你可以：
1. 调整运行时间（修改cron表达式）
2. 自定义同步规则
3. 添加更多的自动化功能
4. 配置邮件或其他通知方式

---

💡 **提示**: 建议先测试sites同步工作流，确认功能正常后再测试上游同步功能。

🔗 **相关文档**: 
- [GitHub Actions使用说明](.github/README.md)
- [同步配置说明](.github/sync-config.yml)