class atm:
    def read_data(self,account_no,name):
        self.account_no=int(input("enter the accont number"))
        name=input("enter the name")

obj=atm
obj.read_data(76,"hari")
obj.display()
