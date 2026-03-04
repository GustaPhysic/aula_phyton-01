Isabela = {"Livro O pequeno príncipe", "perfume", "Bolsa", "Fone sem fio", "Morango"}
Gabriel = {"Fone sem fio", "Garrafa", "par de meias", "camisa ", "short"}
Gustavo = {"Óculos", "Fone sem fio", "Whey", "Mangá Deah Note ", "Livro O pequeno príncipe"}
Victor =  {"Óculos", "Fone sem fio", "Carregador", "Moletom", "Carregador"}

Isabela_itens = set(Isabela)
Gabriel_itens = set(Gabriel)
Gustavo_itens = set(Gustavo)
Victor_itens = set(Victor)

#Caso tenha uma repetição
print(f"Itens de Isabela:{Isabela_itens}")
print(f"Itens de Gabriel:{Gabriel_itens}")
print(f"Itens de Gustavo:{Gustavo_itens}")
print(f"Itens de Victor:{Victor_itens}")

#INTERSCETION
itens_em_comum = Isabela_itens.intersection(Gabriel_itens, Gustavo_itens, Victor_itens)
print(f"Itens em comum entre essas pessoas : {itens_em_comum}\n")

#UNION
total_todos_itens = Isabela_itens.union(Gabriel_itens, Gustavo_itens, Victor_itens)
print(f"Total de itens : {total_todos_itens}\n")
print(len(total_todos_itens))

