
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-17 15:31:35
# @FileName:  get_datetime.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-17 17:44:24
"""

import datetime

class DateTime():
	"""获取日期数据，用于筛选数据"""
	def __init__(self):
		self.today = datetime.date.today()
		self.yesterday = self.today - datetime.timedelta(days=1)

	def get_today(self):
		return self.today

	def get_yesterday(self):
		return self.yesterday

	def get_past_N_day(self, Ndays=1):
		return self.today - datetime.timedelta(days=Ndays)

	def get_future_N_day(self, Ndays=1):
		return self.today + datetime.timedelta(days=Ndays)
