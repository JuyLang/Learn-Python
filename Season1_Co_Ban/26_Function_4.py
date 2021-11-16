#lambda
# Ngoài từ khóa “def”, Python cũng hỗ trợ cho bạn một cách khác để có  thể khai báo một function object, đó chính là lambda. Nó chỉ khác từ  khóa “def” ở chỗ, thay vì def tạo một hàm với một cái tên xác định thì lambda trả về một hàm. Thế nên người ta hay gọi lambda là hàm nặc danh (anonymous). Nó thường được sử dụng thường xuyên để có thể tạo ra một hàm chỉ với  một dòng lệnh.
#lambda argument_1, argument_2, …, argument_n : expression.

ave = lambda a, b, c: (a + b+ c)/3

print(ave(7,8,8))
#Chung quy thì lambda là một công cụ nhanh gọn để bạn có  thể tạo ra một hàm và sử dụng nó.

#Câu điều kiện cho lambda
#b if a else c hoặc (a and b) or c
find_greater = lambda x, y: x if x > y else y
print(find_greater(1, 3))
print(find_greater(6, 2))
cd_of_2_3 = lambda x: (1 if x % 3 == 0 else 0) if x % 2 == 0 else 0
print(cd_of_2_3(6))
#Lambda chồng lambda