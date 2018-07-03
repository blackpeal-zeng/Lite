
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:45:31
# @FileName:  调试.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-07-03 17:23:52
"""

from get_data.base.get_token import Token

token = Token().get_token()
print(token)

from get_data.base.get_datetime import DateTime
print(DateTime().get_today())

# 获取门店营业数据
# from get_data.store.get_business_data import BusinessData
# business_data = BusinessData().get_business_data()
# print("门店营业数据-all>>>", business_data)
# top_total = BusinessData().get_top_info(business_data)
# print("门店营业数据-top>>>", top_total)
# business_statistics = BusinessData().get_business_statistics(business_data)
# print("门店营业数据-business>>>", business_statistics)
# customer_statistics = BusinessData().get_customer_statistics(business_data)
# print("门店营业数据-customer>>>", customer_statistics)
# finance_statistics = BusinessData().get_finance_statistics(business_data)
# print("门店营业数据-business>>>", finance_statistics)

print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
from scripts.payment import 开单收银
# code = 开单收银().挂单()
project = 开单收银().散客服务单()
