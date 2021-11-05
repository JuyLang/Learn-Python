print("xin chào Duy Bài này học Biến: chuỗi, số,array ")

# print("ghi chú python")
    # ( dấu thăng là comment, như các ngôn ngữ khác dùng để ghi chú)
#BigData
# Biến là variable, giúp lưu trữ các dữ liệu
# k = 115445 #int
# a = 4848.77 #float
# b = 144545,8 #tuple Số Phức
# c = True # Boolean
# str = "xin chào" #strings
# print(str)
#kiểu tra kiểu dữ liệu dùng type
# print(type(k))
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(str))
#Kiểu Số
d  =  4 #gán cho biến a giá trị 4, với kiểu số nguyên
# nếu muốn lưu số rất lớn với 20 ngin ty @@, nhưng càng khó hiểu cốt lõi
fl = 3.14 #float, có độ chính xác với 12 dấu phẩy
fl12= 1.23456789101112131415
print(fl12)
# nêu muốn chính xác hơn ta sử dụng decimal, ta cần import một decimal
from decimal import*
import fractions
#import decimal #lấy toàn bộ nội dung của thư viện decimal
getcontext().prec = 30 #lấy tối da 30 phần số nguyên và phần thập phân Decimall

print(Decimal(10)/Decimal(3) ) # nếu mà tính thì sẽ là 3.333(3), dùng decimal với lấy 30  chữ số thập phân

#kiểu phân số, để tạo ta sử dụng Fraction
from fractions import*
fr = Fraction(6,9)
print(fr)
print(type(fr))
#Số Phức, gồm phần thực + phần ảo j
comp = complex(778, 88)
print(complex(445,47))
print(comp)

#toán tử
# + cộng, - trừ, * nhân, / chia kết quả là số thực, 
# // thương nguyên( kết quả luôn luôn nhỏ hơn hoặc bằng x /y)
print(15//8)
#  % chia lấy dư, ** lũy thừa

# cách import thư viện: import tên thư viện
# sử dụng hàm trong thư viện : tên thư viện tên hàm
# một số hàm tính toán cơ bản
#   .trunc(x) trả về một số nguyên của số x
#   .floor(x) trả về một số nguyên được làm tròn từ số x, kết quả
#   nhỏ hơn hoặc bằng x
#   .ceil(x) trả về một số nguyên được làm tròn số từ số x, kết quả luôn lớn hơn hoặc bằng x
#   .fabs(x) trả về một số thực là trị tuyệt đối của số x
#   .sqrt(x) trả về một số thực là căn bậc hao của số x
#   .gcd(x,y) trả về số nguyên là ước chung lớn nhất của x và y

import math
print(math.trunc(888.6)) #888
print(math.floor(797998.888)) # 797998
print(math.ceil(778.20)) # 779
print(math.fabs(-89898)) #89898
print(math.sqrt(5)) # căn 5 = 2.2360067869
print(math.gcd(6,9)) #tính ước chung lớn nhất 3
