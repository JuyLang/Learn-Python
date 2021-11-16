#interation là một khái niệm chung lấy một phần từr
# ví dụ: như ăn một snaack, lấy từng miếng trong túi ra ăn tới hết thì thôi
# COi như là 1 vòng lặp: ta dùng kĩ thuật nào đó lấy bánh to, đo chính là interation

#interable object là một object có hai phương thúc iter và intertor 
#đơn giản là đối tượng nhưng ta không thể lấy bất kì giá trị nào như ta làm với list và chuỗi

from typing import NewType


intera = [ x for x in range(5)] # đây là tupple
interator = ( x for x in range(3)) # đây mới là một iterator
print(intera)
print(interator) # đây chính là interable object
# nhưng ta không thể truy xuất 
# ta cần làm như sau
print(next(interator))
print(next(interator))
print(next(interator))
