#coding=utf-8
file=open('item.txt','r')
info=file.read()
print info[0:50]
print info[-50:len(info)]