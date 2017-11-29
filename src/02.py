#生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
for t in fib(7):
    print(t);
#杨辉三角
def triangles():
    L=[1]
    while True:
        yield L
        L.append(0)
        L=[L[i-1]+L[i] for i in range(len(L))]
n=0
for t in triangles():
   # print(t)
    n=n+1
    if n==10:
        break
#字典
alien={'x':0,'y':25,'speed':'medium'}
if alien['speed']=='slow':
    x_increment=1
elif alien['speed']=='medium':
    x_increment=2
else :
    #速度有点快
    x_increment=3
alien['x']=alien['x']+x_increment
print('new x-position :'+str(alien['x']))
#删除键值对
alien={'color':'green','point':'50'}
del alien['point']
#print(alien)
#遍历字典
user={
    'username':'dantyli',
    'age':'19',
    'address':'shenzhen'
    }
for key,value in user.items():
    print("\nKey:"+key)
    print("\nValue:"+value)
#遍历所有的键
for attr in user.keys():
    print(attr)
#set去重
languages={
     'dantyli':'python',
     'lice':'javascript',
     'xiaoming':'php',
     'jav':'php'
    }
for language in set(languages.values()):
    print(language)
#使用range生成外星人
aliens=[]
for alien_num in range(30):
    new_alien={'color':'blue','point':1,'speed':'fast'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color']=='blue':
        alien['color']='red'
        alien['point']=10
for alien in aliens[:5]:
    print(alien)
print('...')
print('Total number of aliens :'+str(len(aliens)))
