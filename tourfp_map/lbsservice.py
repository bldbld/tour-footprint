#-*-coding:utf-8-*-
'''
Created on 2014-5-29

@author: ballad
'''
import urllib
from xml.etree import ElementTree
from tourfp_map.models import place

# 通过城市名称获取Place对象
def getCityPlaceByBaidu(city_name):
    geo_data = getGeoCoderDataByBaidu(city_name)
    root = ElementTree.fromstring(geo_data)
    place_result = place()
    place_result.lat = root.find('result').find('location').find('lat').text
    place_result.lng = root.find('result').find('location').find('lng').text
    place_result.title = city_name
    return place_result

# 通过城市名称Baidu GEO XML数据
def getGeoCoderDataByBaidu(city_name):
    url = "http://api.map.baidu.com/geocoder/v2/?ak=fci7iKfiurBcqTSeXEm0lGtw&callback=renderOption&output=xml&address="+urllib.parse.quote(city_name)+urllib.parse.quote("市政府")+"&city="+urllib.parse.quote(city_name);
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    text = response.read()
    # print (text)
    return text

# 通过地点名获取地点
def getPlaceByTitle(p_title):
    storage_place = place.objects.get(title = p_title)
    if (storage_place):
        return storage_place

    
if __name__ == '__main__':
    getCityPlaceByBaidu('百度大厦')