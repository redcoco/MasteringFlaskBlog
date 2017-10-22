# -*- coding: utf-8 -*-
"""
配置文件
"""


class Config(object):
    """基础配置"""
    pass

class ProdConfig(Config):
    """生产环境配置"""
    pass

class DevConfig(Config):
    """测试环境配置"""
    DEBUG = True
