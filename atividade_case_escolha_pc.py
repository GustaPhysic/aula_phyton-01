print("Nossos computadores disponíveis na loja: \n|Opção 1| PC para Estudos e tarefas básicas \n|Opção 2| PC para Programação \n|Opção 3| PC para Design gráfico \n|Opção 4| PC para edição de vídeo / 3D / jogos")
      
escolha = int(input("Informe o número correspondente do computador que você se interessa: "))
match escolha:
    case 1:
        print("Informações do PC para Estudos e tarefas básica: \nProcessador:Intel Core i3 ou AMD Ryzen 3, \nArmazenamento:SSD 256 GB , \nMemória RAM:8 GB, \nPlaca de vídeo:integrada (Intel UHD ou Radeon integrada), \nSistema: Windows 11 ou Linux")
    case 2:
        print("PC para Programação: \nProcessador:Intel Core i5 ou AMD Ryzen 5,\nMemória RAM:16 GB, \nArmazenamento:SSD 512 GB NVMe, \nPlaca de vídeo:integrada ou dedicada simples, \nSistema:Windows / Linux ")
    case 3:
        print("PC para Design gráfico: \nProcessador:Intel Core i7 ou Ryzen 75,\nMemória RAM:32 GB\nArmazenamento:SSD 1 TB NVMe, \nPlaca de vídeo:NVIDIA RTX 3060 / 4060, \nSistema:Windows / Linux ")
    case 4:
        print("PC para edição de vídeo / 3D / jogos: \nProcessador:Intel Core i9 ou Ryzen 9,\nMemória RAM: 32/ 64 GB\nArmazenamento:SSD NVMe 1 TB \nPlaca de vídeo:NVIDIA RTX 4070 / 4080, \nSistema:Windows / Linux , \nFonte: 750 W ")

    case _:
        print("Essa opção não está disponível!!!")