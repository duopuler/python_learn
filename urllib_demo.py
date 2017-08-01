#encoding:utf-8
import urllib
import urllib2

URL_IP = 'http://203.244.219.242/ip'

def use_simple_urllib2():
    response = urllib2.urlopen(URL_IP)
