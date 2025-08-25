#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API路径转换测试脚本
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 导入同步脚本中的转换函数
from scripts.sync_sites import transform_api_path

def test_api_path_transformation():
    """测试API路径转换功能"""
    print("🧪 测试API路径转换功能...")
    
    test_cases = [
        {
            "input": {"key": "test1", "name": "测试1", "type": 3, "api": "./app/八戒影视.py"},
            "expected": {"key": "test1", "name": "测试1", "type": 3, "api": "./plugin/app/八戒影视.py"}
        },
        {
            "input": {"key": "test2", "name": "测试2", "type": 3, "api": "./web/山有木兮.py"},
            "expected": {"key": "test2", "name": "测试2", "type": 3, "api": "./plugin/web/山有木兮.py"}
        },
        {
            "input": {"key": "test3", "name": "测试3", "type": 3, "api": "./other/some.py"},
            "expected": {"key": "test3", "name": "测试3", "type": 3, "api": "./other/some.py"}  # 不应该变化
        }
    ]
    
    all_passed = True
    
    for i, case in enumerate(test_cases):
        print(f"\n📋 测试用例 {i+1}:")
        print(f"  输入: {case['input']['api']}")
        
        result = transform_api_path(case['input'].copy())
        
        print(f"  输出: {result['api']}")
        print(f"  期望: {case['expected']['api']}")
        
        if result['api'] == case['expected']['api']:
            print("  ✅ 通过")
        else:
            print("  ❌ 失败")
            all_passed = False
    
    print(f"\n🎯 测试结果: {'✅ 所有测试通过' if all_passed else '❌ 部分测试失败'}")
    return all_passed

def main():
    """主函数"""
    print("=" * 60)
    print("🔧 API路径转换功能测试")
    print("=" * 60)
    
    try:
        success = test_api_path_transformation()
        
        if success:
            print("\n✅ 路径转换功能正常，可以进行同步操作")
        else:
            print("\n❌ 路径转换功能异常，请检查代码")
        
        return success
        
    except Exception as e:
        print(f"\n💥 测试过程中发生错误: {e}")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)