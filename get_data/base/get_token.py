
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 17:44:45
# @FileName:  get_token.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-21 12:02:24
"""
import requests
from config.environment import ENVIRONMENT
from config.users import Users
from config.domain import Domain
from config.headers import Headers


class Token():
	"""获取登录Token"""
	def __init__(self):
		"""初始化"""
		self.env = ENVIRONMENT
		self.user = Users().get_user(self.env)
		self.domain = Domain().get_domain(self.env)
		self.headers = Headers().get_login_headers(self.env)
		self.url = Domain().get_domain(self.env)+"/common/login"

	def get_token(self):
		"""请求登录接口，获取token"""
		response = requests.post(url=self.url, data=self.user, headers=self.headers).json()
		return response.get("response").get("token")




