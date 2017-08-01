#encoding:utf-8
from urllib.request import urlopen
from urllib.request import Request
from urllib import parse

req = Request("http://xueshu.baidu.com/s?wd=python&rsv_bp=0&tn=SE_baiduxueshu_c1gjeupa&rsv_spt=3&ie=utf-8&f=8&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D")

postData = parse.urlencode([
    ("wd", "python"),
    ("rsv_bp", "0"),
    ("tn", "SE_baiduxueshu_c1gjeupa"),
    ("rsv_spt", "3"),
    ("ie", "utf-8"),
    ("f", "8"),
    ("rsv_sug2", "1"),
    ("sc_f_para", "sc_tasktype={firstSimpleSearch}")
])

req.add_header("Referer", "http://xueshu.baidu.com/?tn=SE_baiduxueshu_c1gjeupa&sc_as_para=&sc_from=")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36 LBBROWSER")
resp = urlopen(req, data=postData.encode('utf-8'))

print(resp.read().decode("utf-8"))
