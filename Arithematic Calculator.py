#!/usr/bin/env python
# coding: utf-8

# In[2]:


numeric_1=float(input('Enter First Number: '))
numeric_2=float(input('Enter Second Number: '))
print( 'The user defined numbers are:',numeric_1,numeric_2)

#user choice 
choice=input('Enter which operation to be perfomed: ')

if choice=='+' or choice=='add' or choice=='Add' or choice=='plus' or choice=='addition' or choice=='sum':
    print('The sum of two numbers is: ', numeric_1+numeric_2)
    
elif choice=='-' or choice== 'minus' or choice== 'sub' or choice== 'difference' or choice=='substraction':
    print('The difference of two numbers is :',numeric_1-numeric_2)
    
elif choice =='*' or choice=='product' or choice=='mul' or choice=='into'or choice=='multiplication':
    print('The product of two numbers is : ', numeric_1*numeric_2)
    
elif choice =='/' or choice=='divide' or choice=='division':
    print('The product of two numbers is : ', numeric_1/numeric_2)
    
else:
    print('Invalid input')


# In[ ]:




