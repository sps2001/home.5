#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.length  of a string
str=input("Enter a string ")
print("length os the input string is",len(str))


# In[ ]:





# In[ ]:





# In[ ]:


#2.character frequency
def char_freq(str1):
    dict={ }
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_freq('google.com'))
            


# In[ ]:


# 3.get a single string from two two string
def char_mix_up(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a+' '+new_b
print(char_mix_up('abc','xyz'))


# In[ ]:


#4,upper case and lower case
a=input("Python is a user Interface landuage ")
print("Python is a user Interface language",a.upper())
print("Python is a user Interface language",a.lower())


# In[ ]:


#5.remove new line in python
str1='python exercise\n'
print(str1)
print(str1.rstrip())


# In[ ]:


#6.to count accurrence of a substring
str1='corna is came from chaina'
print()
print(str1.count("from"))
print()


# In[ ]:


#7.string into a list
str1='apple,mango,stwarberry'
print(f'list of items={str1.split(",")}')


# In[ ]:


#8.delete a character
a=[2,3,4,5,6]
del a[1:2]
print(a)


# In[ ]:


#9.print string using loop
x=input("enter the string")
for i in x:
    print(i)


# In[ ]:


#10.finding length without using len()
a="python"
count=0
for i in a:
    count=count+1
print(count)


# In[ ]:




