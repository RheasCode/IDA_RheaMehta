#!/usr/bin/env python
# coding: utf-8

# In[11]:


def calc_Gasvalue(p, gasconst, temp):
    """"
    19.09.2023: Rhea Mehta - Created function to calculate the volume of gas using the Ideal Gas law.
    Arguments:
        pressure(float): pressure in Pascals (Pa)
        temp(float): temp in Kelvin (K)
        gasconst(float): universal gas constant 
    Return:
        float: volume in cubic meters (m^3)
    """"
    return (p*1.0)/(gasconst*temp);


# In[12]:


gas_vol = calc_Gasvalue(10000, 300.0, 8.314);
print("Gas Volume: ",(gas_vol), "m^3");


# In[13]:


def calc_Gasmass(pressure, temp, gasconst, molarmass):
    """"
    19.09.23: Rhea Mehta - Created function to calculate mass of the gas. 
    Calculate the mass of the gas using the ideal gas law and molar mass.
    Args: 
        pressure(float): Pressure in Pascals (Pa)
        temp(float): Temperature in Kelvin (K)
        gasconst(float): Gas const for specific gas
        molarmass: molar mass of gas in g/mol
    returns:
        float: mass in grams (g)
    """"
    volume = calc_Gasvalue(pressure, gasconst, temp);
    return volume*molarmass;


# In[14]:


def factorial(n):
    if n == 0: #base condition
        return 1
    else:
        return n*factorial(n-1) #recursive call


# In[16]:


factorial(0)


# In[23]:


def calc_Totaldepth(segments):
    if not segments:
        return 0
    else:
        curr_Segdepth = segments[0]
        rem_Seg = segments[1:]
        return curr_Segdepth + calc_Totaldepth(rem_Seg)


# In[24]:


calc_Totaldepth ([1,2,3])


# In[25]:


def generate_squares(n):
    for i in range(1,n+1):
        yield i**2


# In[26]:


for i in generate_squares(5):
    print(i)


# In[32]:


def oil_production_m(yearly_value):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    monthly_oil_prod = yearly_value/12;

    for month in months:
        yield month, monthly_oil_prod;


# In[34]:


for month, production in oil_production_m(12000):
    print(f"{month}:{production}")


# In[38]:


def my_dec(fun):
    def wrapper():
        print("I am starting")
        fun()
        print("I am completed")
    return wrapper
@my_dec
def ida_hello():
    print("hello")


# In[39]:


ida_hello()


# In[46]:


import logging

def my_dec01(fun):
    def wrapper(*args, **kwargs):
        logging.warning(f"Calling the function: {fun.__name__}")
        result = fun(*args, **kwargs)
        logging.warning(f"{fun.__name__} Completed")
        return result
    return wrapper

@my_dec01
def calc_Totaldepth(segments):
    if not segments:
        return 0
    else:
        curr_Segdepth = segments[0]
        rem_Seg = segments[1:]
        return curr_Segdepth + calc_Totaldepth(rem_Seg)
    


# In[47]:


calc_Totaldepth([1,2,3])


# In[48]:


def calculate_Energycontent (composition):
    
    lhv = 0
    for gas, percentage in composition.items():
        #LHV values for common gases (in J/kg)
        lhv_values = {
            "methane": 50000,
            "ethane": 48000,
            "propane": 46000,
            "butane": 45000,
        }
        if gas in lhv_values:
            lhv += lhv_values[gas] * (percentage/100)
    return lhv


# In[50]:


gas_composition = {"methane": 80, "ethane": 10, "propane": 5, "butane": 5}


# In[ ]:




