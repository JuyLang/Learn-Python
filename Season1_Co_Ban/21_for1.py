# for <biến> in range():

#range() : có thể là bắt đầu từ đâu, đến bao nhiêu, bước nhảy

# for x in range(0,21,4): #ví dụ in từ 1 - 21 
#     print(x)

#for variable_1, variable_2, .. variable_n in sequence:
#Sequence ở đây là một iterable object (có thể là iterator hoặc là một dạng object cho phép sử dụng indexing hoặc thậm chí không phải hai kiểu trên).

    # Ví dụ in trong intertor (danh sách)
# inter = (x for x in range(5))
# c = 0
# while( c < 5):
#     print(next(inter))
#     c = c+1

#for obj
howteam = {
    "name":"duy",
    "age": 87
}
for key, value in howteam.items():
    print(key, value)

s ="Lăng Khương Duy"
for ch in s:
    if ch == " ":
        continue
    else:
        print(ch)