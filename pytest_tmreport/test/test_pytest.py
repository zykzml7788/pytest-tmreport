"""
@Project ：pytest-tmreport 
@File    ：test_pytest.py
@IDE     ：PyCharm 
@Author  ：kevin
@Date    ：2021/7/8 上午10:45 
"""

import pytest
import time

def test_fun1():
    """
    测试函数111
    :return:
    """
    time.sleep(2)


def test_fun2():
    """
    测试函数1112222
    :return:
    """
    time.sleep(3)
    print(123)

if __name__ == '__main__':
    pytest.main()