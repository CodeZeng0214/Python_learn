drawing_dict = {"火水":"草薙直哉","卧樱":"草薙健一郎","墓志铭的美妙混乱":"御樱稟","天空的彼岸":"恩田宁","向日葵":"夏目圭"}
drawing_dict["樱日狂想"] = "草薙直哉"
drawing_dict["绘空"] = "冰川瑠璃绪"
drawing_dict["圣约翰节前夜————抑或是孕育出艺术之鲜血的意义"] = "本间心铃"
query = input("请输入你想查询的画作名称：")
if query in drawing_dict : 
    print("您查询的" + query + "作者是：" + drawing_dict[query])
else :
    print("暂未收录")
    
for draw, creater in drawing_dict.items():
    print(draw + "的作者是:" + creater)
    
temp = 0;
for i in range(1,101,1):
    temp = temp + i
print(temp)