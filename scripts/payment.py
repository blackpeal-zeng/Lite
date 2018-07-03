
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-06-27 17:18:15
# @FileName:  payment.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-07-03 18:24:14
"""

import requests, time, json
from config.environment import ENVIRONMENT
from config.domain import Domain
from config.headers import Headers
from get_data.base.get_token import Token


class 开单收银(object):
	"""各种开单收银脚本"""
	def __init__(self):
		self.env = ENVIRONMENT
		self.token = Token().get_token()
		self.headers = Headers().get_headers(env=self.env)
		self.domain = Domain().get_domain(env=self.env)

	def get_now_time(self):
		"""返回当前时间"""
		return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

	def 挂单(self, gender=2):
		"""
		挂单，开单通用操作，默认女客，gender=1则男客
		"""
		# 接口地址
		system_url = self.domain+"/salon/order/systemCode/get"
		salon_url = self.domain+"/salon/order/salonCode/get"
		setting_url = self.domain+"/salon/salon/salonSetting/get"
		snap_url = self.domain+"/salon/order/order/snap"
		# 请求接口，获取系统单号和水单号
		system_data = {"token": self.token}
		response1 = requests.get(url=system_url, params=system_data, headers=self.headers).json()
		system_code = response1.get("response").get("system_code")
		salon_data = {"token": self.token, "system_code": system_code}
		response2 = requests.get(url=salon_url, params=salon_data, headers=self.headers).json()
		salon_code = response2.get("response").get("salon_code")
		setting_data = {"token": self.token}
		response3 = requests.get(url=setting_url, params=setting_data, headers=self.headers).json()
		# 挂单，返回订单id，水单号和系统单号
		snap = {"id": 0,
				"system_code": "2018070300002",
				"salon_code": "2018070300002",
				"type": "1",
				"order_date": "2018-07-03 14:19:10",
				"use_system_code": 0,
				"source": "1",
				"gender": "2",
				"member_id": 0,
				"member_name": "",
				"member_card_id": 0,
				"handset": "",
				"order_items": [],
				"pay_ways": [],
				"remark": "",
				"password": "",
				"from_face": False,
				"print_flag": "1",
				"wechat_order_id": 0,
				"fit_coupon_list": [],
				"is_count": 1,
				"create_card_data": {
					"order_items": {
						"card_id": "",
						"member_card_num": "",
						"cost": "",
						"amount": "",
						"gift_amount": ""
					},
					"staff_items": [],
					"department_items": [],
					"card_sold_performance_discount": 0,
					"department_performance_type": "1",
					"card": "null"
				},
				"recharge_data": {
					"order_items": {
						"card_id": "",
						"member_card_id": "",
						"amount": "",
						"gift_amount": ""
					},
					"staff_items": [],
					"department_items": [],
					"card_sold_performance_discount": 0,
					"department_performance_type": "1",
					"card": "null"
				},
				"course_data": {
					"order_items": {
						"course_id": "",
						"amount": "",
						"course_name": "",
						"deduct_amount": ""
					},
					"staff_items": [],
					"department_items": [],
					"department_performance_type": "1",
					"course": "null"
				},
				"custom_course_data": {
					"order_items": {
						"expiry_days": "",
						"amount": "",
						"deduct_amount": ""
					},
					"staff_items": [],
					"department_items": [],
					"course_items": [],
					"department_performance_type": "1"
				},
				"repay_data": {
					"order_items": {
						"amount": "",
						"type": "1"
					},
					"staff_items": [],
					"department_items": [],
					"department_performance_type": "1"
				},
				"coupon_data": {
					"order_items": {
						"amount": "",
						"points": "",
						"deduct_amount": ""
					},
					"coupon_items": []
				},
				"card_upgrade_data": {
					"order_items": {
						"member_card_id": "",
						"amount": "",
						"card_id": "",
						"upgrade_card_id": "",
						"gift_amount": ""
					},
					"staff_items": [],
					"department_items": [],
					"department_performance_type": "1"
				},
				"transfer_card_data": {
					"order_items": {
						"member_id": "",
						"member_card_id": "",
						"amount": 0,
						"gift_amount": 0,
						"cost": 0
					},
					"member": "null",
					"cur_member": "null",
					"to_member": "null"
				}
		}
		snap = json.dumps(snap)
		order_date = self.get_now_time()
		snap_data = {"order_snap_id": 0,
					"system_code": system_code,
					"salon_code": salon_code,
					"order_date": order_date,
					"gender": gender,
					"snap": snap,
					"use_system_code": 0,
					"member_id": 0,
					"type": 1,
					"wechat_order_id": 0,
					"token": self.token
		}
		response4 = requests.post(url=snap_url, data=snap_data, headers=self.headers).json()
		print(response4)
		order = response4.get("response")
		return order

	def 散客服务单(self, gender=2):
		"""散客服务单，默认女客"""
		snap = self.挂单()
		project_url = self.domain+"/salon/order/order/project"
		order_items = [{"project_id": 872,
						"type": "1",
						"discount": 10000,
						"quantity": 1,
						"origin_price": 3500,
						"sell_price": 3500,
						"salon_performance": 3500,
						"member_course_id": 0,
						"member_card_id": 0,
						"coupon_id": 0,
						"coupon_record_id": 0,
						"deduct_amount": 0,
						"cost": 0,
						"performance": 3000,
						"points": 0,
						"staff_items": []
						}]
		pay_ways = [{"type": 2, "amount": 3500},
					{"type": 3, "amount": 0},
					{"type": 4, "amount": 0},
					{"type": 5, "amount": 0},
					{"type": 6, "amount": 0, "group_buy_id": 3},
					{"type": 7, "amount": 0},
					{"type": 8, "amount": 0}]
		salon_performance = order_items.get("salon_performance")
		order_items = json.dumps(order_items)
		pay_ways = json.dumps(pay_ways)
		data = {"system_code": snap.get("system_code"),
				"salon_code": snap.get("salon_code"),
				"order_snap_id": snap.get("id"),
				"type": 1,
				"order_date": self.get_now_time(),
				"source": 1,
				"gender": gender,
				"member_id": 0,
				"member_card_id": 0,
				"remark": "",
				"password": "",
				"wechat_order_id": 0,
				"is_count": 1,
				"order_items": order_items,
				"pay_ways": pay_ways,
				"order_id": 0,
				"token": self.token
		}
		response = requests.post(url=project_url, data=data, headers=self.headers).json()
		print(response)
		return {"salon_performance": salon_performance}










