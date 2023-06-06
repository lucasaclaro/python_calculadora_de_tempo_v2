# 1 minuto -> 60 segundos
# 1 hora -> 3.600 segundos
# 1 dia -> 86.400 segundos
# 1 semana -> 604.800 segundos


tempo = int(input('Qual é o total de segundos?:  '))

print('----' * 20)
print(f'Analisando o valor digitado, {tempo} segundos correspondem a um total de: ')
print('----' * 20)

semana = tempo // 604800
saldo_semana = tempo % 604800
print(f'Semana(s): {semana}.')
dia = saldo_semana // 86400
saldo_dia = saldo_semana % 86400
print(f'Dia(s): {dia}.')
hora = saldo_dia // 3600
saldo_hora = saldo_dia % 3600
print(f'Hora(s): {hora}.')
minuto = saldo_hora // 60
segundo = saldo_hora % 60
print(f'Minuto(s): {minuto}.')
print(f'Segundo(s): {segundo}.')

print('----' * 20)
print('\nEncerrando o programa...')