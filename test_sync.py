#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
本地测试脚本 - 验证sites同步功能
在上传到GitHub之前，可以使用此脚本验证配置同步是否正常工作
"""

import json
import os
from pathlib import Path


def test_sync_functionality():
    """测试同步功能"""
    print("🧪 开始测试sites同步功能...")
    
    # 获取文件路径
    current_dir = Path(__file__).parent
    spider_file = current_dir / 'spider.json'
    moyun_file = current_dir / 'moyun.json'
    
    print(f"📁 检查文件: {spider_file}")
    print(f"📁 检查文件: {moyun_file}")
    
    # 检查文件是否存在
    if not spider_file.exists():
        print(f"❌ spider.json 不存在: {spider_file}")
        return False
    
    if not moyun_file.exists():
        print(f"❌ moyun.json 不存在: {moyun_file}")
        return False
    
    try:
        # 读取spider.json
        with open(spider_file, 'r', encoding='utf-8') as f:
            spider_data = json.load(f)
        print("✅ spider.json 读取成功")
        
        # 读取moyun.json
        with open(moyun_file, 'r', encoding='utf-8') as f:
            moyun_data = json.load(f)
        print("✅ moyun.json 读取成功")
        
        # 检查spider.json中的sites
        spider_sites = spider_data.get('sites', [])
        print(f"📊 spider.json 中有 {len(spider_sites)} 个sites配置")
        
        if not spider_sites:
            print("⚠️ spider.json 中没有sites配置")
            return True
        
        # 显示前几个sites作为示例
        print("\n📋 Sites配置示例:")
        for i, site in enumerate(spider_sites[:3]):
            name = site.get('name', 'Unknown')
            key = site.get('key', 'Unknown')
            api = site.get('api', 'Unknown')
            print(f"  {i+1}. {name} ({key}) - {api}")
        
        if len(spider_sites) > 3:
            print(f"  ... 还有 {len(spider_sites) - 3} 个配置项")
        
        # 验证JSON结构
        print("\n🔍 验证配置结构...")
        valid_count = 0
        invalid_count = 0
        
        required_fields = ['key', 'name', 'type', 'api']
        for site in spider_sites:
            has_all_fields = all(field in site for field in required_fields)
            if has_all_fields:
                valid_count += 1
            else:
                invalid_count += 1
                missing = [field for field in required_fields if field not in site]
                print(f"  ⚠️ 配置项缺少字段: {missing} - {site.get('name', 'Unknown')}")
        
        print(f"✅ 有效配置: {valid_count}")
        if invalid_count > 0:
            print(f"⚠️ 无效配置: {invalid_count}")
        
        # 检查moyun.json结构
        print("\n🔍 检查moyun.json结构...")
        current_sites = moyun_data.get('sites', [])
        print(f"📊 moyun.json 当前有 {len(current_sites)} 个sites配置")
        
        # 检查其他必要字段
        other_fields = ['parses', 'flags', 'lives']
        for field in other_fields:
            if field in moyun_data:
                count = len(moyun_data[field]) if isinstance(moyun_data[field], list) else 'N/A'
                print(f"  ✅ {field}: {count} 个配置项")
            else:
                print(f"  ⚠️ {field}: 不存在")
        
        print("\n🎉 配置验证完成！")
        print(f"📈 同步后moyun.json将有 {valid_count} 个sites配置")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON格式错误: {e}")
        return False
    except Exception as e:
        print(f"❌ 测试失败: {e}")
        return False


def main():
    """主函数"""
    print("=" * 60)
    print("🧪 Sites同步功能本地测试")
    print("=" * 60)
    
    success = test_sync_functionality()
    
    if success:
        print("\n✅ 测试通过！可以安全上传到GitHub进行工作流测试。")
        print("\n📋 下一步操作:")
        print("1. 将所有文件上传到GitHub仓库")
        print("2. 在Actions页面测试 'Sync Sites Configuration' 工作流")
        print("3. 使用预览模式先测试，确认无误后进行正式同步")
    else:
        print("\n❌ 测试失败！请检查配置文件格式。")
    
    return success


if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)