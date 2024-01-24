burger = 115.0
Sandwich = 75.0
Strips= 20.0

def combo(a,b) : 
    price = ( a-b) * 0.9 
    return price 

def gift_pack (a,b,c): 
    price =(a-b-c) *0.75
    return price 

print  ("Online Order") 
print("-----------------------------------------------------------------------------------")
print("Product(s)                                                  price") 
print(f"burger1                                                     {burger}")
print(f"Sandwich2                                                   {Sandwich}")
print(f"Strips3                                                     {Strips}") 
print(f"Combo1 (burger + Sandwich))                                 {combo(burger,Sandwich)}") 
print(f"Combo2 (Sandwich + Strips))                                 {combo(Sandwich,Strips)}")
print(f"Combo3 (Burger+Strips)                                      {combo(burger,Strips)}")
print(f"Combo4 (Burger+Sandwich+Strips)                             {gift_pack(burger,Sandwich,Strips)}")
print('-------------------------------------------------------------------------------------\nFor delivery Conact: 0590633022')
