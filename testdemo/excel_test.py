#-*-coding:gb2312-*-
## ����д��excel
import sys
import xlwt
def write_ecvel_data():
    # ����������
    book = xlwt.Workbook(encoding='utf-8',style_compression=0) ##utf-8��ʽ����ѹ��
    # ����һ��sheet
    sheet1 = book.add_sheet('Sheet1', cell_overwrite_ok=True)
    col = ('AGPOINTNAME', '����', 'status', 'value', '����')
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