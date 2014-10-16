#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User  

# Create your models here.

# 地点类
class place(models.Model):
    title = models.CharField(max_length=100)  # 地点标题
    lng = models.CharField(max_length=20)  # 经度
    lat = models.CharField(max_length=20)  # 纬度
    is_manual = models.BooleanField()  # 是否为手动添加，手动添加不更新
    update_time = models.DateTimeField()  # 更新时间，当发现过旧，会更新该地点
    
    def __unicode__(self):
        return '%s %s %s %s %s' % (self.title, self.lng, self.lat, self.is_manual, self.update_time)

# 旅行集
class tourset(models.Model):
    owner = models.ForeignKey(User)  # 所属用户
    title = models.CharField(max_length=200)  # 旅行标题
    def __unicode__(self):
        return '%s %s' % (self.owner, self.title)


# 旅行类 
class trip(models.Model):
    owner = models.ForeignKey(User)  # 所属用户
    date = models.DateField()  # 旅行日期
    create_time = models.DateTimeField()  # 创建时间
    remark = models.CharField(max_length=200)  # 旅行备注
    url = models.URLField()  # 关联网址
    tourset = models.ForeignKey(tourset)  # 所属旅行集
    color = models.CharField(max_length=20)  # 旅行颜色
    weight = models.IntegerField()  # 旅行权重
    
    def __unicode__(self):
        return '%s %s %s %s %s %s' % (self.owner, self.date, self.create_time, self.remark, self.url, self.tourset)

# 路线类 
class route(models.Model):
    place_from = models.ForeignKey(place, related_name='place_from_id')  # 起点
    place_to = models.ForeignKey(place, related_name='place_to_id')  # 终点
    tour = models.ManyToManyField(trip)  # 所属旅行，同一条线路可能为多个旅行公用
    
    def __unicode__(self):
        return '%s %s %s' % (self.place_from, self.place_to, self.tour)
