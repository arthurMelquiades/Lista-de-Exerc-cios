duracaoemsegundos = int(input("diga a duração em segundos do evento na fábrica: "))
horas = duracaoemsegundos // 3600
minutos = (duracaoemsegundos % 3600) // 60
segundos = duracaoemsegundos % 60
print(horas, ":", minutos, ":", segundos )