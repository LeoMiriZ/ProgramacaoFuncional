estudante = [{'ra': 123, 'curso': 'ADS', 'nota': 8.5},
             {'ra': 456, 'curso': 'SI', 'nota': 5.0},
             {'ra': 789, 'curso': 'BD', 'nota': 7.5}]

notas_menores = filter(lambda x: x['nota'] < 7.0, estudante)
print(list(notas_menores))