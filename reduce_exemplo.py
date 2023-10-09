from functools import reduce

estudante = [{'ra': 123, 'curso': 'ADS', 'nota': 8.5},
             {'ra': 456, 'curso': 'SI', 'nota': 5.0},
             {'ra': 789, 'curso': 'BD', 'nota': 7.5}]

soma_notas = reduce(lambda nota, estudante: nota + estudante['nota'], estudante, 0)
print(soma_notas)