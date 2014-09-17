#-*-coding:utf-8-*-
'''
Created on 2014-5-29

@author: ballad
'''
import urllib
from xml.etree import ElementTree
from tourfp_simplemap.models import SimpleRoute

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
    url = "http://api.map.baidu.com/geocoder/v2/?ak=fci7iKfiurBcqTSeXEm0lGtw&callback=renderOption&output=xml&address="+urllib.parse.quote(city_name)+urllib.parse.quote("市政府")+"&city="+urllib.parse.quote(city_name);
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    text = response.read()
    print (text)
    return text

if __name__ == '__main__':
    getCityPlaceByBaidu('百度大厦')