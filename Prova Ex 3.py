#Faça um programa que seja semelhante ao jogo da forca, mas com uma
#única letra. A letra que o usuário deve adivinhar deve ser definida no
#código do programa. O usuário tem 5 chances de acertar a letra. O
#programa finaliza sua execução quando o usuário acerta a letra ou
#quando acabam suas chances.

import random
vidas = 5
letra_random = ["a", "b", "c", "d", "e", "f"]
letra_choice = random.choice(letra_random)
while vidas > 0:
    player_choice = str(input("Digite uma letra: a, b, c, d, e ou f: "))
    if player_choice != letra_choice:
        vidas -= 1
    else:
        break
if player_choice == letra_choice:
    print("Você acertou")
else:
    print("Você não acertou")

