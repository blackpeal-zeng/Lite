
"""
# -*- coding: utf-8 -*-
# @Author: zengqiu
# @Date:   2018-05-16 16:31:42
# @FileName:  headers.py
# @Project: SubWorkSpace
# @Last Modified by:   Zeng Ball
# @Last Modified time: 2018-05-16 18:40:29
"""
import json

class SitHeaders():
	"""存放接口请求头部信息"""
	def __init__(self):
		login_headers = {"Host": "salon-sit.lite.meimeifa.cn",
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
		headers = {"Host": "salon-sit.lite.meimeifa.cn",
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

	def get_login_headers(self):
		return json.dumps(self.login_headers)

	def get_headers(self):
		return json.dumps(self.headers)

class UatHeaders():
	"""存放接口请求头部信息"""
	pass


if __name__ == '__main__':
	print(HEADERS.get("sit"))