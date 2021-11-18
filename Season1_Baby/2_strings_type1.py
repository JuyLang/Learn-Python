'''
    xin chào đây là docstrings test
    muốn ghi gì cũng được, giống comment 
'''

# chuỗi thực chất là một mảng kiểu char thôi
# chuỗi là những thứ được đặt trong cặp dấu ‘ ’, hoặc “ ”
# có thể cũng là trong cặp  ‘’’ ‘’’, “”” “””. Nhưng cơ bản và thường đường sử dụng nhất là cặp ‘ ‘ và “ “.


print("Lăng Khương Duy")

#SOLID : Chuẩn
str = "Lăng Khương Duy"
print(str)
print(type(str))
#Một số khù khằm
# str1 = 'I'm Beginner' # sẽ không được 
# ta viết kiểu này
str1 = "I'm Beginner"
# cách sử dụng chuỗi nhiều dòng
str3 = ''' 
helo
hello2
heloo3
hess4
haiii
'''
print(str3) 
#bản chất chính là
str4 = """ Hello1\nHello2\nHello3"""
print(str4)

#hai cặp dãy này không để tạo ra chuỗi nhiều dòng, mà dùng để làm note strings ( một dạng chú thích nhiều dòng)
#Ví dụ: quay lên đầu

#Escape Sequence
# \a phát ra tiếng bip
# \b đưa con trỏ về một khoảng trắng
# \n đưa con trỏ xuống dướ
# \t một tab 
# \' in ra kí tự '
# \" in ra kí tự "
# \\ in ra kí tự \
print("\a")