class valuta:
    def __init__(self,amount,name = ''):
        self.amount = amount
        self.name = name
    
    @staticmethod
    def convert(amount,name1,name2):
        koeff_euro_rub = 81.34 
        koeff_doll_rub = 71.52
        koeff_chf_rub = 71.62
        koeff_try_rub = 11.09
        if name1 == 'RUB':
            conv_amount = amount
        elif name1 == 'USD':
            conv_amount = amount*koeff_doll_rub
        elif name1 == 'EUR':
            conv_amount = amount*koeff_euro_rub
        elif name1 == 'CHF':
            conv_amount = amount*koeff_chf_rub
        elif name1 == 'TRY':
            conv_amount = amount*koeff_try_rub
            
        if name2 == 'RUB':
            res = conv_amount
        elif name2 == 'USD':
            res = conv_amount/koeff_doll_rub
        elif name2 == 'EUR':
            res = conv_amount/koeff_euro_rub  
        elif name2 == 'CHF':
            res = conv_amount/koeff_chf_rub
        elif name2 == 'TRY':
            res = conv_amount/koeff_try_rub
        
        return res
    
    def __add__(self,other):
        if type(self) == type(other):
            if self.name == '':
                return valuta(round(self.amount + other.amount,2), other.name)
            elif other.name == '':
                return valuta(round(self.amount + other.amount,2), self.name)
            return valuta(round(self.amount + self.convert(other.amount,other.name,self.name),2),self.name)
        else:
            return valuta(round(self.amount + other,2),self.name)
    
    
    def __str__(self):
        return f"amount {round(self.amount,2)}, quality {self.name}"
    
    def __repr__(self):
        return f"amount {round(self.amount,2)}, quality {self.name}"    
        
    
