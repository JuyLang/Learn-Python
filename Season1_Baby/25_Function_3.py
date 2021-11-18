# Giả sử bạn viết một hàm xử lí một công việc và bạn muốn sao lưu kết quả sau khi xử lí xong ra một biến. Nhưng bạn lại không thể làm điều đó. Vì nếu tạo ra một biến và lưu ngay trong hàm thì như ta đã biết, nó không thể sử dụng được ở mức toàn chương trình (global).

# Giá mà bạn có thể ném cái dữ liệu sau khi xử lí xong ra ngoài nhỉ
#Đây là lệnh chỉ sử dụng được ở trong hàm (nếu sử dụng ở ngoài hàm sẽ có nhắc lỗi)
#return [object]
# như các ngôn ngữ khác

#Dùng return để trả về nhiều giá trị một lúc
#Với Python, việc bạn có thể return nhiều giá trị một lúc bản chất nó không nằm ở câu lệnh Python, mà là do Python thiết kế đặc biệt để có thể unpack các object trả về. Bạn hãy xem ví dụ về khai báo sau đây

def chuvivadientich(a,b):
    chuvi = (a+b)*2
    dientich = a*b
    return chuvi, dientich
width = 100
height = 36
chuvih2, dientichh2 = chuvivadientich(width,height)
print(chuvih2)
print(dientichh2)

#Yield
# iterables Khi bạn tạo  ra một list, bạn có thể truy xuất lần lượt từng giá trị của list đó. Người ta gọi đó là iteration
lst = [1, 'KDuy', 2]
for value in lst:
    print(value)

#generator
#Generator là iterator, một dạng của iterable nhưng khác ở chỗ bạn không thể tái sử dụng. Vì sao lại như vậy? Generator không lưu trữ tất cả các giá trị của bạn ở bộ nhớ, mà nó sinh ra lần lượt
kteam_gen = (value for value in range(8))
for value in  kteam_gen:
    print(value)

#Lệnh yield
#Lệnh này cách sử dụng gần giống với lệnh return, tuy nhiên nó khác return ở chỗ trả về một object thì yield sẽ trả về một generator.


def square(lst):
    sq_lst = []
    for num in lst:
        sq_lst.append(num**2)
    return sq_lst

kteam_ret = square([1, 2, 3])
for value in kteam_ret:
        print(value)
#đây là return thông thường

#sử dụng yield
def square(lst):
    for num in lst:
        yield num**2

kteam_ret = square([1, 2, 3])
for value in kteam_ret:
        print(value)

#send Đây là phương thức giúp bạn gửi giá trị vào trong một generator..
