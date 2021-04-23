#!/usr/bin/env python
# coding: utf-8

# In[67]:


class PricingRules:
    # class for price rule settings
    
    def __init__(self):
        #initial SKU unit price
        self.IPD = 549.99
        self.IPD_BULK = 499.99
        self.MBP = 1399.99
        self.ATV = 109.5
        self.VGA = 30

    # opening day special 1: have a 3 for 2 deal on Apple TVs,buy 2 get 1 free, return discount amount
    def _special_1(self):
        return self.count_atv // 3 * self.ATV
    
    # opening day special 2: the price of super ipad have a discount that the price will drop to $499.99 each,return discount amount
    def _special_2(self):
        if self.count_ipd >4:
            return self.count_ipd*(self.IPD-self.IPD_BULK)
        else:
            return 0
        
    # opening day special 3: get VGA free of charge with every Macbook pro,return discount amount
    def _special_3(self):
        if self.count_mbp>=self.count_vga:
            return self.count_vga*self.VGA
        else:
            return self.count_mbp*self.VGA
        

class Checkout(PricingRules):
    
    def __init__(self):
        super().__init__()
        self.count_ipd = 0
        self.count_mbp = 0
        self.count_atv = 0
        self.count_vga = 0
        self.sku_list = []
        
    def scan(self,item):
        isValid = True
        
        if (item=='ipd'):
            self.count_ipd +=1
        elif (item=='mbp'):
            self.count_mbp +=1
        elif (item=='atv'):
            self.count_atv +=1
        elif (item=='vga'):
            self.count_vga +=1
        else:
            isValid = False
            print("invalid SKU: %s"%item)
            
        if isValid:
            self.sku_list.append(item)
    
    def get_subtotal(self):
        return self.count_ipd*self.IPD + self.count_mbp*self.MBP + self.count_atv*self.ATV + self.count_vga*self.VGA
    
    def total(self):
        sub_total= self.get_subtotal()
        discount_total = self._special_1() + self._special_2()  + self._special_3()
        total = sub_total - discount_total
        
        print('SKU Scanned: %s \nTotal expected: $%.2f'% (', '.join(self.sku_list),total))    


# In[72]:


#testing case 1
co= Checkout()
co.scan('atv')
co.scan('atv')
co.scan('atv')
co.scan('vga')
co.total()


# In[73]:


#testing case 2
co= Checkout()
co.scan('atv')
co.scan('ipd')
co.scan('ipd')
co.scan('atv')
co.scan('ipd')
co.scan('ipd')
co.scan('ipd')
co.total()


# In[74]:


#testing case 3
co= Checkout()
co.scan('mbp')
co.scan('vga')
co.scan('ipd')
co.total()


# In[75]:


#test case 4 invalid item
co= Checkout()
co.scan('mbp')
co.scan('vga')
co.scan('ipd')
co.scan('ipod')
co.scan('vga')
co.scan('ipd')

co.total()


# In[ ]:




