#初始化方法
d = {'name':'姬织', 'age':18}
print(d['name'])
#函数创建字典的两种方法
l = [('name', u'姬织'), ('age', '18')]
d = dict(l)

d = dict(name = '姬织', age = '18')

#空字典
d = dict()
d = {}

##集合
#元素不可重复
s = {'姬织', '姬织', '小黑', '千和', '千和'}
print(s)