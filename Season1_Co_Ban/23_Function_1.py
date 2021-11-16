# Thời gần xưa, con người ta khi viết các dòng code thì sẽ viết từ trên viết xuống, lệnh nào làm trước thì viết trước và cứ thế hoàn thành đoạn script. Ta gọi, đó là Lập trình tuyến tính (linear programming).

#Và khi nhiều vấn đề phát sinh từ linear programming như việc sửa đổi, cập nhật, rất khó khăn và nhiều nguyên nhân khác đã đưa ra một thời kì lập trình mới, đó chính là Lập trình thủ tục (procedural programming)

#Để có thể có một chương trình theo hướng procedural programming, thì ta phải biết khái niệm hàm và cụ thể trong bài này,sẽ giới thiệu với các bạn về nó.

#  cấu trúc
# def <function_name>(parameter_1, parameter_2, .., parameter_n):
    # function-block

def Tong(a, b):
    return float(a + b)
print(Tong(8989,98.898))

# có thể thêm defaul param ở cuối

#Positional argument và keyword argument
def kteam(a, b):
    pass # lệnh giữ chỗ.
# ?Thì ta có thể pass argument vào cho hàm như sau
# Trong ví dụ trên, hai giá trị là số 3 và chuỗi ‘Free Education’ gọi là positional argument.

# Còn với trường hợp dưới đây
kteam(3,'Free Education')
kteam(a=3, b='Free Education')
kteam( b='Free Education',a=3)
# cả 3 đều giống nhau


# keyword argument.
def Teo(a, b=2, c=3, d=4):
    f = (a + d) * (b + c)
    print(f)
Teo(1) #25
# Tèo gọi hàm thì thấy kết quả theo đúng ý mình. Giờ Tèo muốn đổi giá trị của parameter d thành 5. Nên Tèo phải truyền lại các giá trị 2 và 3 cho các parameter b và c.
Teo(1, 2, 3, 5) #30

# Vậy, ta có cách nào không phải truyền lại hai giá trị cho parameter b và c không?
Teo(1, d=5)
# /Python cho phép chúng ta tạo ra các parameter chỉ nhận giá  trị bằng việc pass argument theo kiểu keyword argument.
# Cú pháp
    # def function (*, key_arg1, key_arg2):
    # function-block.

#ví dụ 
def kteam2(pos_or_key_arg, *, key_arg1, key_arg2):
    print(pos_or_key_arg)
    print(key_arg1)
    print(key_arg2)
kteam2(1, key_arg1=2, key_arg2='Kteam')
#lỗi #kteam2(1, 2, key_arg2='Kteam')
# cũng lỗi kteam(1, 2, 'Kteam')



#Positional argument
#input(prompt=None, /)
