#Functional tools
#Chúng ta thường hay phải xử lí các phần tử của một list hoặc một container nào đó bằng một phương thức.
kteam = [1, 2, 3, 4]
# map(func, iterable)
def mymap(func, iterable):
    for x in iterable:
        yield func(x)

def inc(x): return x + 1
print(list(map(inc,kteam)))
#hoặc
incl = lambda x: x+1
print([inc(x) for x in kteam ])

#Hàm filter. Filter có nghĩa là bộ phận lọc
#Hàm reduce
#đệ quy
# Đệ quy là một mảng kiến thức nâng cao, ở Python thì nó không thường xuyên được dùng đến, do cách xử lí của Python có thể sử dụng những cấu  trúc vòng lặp đơn giản mà không cần dùng tới đệ quy. Nhưng dù sao thì đây cũng là  một kĩ thuật khá hữu dụng mà bạn đọc nên biết. Nó cũng chỉ đơn giản là việc chính nó gọi nó
def cal_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + cal_sum(lst[1:])
print(cal_sum([1,2,3,4,5,6]))