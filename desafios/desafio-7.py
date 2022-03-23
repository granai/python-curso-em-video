alt = float(input('Altura da parede a ser pintada?: '))
larg = float(input('Largura da parede a ser pintada?: '))
area = larg * alt
print(f'Sua parede tem a dimensao de {larg}x{alt} e sua area é de {area} metros quadrados.')
print(f'A quantidade total de tinta será {area/2:.1f} litros.')


