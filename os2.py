import subprocess
import os

def executar_comando(comando):
    try:
        resultado = subprocess.run(comando, shell=True)
    except Exception as e:
        print("Erro ao executar comando:",e)

def mostrar_hostname():
    executar_comando("hostname")

def exibir_hora():
    executar_comando("time")

def mostrar_data():
    executar_comando("date")

def abrir_paint():
    executar_comando("pbrush")

def reiniciar_computador():
    executar_comando("shutdown -r}")

def mostrar_gerenciador_de_tarefas():
    executar_comando("taskmgr")

def abrir_painel_de_controle():
     executar_comando("control")

def mostrar_versao_windows():
    executar_comando("winver")

def desligar_computador():
    executar_comando("logoff}")

def abrir_bloco_de_notas():
    executar_comando("notepad")

def menu():
    while True:
        print(" ================Ferramenta de Rede============ ")
        print("1 - MOSTRAR O HOSTNAME")
        print("2 - EXIBIR HORA")
        print("3 - MOSTRAR ou MUDAR DATA")
        print("4 - ABRIR PAINT")
        print("5 - REINICIAR COMPUTADOR")
        print("6 - MOSTRA O GERENCIADOR DE TAREFAS")
        print("7 - ABRIR PAINEL DE CONTROLE")
        print("8 - MOSTRAR VERSÃO DO WINDOWS")
        print("9 - DESLIGAR COMPUTADOR")
        print("10 - ABRIR BLOCO DE NOTAS")
        print("0 - SAIR")
        print("================Criado por:GustPhysic===========")
        opcao = str(input("Escolha:"))
        match opcao:
            case "1":
                mostrar_hostname()
            case "2":
                exibir_hora()
            case "3":
                mostrar_data()
            case "4":
                abrir_paint()
            case "5":
                reiniciar_computador()
            case "6":
                mostrar_gerenciador_de_tarefas()
            case "7":
                abrir_painel_de_controle()
            case "8":
                mostrar_versao_windows()
            case "9":
                desligar_computador()
            case "10":
                abrir_bloco_de_notas()
            case "0":
                print("Saindo")
                break
            case _:
                print("Erro")
if __name__ == "__main__":
     menu()  
     