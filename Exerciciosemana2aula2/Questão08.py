"""Escreva um programa que solicite ao usuário um número e verifique se ele é par ou ímpar. Imprima uma mensagem informando o resultado."""

numero = int(input("Digite o seu numero"))

sobra = numero % 2
par = sobra == 0

print("o numero é par", par)