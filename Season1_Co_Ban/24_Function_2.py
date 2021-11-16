#acking và unpacking arguments

from typing import ValuesView


def kteam(k, t, e, r):
    print(k)
    print(t, e)
    print('end', r)
#Bạn thấy đấy! Hàm này gồm 4 parameter và không có default argument. Vậy nên khi gọi hàm này, bạn buộc phải đưa vào 4 argument.  
# Nhưng bạn có một vấn đề, 4 argument cần  truyền vào khi gọi hàm này lại nằm trong một List.
lst = ['123', 'Kteam', 69.96, 'Henry']
kteam(lst[0], lst[1], lst[2], lst[3])

#Lập trình viên lười lắm, họ không làm chuyện đó đâu. Vậy nên, Python cho phép làm điều đó đơn giản chỉ bằng một dấu *
kteam(*lst)

#nhưng sẽ k dùng đc keywork asgemet


# Bạn còn nhớ hàm print chứ? Nó có khả năng nhận được bao nhiêu argument cũng được. Làm sao nó làm được như thế?

# Đó chính là nhờ packing argument. Đôi lúc, bạn sẽ không thể biết trước được bạn sẽ pass vào bao nhiêu argument. Việc kiểm soát điều đó đôi lúc là bất khả thi.

# Khi bạn sử dụng packing argument. Đồng nghĩa với việc bạn nhờ  một biến đi gói tất cả các giá trị truyền vào cho hàm bằng positional argument thành một Tuple. Nếu không có gì để gói (bạn không truyền vào bất cứ argument nào) thì bạn sẽ nhận được một tuple rỗng. Để giao nhiệm vụ cho một biến làm công việc này, bạn đặt một dấu * trước nó.

def kteam2(*args):
    print(args)
    print(type(args))
kteam2('Kteam', 69.96, 'Henry')
kteam2(*(x for x in range(7)))

#sử dụng dùng packing parameter ta thêm vô số 


# Nếu sau một packing parameter còn có những parameter khác, khi gọi hàm muốn truyền giá trị vào cho các parameter sau packing parameter bạn cần phải sử dụng keyword argument.
def f(*args,kter):
    print(kter)
# f('1', '2') sẽ lỗi
f('1', '2', kter='3')
f(*(x for x in range(7)), kter='3')


#param dict

def kduy(name,age):
    print("Tên : ",name )
    print("Tuổi : ",age)
dict = {
    'name': "duy",
    'age': 21
}
kduy(**dict) # kiểu này sẽ k đc ta phải sửa lại hàm


#unpacking dict
def unpk(**kwargs): #keywordasgment
    print(kwargs)
    print(type(kwargs))
unpk(name="kduy",age=21)
#hoặc
def unpka(**kwargs):
    for key,value in kwargs.items():
        print(key,value)
dicts2 = {
    'name': "duy",
    'age': 21,
    'name3': "Khươngduy",
    'age3': 27,
    'name4': "Lươnduy",
    'age4': 29
}
unpka(**dicts2)


# Biến locals và globals
# Giả sử, bạn có một đoạn script như sau với việc khai báo một biến ngoài hàm và sử dụng ở trong hàm
kteam = 'How Kteam'
def say_slogan():
    print("We are", kteam)
say_slogan()
# Thử một trường hợp tiếp theo là khai báo biến ở trong hàm và sử dụng ở trong hàm

def say_slogan3():
    kteam2 = 'How Kteam'
    print("We are", kteam2)
say_slogan3()
#kết quả giống nhau
#nhưng ta thử gọi thằng kteam2
print(kteam2) #sẽ có vấn đề
#Việc bạn khai báo một biến ở một hàm nào đó thì biến đó chỉ có thể sử dụng trong hàm đó. Còn nếu đi ra ngoài hàm khai báo nó thì biến đó hoàn toàn vô danh > thông báo chưa được khởi tạo

#Biến khai báo ở hàm cha có thể sử dụng trong hàm con nhưng biến ở hàm con không thể sử dụng ở hàm cha.

#Sử dụng lệnh global 
#global <variable>

def vdglobal():
    global duy
    duy = 100
def vdlocal():
    duy2 = 50
    print("biến local = ",duy2)
vdglobal()
vdlocal()
print(duy) # ta thấy khi hàm đc gọi sẽ tạo biến Duy, sử dụng global duy sẽ thành biến toàn cục
# print(duy2) sẽ dùng biến này đc 