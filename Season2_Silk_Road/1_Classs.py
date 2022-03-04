class People:
    #2, properties Class.
    name = "Lăng Khương Duy";
    age = 22;
    male = True
    #3. method Class.
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
#Initialization Class
duy = People()
print(duy.name)
duy.setName('Lươn Khương Duy')
print(duy.getName())

