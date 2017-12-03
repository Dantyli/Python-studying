#while循环使用户可选择何时退出
prompt="\nTell me something and i will repeat it back to you :"
prompt+="\nEnter 'quit' to end the program\n"
message=""
while message=='quit':
    message=input(prompt)
    if message!='quit':
        print(message)
#列表之间移动元素
unconfirmed_users=['alice','bob','dantyli']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print('Vertifying user:'+current_user.title())
    confirmed_users.append(current_user)
print('\nThe following users have been confirmed :')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
responses={}
polling_active=False
while polling_active:
    name=input('\nWhat is your name ?')
    response=input('\nWhat mountain would you like to climb ?')
    responses[name]=response
    repeat=input('Would you like to let another person respond ? (yes/no)')
    if repeat=='no':
        polling_active=False
for name,response in responses.items():
    print(name+' would like to climb '+response+'!')
#可选实参
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
    else :
        full_name=first_name+' '+last_name
    return full_name
musician=get_formatted_name('jimi','hendrix')
#任意数量的实参
def make_pizza(*toppings):
    print(toppings)
#make_pizza('water')
#make_pizza('meat','mian','fruit')
#将函数存储在模块中，导入整个模块
#from module_name import function_name，使用as给函数指定别名

