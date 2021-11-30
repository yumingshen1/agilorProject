#-*-coding:gb2312-*-
## 数据写入excel
import sys
import xlwt
def write_ecvel_data():
    # 创建工作簿
    book = xlwt.Workbook(encoding='utf-8',style_compression=0) ##utf-8格式，不压缩
    # 创建一个sheet
    sheet1 = book.add_sheet('Sheet1', cell_overwrite_ok=True)
    col = ('AGPOINTNAME', '日期', 'status', 'value', '类型')
    for i in range(0,5):
        sheet1.write(0,i,col[i])
    #
    # for i in range(0,2):
    #     data = data[i]
    #     for j in range(0,5):
    #         sheet1.write(i+1,j,data[j])
    savepath = 'sum1.xls'
    book.save(savepath)

if __name__ == '__main__':
    write_ecvel_data()