#method dict
#có hỗ trợ một số phương thức, như các dữ liệu tr
 
#copy 
dict1 = {
    'name':'duy',
    'age': 86
}
print(dict1)
dict2 = dict1.copy()
print(dict2) #vùng nhớ mới
#get theo key
dict3 = dict1.get('name') #lấy ra value của key name
print(dict3)
#atend
dict4 = dict1.items() #trả ra tuple với đầu tiên là key và value

print(dict4)
dict5 = list(dict4)#chuyển thành list để lấy
print(list(dict5[0])) 

#value để lấy ra value
#pop lấy ra và xóa
#update thêm value mới cập nhật cho value cũ


