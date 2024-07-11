# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:23:03 2024

@author: gbulb
"""

class possible_pairing:
        def obtaining_values(): #make a list of signed values which are up to 2.
            list_of_values=[]
            for i in range(1,3):
                list_of_values.append(-1*i)
                list_of_values.append(+1*i)
            return list_of_values
        def pairing(list_of_values): #obtain possible pairs 
          i=0
          for ele1 in list_of_values:
              for ele2 in list_of_values:
                  if ele1!=ele2 and ele1!=-(ele2):
                     i+=1
                     print(ele1,ele2)
          print(f'{i} is the number of the possible pairs which are allowed!')      
if __name__=="__main__":
    list_of_values=possible_pairing.obtaining_values()
    possible_pairing.pairing(list_of_values)