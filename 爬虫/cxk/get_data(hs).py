
# -*- codeing = utf-8 -*-
from 爬虫.cxk.cxk_hs import *
import xlwt

#设置excel
wb = xlwt.Workbook(encoding="utf-8",style_compression=0)
sheet = wb.add_sheet("b站爬去",cell_overwrite_ok=True)
sheet.write(0,0,"序号")
sheet.write(0,1,"名称")
sheet.write(0,2,"链接")
sheet.write(0,3,"观看次数")
sheet.write(0,4,"弹幕")
sheet.write(0,5,"时间")
sheet.write(0,6,"作者")

n = 1
browser = search("https://www.bilibili.com/")
all_h = browser.window_handles
browser.switch_to.window(all_h[1])

total = browser.find_element_by_xpath("//*[@id='i_cecream']/div/div[2]/div[2]/div/div/div/div[2]/div/div/button[9]").text
# n = save_to_excel(browser,sheet,n,wb) #调用函数存储页面数据
# browser = next_page(browser)
for i in range(1,int(total)+1):

    time.sleep(3) #等待加载
    n = save_to_excel(browser,sheet,n,wb)  # 调用函数存储页面数据
    browser = next_page(browser)  # 翻页



