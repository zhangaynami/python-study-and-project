# -*- codeing = utf-8 -*-
# -*- codeing = utf-8 -*-

import xlwt
from cxk_hs import *
wb = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = wb.add_sheet("b站爬去",cell_overwrite_ok=True)
sheet.write(0,0,"序号")
sheet.write(0,1,"名称")
sheet.write(0,2,"链接")
sheet.write(0,3,"观看次数")
sheet.write(0,4,"弹幕")
sheet.write(0,5,"时间")
sheet.write(0,6,"作者")
search("https://www.bilibili.com/")