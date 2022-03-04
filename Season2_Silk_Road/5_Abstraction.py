# Abstract class là một class mà bên trong nó chứa một hoặc nhiều phương thức trừu tượng. Phương thức trừu tượng ở đây là một phương thức mà chúng ta chỉ được phép khai báo nó và không được phép viết code thực thi nó. Khi một class được khai báo ở dạng abstract thì nó sẽ không thể nào khởi tạo được, mà chỉ có thể khởi tạo được thông qua các class con của nó. Một class kế thừa lại abstract class thì phải khai báo lại toàn bộ các
#  phương thức trừu tượng bên trong abstract class mà nó kế thừa.

#Để có thể khai báo được một abstract class trong Python, 
# thì class này bắt buộc phải được kế thừa từ một ABC (Abstract Base Classes) của Python
from abc import ABC
class PersonAbstact(ABC):
    name = None
    age = 0
    def getName(self):
        print(self.name)
    def getAge(self):
        print(self.age)

#, Khai báo phương thức abstract trong Python.
# Để có thể khai báo một abstract method - phương thức trừu tượng  trong Python thì chúng ta cần phải import thêm module abstractmethod ở trong package abc.
from abc import ABC, abstractmethod

#cú pháp
from abc import ABC, abstractmethod

class ClassName(ABC):
    # khai bao phuong thuc truu tuong
    @abstractmethod
    def methodName(self):
        pass
