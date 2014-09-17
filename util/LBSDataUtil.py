'''
Created on 2014-9-16

@author: ballad
'''
import  xml.dom.minidom

if __name__ == '__main__':
    # 获得中国地区的坐标数据
    dom = xml.dom.minidom.parse('chinacities.xml')
    root = dom.documentElement
    worksheets = root.getElementsByTagName('Worksheet')
    tables = worksheets[0].getElementsByTagName('Table')
    rows = tables[0].getElementsByTagName('Row') 
    for row in rows:
        cells = row.getElementsByTagName('Cell')
        datas = cells[1].getElementsByTagName('Data')
        print (datas[0].firstChild.data)
    