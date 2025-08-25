# 📋 文件上传清单

## 📁 需要上传到GitHub的文件

### ✅ 必需文件（核心功能）

#### 1. GitHub Actions 工作流文件
- [ ] `.github/workflows/sync-upstream.yml` - 基础上游同步工作流
- [ ] `.github/workflows/sync-upstream-advanced.yml` - 高级上游同步工作流（推荐）
- [ ] `.github/workflows/sync-sites.yml` - Sites配置同步工作流

#### 2. 同步脚本
- [ ] `scripts/sync_sites.py` - Sites配置同步核心脚本

### 📚 文档文件（推荐上传）

- [ ] `.github/README.md` - GitHub Actions使用说明
- [ ] `.github/sync-config.yml` - 配置参数说明
- [ ] `UPLOAD_GUIDE.md` - 上传和测试指南
- [ ] `FILES_CHECKLIST.md` - 本文件清单

### 🧪 测试文件（可选）

- [ ] `test_sync.py` - 本地测试脚本（可在上传前测试功能）

## 📂 文件结构预览

上传后你的仓库结构将是这样的：

```
your-repo/
├── .github/
│   ├── workflows/
│   │   ├── sync-upstream.yml
│   │   ├── sync-upstream-advanced.yml
│   │   └── sync-sites.yml
│   ├── README.md
│   └── sync-config.yml
├── scripts/
│   └── sync_sites.py
├── base/                              # 原有文件
│   ├── localProxy.py
│   └── spider.py
├── plugin/                            # 原有文件
│   └── ...
├── spider.json                        # 原有文件（源配置）
├── moyun.json                         # 原有文件（目标配置）
├── README.md                          # 原有文件
├── UPLOAD_GUIDE.md                    # 新增
├── FILES_CHECKLIST.md                 # 新增
└── test_sync.py                       # 新增（可选）
```

## 🚀 上传方式

### 方法1: GitHub网页界面（推荐）
1. 访问你的仓库页面
2. 点击 "Add file" → "Create new file"
3. 逐个创建文件并复制内容，或者
4. 点击 "Upload files" 批量上传

### 方法2: Git命令行
```bash
# 添加所有新文件
git add .github/ scripts/ *.md test_sync.py

# 提交变更
git commit -m "🔧 Add automated sync workflows and sites configuration sync

Features:
- ⚡ Automated upstream repository sync (daily)
- 🔄 Sites configuration sync (spider.json → moyun.json) 
- 📊 Detailed sync reports and statistics
- 🛡️ Safe backup and conflict resolution
- 🧪 Test scripts and comprehensive documentation

Workflows:
- sync-upstream.yml: Basic upstream sync
- sync-upstream-advanced.yml: Advanced sync with backup & notifications
- sync-sites.yml: Independent sites configuration sync"

# 推送到GitHub
git push origin main
```

## ✅ 上传后的验证步骤

### 1. 检查文件是否成功上传
- [ ] 在仓库主页确认所有文件都存在
- [ ] 检查 `.github/workflows/` 目录下的工作流文件

### 2. 验证GitHub Actions
- [ ] 访问仓库的 **Actions** 页面
- [ ] 确认能看到三个工作流：
  - "Sync Upstream Repository"
  - "Advanced Upstream Sync" 
  - "Sync Sites Configuration"

### 3. 测试Sites同步功能
- [ ] 点击 "Sync Sites Configuration" 工作流
- [ ] 点击 "Run workflow"
- [ ] 勾选"预览模式"进行安全测试
- [ ] 查看运行结果和摘要报告

### 4. 测试上游同步功能（可选）
- [ ] 点击 "Advanced Upstream Sync" 工作流  
- [ ] 手动触发测试
- [ ] 检查是否成功同步上游内容

## 🎯 预期结果

成功后你将获得：

✅ **自动化上游同步**
- 每天自动拉取上游仓库最新内容
- 安全的合并策略和备份机制
- 详细的同步报告

✅ **Sites配置自动同步** 
- `spider.json` 变更时自动同步到 `moyun.json`
- 数据验证和格式检查
- 保持其他配置不变

✅ **完善的监控和通知**
- GitHub Actions摘要报告
- 失败时自动创建Issue
- 详细的运行日志

## 🆘 需要帮助？

如果遇到问题：

1. **上传问题**: 检查文件路径和权限
2. **工作流问题**: 查看Actions页面的错误日志
3. **配置问题**: 使用 `test_sync.py` 在本地验证
4. **同步问题**: 检查 `spider.json` 和 `moyun.json` 格式

---

📅 **创建时间**: 2025-08-25  
🔄 **最后更新**: 上传完成后请删除此清单文件