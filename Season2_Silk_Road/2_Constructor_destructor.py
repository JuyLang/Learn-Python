#1, Phương thức khởi tạo - constructor.
#Phương thức khởi tạo là một phương thức đặc biệt ở trong class, phương thức này mặc định sẽ được gọi khi chúng ta khởi tạo class đó. Nó thường được dùng để khởi tạo các thuộc, xử lý phương thức hoặc là dùng để nhận các tham số truyền vào class khi khởi tạo.

#Để khai báo một phương thức khởi tạo trong class thì mọi người chỉ cần viết 
# một hàm có tên là __init__ với cú pháp như sau:
# class className:
#     def __init__(self, param1, param2,...):
#         code

class Person():
    def __init__(self):
        print("class được khởi tạo")

test = Person()
#VD: Khai báo các tham số truyền vào cho phương thức khởi tạo.
class People():
    def __init__(self, name, age,male):
        print("class được khởi tạo")
        print("Name: "+name +" Age:" + age + " Male: "+male )
        print("name: %s age: %s male: %s" %(name,age,male))
duy = People("Lăng Khương Duy", '20' , "Nam")    

#2, Phương thức hủy - deconstructor.
#Trái ngược với phương thức khởi tạo, thì phương thức hủy sẽ được gọi khi chúng ta hủy một class, 
# hay nó cách khác nó luôn được thực thi cuối cùng khi chúng ta khởi tạo một class. 
# Nó thường được dùng để giải phóng tài nguyên của class.


#cú pháp
# def __del__(self):
#     # code

class Person():
    def __init__(self):
        print("class được khởi tạo")
    def __del__(self):
        print("class đã bị hủy")
        
test2 = Person()
test3 = Person()
#ví dụ 
# class Person:
#     def __init__(self, name, age, male):
#         print("Class person được khởi tạo!")
#         self.name, self.age, self.male = name, age, male
    
#     def getName(self):
#         print("Name: %s" %(self.name))
    
#     def getAge(self):
#         print("Age: %d" %(self.age))
    
#     def getMale(self):
#         print("Male: %d" %(self.male))
    
#     def __del__(self):
#         print('Class Person được hủy')
#         del self.name,self.age,self.male

# person = Person('Vu Thanh Tai', 22, True)
# person.getName()
# person.getAge()
# person.getMale()
# kết quả: 
# Class person được khởi tạo!
# Name: Vu Thanh Tai
# Age: 22
# Male: 1
# Class Person được hủy

