# def countdown(n): 
#     while n > 0: 
#         yield n 
#         n -= 1
        
# print(list(countdown(3)))

###################################

# it = iter([1, 2, 3]) 
# print(next(it)) 
# print(next(it)) 
# print(next(it)) 
# print(next(it))

###################################

# def capitalize_decorator(func): 
#     def wrapper(): 
#         return func().upper() 
#     return wrapper

# @capitalize_decorator 
# def greet(): 
#     return "hello" 

# print(greet())

####################################

from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = '%d/%m/%Y'
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr)) # Pode ser cortado

data_convertida = print(datetime.strptime(data_hora_str, mascara_en))
print(data_convertida)
print(type(data_convertida))

