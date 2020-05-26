class Book:
    def __init__(self,tt,aut,pub,pr,cp):  #royalty is not passed by user, it should be calculated
        self.title=tt
        self.author=aut
        self.publisher=pub
        self.price=pr
        self.royality=0  #initialize royality with 0
        self.copy=cp
    def get_title(self):
        return self.title
    def set_title(self,tt):
        self.title=tt
        return
    def get_author(self):
        return self.author
    def set_author(self,aut):
        self.author=aut
        return
    def get_publisher(self):
        return self.publisher
    def set_publisher(self,pub):
        self.publisher=pub
        return
    def get_price(self):
        return self.price
    def set_price(self,pr):
        self.price=pr
        return
    def get_royality(self):
        return self.royality
    def set_royality(self,ro):
        self.royality=ro
        return
    def get_royality(self):  #never give same name to variable and function
        if self.copy<=500:
           self.royality=self.copy*self.price*0.10  #store royalty in a variable
           print("royality is:",self.copy*self.price*0.10)
        elif self.copy>500 and self.copy<1500:
            self.royality=self.copy*self.price*0.125
            print("royality is:",self.copy*self.price*0.125)
        else:
            self.royality=self.copy*self.price*0.15
            print("royality is:",self.copy*self.price*0.15)
        return self.royality   #return calculated royalty

class ebook(Book):
    def __init__(self,tt,aut,pub,pr,cp,fr):
        super().__init__(tt,aut,pub,pr,cp)
        self.format=fr
    def format(self):
        return self.format
    def get_royality(self):
        ryl=super().get_royality()  #fetch royality using parent class
        ryl=ryl-ryl*12/100  #add the extra tip
        self.royality=ryl
        return self.royality  #return the value


#Testing code, you can put your code and values here        
if __name__== "__main__":
    print ('print book example')
    b1=Book('bb','aa','ss',100,600)  #save returned value
    print ("Royalty earned : ", b1.get_royality())
    print ('ebook example')
    e1=ebook("nn",'aa','ss',100, 3, 'PDF')  #save returned value
    print ('Royalty earned' , e1.get_royality())
