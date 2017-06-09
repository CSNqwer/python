#-*- coding:utf-8 -*-
print 'hello world'
print u'你好'
a=['Adam=95.5','Lisa=85','Bart=59']
print a
print a[0]
print a[-1]
a.append('Lily=44')
print a
a.insert(0,'Tom=100')
print a
a.pop()
print a
a.pop(0)
print a
a[1]='Paul=77'
print a
b=a[0]
a[0]=a[2]
a[2]=b
print a
a[0],a[2]=a[2],a[0]
print a
c=("aaa","bbb","cccc")
print c
#这里说的tuple“不变”，是说指向永远不变。
d=('qqqq','wwww',['eeee','rrrr'])
print d
f=d[2]
f[1]="ffffffff"
print d
d[2][0]='999999'
print d
d[2].pop(0)
print d
print len(d)
aa={'aaa':11,'bbb':22,'ccc':33}
print aa['aaa']
print aa.get('aaa')
#key不能使可变的，所以不能用list做key