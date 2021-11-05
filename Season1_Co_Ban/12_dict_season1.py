#dict ( Dictionary) cũng là 1 container như List, Tuple

# Có Khác biệt là những container như có để dùng index
# để phân biệt, con Dict thì dùng key để phân biệt


# Giống như từ điển Tiếng Anh, Dict hoạt động như vậy

#Các yếu tố
#   được gioi hạn bởi cặp nhọn {}, tất cả những gì nằm trong đó là những phần từ Dict
#   Các phần tử của Dict được phân cách nhau bởi dấu phẩy 
#   Các phần từ của Dict phải là 1 cặp Key-value
#   Cặp Key-value của phần tử Dict được phân bởi dấu 2 chấm :
#   Các key buộc phải là 1 hash objecy

from typing import Dict


did = { 'name': "Duy", 'age' : 89}
print(did)

dic = { key : value for key, value in [('name','duy'), ('mem',69)]}
print(dic)

#4 cách khởi tạo dic

dic1 = dict()
#dict(mapping) mapping object cũng gần giống so với dict object
# một bj cũng là một mapping object tuy nhiên không phải mapping object nào cũng là dict object

    #khởi tạo bằng iterable
iterr = [('name', 'duy'), ('men', 69)]
print(type(iter))

#fromkey, thay value đồng loại

iter1 = ('name', 'number', 69, True)
frkey = dict.fromkeys(iter1, 'day la Value')
print(frkey)
print(frkey['name'])