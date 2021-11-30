import xlrd
import xlwt
import pandas as pd

# csv文件转换成xlsx文件
def csv_to_xlsx_pd(data1, data2):
    csv = pd.read_csv(data1, encoding='utf-8')
    csv.to_excel(data2, sheet_name='sheet1')

def compare_excel(file1_name, file2_name):
    open_excel1 = xlrd.open_workbook(file1_name)  # 用于比较的第一个文件
    open_excel2 = xlrd.open_workbook(file2_name)  # 用于比较的第二个文件
    result_excel = xlwt.Workbook()  # 创建一个文件用来存放比较结果
    comp_restult = result_excel.add_sheet("比对结果")

    excel1_name = open_excel1.sheet_names()
    tp1 = open_excel1.sheet_by_name(excel1_name[0])  # 打开excel文件中的第一个表格

    excel2_name = open_excel2.sheet_names()
    tp2 = open_excel2.sheet_by_name(excel2_name[0])
    for i in range(tp1.nrows):
        for j in range(tp1.ncols):
            if i == 0:
                comp_restult.write(i, j, str(tp2.cell(i, j).value))  # 第一行数据不比对
            else:
                if str(tp1.cell(i, j).value) != str(tp2.cell(i, j).value):  # 将两个excel表格中同行同列进行比较
                    #style = xlwt.easyxf('font:bold 1, color blue')  # 设置不匹配内容的字体及其颜色
                    result = str(tp1.cell(i, j).value) + "和" + str(tp2.cell(i, j).value) + "不一致"
                    comp_restult.write(i, j, result)
                else:
                    comp_restult.write(i, j, tp1.cell(i, j).value)
    result_excel.save('E:/sym/4.2迁移/Agilordata比对结果.xls')


if __name__ == '__main__':
    file1_name = 'E:/sym/4.2迁移/db6.0-5.xlsx'
    file2_name = 'E:/sym/4.2迁移/修改数据4.2/db4.2-5.xlsx'
    compare_excel(file1_name, file2_name)