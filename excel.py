#-*-coding:gb2312-*-
# �Ѷ�ά�б����excel��
import openpyxl

def writeToExcel(file_path, new_list):
    # total_list = [['A', 'B', 'C', 'D', 'E'], [1, 2, 4, 6, 8], [4, 6, 7, 9, 0], [2, 6, 4, 5, 8]]
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'mx'
    for r in range(len(new_list)):
        for c in range(len(new_list[0])):
            ws.cell(r + 1, c + 1).value = new_list[r][c]
            # excel�е��к����Ǵ�1��ʼ�����ģ�������Ҫ+1
    wb.save(file_path)  # ע�⣬д���һ��Ҫ����
    print("�ɹ�д���ļ�: " + file_path + " !")
    return 1
path = 'tt.xls'
total_list = [['A', 'B', 'C', 'D', 'E'], [1, 2, 4, 6, 8], [4, 6, 7, 9, 0], [2, 6, 4, 5, 8]]
writeToExcel(path,total_list)

#
# list1 = [['����','��','δ��',20],['����','��','�ѻ�',28],['С��','Ů','δ��',18],['С��','Ů','�ѻ�',25]]
# output = open('data.xls','w',encoding='gbk')
# output.write('name\tgender\tstatus\tage\n')
# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         output.write(str(list1[i][j]))  #write��������дint���͵Ĳ���������ʹ��str()ת��
#         output.write('\t')  #�൱��Tabһ�£���һ����Ԫ��
#     output.write('\n')    #д��һ��������
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