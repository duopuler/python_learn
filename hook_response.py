#encoding:utf-8
# import requests
#
# def get_key_info(response,*args,**kwargs):
#
#     print(response.headers['Content-type'])
#
# def main():
#
#     requests.get('https://api.gihub.com',hooks=dict(response=get_key_info))
#
#
# main()

from urllib import request

response = request.urlopen('http://www.baidu.com')

print(response.getcode())
count = response.read()