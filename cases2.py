while True:

    escolha = str(input("Confirmar operação? "))

    match escolha:
        case "sim" | "yes" | "s" | "y":
            print("Confiramdo!!!!")
            break
        case "não" | "no" | "n" | "nope":
            print("Rejeitado!!!!")
            break
        case _:
            print("Selecione novamente: ")