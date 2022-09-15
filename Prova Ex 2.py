#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
#pode ou não se aposentar. As condições para aposentadoria são: (1,5)
#a. Ter pelo menos 65 anos;
#b. Ou ter trabalhado pelo menos 30 anos;
#c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade_trab = int(input("Qual a sua idade: "))
tempo_servico = int(input("Quantos anos você trabalhou: "))
if idade_trab >= 65:
    print("Pode se aposentar")
elif tempo_servico >= 30:
    print("Pode se aposentar")
elif idade_trab >= 60:
    if tempo_servico >= 25:
        print("Pode se aposentar")
else:
    print("Não pode se aposentar")
