# 🔧 YAML语法错误修复指南

## ❌ 遇到的问题

GitHub Actions显示以下错误：
```
(Line: 8, Col: 3): 'schedule' is already defined
```

## 🔍 问题原因

在 `.github/workflows/sync-upstream-advanced.yml` 文件中，`schedule` 键被重复定义了，这违反了YAML语法规则。

## ✅ 解决方案

### 方法1: 直接在GitHub网页上修改 (推荐)

1. **访问你的仓库页面**
2. **导航到文件**: `.github/workflows/sync-upstream-advanced.yml`
3. **点击编辑按钮** (铅笔图标)
4. **查找第5-8行**，应该类似这样的错误格式：
   ```yaml
   schedule:
     - cron: '0 0 * * *'
   # 每周一额外运行一次作为备份  
   schedule:
     - cron: '0 2 * * 1'
   ```

5. **替换为正确格式**:
   ```yaml
   # 定时运行计划
   schedule:
     # 每天北京时间08:00运行（UTC 00:00）
     - cron: '0 0 * * *'
     # 每周一额外运行一次作为备份
     - cron: '0 2 * * 1'
   ```

6. **提交更改**

### 方法2: 重新上传修复后的文件

如果你有本地Git环境，可以：

1. **下载修复后的文件** (从这个项目目录)
2. **替换GitHub上的文件**
3. **提交并推送更改**

## 📋 完整的正确文件开头

确保你的 `sync-upstream-advanced.yml` 文件开头是这样的：

```yaml
name: Advanced Upstream Sync

on:
  # 定时运行计划
  schedule:
    # 每天北京时间08:00运行（UTC 00:00）
    - cron: '0 0 * * *'
    # 每周一额外运行一次作为备份
    - cron: '0 2 * * 1'
  # 手动触发
  workflow_dispatch:
    inputs:
      force_sync:
        description: '强制同步（即使没有检测到变更）'
        required: false
        default: 'false'
        type: boolean

jobs:
  sync:
    runs-on: ubuntu-latest
    # ... 其余内容保持不变
```

## 🎯 验证修复

修复后，你应该看到：

1. ✅ **GitHub Actions页面不再显示错误**
2. ✅ **工作流可以正常触发和运行**
3. ✅ **Actions页面显示三个可用的工作流**:
   - Sync Upstream Repository
   - Advanced Upstream Sync
   - Sync Sites Configuration

## 🔍 其他常见YAML错误

### 1. 缩进错误
❌ 错误：
```yaml
on:
schedule:
  - cron: '0 0 * * *'
```

✅ 正确：
```yaml
on:
  schedule:
    - cron: '0 0 * * *'
```

### 2. 重复键定义
❌ 错误：
```yaml
schedule:
  - cron: '0 0 * * *'
schedule:
  - cron: '0 2 * * 1'
```

✅ 正确：
```yaml
schedule:
  - cron: '0 0 * * *'
  - cron: '0 2 * * 1'
```

### 3. 引号问题
❌ 错误：
```yaml
description: 强制同步（即使没有检测到变更）
```

✅ 正确：
```yaml
description: '强制同步（即使没有检测到变更）'
```

## 📞 需要帮助？

如果修复后仍然有问题：

1. **检查文件编码**: 确保使用UTF-8编码
2. **检查隐藏字符**: 可能存在不可见的字符
3. **重新创建文件**: 在GitHub上删除文件，然后重新创建
4. **联系支持**: 如果问题持续存在

---

**创建时间**: 2025-08-25  
**状态**: 修复完成 ✅