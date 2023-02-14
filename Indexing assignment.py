#!/usr/bin/env python
# coding: utf-8

# In[1]:


element= 'helium'
print(element[0])


# In[2]:


element= 'helium'
print(element[2])


# In[3]:


element= 'helium'
print(element[-1])


# In[4]:


s= 'helium'
print(s[2:5])


# In[6]:


s= 'helium'
print(s[-4:-1])


# The other options don't work because they either go too far a character or don't go far enough in their three character ranges

# In[7]:


s = "supercalifragilisticexpialidocious"
print([s[16], s[18], s[20]][1])


# In[9]:


s = "supercalifragilisticexpialidocious"
print(s[14:17][-2])


# Options 1,2,3,5,6 and 7 all will give a result of "i".

# In[11]:


print(s[::2])


# In[12]:


print(s[1::2])


# It will print the first 5 characters of the word

# In[14]:


s = "supercalifragilisticexpialidocious"
print(s[5:0])


# In[ ]:


It will print the fifth through tenth characters of the word


# In[15]:


s = "supercalifragilisticexpialidocious"
print(s[5:10])


# It will print "lidoc" from the end

# In[16]:


s = "supercalifragilisticexpialidocious"
print(s[-10:-5])


# It will print dilai

# In[17]:


s = "supercalifragilisticexpialidocious"
print(s[-5:-10])


# In[19]:


fruits=[apple, banana, cantaloupe, durian]
print(fruits,[2])


# In[ ]:




