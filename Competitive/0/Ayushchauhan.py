import math 
  

def egyptianFraction(nu, den): 
  
    print("The Egyptian Fraction " +
          "Representation of {0}/{1} is".format(nu, den), end="\n") 
  
    
    ef = [] #stores denominator
  
    # while loop runs until  
    # fraction becomes 0 i.e, 
    # numerator becomes 0 
    while nu != 0: 
  
        # taking ceiling 
        x = math.ceil(den / nu) 
  
        # storing value in ef list 
        ef.append(x) 
  
        # updating new numerator and denominator 
        nu = x * nu - den 
        den = den * x 
  
  
    for i in range(len(ef)): 
        if i != len(ef) - 1: 
            print(" 1/{0} +" .  
                    format(ef[i]), end = " ") 
        else: 
            print(" 1/{0}" . 
                    format(ef[i]), end = " ") 
  
egyptianFraction(2,3) 
  
