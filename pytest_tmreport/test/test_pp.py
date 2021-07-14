"""
@Project ：test_py 
@File    ：test_pp.py
@IDE     ：PyCharm 
@Author  ：kevin
@Date    ：2021/7/8 上午11:52 
"""
import time
from loguru import logger
import pytest

def test_001():
    """
        测试函数1
    :return:  123
    """
    logger.info("关注迅捷小侯")

@pytest.mark.parametrize('param', [1,2,3,4,5,6,7,8,9,10])
def test_002(param):
    print(param)

def test_测试_1():
    """
        测试函数1
    :return:  123
    """
    print("关注迅捷小侯")
    logger.info("关注迅捷小侯关注迅捷小侯关注迅捷小侯关注迅捷小侯关注迅捷小侯关注迅捷小侯关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    logger.info("关注迅捷小侯")
    time.sleep(1)


class TestApi():

    def test_测试(self):
        """
                测试函数1
            :return:  123
        """
        logger.info("关注迅捷小侯")

    def test_2(self):
        assert 1 == 2


import pytest

if __name__ == '__main__':
    pytest.main(['-s', '--pytest-tmreport-name test.html', 'test_pp.py'])
