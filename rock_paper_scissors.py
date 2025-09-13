#!/usr/bin/env python
# coding: utf-8

# In[15]:


import time
import getpass
r="rock"
s="scissors"
p="paper"
n1=input("enter a name : ")
n2=input("enter a name : ")
for i in range(10, 0, -1):
    print(i)
    time.sleep(1)  
print("Time's up! and game starts")
p1=getpass.getpass("Player 1, enter your choice (rock/paper/scissors): ")
p2=getpass.getpass("Player 2, enter your choice (rock/paper/scissors): ")
print("player 1 choose : ", p1)
print("Player 2 choose : ", p2)
if p1==r and p2==s:
    print("p1 wins")
elif p1==p and p2==s:
    print("p2 wins")
elif p1==s and p2==s:
    print("match is tie")
elif p1==s and p2==p:
    print("p1 wins")
elif p1==p and p2==r:
    print("p1 wins")
elif p1==r and p2==p:
    print("p2 wins")
elif p1==p and p2==p:
    print("match is tie")
elif p1==s and p2==r:
    print("p2 wins")
elif p1==r and p2==r:
    print("match is tie")
else:
    print("you are not interested")
print("Game is end!")    


# In[ ]:




