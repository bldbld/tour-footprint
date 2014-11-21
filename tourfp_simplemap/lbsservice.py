#-*-coding:utf-8-*-
'''
Created on 2014-5-29

@author: ballad
'''
import urllib
#from urlparse import urlparse
from xml.etree import ElementTree
from util.CoordinateDataUtil import CoordinateDataUtil

# 坐标点信息
class SimplePoint():
    lat = None
    lng = None

# 通过城市名称获取坐标点SimplePoint
def getCityPlaceByBaidu(city_name):
    geo_data = getGeoCoderDataByBaidu(city_name)
    root = ElementTree.fromstring(geo_data)
    result = SimplePoint()
    result.lat = root.find('result').find('location').find('lat').text
    result.lng = root.find('result').find('location').find('lng').text
    print(result.lat)
    print(result.lng)
    return result

# 通过城市名称Baidu GEO XML数据
def getGeoCoderDataByBaidu(city_name):
    city_name = urllib.quote(city_name.encode('utf-8', 'replace'));
    spt_str = urllib.quote("市政府".encode('utf-8', 'replace'))
    url = "http://api.map.baidu.com/geocoder/v2/?ak=fci7iKfiurBcqTSeXEm0lGtw&callback=renderOption&output=xml&address="+city_name+spt_str+"&city="+city_name;
    print("Starting Req Baidu")
    print(city_name)
    print(url)
    # url = url.decode('gbk', 'replace')
    # url = urllib.quote(url.encode('utf-8', 'replace'))
    # req = urllib.Request(url)
    try:
        response = urllib.urlopen(url)
        text = response.read()
    except:
        print ("got exception")
    print (text)
    return text

# 通过城市名称获取本地存储的 XML数据
def getGeoCoderDataByLocalUtil(city_name):
    city_name = urllib.quote(city_name.encode('utf-8', 'replace'));
    util = CoordinateDataUtil.instance()
    spt_str = urllib.quote("市政府".encode('utf-8', 'replace'))
    url = "http://api.map.baidu.com/geocoder/v2/?ak=fci7iKfiurBcqTSeXEm0lGtw&callback=renderOption&output=xml&address="+city_name+spt_str+"&city="+city_name;
    print("Starting Req Baidu")
    print(city_name)
    print(url)
    # url = url.decode('gbk', 'replace')
    # url = urllib.quote(url.encode('utf-8', 'replace'))
    # req = urllib.Request(url)
    try:
        response = urllib.urlopen(url)
        text = response.read()
    except:
        print ("got exception")
    print (text)
    return text

if __name__ == '__main__':
    getCityPlaceByBaidu('北京')
