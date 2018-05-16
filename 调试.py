
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:45:31
# @FileName:  调试.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-16 18:30:33
"""

from get_data.get_token import Token

Token().get_token()

from config.environment import ENVIRONMENT
print(ENVIRONMENT)
