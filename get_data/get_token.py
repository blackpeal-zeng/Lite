
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:44:45
# @FileName:  get_token.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-16 18:37:06
"""
import requests
from config.environment import ENVIRONMENT
from config.users import Users
from config.domain import Domain
from config.headers import *



class Token():
	"""获取登录Token"""
	def __init__(self):
		"""初始化"""
		self.env = ENVIRONMENT
		self.user = Users().get_user(self.env)
		self.domain = Domain().get_domain(self.env)
		self.url = self.domain+"/common/login"
		self.headers = HEADERS.get(self.env)().get_login_headers()

	def get_token(self):
		"""请求登录接口，获取token"""
		response = requests.post(self.url, self.user, headers=self.headers).json()
		print(response)
		# return response.get("token")




