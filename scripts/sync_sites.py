#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Spider Sites Sync Script
将 spider.json 中的 sites 配置同步到 moyun.json 中
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path


def load_json_file(file_path):
    """安全加载JSON文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON格式错误 {file_path}: {e}")
        return None
    except Exception as e:
        print(f"❌ 读取文件失败 {file_path}: {e}")
        return None


def save_json_file(data, file_path, backup=True):
    """安全保存JSON文件"""
    try:
        # 创建备份
        if backup and os.path.exists(file_path):
            backup_path = f"{file_path}.backup.{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            os.rename(file_path, backup_path)
            print(f"📁 已创建备份: {backup_path}")
        
        # 保存文件
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 文件保存成功: {file_path}")
        return True
    except Exception as e:
        print(f"❌ 保存文件失败 {file_path}: {e}")
        return False


def validate_site_item(site):
    """验证site项目的必要字段"""
    required_fields = ['key', 'name', 'type', 'api']
    for field in required_fields:
        if field not in site:
            return False, f"缺少必要字段: {field}"
    return True, None


def transform_api_path(site):
    """转换API路径，将./app/和./web/转换为./plugin/app/和./plugin/web/"""
    if 'api' in site:
        api_path = site['api']
        if api_path.startswith('./app/'):
            site['api'] = api_path.replace('./app/', './plugin/app/')
        elif api_path.startswith('./web/'):
            site['api'] = api_path.replace('./web/', './plugin/web/')
    return site


def sync_sites(spider_file, moyun_file, dry_run=False):
    """
    同步sites配置
    
    Args:
        spider_file: spider.json 文件路径
        moyun_file: moyun.json 文件路径  
        dry_run: 是否只进行预览不实际修改文件
    """
    print("🚀 开始同步sites配置...")
    print(f"📖 源文件: {spider_file}")
    print(f"📝 目标文件: {moyun_file}")
    
    # 加载源文件
    spider_data = load_json_file(spider_file)
    if spider_data is None:
        return False
    
    # 加载目标文件
    moyun_data = load_json_file(moyun_file)
    if moyun_data is None:
        return False
    
    # 提取并验证sites数据
    spider_sites = spider_data.get('sites', [])
    if not spider_sites:
        print("⚠️  spider.json 中没有找到sites配置")
        return True
    
    print(f"📊 找到 {len(spider_sites)} 个sites配置项")
    
    # 验证sites数据
    valid_sites = []
    invalid_count = 0
    
    for i, site in enumerate(spider_sites):
        is_valid, error_msg = validate_site_item(site)
        if is_valid:
            # 转换API路径
            transformed_site = transform_api_path(site.copy())
            valid_sites.append(transformed_site)
        else:
            print(f"⚠️  跳过无效配置项 [{i+1}]: {error_msg} - {site.get('name', 'Unknown')}")
            invalid_count += 1
    
    print(f"✅ 有效配置项: {len(valid_sites)}")
    if invalid_count > 0:
        print(f"⚠️  无效配置项: {invalid_count}")
    
    # 检查是否有变化
    current_sites = moyun_data.get('sites', [])
    if current_sites == valid_sites:
        print("ℹ️  配置已是最新，无需同步")
        return True
    
    # 显示变更信息
    print(f"📈 当前moyun.json中有 {len(current_sites)} 个sites")
    print(f"🔄 将更新为 {len(valid_sites)} 个sites")
    
    if dry_run:
        print("🔍 预览模式 - 不会实际修改文件")
        print("📋 将要同步的sites配置:")
        for i, site in enumerate(valid_sites[:5]):  # 只显示前5个
            print(f"  {i+1}. {site['name']} ({site['key']})")
        if len(valid_sites) > 5:
            print(f"  ... 还有 {len(valid_sites) - 5} 个")
        return True
    
    # 更新moyun.json
    moyun_data['sites'] = valid_sites
    
    # 添加同步信息到配置中
    if 'sync_info' not in moyun_data:
        moyun_data['sync_info'] = {}
    
    moyun_data['sync_info'].update({
        'last_sync': datetime.now().isoformat(),
        'source_file': os.path.basename(spider_file),
        'sites_count': len(valid_sites),
        'sync_script': 'sync_sites.py'
    })
    
    # 保存文件
    success = save_json_file(moyun_data, moyun_file, backup=True)
    
    if success:
        print("🎉 Sites配置同步完成！")
        return True
    else:
        print("❌ 同步失败")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("🔄 Spider Sites 同步工具")
    print("=" * 60)
    
    # 解析命令行参数
    dry_run = '--dry-run' in sys.argv or '--preview' in sys.argv
    
    # 获取文件路径
    script_dir = Path(__file__).parent
    
    # 优先使用GitHub Actions工作区路径，否则使用脚本父目录
    if 'GITHUB_WORKSPACE' in os.environ:
        workspace = Path(os.environ['GITHUB_WORKSPACE'])
        spider_file = workspace / 'spider.json'
        moyun_file = workspace / 'moyun.json'
        working_dir = workspace
    else:
        # 本地运行时，文件在脚本的父目录（项目根目录）
        working_dir = script_dir.parent
        spider_file = working_dir / 'spider.json'
        moyun_file = working_dir / 'moyun.json'
    
    print(f"🔍 工作目录: {working_dir}")
    print(f"📁 Spider文件: {spider_file}")
    print(f"📁 Moyun文件: {moyun_file}")
    
    # 检查文件是否存在
    if not spider_file.exists():
        print(f"❌ spider.json 文件不存在: {spider_file}")
        sys.exit(1)
    
    if not moyun_file.exists():
        print(f"❌ moyun.json 文件不存在: {moyun_file}")
        sys.exit(1)
    
    # 执行同步
    try:
        success = sync_sites(str(spider_file), str(moyun_file), dry_run=dry_run)
        if success:
            print("\n✅ 同步操作完成")
            sys.exit(0)
        else:
            print("\n❌ 同步操作失败")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n⏹️  操作被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 发生未预期的错误: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()