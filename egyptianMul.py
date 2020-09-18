'''
Created on Aug 10, 2020

@author: rabel
'''
class EgyptianMu:
    ##get the multiplication of  two number using the Egyptian/ Russian peasant method
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
        ## we use a hashtable containing powers of 2 as keys and the second value 
        ## as a sum of itself
        self.htable = {}
        ## the array below stores all the keys needed to sum the first value as a sum of 
        ##powers of 2
        self.b_conv = []
        
    def createHash(self):
        ##converts the first number into a string containing the  binary number/ then we reverse the string
        b = bin(self.num1)[::-1]
        ## takes out the last characters of the reverse string which are not needed
        bc = b[:len(b)-2]
        
        ## this loop populates the hash table
        pw = 1
        while pw < self.num1:
            self.htable[pw] = self.num2 
            pw *= 2
            ##pw are the powers of 2
            self.num2 += self.num2    
        
        ##we populate our array containing all keys from the binary character
        ## these keys are needed to get the values for the sum
        ps = 1
        for char in bc:
            if char == '1':
                self.b_conv.append(ps)
            ps *=2            
    
    def getMul(self):
        ##gets the values needed from the hash tables and adds them
        sum = 0
        for key in self.b_conv:
            sum += self.htable.get(key)
        return sum
                   
if __name__ == "__main__":
    
    e = EgyptianMu(67,89)
    e.createHash()
    print(e.getMul())
