
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:45:31
# @FileName:  调试.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-17 16:37:45
"""

from get_data.get_token import Token

token = Token().get_token()
print(token)

from base.get_datetime import Date
print(Date().get_today())
