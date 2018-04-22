
# coding: utf-8

# In[1]:


def myreduce(list1):
    x = 1
    for i in list1:
        x = x * i
    return x
list1 = [1,2,3,4]
print(myreduce(list1))

