dias = int(input("dias: "))
horas = int(input("horas: "))
minutos = int(input("minutos: "))
segundos = int(input("segundos: "))
resultado = (dias * 86400 + horas + 60 + minutos * 60)
print(segundos + resultado)