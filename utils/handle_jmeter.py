# -*- coding: utf-8 -*-
# @Time: 2022/1/5 11:12
# @Author: shenyuming
# b = ''
# for i in range(1,20001):
#     #a = "${table1},AGPOINTNAME=tag_F_${__intSum("+str(i)+r',${num1},)} F=${__Random(1,99999,)}.${__Random(1,9999999,)}${__unescape(\n)}'
#     t = "${table1},AGPOINTNAME=tag_F_${__intSum("+str(i)+r',${num1},)} F=${__Random(1,99999,)}.${__Random(1,9999999,)},F1=${__Random(1,99999,)}.${__Random(1,9999999,)},L=${__Random(1,99999,)}${__unescape(\n)}'
#     b=b+t
# # b = b.split('${__unescape(\n)}')[1]
# filename = r'E:\sym\performance\body.txt'
# with open(filename,'w')as f:
#     f.write(b)
#
#

a = ''
for i in range(1,751):
    f = "${table1},AGPOINTNAME=tag_F_${__intSum("+str(i)+r',${num1},)} F=${__Random(1,99999,)}.${__Random(1,9999999,)}${__unescape(\n)}'
    a=a+f
filename = r'E:\sym\performance\F.txt'
with open(filename,'w')as f:
    f.write(a)

a=''
for i in range(1,751):
    l = "${table1},AGPOINTNAME=tag_L_${__intSum("+str(i)+r',${num1},)} L=${__Random(1,99999,)}${__unescape(\n)}'
    a=a+l
filename = r'E:\sym\performance\L.txt'
with open(filename,'w')as f:
    f.write(a)

a=''
for i in range(1,751):
    s = "${table1},AGPOINTNAME=tag_S_${__intSum("+str(i)+r',${num2},)} S="${__UUID}"${__unescape(\n)}'
    a=a+s
filename = r'E:\sym\performance\S.txt'
with open(filename,'w')as f:
    f.write(a)

a=''
for i in range(1,751):
    b = "${table1},AGPOINTNAME=tag_B_${__intSum("+str(i)+r',${num2},)} B=true${__unescape(\n)}'
    a=a+b
filename = r'E:\sym\performance\B.txt'
with open(filename,'w')as f:
    f.write(a)