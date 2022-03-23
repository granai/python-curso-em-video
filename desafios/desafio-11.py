km = float(input('Quantos quilômetros voce percorreu?'))
dias = float(input('Quantos dias voce ficou com o carro?'))
print(f'Pelo total de {dias:.0f} dias, o valor a ser pago é R${60*dias:.2f} ')
print(f'Pelo total de {km} quilômetros percorridos, o valor a ser pago é R${0.15*km:.2f}')
total = dias * 60 + km * 0.15
print(f'O valor final a ser pago é {total}')

