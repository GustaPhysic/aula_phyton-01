def menu():
    print("==========Deseja fazer um pedido online em nossa loja?==========")
    print("1 - SIM ")
    print("2 - NÃO ")
    print("==============Obrigado pela visita============")


menu()

opcao = str(input("Escolha uma das opções para prosseguir: "))
match opcao:
   case "1":
        print("Seja Bem vindo ,venha ver nossos produtos!!")
   case "2":
        print("Obrigado por sua atenção!!")
   case _:
        print("Opção inexistente!")
   
        





    