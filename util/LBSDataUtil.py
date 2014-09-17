'''
Created on 2014-9-16

@author: ballad
'''
import  xml.dom.minidom
from xml.dom.minidom import Document
from tourfp_simplemap.lbsservice import SimplePoint, getCityPlaceByBaidu

if __name__ == '__main__':
    # 获得中国地区的坐标数据
    # 导入的XML为Office 2013Excel导出
    # 解析
    dom = xml.dom.minidom.parse('chinacities.xml')
    root = dom.documentElement
    worksheets = root.getElementsByTagName('Worksheet')
    tables = worksheets[0].getElementsByTagName('Table')
    rows = tables[0].getElementsByTagName('Row') 
    # 写入的文档
    writedoc = Document()
    wroot = writedoc.createElement('root')
    writedoc.appendChild(wroot)
    start = False
    for row in rows:
        error = False
        cells = row.getElementsByTagName('Cell')
        datas = cells[0].getElementsByTagName('Data')
        place_code = datas[0].firstChild.data
        datas = cells[1].getElementsByTagName('Data')
        place_name = datas[0].firstChild.data
        show_name = place_name
        if place_name == '富县':
            start = True
        if not start:
            continue
        # 一些判断
        if place_name == '市辖区':
            continue
        elif place_name == '县':
            continue
        elif place_name.endswith('省') or place_name.endswith('自治区') :
            continue
        elif place_name.endswith('自治县'):
            pass
        elif place_name.endswith('县') and len(place_name) > 2:
            show_name = place_name[:-1]
        elif place_name.endswith('市') and len(place_name) > 2:
            show_name = place_name[:-1]
        elif place_name.endswith('区') and len(place_name) > 2:
            show_name = place_name[:-1]
        elif place_name.endswith('省'):
            continue
        point = getCityPlaceByBaidu(show_name)
        if point.lat is None or point.lng is None:
            error = True
            print ('error')  
            prtstr = place_code+","+place_name+","+show_name
            print (prtstr)
        else :
            prtstr = place_code+","+place_name+","+show_name+","+point.lat+","+point.lng
            print (prtstr)
        wplace = writedoc.createElement('place')
        wroot.appendChild(wplace)
        # 国家代码
        wcode = writedoc.createElement('code')
        wplace_code = writedoc.createTextNode(place_code)
        wcode.appendChild(wplace_code)
        # 地点名
        wname = writedoc.createElement('name')
        wplace_name = writedoc.createTextNode(place_name)
        wname.appendChild(wplace_name)
        # 显示名
        wshow = writedoc.createElement('showname')
        wshow_name = writedoc.createTextNode(show_name)
        wshow.appendChild(wshow_name)
        # 追加子节点
        wplace.appendChild(wcode)
        wplace.appendChild(wname)
        wplace.appendChild(wshow)
        if not error:
            # 坐标LNG
            wlng = writedoc.createElement('lng')
            wlng_text = writedoc.createTextNode(point.lng)
            wlng.appendChild(wlng_text)
            # 坐标LAT
            wlat = writedoc.createElement('lat')
            wlat_text = writedoc.createTextNode(point.lat)
            wlat.appendChild(wlat_text)
            wplace.appendChild(wlng)
            wplace.appendChild(wlat)
    print (writedoc.toxml())
    
