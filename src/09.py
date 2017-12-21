#with语句自动调用close方法
with open('dantyli.txt','w') as f:
    f.write('dantyli\nlalala')
with open('dantyli.txt') as f:
    print(f.read())
#file-like Object 
#with open('iwz.png','rb') as f:  读取图片崩溃
#    print(f.read())
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('dantyli')
print(f.getvalue()) #getvalue()用于获得写入后的str
from io import BytesIO #操作二进制数据
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue)
#操作文件和目录
import os
os.name #操作系统类型
#json
import json
d=dict(name='dantyli',age=24,score=99)
json.dumps(d) #返回为str
json_str='{"age":20,"score":99,"name":"dantyli"}'
print(json.loads(json_str))
#进程和线程
from multiprocessing import Process
import os
#子进程执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end')
#re模块
s=r'ABC\-001'
import re
if re.match(r'^\d{3}\-\d{3,8}$','010-12345'):
    print('ok')
#切分字符串
re.split(r'[\s\,]','a b  c')
#分组
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(1)) #0为原始字符串
re_phone=re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_phone.match('010-12345').groups())
#常用内建模块
from datetime import datetime
now=datetime.now()
dt=datetime(2017,12,21,13,43)
print(dt.timestamp())
#collections
from collections import namedtuple
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
