
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:10:04
# @FileName:  users.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-06-26 15:50:53
"""

class Users():
	"""存放Lite测试账号"""
	def __init__(self):
		self.user = {"sit": {"account": "zengsx1", "password": "123456"},
					"uat": {"account": "zengqiu", "password": "123456"}}

	def get_user(self, env="sit"):
		return self.user.get(env)

if __name__ == '__main__':
	print(Users().get_user("uat"))
