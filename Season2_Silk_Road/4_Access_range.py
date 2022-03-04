# 1, Phạm vi truy cập thuộc tính và phương thức.

#Public.

#Public là trạng thái công khai nhất trong ba mức độ, 
# khi một thành phần trong class được khai báo ở dạng public tức là chúng ta
#  có thể sử dụng được thành phần đó từ bất kỳ đâu trong chương trình. 
# Và để khai báo một thành phần trong class là public thì mọi người chỉ cần tuân thủ quy tắc sau:

#Tên của thành phần không được bắt đầu bằng ký tự _ mà phải bắt đầu bằng chữ cái.
class Foo:
    # Khai báo thuộc tính ở dạng public
    name = "Foo"
    # Khai báo phương thức ở dạng public
    def getName(self):
        # gọi thành phần trong class
        print(self.name)

# gọi thành phần ngoài class
print(Foo().name) # Foo
Foo().getName() # Foo

class Bar(Foo):
    pass

#test
Bar().getName() # Foo