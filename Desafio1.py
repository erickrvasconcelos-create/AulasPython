
from datetime import date

ano_atual = date.today().year

nome = input("Insira Seu nome:")

while True: 
    try:
        data = int(input("Insira Seu ano de nascimento:"))

        if not (1900 <= data  <= ano_atual):
           print ("Ano Invalido, tente novamente")
        else:
             break
    except ValueError:
            print("Ano Invalido, digite novametne")
 
idade =  ano_atual - data


idade_cem = 100 - idade

dias_vividos = idade * 365

horas_vividas = dias_vividos *  24

print(f"{nome}, em {ano_atual} vc possui {idade} anos.")
print(f"você viveu aproximadamente {dias_vividos} dias, aproximadamente {horas_vividas} horas e faltam aproximadamente {idade_cem} para você completar 100 anos!")
