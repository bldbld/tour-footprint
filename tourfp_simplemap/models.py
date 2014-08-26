from django.db import models
from django.contrib.auth.models import User  

# 路线类 
class SimpleRoute(models.Model):
    from_title = models.CharField(max_length=100)  # 地点标题
    from_lng = models.CharField(max_length=20)  # 经度
    from_lat = models.CharField(max_length=20)  # 纬度
    to_title = models.CharField(max_length=100)  # 地点标题
    to_lng = models.CharField(max_length=20)  # 经度
    to_lat = models.CharField(max_length=20)  # 纬度
    owner = models.ForeignKey(User)  # 所属用户
    
    def to_json_brief (self):
        return "{id:'%s', from_title:'%s', to_title:'%s'}" % (self.id, self.from_title, self.to_title)

    def to_json_line (self):
        return "{id:'%s', from_title:'%s', to_title:'%s', from_lng:'%s', from_lat:'%s',to_lng:'%s',to_lat:'%s'}" % (self.id, self.from_title, self.to_title, self.from_lng, self.from_lat, self.to_lng, self.to_lat)
    
    def __unicode__(self):
        return '%s %s %s %s %s %s %s' % (self.from_title, self.from_lng, self.from_lat, self.to_title, self.to_lng, self.to_lat, self.owner)

# 地点缓存，记录已经保存的地点信息
class RouteCache(models.Model):
    title = models.CharField(max_length=100)  # 地点标题
    lng = models.CharField(max_length=20)  # 经度
    lat = models.CharField(max_length=20)  # 纬度
