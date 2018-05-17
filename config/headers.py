
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 16:31:42
# @FileName:  headers.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-17 12:14:40
"""
import json

class Headers():
	"""存放接口请求头部信息"""
	def __init__(self):
		sit_login_headers = {"Host": "salon-sit.lite.meimeifa.cn",
		"Connection": "keep-alive",
		"Content-Length": "",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Origin": "http://salon-client-sit.lite.meimeifa.cn",
		"X-Request-Sign": "6f7d9849c723ee369f8398fbfcc28e8f,1526454898",
		"X-Application-Key": "",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
		(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
		"Content-Type": "application/x-www-form-urlencoded",
		"Accept": "application/json, text/plain, */*",
		"Referer": "http://salon-client-sit.lite.meimeifa.cn/",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7"
		}
		sit_headers = {"Host": "salon-sit.lite.meimeifa.cn",
		"Connection": "keep-alive",
		"Pragma": "no-cache",
		"Cache-Control": "no-cache",
		"Accept": "application/json, text/plain, */*",
		"Origin": "http://salon-client-sit.lite.meimeifa.cn",
		"X-Request-Sign": "2f97ac0e610c63aa878c82c362b093f2,1526460143",
		"X-Application-Key": "",
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 \
		(KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
		"Referer": "http://salon-client-sit.lite.meimeifa.cn/",
		"Accept-Encoding": "gzip, deflate",
		"Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7"
		}
		self.login_headers = {"sit": sit_login_headers, "uat": {}}
		self.headers = {"sit": sit_headers, "uat": {}}

	def get_login_headers(self, env="sit"):
		return self.login_headers.get(env)

	def get_headers(self, env="sit"):
		return self.headers.get(env)


if __name__ == '__main__':
	print(Headers().get_login_headers("uat"))