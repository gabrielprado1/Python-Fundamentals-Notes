# Módulo datetime - lidar com datas e horas; classes úteis sendo date, time e timedelta
from datetime import date, datetime, time

date(2025, 2, 23)
####
print(date.today())

###
data_hora = datetime(2025, 2, 25, 10, 3, 10)
print(data_hora)

####
print(datetime.today())

# Manipulação de datas com timedelta
from datetime import timedelta

tipo_carro = "P" # P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now() # .utcnow()

if tipo_carro == "G":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f"O carro chegou: {data_atual} e ficará pronto às {data_estimada}")

# Poderia trocar o minutes por days, seconds, e várias outras opções

print(date.today() - timedelta(days=1))

# Quando for trabalhar com o obj timedelta, precisa ter a date junto, senão não funcionará
resultado = datetime(2024, 7, 25, 10, 19, 20) - timedelta(hours=1)
print(resultado.time())

###
print(datetime.now().date())

# Conversão e formatação de data e hora - métodos:
# strftime (string format time) - formatando data e hora
d = datetime.datetime.now()
print(d.strftime("%d/%m/%Y %H:%M"))

# strptime (string parse time) - convertendo string para datetime
date_string = "20/07/2023 15:30"
d = datetime.datetime.strptime(date_string, "%d/%m/%Y %H:%M")

# pytz - biblioteca de terceiros para trabalhar com os fusos horários diversos

# Trabalhando com timezone sem bibliotecas externas