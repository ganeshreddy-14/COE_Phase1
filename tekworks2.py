#!/usr/bin/env python
# coding: utf-8

# In[9]:


a=35.5
c=3
d="Ganesh"
e=float(c)
f=str(a)

print(type(a))
print(type(c))
print(type(e))
print(type(f))




# In[14]:


amount=int(input("Enter your amount")) #amount 800
if amount%100==0:
    if amount>=500:
        five=amount//500
        print("Number of 500 notes are :",five)
        amount=amount-500*five
    if amount>=200:
        two=amount//200
        print("Number of 200 notes are :",two)
        amount=amount-200*two
    if amount>=100:
        one=amount//100
        print("Number of 100 notes are :",one)
        amount=amount-100*one
else :
    print("Please enter multiples of 100 only")
        


# In[22]:


basic=int(input("Enter basic salary :"))
if basic<=20000:
    gross=basic+(76/100)*basic+(78/100)*basic
    print("Your Gross salary is:",gross)
if basic>20000 and basic<=30000:
    gross=basic+(79/100)*basic+(82/100)*basic
    print("Your Gross salary is:",gross)
if basic>30000:
    gross=basic+(85/100)*basic+(89/100)*basic
    print("Your Gross salary is:",groos)



# In[39]:


salary = int(input("Enter your salary: "))

if salary <= 500000:
    print("No TDS")
elif salary <= 1000000:
    rem = salary -500000
    if rem <= 200000:
        tds = (5/100)*rem
        print("Your TDS is:", tds)
    else:
        tds =(5/100)* 200000
        rem = salary- 700000
        if rem <= 300000:
            tds = tds+(10/100) * rem
            print("Your TDS is:", tds)
        else:
            tds= tds+(10/100)*300000
            rem =tds- 300000
            tds =tds+ rem *(15/100)
            print("Your TDS is:", tds)
elif salary <= 1500000:
    rem = salary - 1000000
    tds = (5/100) * 200000 + (10/100) * 300000 
    if rem <= 500000:
        tds =tds+ (15/100) * rem
        print("Your TDS is:", tds)
    else:
        tds =tds+ (15/100) * 500000
        rem =tds- 500000
        tds = tds+rem * (20/100)
        print("Your TDS is:", tds)
elif salary <= 2000000:
    rem = salary - 1500000
    tds = (5/100)*200000 + (10/100) * 300000 + (15/100) * 500000
    if rem <= 500000:
        tds =tds+ (20/100) * rem
        print("Your TDS is:", tds)
    else:
        tds =tds+ (20/100) * 500000
        rem = tds-500000
        tds = tds+rem * (30/100)
        print("Your TDS is:", tds)
else:
    rem = salary - 2000000
    tds = (5/100) * 200000 + (10/100)*300000 +(15/100) * 500000 + (20/100) * 500000
    tds = tds+rem * (30/100)
    print("Your TDS is:", tds)
        
    





    
    
    


# In[ ]:





# In[ ]:




