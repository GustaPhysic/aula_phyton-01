#Criaçao do dicionários dos jogadores
jogador = {}
for g in range (3):
   nome = input("Informe o nome do jogador: ")
   pontuacao = int(input("Informe os pontos iniciais: "))
   print("--------------------")

   jogador[nome] = pontuacao

#ADICIONAR PONTOS AOS JOGADORES
for y in range (3):
   jogador_nome = input("\nDigite o nome do jogador para nova pontuação: ")
   novos_pontos = int(input("Informe os novos pontos: "))

if jogador_nome in jogador:
    if novos_pontos != jogador[nome]:
      jogador[nome] = jogador[nome] + novos_pontos
      print(f"Pontução atualizada")
else:
    print("Jogador não encontrado") 
#LISTAGEM DA PONTUAÇÃO ATUALIZADA DOS JOGADORES
for nome, pontuacao in jogador.items():
  print(f"{nome} | {pontuacao}")
     
     



  







