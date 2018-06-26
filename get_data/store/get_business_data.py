
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-21 10:54:14
# @FileName:  get_business_data.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-06-26 17:21:41
"""
import requests
from config.environment import ENVIRONMENT
from config.domain import Domain
from config.headers import Headers
from get_data.base.get_token import Token
from get_data.base.get_datetime import DateTime



class BusinessData():
	"""获取门店数据>门店营业数据"""
	def __init__(self):
		self.api = "/salon/salonBusiness/data/overview"
		self.env = ENVIRONMENT
		self.token = Token().get_token()
		self.headers = Headers().get_headers(env=self.env)
		self.url = Domain().get_domain(env=self.env)+self.api

	def get_business_data(self, Ndays=30, ispast=True):
		"""获取门店营业数据"""
		today = DateTime().get_today()
		if ispast:
			begin_date = DateTime().get_past_N_day(Ndays=Ndays)
			end_date = today
		else:
			begin_date = today
			end_date = DateTime().get_future_N_day(Ndays=Ndays)
		data = {"department_id": "",
				"begin_date": begin_date,
				"end_date": end_date,
				"token": self.token
				}
		print(data)
		response = requests.get(self.url, params=data, headers=self.headers).json()
		return response

	def get_top_info(self, business_data):
		"""
		获取门店营业数据-顶部统计
		包括以下数据：
		1.服务业绩(劳动)&环比
		2.商品销售业绩&环比
		3.卡项销售业绩&环比
		4.套餐销售业绩&环比
		5.优惠券销售业绩&环比
		6.总营业额
		"""
		_data = business_data.get("response").get("overview")
		top_data = {"服务业绩(劳动)": _data.get("service"),
					"服务业绩环比": _data.get("service_ratio"),
					"商品销售业绩": _data.get("goods"),
					"商品销售业绩环比": _data.get("goods_ratio"),
					"卡项销售业绩": _data.get("card"),
					"卡项销售业绩环比": _data.get("card_ratio"),
					"套餐销售业绩": _data.get("course"),
					"套餐销售业绩环比": _data.get("course_ratio"),
					"优惠券销售业绩": _data.get("coupon"),
					"优惠券销售业绩环比": _data.get("coupon_ratio"),
					"总营业额": _data.get("total")
		}
		return top_data

	def get_business_statistics(self, business_data):
		"""
		获取门店营业数据-营业统计
		"""
		_total = business_data.get("response").get("business").get("total")
		_data = business_data.get("response").get("business").get("items")
		business_data = {"服务销售": {"现金": _data[0].get("cash"),
									"银联": _data[0].get("union_pay"),
									"微信": _data[0].get("wechat_pay"),
									"支付宝": _data[0].get("ali_pay"),
									"团购": _data[0].get("group_buy"),
									"现金券	": _data[0].get("cash_coupon"),
									"耗卡": _data[0].get("card"),
									"疗程消耗": _data[0].get("course"),
									"耗赠金": _data[0].get("card_gift"),
									"优惠券": _data[0].get("coupon"),
									"免单": _data[0].get("free"),
									"欠款": _data[0].get("arrears"),
									"总现金": _data[0].get("total_cash"),
									"总耗卡": _data[0].get("total_card"),
									"总疗程消耗": _data[0].get("total_course"),
									"总赠金": _data[0].get("total_card_gift"),
									"小计": _data[0].get("total")
									},
						"商品销售": {"现金": _data[1].get("cash"),
									"银联": _data[1].get("union_pay"),
									"微信": _data[1].get("wechat_pay"),
									"支付宝": _data[1].get("ali_pay"),
									"团购": _data[1].get("group_buy"),
									"现金券": _data[1].get("cash_coupon"),
									"耗卡": _data[1].get("card"),
									"疗程消耗": _data[1].get("course"),
									"耗赠金": _data[1].get("card_gift"),
									"优惠券": _data[1].get("coupon"),
									"免单": _data[1].get("free"),
									"欠款": _data[1].get("arrears"),
									"总现金": _data[1].get("total_cash"),
									"总耗卡": _data[1].get("total_card"),
									"总疗程消耗": _data[1].get("total_course"),
									"总赠金": _data[1].get("total_card_gift"),
									"小计": _data[1].get("total")
									},
						"卡项销售": {"现金": _data[2].get("cash"),
									"银联": _data[2].get("union_pay"),
									"微信": _data[2].get("wechat_pay"),
									"支付宝": _data[2].get("ali_pay"),
									"团购": _data[2].get("group_buy"),
									"现金券": _data[2].get("cash_coupon"),
									"耗卡": _data[2].get("card"),
									"疗程消耗": _data[2].get("course"),
									"耗赠金": _data[2].get("card_gift"),
									"优惠券": _data[2].get("coupon"),
									"免单": _data[2].get("free"),
									"欠款": _data[2].get("arrears"),
									"总现金": _data[2].get("total_cash"),
									"总耗卡": _data[2].get("total_card"),
									"总疗程消耗": _data[2].get("total_course"),
									"总赠金": _data[2].get("total_card_gift"),
									"小计": _data[2].get("total")
									},
						"套餐销售": {"现金": _data[3].get("cash"),
									"银联": _data[3].get("union_pay"),
									"微信": _data[3].get("wechat_pay"),
									"支付宝": _data[3].get("ali_pay"),
									"团购": _data[3].get("group_buy"),
									"现金券": _data[3].get("cash_coupon"),
									"耗卡": _data[3].get("card"),
									"疗程消耗": _data[3].get("course"),
									"耗赠金": _data[3].get("card_gift"),
									"优惠券": _data[3].get("coupon"),
									"免单": _data[3].get("free"),
									"欠款": _data[3].get("arrears"),
									"总现金": _data[3].get("total_cash"),
									"总耗卡": _data[3].get("total_card"),
									"总疗程消耗": _data[3].get("total_course"),
									"总赠金": _data[3].get("total_card_gift"),
									"小计": _data[3].get("total")
									},
						"优惠券销售": {"现金": _data[4].get("cash"),
									"银联": _data[4].get("union_pay"),
									"微信": _data[4].get("wechat_pay"),
									"支付宝": _data[4].get("ali_pay"),
									"团购": _data[4].get("group_buy"),
									"现金券": _data[4].get("cash_coupon"),
									"耗卡": _data[4].get("card"),
									"疗程消耗": _data[4].get("course"),
									"耗赠金": _data[4].get("card_gift"),
									"优惠券": _data[4].get("coupon"),
									"免单": _data[4].get("free"),
									"欠款": _data[4].get("arrears"),
									"总现金": _data[4].get("total_cash"),
									"总耗卡": _data[4].get("total_card"),
									"总疗程消耗": _data[4].get("total_course"),
									"总赠金": _data[4].get("total_card_gift"),
									"小计": _data[4].get("total")
									},
						"会员管理费": {"现金": _data[5].get("cash"),
									"银联": _data[5].get("union_pay"),
									"微信": _data[5].get("wechat_pay"),
									"支付宝": _data[5].get("ali_pay"),
									"团购": _data[5].get("group_buy"),
									"现金券": _data[5].get("cash_coupon"),
									"耗卡": _data[5].get("card"),
									"疗程消耗": _data[5].get("course"),
									"耗赠金": _data[5].get("card_gift"),
									"优惠券": _data[5].get("coupon"),
									"免单": _data[5].get("free"),
									"欠款": _data[5].get("arrears"),
									"总现金": _data[5].get("total_cash"),
									"总耗卡": _data[5].get("total_card"),
									"总疗程消耗": _data[5].get("total_course"),
									"总赠金": _data[5].get("total_card_gift"),
									"小计": _data[5].get("total")
									},
						"汇总": {"现金": _total.get("cash"),
									"银联": _total.get("union_pay"),
									"微信": _total.get("wechat_pay"),
									"支付宝": _total.get("ali_pay"),
									"团购": _total.get("group_buy"),
									"现金券": _total.get("cash_coupon"),
									"耗卡": _total.get("card"),
									"疗程消耗": _total.get("course"),
									"耗赠金": _total.get("card_gift"),
									"优惠券": _total.get("coupon"),
									"免单": _total.get("free"),
									"欠款": _total.get("arrears"),
									"总现金": _total.get("total_cash"),
									"总耗卡": _total.get("total_card"),
									"总疗程消耗": _total.get("total_course"),
									"总赠金": _total.get("total_card_gift"),
									"小计": _total.get("total")
									}
		}
		return business_data

	def get_customer_statistics(self, business_data):
		"""
		获取门店营业数据-客户统计
		"""
		_data = business_data.get("response").get("customer")
		customer_statistics = {"总客数": _data.get("total_analysis").get("serve"),
								"总业绩": _data.get("total_analysis").get("performance"),
								"客单价": _data.get("total_analysis").get("serve_price"),
								"指定客数": _data.get("specify_analysis").get("specify_number"),
								"指定业绩": _data.get("specify_analysis").get("specify_performance"),
								"指定客单价": _data.get("specify_analysis").get("specify_price"),
								"指定率": _data.get("specify_analysis").get("specify_ratio"),
								"非指定客数": _data.get("specify_analysis").get("not_specify_number"),
								"非指定业绩": _data.get("specify_analysis").get("not_specify_performance"),
								"非指定客单价": _data.get("specify_analysis").get("not_specify_price"),
								"非指定率": _data.get("specify_analysis").get("not_specify_ratio"),
								"会员客数": _data.get("customer_analysis").get("member_number"),
								"会员业绩": _data.get("customer_analysis").get("member_performance"),
								"会员客单价": _data.get("customer_analysis").get("member_price"),
								"会员率": _data.get("customer_analysis").get("member_ratio"),
								"散客数": _data.get("customer_analysis").get("not_member_number"),
								"散客业绩": _data.get("customer_analysis").get("not_member_performance"),
								"散客客单价": _data.get("customer_analysis").get("not_member_price"),
								"散客率": _data.get("customer_analysis").get("not_member_ratio"),
								"女客数": _data.get("male_female_analysis").get("female_number"),
								"女客业绩": _data.get("male_female_analysis").get("female_performance"),
								"女客客单价": _data.get("male_female_analysis").get("female_price"),
								"女客率": _data.get("male_female_analysis").get("female_ratio"),
								"男客数": _data.get("male_female_analysis").get("male_number"),
								"男客业绩": _data.get("male_female_analysis").get("male_performance"),
								"男客客单价": _data.get("male_female_analysis").get("male_price"),
								"男客率": _data.get("male_female_analysis").get("male_ratio")
		}
		return customer_statistics

	def get_finance_statistics(self, business_data):
		"""
		获取门店营业数据-收支统计
		"""
		_data = business_data.get("response").get("finance").get("items")
		_total = business_data.get("response").get("finance").get("total")
		finance_statistics = {"现金": {"营业收入": _data[0].get("business_income"),
										"其他收入": _data[0].get("other_income"),
										"支出": _data[0].get("pay"),
										"资金结余": _data[0].get("balance"),
										},
							"银联": {"营业收入": _data[1].get("business_income"),
										"其他收入": _data[1].get("other_income"),
										"支出": _data[1].get("pay"),
										"资金结余": _data[1].get("balance"),
										},
							"微信": {"营业收入": _data[2].get("business_income"),
										"其他收入": _data[2].get("other_income"),
										"支出": _data[2].get("pay"),
										"资金结余": _data[2].get("balance"),
										},
							"支付宝": {"营业收入": _data[3].get("business_income"),
										"其他收入": _data[3].get("other_income"),
										"支出": _data[3].get("pay"),
										"资金结余": _data[3].get("balance"),
										},
							"合计": {"营业收入": _total.get("business_income"),
										"其他收入": _total.get("other_income"),
										"支出": _total.get("pay"),
										"资金结余": _total.get("balance"),
										}					
		}
		return finance_statistics










