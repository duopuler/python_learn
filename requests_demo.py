#encoding:utf-8
import requests

# URL_IP = 'http://203.244.219.242/ip'
URL_IP = 'https://www.httpbin.org/ip'
# URL_IP = 'https://www.baidu.com'

URL_GET = 'http://203.244.219.242/get'

def use_simple_requests():
    response = requests.get(URL_IP)
    print('>>>>Response Headers:')
    print(response.headers)
    print('>>>>Response Body:')
    print(response.text)

def use_params_requests():
    params = {'parma1': 'hello', 'param2': 'world'}
    response = requests.get(URL_IP,params=params)

    print('>>>>Response Headers:')
    print(response.headers)
    print('>>>>Status Code:')
    print(response.status_code)
    print(response.reason)
    print('>>>>Response Body:')
    print(response.json())

if __name__ == '__main__':
    print('>>>>Use simple requests:')
    use_params_requests()
    print()
    print('>>>>Use params requests:')
    use_params_requests()