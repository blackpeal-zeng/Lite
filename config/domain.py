
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:36:50
# @FileName:  domain.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-16 18:06:48
"""

class Domain():
	"""存放Lite测试账号"""
	def __init__(self):
		self.user = {"sit": "http://salon-client-sit.lite.meimeifa.cn",
					"uat": "http://salon-client-uat.lite.meimeifa.cn/"}

	def get_domain(self, env="sit"):
		return self.user.get(env)