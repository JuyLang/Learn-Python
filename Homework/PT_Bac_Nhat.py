print('Nhập vào ax + b')
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
if(a == 0):
    print("Phương trình vô số nghiệm")
else:
    if(b == 0 ):
        print('Phương trình có nghiệm = 0')
    else:
        print('Phương trình có nghiệm x = -b/a = ', -b/a)