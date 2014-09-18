'''
Created on 2014-9-18

@author: ballad
'''
from django.core.files import File

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
        ft = open("C:/Users/ballad/Git/tour-footprint/util/chinadata.csv")
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
        
    @classmethod    
    def instance(cls):    
        if not hasattr(cls, "_instance"):    
            cls._instance = cls()    
            cls._instance.initData()
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
        for place in self.placeList:
            if place.startswith(text):
                returnList.append(place)
        return returnList

print (CoordinateDataUtil.initialized()  )  
ioloop = CoordinateDataUtil.instance()    
ioloop.service()    
    
#if os.fork() == 0:  
print (CoordinateDataUtil.initialized() )   
ioloop = CoordinateDataUtil.instance()    
ioloop.service()   

