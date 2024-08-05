user_weight = float(input("请输入您的体重(kg):"))
user_high = float(input("请输入您的身高(m):"))
user_BMI = user_weight / user_high**2
print(str(user_BMI))

if 25 > user_BMI > 18.5 : 
    print("你属于健康体型")
elif user_BMI <= 18 :
    print("您是偏瘦体形")
else : 
    print("您是偏胖体型")