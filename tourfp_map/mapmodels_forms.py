# coding=utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from tourfp_map.models import tourset, trip, place

# 添加旅行集
class add_tourset_form(forms.Form):
    tourset_name = forms.CharField(label=_("旅行集名称："), max_length=200, widget=forms.TextInput(attrs={'size': 30, })) 

# 添加旅行
class add_trip_form(forms.Form):
    CHOICES = [
        (1, 'Example'),
    ]
    trip_remark = forms.CharField(label=_("旅行备注："), max_length=200, widget=forms.TextInput(attrs={'size': 30, })) 
    trip_tourset = forms.ChoiceField(choices=[(1, 'Example'), ], required=True, label='旅行集：')
         
    def __init__(self, *args, **kwargs):
        super(add_trip_form, self).__init__(*args, **kwargs)
        self.fields['trip_tourset'].widget.choices = kwargs.pop('trip_tourset_choices', [(tourset(), 'Example'), ])
        # trip_date = forms.DateField(label=_("旅行日期："), widget=forms.DateInput(attrs={'size': 30, })) 
    
# 添加一条路线
class add_route_form(forms.Form):
    route_place_from = forms.ChoiceField(choices=[(1, 'Example'), ], required=True, label='起点：')
    route_place_to = forms.ChoiceField(choices=[(1, 'Example'), ], required=True, label='终点：')
    route_trip = forms.ChoiceField(choices=[(1, 'Example'), ], required=True, label='所属旅行：')
    
    def __init__(self, *args, **kwargs):
        super(add_route_form, self).__init__(*args, **kwargs)
        self.fields['route_place_from'].widget.choices = kwargs.pop('route_place_from_choices', [(place(), 'Example'), ])
        self.fields['route_place_to'].widget.choices = kwargs.pop('route_place_to_choices', [(place(), 'Example'), ])
        self.fields['route_trip'].widget.choices = kwargs.pop('route_trip_choices', [(trip(), 'Example'), ])

# 添加一条路线 (文本模式)
class add_route_text_form(forms.Form):
    route_place_from = forms.CharField(label=_("起点："), max_length=100, widget=forms.TextInput(attrs={'size': 30, })) 
    route_place_to = forms.CharField(label=_("终点："), max_length=100, widget=forms.TextInput(attrs={'size': 30, })) 
    route_trip = forms.ChoiceField(choices=[(1, 'Example'), ], required=True, label='所属旅行：')
    
    def __init__(self, *args, **kwargs):
        super(add_route_text_form, self).__init__(*args, **kwargs)
        self.fields['route_trip'].widget.choices = kwargs.pop('route_trip_choices', [(trip(), 'Example'), ])

# 添加一条路线 (简单文本模式)
class add_route_simple_form(forms.Form):
    route_place_from = forms.CharField(label=_("起点："), max_length=100, widget=forms.TextInput(attrs={'size': 30, })) 
    route_place_to = forms.CharField(label=_("终点："), max_length=100, widget=forms.TextInput(attrs={'size': 30, })) 

# 手工添加地点
class add_place_form(forms.Form):
    place_title = forms.CharField(label=_("地点："), max_length=100, widget=forms.TextInput(attrs={'size': 30, })) 
    place_lng = forms.CharField(label=_("经度："), max_length=20, widget=forms.TextInput(attrs={'size': 10, })) 
    place_lat = forms.CharField(label=_("纬度："), max_length=20, widget=forms.TextInput(attrs={'size': 10, })) 
