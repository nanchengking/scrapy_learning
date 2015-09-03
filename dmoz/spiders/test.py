#coding=utf-8
file=open('item.txt','r')
info=file.read()
print info[0:300]
print info[-300:len(info)]