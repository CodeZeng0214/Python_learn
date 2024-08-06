user_list = [] ##不可放入None作为空
while 1 :
    user_in = input("请输入你要求的数字组，q结束")
    if user_in == "q" :
        break
    else : 
        user_list.append(float(user_in)) ##不是赋值
print(sum(user_list) / len(user_list))
        