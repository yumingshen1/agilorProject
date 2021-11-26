#-*-coding:gb2312-*-
# 把二维列表存入excel中
import openpyxl

def writeToExcel(file_path, new_list):
    # total_list = [['A', 'B', 'C', 'D', 'E'], [1, 2, 4, 6, 8], [4, 6, 7, 9, 0], [2, 6, 4, 5, 8]]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'mx'
    for r in range(len(new_list)):
        for c in range(len(new_list[0])):
            ws.cell(r + 1, c + 1).value = new_list[r][c]
            # excel中的行和列是从1开始计数的，所以需要+1
    wb.save(file_path)  # 注意，写入后一定要保存
    print("成功写入文件: " + file_path + " !")
    return 1
path = 'tt.xls'
total_list = [['A', 'B', 'C', 'D', 'E'], [1, 2, 4, 6, 8], [4, 6, 7, 9, 0], [2, 6, 4, 5, 8]]
writeToExcel(path,total_list)

#
# list1 = [['张三','男','未婚',20],['李四','男','已婚',28],['小红','女','未婚',18],['小芳','女','已婚',25]]
# output = open('data.xls','w',encoding='gbk')
# output.write('name\tgender\tstatus\tage\n')
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         output.write(str(list1[i][j]))  #write函数不能写int类型的参数，所以使用str()转化
#         output.write('\t')  #相当于Tab一下，换一个单元格
#     output.write('\n')    #写完一行立马换行
# output.close()


list1 = '''
,result,table,_start,_stop,_time,_value,AGPOINTNAME,_field,_table
,_result,0,2021-11-23T03:35:22.906520247Z,2021-11-26T02:35:22.906520247Z,2021-11-23T03:35:23Z,true,Simu1_1,B,test_table
,_result,0,2021-11-23T03:35:22.906520247Z,2021-11-26T02:35:22.906520247Z,2021-11-23T03:35:24Z,true,Simu1_1,B,test_table
,_result,0,2021-11-23T03:35:22.906520247Z,2021-11-26T02:35:22.906520247Z,2021-11-23T03:35:25Z,true,Simu1_1,B,test_table
,_result,0,2021-11-23T03:35:22.906520247Z,2021-11-26T02:35:22.906520247Z,2021-11-23T03:35:26Z,true,Simu1_1,B,test_table
'''

def test_split(str):
    str = str.split(',_table')[1]
    print(str)

if __name__ == '__main__':
    test_split(list1)