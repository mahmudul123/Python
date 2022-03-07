# -----------------------------------------------------------
# Survey for non-citizens
# (C) 2020 Mahmudul Alam
# Released under Colorado State University-Global Campus
# email mahmudul.alam@csuglobal.edu
# -----------------------------------------------------------
"""""""""""""""""
@des father class to define attributes for user personal information
"""""""""""""""""
class Father:

    def __init__(self, name, eye, height):
        self.Name=name
        self.Eye=eye
        self.Height=height

    # Get methods
    def get_Name(self):
        return self.Name
    def get_Eye(self):
        return self.Eye
    def get_Height(self):
        return self.Height

    # Set methods
    def set_Price(self, value):
        self.Name=value
    def set_Name(self, value):
        self.Eye=value
    def set_Description(self, value):
        self.Height=value

"""""""""""""""""
@des son(father) inherited father class
@adds attributes and methods to extend father class
"""""""""""""""""
class Son(Father):
    def __init__(self, social, country, name, eye, height):
        super().__init__(name, eye, height)
        self.Social=social
        self.Country=country

    # Get methods
    def get_Social(self):
        return self.Social
    def get_Country(self):
        return self.Country

    # Set methods
    def set_Social(self, value):
        self.Social=value
    def set_Country(self, value):
        self.Country=value


    def __str__(self):
        return "Name: "+self.get_Name()+" Eye color: "+self.get_Eye()+" Height: "+self.get_Height()+\
               " Thread Count: "+self.get_Social()+" Made: "+self.get_Country()

def main():
        list=[]
        while True:
            choice=input("Do you want to continue Y/N?  ")
            choice1 =input("Are you a US citizen Y/N?  ")
            if choice=='N' or choice1=='Y':
                break
            name=input("What is your name ? ")
            eye=input("Color of your eye ? ")
            height=input("Your height ? ")
            social = input("What is your social security number? ")
            country = input("What is your country of or origin ? ")
            entry = Son(social, country, name, eye, height)
            list.append(entry)
        for gar in list:
            print(gar)
main()
# ----------------------END-----------------------#
