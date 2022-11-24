#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Write a Program to print the largest and smallest number of the list
list1 = [10,20,30,40,34,67,89,65,467]

list1.sort()

print("Smallest number in the list is :", min(list1))
print(" Minimum element in the list is :", max(list1))


# In[29]:


# Write a Program to delete alternative number in a list

list1 = [10, 20, 10, 30, 10, 40, 10, 50]

n = 10


print ("Original list:")
print (list1)


i=0 #loop counter
length = len(list1)  #list length 
while(i<length):
    if(list1[i]==n):
        list1.remove (list1[i])
       
        length = length -1  
         
        continue
    i = i+1

# print list after removing given element
print ("list after removing elements:")
print (list1)


# In[18]:


# Write a Program to delete odd numbers in a list and print the even numbers
lst = [11, 22, 44, 33, 88]
print("origional list before Removal of odd Numbers:", lst)

for i in lst:
    if(i%2 !=0 ):
        lst.remove(i)

print("The left Event Numbers are :", lst)


# In[ ]:




