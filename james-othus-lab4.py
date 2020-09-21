#!/usr/bin/env python
# coding: utf-8

# Lab 4
# ---
# Hello All,
# 
# I am Dhrumil Soni, the CP of the course DSCI 510. Welcome to the lab.
# 
# Guidelines for the Lab:
# - You will be given the lab assignment in the start of the lab. You're supposed to complete it by the deadline stated on DEN. Should be usually on Friday Midnight.  
# 
# - You've to complete the assignments individually. If you are having trouble completing the assignment do let me know, I will clear your doubts and guide you but I'll not write code for you and no one else should :) !!!  
# 
# - You have to fill in the code to this notebook and upload it to your repository. And simply, submit the link to the repo. Also, the repository name has to be in the form '(First name)-(Last name)-lab(Lab Number)'. All characters in lowercase. For example, first lab for me would be 'dhrumil-soni-lab1'  
# 
# - You are encouraged to look up resources online like python docs and stackoverflow. But, you are encouraged to look up the topics and not the questions themselves  
# 
# - Your last submission will be counted towards your grade on DEN and do not edit the repository after the deadline  

# Q1.[10 points]
# ---
# Given a password(string), return the score of the password as per the formula below and classify into categories as described below.
# 
# $l = number\ of\ lowercase\ characters$  
# $u = number\ of\ uppercase\ characters$  
# $d = number\ of\ digits(0-9)$  
# $s = number\ of\ special\ characters(any\ character\ not\ in\ l,u,d)$  
# $unique = number\ of\ unique\ characters(characters\ that\ appear\ atleast\ once)$  
# $entropy = log_2(unique^{l+u+d+s})$
# 
# $Formula:$  
# $score = (l*0.2+u*0.4+d*0.3+s*0.5)*entropy$  
# 
# Classification -> Weak: $score<=50$, Medium: $50<score<=100$, Strong: $score>100$  
# 
# **Print the Classification category and return the score calculated from the above formula.**  
# 
# Input: string  
# Output: Return->float, print->string
# 
# Note: Importing math is fine for this question
# 
# Example:  
# 1. 
# ```
# Input  
# password  
# Output  
# Print: Weak password  
# Return: 35.934143002337336  
# ```
# 2. 
# ```
# Input  
# badpassword123!  
# Output  
# Print: Strong password  
# Return: 193.58797503894243  
# ```
# 
# ---
# Grading Rubric: 5 points if either of classification or score is incorrect. 10 points if both are correct. 

# In[39]:


import math
# Use this cell for your solution
def password_strength(password):
    l = [] # define empty lists to be appended to for l, u, d, s
    u = []
    d = []
    s = []
    for i in password : # for all characters in password string
        if i.islower() : # if character is lower case, append to list l
            l.append(i)
        elif i.isupper() : # if character is upper case, append to list u
            u.append(i)
        elif i.isnumeric() : # if character is numeric, append to list d
            d.append(i)
        else : #if character is special, not one of others, append to list s
            s.append(i) 
    
    unique = len(set(l + u + d + s)) #calculate number of unique characters
    entropy = math.log2(unique**(len(l + u + d + s))) #calculate entropy
   
    score = (len(l) * 0.2 + len(u) * 0.4 + len(d) * 0.3 + len(s) * 0.5) * entropy # calculate score using defined equation
    
    if score <= 50 : # categorize password as weak, medium, or strong based on score, print password strength
        print('Weak password')
    elif score >= 100 :
        print('Strong password')
    else :
        print('Medium password')

    return score # return value of score


# In[43]:


password_strength("badpassword123!")
# abspword123!


# Q2.[10 points]
# ---
# Given a list of integers `arr` and a integer `product`, return an array of size 2 of numbers(pair of numbers) from the array `arr`, whose multiplication results into `product`. Return None if no pair exists.(None is not the same as 'None')   
# 
# We will see a faster version of this soon. Try to think, what could we do to implement this function efficiently.
# 
# Input: list(integers), integer  
# Output: return->list(integers)
# 
# ---
# Example 1:
# ```
# Input:  
# arr=[1, 2, 3], product=3  
# Output:  
# [1, 3]  
# ```
# Example 2:
# ```
# Input:  
# arr=[12, 24, 36, 48], product=576  
# Output:  
# [12, 48]
# ```
# ---
# Grading Rubric: Binary

# In[86]:


# Use this cell for your solution
def find_pair(arr, product):
    arr1 = [] # create list to append values of i
    arr2 = [] # create list to append values of val
    for i in arr : # for loop with each value of arr
        arr1.append(i) #add i to list arr1
        for val in arr : #for loop with each val
            arr2.append(val) #add i to list arr2
            if i * val == product and len(arr1) != len(arr2): #check to see if i * val equals product, ensure different list locations
                return([i, val]) #return 2 values that mult to equal product
    else : 
        print('None') # print none if no two values mult to equal product.


# In[87]:


find_pair([12, 24, 36, 48],576)


# Q3.[10 points] 
# ---
# Given two strings you need to return the list of **unique common words** from the two strings. Fill in two functions, one for `common_words` and other for `distinct_words`. You will find it helpful to use the `distinct_words` function in the `common_words` function. Apart from this, you will need to remove special characters from the words and hence, using the filled in function `remove_special_characters` function would be useful.
# 
# Note: 
# - You need to consider 'How' and 'how' as the same i.e., words are not case-sensitive. Hint: (Convert into common format)
# - You are not required to use the distinct_words function. But, it could be useful and clean.  
# 
# Hint: set() function on a list, converts list to a set(a set could have only unique elements)
# 
# Input: string, string  
# Output: return->list/set of strings  
# 
# ---
# Example: 
# 1.  
# ```
# Input:  
# txt1 = 'how are you?', txt2 = 'are you sure?'  
# Output:  
# ['are', 'you']  
# ```
# 2.  
# ```
# Input:  
# txt1 = 'Can you can a can as a canner can can a can?', txt2 = "Its time to think, Can you really can a can?"  
# Output:  
# ['can', 'a', 'you']
# ```
# 
# ---
# Grading Rubric:  
# 5 points if common words are found correctly without considering cases or special characters.  
# 7 points if common words are found correctly without considering one of cases or special characters.  
# 10 points if code works for all cases. 

# In[111]:


import re

def remove_special_characters(word):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', word)


# In[312]:


import math
def distinct_words(text):
    lowtxt = text.lower() # make all lower case
    unique = lowtxt.split() # split string
    
    index = 0
    while index < len(unique) : #go through all indexes, remove special characters
        unique[index] = remove_special_characters(unique[index])
        index = index+1
    
    uniquewords = set(unique) #remove duplicates in list
    return uniquewords #return list


# In[323]:


# Use this cell for your solution
def common_words(txt1, txt2):
    unique1 = list(distinct_words(txt1)) #define unique list for first string
    unique2 = list(distinct_words(txt2)) #define unique list for 2nd string
    common = [] # set initial list
    for i in unique1 :        
        for j in unique2 : 
            if i == j : #compare list elements
                common.append(j) #add matching elements to common list
    return(common) #return common list


# In[324]:


# Do not change this cell 
print('Your output->', common_words('how are you?', 'are you sure?'), 'Actual Output->', ['are', 'you'])
print('Your output->', common_words('Can you can a can as a canner can can a can?', 'Its time to think, Can you really can a can?'), 'Actual Output->', ['can', 'a', 'you'])


# Finished Early? 
# 
# Bonus Question[5 points] 
# ---
# Person A comes to class every nth day and person B comes to class every mth day. After how many days will they meet for first time after the classes have started?  
# 
# Input: integer, integer  
# Output: return->integer  
# 
# Yes, there is a obvious implementation to this. Can you make it **faster**?  
# 
# Example:  
# ```
# Input  
# n=2, m=3  
# Output  
# 6
# ```
# 
# ---
# Grading Rubric: Binary

# In[98]:


from math import gcd
def every_n_m_day(n, m):
    print(n*m // gcd(n,m)) # multiply values and divide by greatest common denominator


# In[99]:


every_n_m_day(2,3)


# In[ ]:




