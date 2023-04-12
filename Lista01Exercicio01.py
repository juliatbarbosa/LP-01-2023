""" A velocidade média de um veículo é dado pela expressão Vm= ∆S/∆t, onde: 
∆S: variação de espaço (ponto de chegada - ponto de partida) em quilômetros
∆t: variação de tempo (tempo final - tempo inicial) em horas
Escreva um programa para calcular a velocidade média dada a variação espacial e a variação temporal.  
 """
deltaS = float(input('Digite quantos quilometros você andou: '))
deltaT = float(input('Digite quanto tempo você gastou em horas: '))

Vm = deltaS / deltaT

print(f'Sua velocidade média foi de {Vm:.0f}km/h.')