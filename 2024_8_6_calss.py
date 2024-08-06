class Student : 
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.grades = {"语文":"0","数学":"0","英语":"0"}
    def set_grade(self,couse,grade):
        if couse in self.grades:
            self.grades[couse] = grade
            
    def print_grades(self):
        print(f"学生{self.name}学号{self.id}的成绩为：")
        for couse in self.grades:
            print(f"{couse}:{self.grades[couse]}")
            
zeng = Student("zkx","2021110571")
zeng.set_grade("语文",97)
zeng.set_grade("数学",100)
zeng.set_grade("英语",95)
zeng.print_grades()