#encoding: utf-8
'''
Created on 2014-9-18

@author: ballad
'''
from django.core.files import File
from util.lbsmodel import CoordinatePoint 
from util.lbsdata_china import ChinaCitiesData

# 坐标服务工具类
class CoordinateDataUtil(object):
    '''
    classdocs
    '''
    placeList = []
    placeCoorDict = {}

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    # 初始化数据
    def initData(self):
        ft = open("/tour-footprint/util/chinadata.csv")
        f = File(ft)
        line = f.readline() # 调用文件的 readline()方法
        while line:
            # print (line, end = '') # 将忽略换行符
            line = f.readline()
            linedata = line.split(',')
            if len(linedata) == 5:
                self.placeList.append(linedata[2])
                if len(linedata[3]) == 0:
                    print('hasnone' + linedata[2])
        f.close()
        
    # 初始化数据
    def initDataStr(self):
        chinaData = ChinaCitiesData()
        chinaDatas = chinaData.getData().split(';')
        for line in chinaDatas:
            #print (line) 
            linedata = line.split(',')
            if len(linedata) == 5: #code,full-title,title,lng,lat
                self.placeList.append(linedata[2])
                if len(linedata[3]) == 0 or (len(linedata[4]) == 0):
                    # 如果没有坐标数据，不生成
                    print('hasnone lng' + linedata[2])
                else:
                    p = CoordinatePoint()
                    p.lng = linedata[3]
                    p.lat = linedata[4]
                    p.id = linedata[0]
                    self.placeCoorDict[p.id] = p
                    
    @classmethod    
    def instance(cls):    
        if not hasattr(cls, "_instance"):    
            cls._instance = cls()    
            cls._instance.initDataStr()
        return cls._instance    
  
    @classmethod    
    def initialized(cls):    
        """Returns true if the singleton instance has been created."""    
        return hasattr(cls, "_instance")    
    
    def service(self):    
        #print (self.i)  
        print(self.placeList[0])
        return
    
    # 一个基本匹配方法，TODO 后续完善
    def match(self, text):
        returnList = []
        count = 0
        for place in self.placeList:
            if place.startswith(text):
                print('match')
                returnList.append(place)
                count = count + 1
            if count >= 10: # 最多提供10个
                break
        return returnList
    
    # 通过城市标题获得 坐标
    def getCoordinateByTitle(self, text):
        for place in self.placeList:
            if place == text:
                print('get')
        # TODO
                
    def geneCoordinatePoint(self):
        # TODO
        return

print (CoordinateDataUtil.initialized()  )  
ioloop = CoordinateDataUtil.instance()    
ioloop.service()    
    
#if os.fork() == 0:  
print (CoordinateDataUtil.initialized() )   
ioloop = CoordinateDataUtil.instance()    
ioloop.service()   

