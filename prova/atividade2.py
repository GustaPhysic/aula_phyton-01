import subprocess
import os

def menu():
    print("1 - Abrir Bloco de Notas")
    print("2 - Ver a versão do windows que está no seu computador")
    print("3 - Abrir o painel de controle")
    print("4 - Desligar o computador")
    print("5 -  Abrir o Particionador de Disco rígido ")

menu()

opcao = str(input("Escolha: "))

match opcao:
    case "1":
         subprocess("notepad")






    
