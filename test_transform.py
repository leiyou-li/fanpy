#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API路径转换测试脚本
"""

import sys
import os
import json

# 直接定义转换函数
def transform_api_path(site):
    """转换API路径，将./app/和./web/转换为./plugin/app/和./plugin/web/"""
    if 'api' in site:
        api_path = site['api']
        if api_path.startswith('./app/'):
            site['api'] = api_path.replace('./app/', './plugin/app/')
        elif api_path.startswith('./web/'):
            site['api'] = api_path.replace('./web/', './plugin/web/')
    return site

def test_transformation():
    """测试API路径转换功能"""
    print("🧪 测试API路径转换功能...")
    
    # 测试用例
    test_sites = [
        {"key": "test1", "name": "测试1", "type": 3, "api": "./app/八戒影视.py"},
        {"key": "test2", "name": "测试2", "type": 3, "api": "./web/山有木兮.py"},
        {"key": "test3", "name": "测试3", "type": 3, "api": "./other/some.py"},
        {"key": "test4", "name": "测试4", "type": 3, "api": "./app/AppMuou.py"},
    ]
    
    print("📋 转换结果:")
    for site in test_sites:
        original = site['api']
        transformed = transform_api_path(site.copy())
        result = transformed['api']
        
        print(f"  原始: {original}")
        print(f"  转换: {result}")
        print(f"  {'✅ 已转换' if original != result else '⭕ 未变化'}")
        print()

def test_real_spider_data():
    """测试真实的spider.json数据"""
    print("🔍 测试真实spider.json数据转换...")
    
    try:
        with open('spider.json', 'r', encoding='utf-8') as f:
            spider_data = json.load(f)
        
        sites = spider_data.get('sites', [])
        print(f"📊 找到 {len(sites)} 个sites")
        
        # 转换前几个进行测试
        for i, site in enumerate(sites[:5]):
            original = site.copy()
            transformed = transform_api_path(site.copy())
            
            print(f"\n📋 Site {i+1}: {site['name']}")
            print(f"  原始API: {original['api']}")
            print(f"  转换API: {transformed['api']}")
            
            if original['api'] != transformed['api']:
                print(f"  ✅ 路径已转换")
            else:
                print(f"  ⭕ 路径未变化")
                
    except Exception as e:
        print(f"❌ 测试失败: {e}")

if __name__ == '__main__':
    print("=" * 60)
    print("🔧 API路径转换功能测试")
    print("=" * 60)
    
    test_transformation()
    print("-" * 40)
    test_real_spider_data()