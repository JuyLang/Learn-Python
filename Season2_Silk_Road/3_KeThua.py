#Nhắc đến hướng đối tượng, thì chúng ta sẽ phải nhắc về 4 tính chất đặc thù của nó
#  là trừu tượng, kế thừa, đóng gói và đa đa hình. 
# Bài hôm nay chúng ta sẽ tìm hiểu về kế thừa trong Python hướng đối tượng.
#Kế thừa là sử dụng lại một cái gì đó đã có vào trong cái mới để phát triển ra cái mới.

# Giả sử bạn được sếp giao cho một task viết 2 class Male và Femal chứa 2 phương thức getName,getAge. 
# Nếu như bạn không sử dụng tính kế thừa trong hướng đối tượng thì bạn sẽ phải viết 2 class có các phương thức và thuộc tính tương đối giống nhau như trên.
#  Nhưng thay vào đó nếu như bạn nhận thấy 2 class này có các điểm chung giống nhau thì bạn có thể tạo ra một class cha chứa những điểm chúng này, từ đó ở mỗi class con sẽ kế thừa những điểm chung đó và phát triển thêm các điểm riêng.
#  Thay vì phải viết lại như trước....


# cú pháp
# class className(inherit1, inherit2,...):
    #code

# Trong đó: Cú pháp khai báo class thì mình đã giới thiệu với mọi người ở bài trước rồi. 
# inherit1, inherit2,... là tên của các class mà bạn muốn kế thừa.
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def getName(self):
        print("Name: %s" %(self.name))
    
    def getAge(self):
        print("Age: %d" %(self.age))
    def getSex(self):
        print("Sex: %s" %(self.sex))

# một class Male kế thừa từ class Person.
class Male(Person):
    sex = "Nam";

#Mình sẽ khởi tạo class Male và gọi một vài phương thức được khai báo trong lớp cha của nó

m = Male("Lươn Khươn Duy",20)
m.getName()
m.getAge()
m.getSex()

#4, Ghi đè phương thức và thuộc tính.
#Trong trường hợp cả hai class cha và con tồn tại các thuộc tính và phương thức có cũng tên,
#thì trong Python sẽ nó sẽ ưu tiên thực thi và gọi các phương thức và thuộc tính khai báo trong class được khởi tạo.
class Foo:
    name = 'Foo'
    def getName(self):
        print("Class: Foo")
class Bar(Foo):
    name = 'Bar'
    def getName(self):
        print("Class: Bar")
b = Bar()
b.getName()

#Super()
#Trong trường hợp ở class con mà bạn muốn sử dụng đến các thành phần trong class cha 
# thì bạn phải sử dụng hàm super theo cú pháp sau:

## Đối với thuộc tính.
# super().variableName
# # Đối với phương thức.
# super().methodName()
class Foo:
    name = 'Foo'
    def getName(self):
        print("Class: Foo")
        
class Bar(Foo):
    name = 'Bar'
    def getName(self):
        print("Atribute name = " + super().name)
        super().getName()

Bar().getName()

#5, Đa kế thừa trong Python.
class First:
    def getFirst(self):
        print("đây là class1")
class Second:
    def getSecond(self):
        print("đây là class2")

class Third(First, Second):
    def getThird(self):
        print("Kế Thừa 2 class")

test10 = Third()
test10.getFirst()
test10.getSecond()
test10.getThird()