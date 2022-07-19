from enum import IntEnum
import random 
from time import sleep
from os import system

jogoCompleto = False
tempoLoad = 2.5
posição = 0
dado = 0
dano = 0

#Itens
MoedasOuro = 0
PoçõesVida = 0

#Armas
adaga = 1
adagaDano = 4

espadaLonga = 0
espadaLongaDano = 10

lançaMetal = 0
lançaMetalDano = 16

machado = 0
machadoDano = 22

katana = 0
katanaDano = 36

excalibur = 0
excaliburDano = 60


#Eu
inventario = [["[1]",MoedasOuro,'x','Moedas de Ouro   |', "[5]",0, 'x', 'Chave'], ["[2]",PoçõesVida,'x','Poção de Vida    |', "[6]",lançaMetal, 'x', 'Lança de Metal'], ["[3]",adaga,'x','Adaga            |', "[7]",machado, 'x', 'Machado de Dois Gumes'],["[4]",espadaLonga,'x','Espada Longa     |', "[8]",katana, 'x', 'Katana']]
hp = 100
hpMax = 100
escudo = 10

#Inimigos
goblinsVivos = True
danoGoblins = random.randint(1, 3)
goblin1Vivo = True
goblin2Vivo = True
goblin3Vivo = True

slimesVivos = True
danoSlimes = random.randint(3, 8)
slime1Vivo = True
slime2Vivo = True

trollVivo = True
danoTroll = random.randint(7, 14)

elfoVivo = True
danoElfo = random.randint(4, 18)

mortosVivosVivos = True
danoMortosVivos = random.randint(4,8)
mortovivo1Vivo = True
mortovivo2Vivo = True
mortovivo3Vivo = True

minotauroVivo = True
danoMinotauro = random.randint(8,16)

dragaoVivo = True
dragaoDano = random.randint(15,32)


#Funções
def Inventario():
    global hp, PoçõesVida

    inventario = [["[1]",MoedasOuro,'x','Moedas de Ouro   |', "[5]",0, 'x', 'Chave'], ["[2]",PoçõesVida,'x','Poção de Vida    |', "[6]",lançaMetal, 'x', 'Lança de Metal'], ["[3]",adaga,'x','Adaga            |', "[7]",machado, 'x', 'Machado de Dois Gumes'],["[4]",espadaLonga,'x','Espada Longa     |', "[8]",katana, 'x', 'Katana']]

    print("")
    for n in inventario:
        print(*n)
    print(f"\nInventario:\n[1] - Usar\n[2] - Sair\n")
    ação = input("Qual sua ação?\n")
    if(ação == "1"):
        usar = input("Qual item deseja usar?\n")
        if(usar == "2"):
            if(PoçõesVida > 0):
                if(hp <= 99):
                    PoçõesVida = PoçõesVida - 1
                    print(f"HP: {hp} + 25")
                    hp = hp + 25
                    print(f"HP: {hp}\n")
                    sleep(1.5)
                else:
                    print("\nVocê está de vida cheia.\n")
                    sleep(1.5)
                    return
            else:
                print("\nVocê não possui nenhum deste item.\n")
                sleep(1.5)
                return

    elif(ação == "2"):
        pass

def Morte():
    print("Game over!")
    sleep(10)
    quit()

def Danos():
    global dano
    if(adaga > 0 and espadaLonga == 0):
        dano = adagaDano
    if(espadaLonga > 0 and lançaMetal == 0):
        dano = espadaLongaDano
    if(lançaMetal > 0 and machado == 0):
        dano = lançaMetalDano
    if(machado > 0 and katana == 0):
        dano = machadoDano
    if(katana > 0 and excalibur == 0):
        dano = katanaDano
    if(excalibur > 0):
        dano = excaliburDano
            
print("\n"+"-" * 120)
print("Você é um guerreiro altamente habilidoso, em uma noite de inverno você deixou sua casa para caçar.\nPorém só voltou a tempo de ver um dragão enorme voando para longe enquanto sua mulher e filhos\nqueimavam dentro de sua casa. Ninguém sobreviveu.\n" + "-" * 120 + "\nDesde aquele dia, já se passaram 5 anos e sua busca insaciavel pelo covil do dragão chegou ao fim,\npois você descobriu que ele vive no ultimo andar de uma dungeon nivel 10, o tipo mais perigoso que existe,\n e agora você se encontra em frente a dungeon, pronto para vingar sua familia.")
print("-" * 120)
sleep(5)
while(jogoCompleto == False):

    if(posição == 0): #Base
        Danos()
        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O  O  O  O\n\n[O]\n")
        print(F"HP: {hp}\n")
        print(F"      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Inventário\n[3] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")
        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            Inventario()
            continue
        elif(escolha == "3"):
            break
        
    elif(posição == 1): #GoblinsLanceiros
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
        print(F"Você se depara com uma pequena horda composta de 3 goblins lanceiros, Qual sua ação?\n")
        vidatotalGoblin = 10
        vidaGoblin1 = vidatotalGoblin
        vidaGoblin2 = vidatotalGoblin
        vidaGoblin3 = vidatotalGoblin

        while goblinsVivos == True:
            danoTotal = 0
            print(F"HP Goblin 1: {vidaGoblin1}/{vidatotalGoblin}     HP Goblin 2: {vidaGoblin2}/{vidatotalGoblin}     HP Goblin 3: {vidaGoblin3}/{vidatotalGoblin}\n\nHP: {hp}\n")
            print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                inimigoEscolhido = input("Sua vez, qual você atacará? \n[1] - Goblin Lanceiro\n[2] - Goblin Lanceiro \n[3] - Goblin Lanceiro\n")
                if(inimigoEscolhido == "1"):
                    if(vidaGoblin1 > 0):
                        vidaGoblin1 -= dano
                    else:
                        print("\nInimigo já morto.\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
                        continue
                if(inimigoEscolhido == "2"):
                    if(vidaGoblin2 > 0):
                        vidaGoblin2 -= dano
                    else:
                        print("\nInimigo já morto.\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
                        continue
                if(inimigoEscolhido == "3"):
                    if(vidaGoblin3 > 0):
                        vidaGoblin3 -= dano
                    else:
                        print("\nInimigo já morto.\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
                        continue
                print(f"HP Goblin1: {vidaGoblin1}/{vidatotalGoblin}")
                print(f"HP Goblin2: {vidaGoblin2}/{vidatotalGoblin}")
                print(f"HP Goblin3: {vidaGoblin3}/{vidatotalGoblin}")

                if(vidaGoblin1 <= 0):
                    goblin1Vivo = False
                if(vidaGoblin2 <= 0):
                    goblin2Vivo = False
                if(vidaGoblin3 <= 0):
                    goblin3Vivo = False
                if(vidaGoblin1 <= 0 and vidaGoblin2 <= 0 and vidaGoblin3 <= 0):
                    goblinsVivos = False
                    break

                print("\nEles te atacam de volta\n")

                if(goblin1Vivo == True):
                    danoGoblins = random.randint(1, 3)
                    hp = hp - danoGoblins
                    print(f"1º Goblin: {danoGoblins} de dano")
                if(goblin2Vivo == True):
                    danoGoblins = random.randint(1, 3)
                    hp = hp - danoGoblins
                    print(f"2º Goblin: {danoGoblins} de dano")
                if(goblin3Vivo == True):
                    danoGoblins = random.randint(1, 3)
                    hp = hp - danoGoblins
                    print(f"3º Goblin: {danoGoblins} de dano\n")
                print(f"HP: {hp}\n")
            elif(escolha == "2"):
                print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                
                if(goblin1Vivo == True):
                    danoGoblins = random.randint(1, 3)
                    danoTotal = danoTotal + danoGoblins
                    print(f"1º Hit: {danoGoblins} de dano")
                if(goblin2Vivo == True):
                    danoGoblins = random.randint(1, 3)
                    danoTotal = danoTotal + danoGoblins
                    print(f"2º Hit: {danoGoblins} de dano")
                if(goblin3Vivo == True):
                    danoGoblins = random.randint(1, 3)
                    danoTotal = danoTotal + danoGoblins
                    print(f"3º Hit: {danoGoblins} de dano\n")
                danoRecebido = danoTotal - escudo
                if(danoRecebido < 0):
                    danoRecebido = 0
                hp = hp - danoRecebido
                print(f"Dano total: {danoTotal}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                print(f"HP: {hp}\n")
            if(hp<= 0):
                Morte()
            elif(escolha == "3"):
                Inventario()
                continue
            sleep(tempoLoad)
            system('cls')
            print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
        
        print("\nVocê encontrou:\n 1x - Poção de vida\n15x - Moedas de Ouro\n")
        PoçõesVida =+ 1
        MoedasOuro =+ 15
        print(F"HP: {hp}\n")
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 2): #Bau Ruim
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O [O] O  O  O\n\n O\n")
        print(F"HP: {hp}\n")
        print(F"Ao entrar em uma pequenina sala, você vê um baú bem no centro.")
        print(F"      Ações: \n\n[1] - Abrir\n[2] - Passar Reto\n[3] - Inventário\n")
        escolha = input("Sua Ação: ")
        

        if(escolha == "1"):
            print("Você estende sua mão para abrir o baú,\n de repente, dentes enormes aparecem e mordem seu braço")
            print("-7 de dano")
            hp = hp - 7
            print(f"HP: {hp}\n")
            if(hp<= 0):
                        Morte()
            
        elif(escolha == "2"):
            pass
        elif(escolha == "3"):
            Inventario()
            continue
        
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 3): #Slimes
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O [O] O  O\n\n O\n")
    
        print(F"Seus calçados começam a grudar no chão conforme você avança, mais alguns passos e você encontra dois slimes enormes em sua frente.\n")
        vidatotalSlime = 16
        vidaslime1 = vidatotalSlime
        vidaslime2 = vidatotalSlime

        while slimesVivos == True:
            danoTotal = 0
            print(F"HP Slime 1: {vidaslime1}/{vidatotalSlime}     HP Slime 2: {vidaslime2}/{vidatotalSlime}\n\nHP: {hp}\n")
            print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                inimigoEscolhido = input("Sua vez, qual você atacará? \n[1] - Slime\n[2] - Slime \n")
                if(inimigoEscolhido == "1"):
                    if(vidaslime1 > 0):
                        vidaslime1 -= dano
                    else:
                        print("\nInimigo já morto.\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O [O] O  O\n\n O\n")
                        continue
                if(inimigoEscolhido == "2"):
                    if(vidaslime2 > 0):
                        vidaslime2 -= dano
                    else:
                        print("\nInimigo já morto.\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O [O] O  O\n\n O\n")
                        continue
                print(f"HP Slime1: {vidaslime1}/{vidatotalSlime}")
                print(f"HP Slime2: {vidaslime2}/{vidatotalSlime}")

                if(vidaslime1 <= 0):
                    slime1Vivo = False
                if(vidaslime2 <= 0):
                    slime2Vivo = False
                if(vidaslime1 <= 0 and vidaslime2 <= 0):
                    slimesVivos = False
                    break
                print("\nEles te atacam de volta\n")
                if(slime1Vivo == True):
                    danoSlimes = random.randint(1, 8)
                    hp = hp - danoSlimes
                    print(f"1º Slime: {danoSlimes} de dano")
                if(slime2Vivo == True):
                    danoSlimes = random.randint(1, 8)
                    hp = hp - danoSlimes
                    print(f"2º Slime: {danoSlimes} de dano")
                print(f"HP: {hp}\n")
            elif(escolha == "2"):
                print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                
                if(slime1Vivo == True):
                    danoSlimes = random.randint(1, 8)
                    danoTotal = danoTotal + danoSlimes
                    print(f"1º Hit: {danoSlimes} de dano")
                if(slime2Vivo == True):
                    danoSlimes = random.randint(1, 8)
                    danoTotal = danoTotal + danoSlimes
                    print(f"2º Hit: {danoSlimes} de dano")
                danoRecebido = danoTotal - escudo
                if(danoRecebido < 0):
                    danoRecebido = 0
                hp = hp - danoRecebido
                print(f"Dano total: {danoTotal}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                print(f"HP: {hp}\n")
            if(hp<= 0):
                Morte()
            elif(escolha == "3"):
                Inventario()
                continue
            sleep(tempoLoad)
            system('cls')
            print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O [O] O  O\n\n O\n")

        print("\nVocê encontrou:\n 1x - Espada Longa\n20x - Moedas de Ouro\n")
        espadaLonga += 1
        MoedasOuro = MoedasOuro + 20
        print(F"HP: {hp}\n")
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break
    
    elif(posição == 4): #Loja
        Danos()
        #Preços
        preçoPoção = 15
        system('cls')
        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O  O  [O] O\n\n O\n")
    
        print(F"Ao caminhar, você se depara com uma pequena tenda improvisada e um anão em frente a tenda.\n\n-Boa tarde jovem guerreiro, deseja dar uma olhada em meu estoque? \n Lhe garanto que meus produtos são de qualidade!")
        print(F"\n      Ações: \n\n[1] - Comprar\n[2] - Seguir Viagem\n[3] - Inventário\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            print(F"\n      Itens: \n\n[1] - Poção de vida 30$\n[2] - Sair\n")
            compra = input("Qual item deseja?\n")
            if(compra == "1"):
                if(MoedasOuro > preçoPoção):
                    MoedasOuro -= preçoPoção
                    PoçõesVida += 1
                    print("Você comprou uma poção de vida!")
                    sleep(tempoLoad)
                else:
                    print("\nVocê não tem dinheiro o suficiente")
                    sleep(tempoLoad)
                    pass
            elif(compra == "2"):
                pass
        elif(escolha == "2"):
            print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                dado = random.randint(1, 3)
                print(dado)
                sleep(1)
                posição = posição + dado
            elif(escolha == "2"):
                break
        elif(escolha == "3"):
            Inventario()
            continue

    elif(posição == 5): #Troll Ponte
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n O  O  O  O [O]\n\n O\n")
        print(F"Você chega a um campo cheio de plantas mortas, com um grande rio e uma ponte o atravessando.\nGuardando a ponte está um troll de 2 metros e meio de altura te encarando.\n\n-Para atravessar minha ponte, você precisará acertar minha charada, \na falha será recompensada com morte, vamos iniciar...\n\nEu falo, mas não tenho boca.\nEu ouço, mas não tenho ouvidos.\nNão tenho corpo, mas vivo com o vento.\nQuem sou eu?\n")
        vidatotalTroll = 50
        vidaTroll = vidatotalTroll

        resposta = input("Resposta:\n")
        
        if(resposta == "ECO" or resposta == "eco"):
            print("- Resposta Correta, você mereceu o direito de passar pela ponte.\n")
            pass
        else:
            print("\n- Resposta incorreta, você pagará com sua vida.\n")
            print("\nO troll te ataca com um porrete gigantesco.\n")

            hp = hp - 12
            print(f"Troll: {12} de dano")
            print(f"HP: {hp}\n")
            sleep(tempoLoad)

            while trollVivo == True:
                print(F"HP Troll: {vidaTroll}/{vidatotalTroll}\n\nHP: {hp}\n")
                print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
                escolha = input("Sua Ação: ")

                if(escolha == "1"):
                    if(vidaTroll > 0):
                        vidaTroll = vidaTroll - dano
                    print(f"HP Troll: {vidaTroll}/{vidatotalTroll}")

                    if(vidaTroll <= 0):
                        trollVivo = False
                        break

                    print("\nEle te ataca de volta\n")

                    if(trollVivo == True):
                        danoTroll = random.randint(7, 14)
                        hp = hp - danoTroll
                        print(f"Troll: {danoTroll} de dano")
                    print(f"HP: {hp}\n")

                elif(escolha == "2"):
                    print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                    if(trollVivo == True):
                        danoTroll = random.randint(7, 14)
                        print(f"1º Hit: {danoTroll} de dano")
                    danoRecebido = danoTroll - escudo
                    if(danoRecebido < 0):
                        danoRecebido = 0
                    hp = hp - danoTroll
                    print(f"Dano total: {danoTroll}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                    print(f"HP: {hp}\n")

                elif(escolha == "3"):
                    Inventario()
                    continue

                if(hp<= 0):
                    Morte()

                sleep(tempoLoad)
                system('cls')
                print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
        
        if(trollVivo == True):
            print(F"HP: {hp}")
            print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
            escolha = input("Sua Ação: ")
            
            if(escolha == "1"):
                dado = random.randint(1, 3)
                print(dado)
                sleep(1)
                posição = posição + dado
            elif(escolha == "2"):
                break
        else:
            print("\nVocê encontrou:\n 2x - Poções de vida\n45x - Moedas de Ouro\n")
            PoçõesVida = PoçõesVida + 2
            MoedasOuro = MoedasOuro + 45
            print(F"HP: {hp}")
            print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                dado = random.randint(1, 3)
                print(dado)
                sleep(1)
                posição = posição + dado
            elif(escolha == "2"):
                break

    elif(posição == 6): #Elfo Assasino
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O  O  O\n\n            [O]\n\n O  O  O  O  O\n\n O\n")
        print(F"Ao se encontrar em uma sala totalmente escura, você sente a presença de alguém ali dentro junto com você, forçando a vista você encontra um Elfo assasino altamente treinado pronto para o combate\n")
        vidaTotalElfo = 30
        vidaElfo = vidaTotalElfo

        while elfoVivo == True:
            danoTotal = 0
            print(F"HP Elfo: {vidaElfo}/{vidaTotalElfo}\n\nHP: {hp}\n")
            print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                vidaElfo -= dano
                print(f"HP Elfo: {vidaElfo}/{vidaTotalElfo}")

                if(vidaElfo <= 0):
                    elfoVivo = False
                    break

                print("\nEle te ataca de volta\n")

                if(elfoVivo == True):
                    danoElfo = random.randint(4, 18)
                    hp = hp - danoElfo
                    print(f"Elfo: {danoElfo} de dano")
                print(f"HP: {hp}\n")
                
            elif(escolha == "2"):
                print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                
                if(elfoVivo == True):
                    danoElfo = random.randint(4, 18)
                    print(f"Elfo: {danoElfo} de dano")
                danoRecebido = danoElfo - escudo
                if(danoRecebido < 0):
                    danoRecebido = 0
                hp = hp - danoRecebido
                print(f"Dano total: {danoElfo}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                print(f"HP: {hp}\n")
            if(hp<= 0):
                Morte()
            elif(escolha == "3"):
                Inventario()
                continue
            sleep(tempoLoad)
            system('cls')
            print(f"\n\n O\n\n O  O  O  O  O\n\n             O\n\n[O] O  O  O  O\n\n O\n")
        
        print("\nVocê encontrou:\n 3x - Poções de vida\n45x - Moedas de Ouro\n")
        PoçõesVida = PoçõesVida + 3
        MoedasOuro = MoedasOuro + 45
        print(F"HP: {hp}\n")
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 7): #Bau Bom
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O  O [O]\n\n             O\n\n O  O  O  O  O\n\n O\n")
        print(F"HP: {hp}\n")
        print(F"Ao entrar em uma pequenina sala, você vê um baú bem no centro.")
        print(F"      Ações: \n\n[1] - Abrir\n[2] - Passar Reto\n[3] - Inventário\n")
        escolha = input("Sua Ação: ")
        

        if(escolha == "1"):
            print("Você Encontra 1x Lança de metal e 3x Poções de vida\n")
            lançaMetal += 1
            PoçõesVida += 3  
        elif(escolha == "2"):
            pass
        elif(escolha == "3"):
            Inventario()
            continue
        
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 8): #Mortos Vivos
        Danos()
        system('cls')
        print(f"\n\n O\n\n O  O  O [O] O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        print(F"Ao entrar na sala você sente um cheiro terrivel de carne podre, dentro dela estão 3 mortos-vivos sedentos por carne humana.\n")
        vidatotalMortoVivo = 40
        vidaMortoVivo1 = vidatotalMortoVivo
        vidaMortoVivo2 = vidatotalMortoVivo
        vidaMortoVivo3 = vidatotalMortoVivo

        while mortosVivosVivos == True:
            danoTotal = 0
            print(F"HP Morto-Vivo 1: {vidaMortoVivo1}/{vidatotalMortoVivo}     HP Morto-Vivo 2: {vidaMortoVivo2}/{vidatotalMortoVivo}     HP Morto-Vivo 3: {vidaMortoVivo3}/{vidatotalMortoVivo}\n\nHP: {hp}\n")
            print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                inimigoEscolhido = input("Sua vez, qual você atacará? \n[1] - Morto-Vivo\n[2] - Morto-Vivo \n[3] - Morto-Vivo\n")
                if(inimigoEscolhido == "1"):
                    if(vidaMortoVivo1 > 0):
                        vidaMortoVivo1 -= dano
                    else:
                        print("\nInimigo já morto...Duas vezes\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O [O] O\n\n             O\n\n O  O  O  O  O\n\n O\n")
                        continue
                if(inimigoEscolhido == "2"):
                    if(vidaMortoVivo2 > 0):
                        vidaMortoVivo2 -= dano
                    else:
                        print("\nInimigo já morto...Duas vezes\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O [O] O\n\n             O\n\n O  O  O  O  O\n\n O\n")
                        continue
                if(inimigoEscolhido == "3"):
                    if(vidaMortoVivo3 > 0):
                        vidaMortoVivo3 -= dano
                    else:
                        print("\nInimigo já morto...Duas vezes\n")
                        sleep(tempoLoad)
                        system('cls')
                        print(f"\n\n O\n\n O  O  O [O] O\n\n             O\n\n O  O  O  O  O\n\n O\n")
                        continue
                print(f"HP Morto-Vivo 1: {vidaMortoVivo1}/{vidatotalMortoVivo}")
                print(f"HP Morto-Vivo 2: {vidaMortoVivo2}/{vidatotalMortoVivo}")
                print(f"HP Morto-Vivo 3: {vidaMortoVivo3}/{vidatotalMortoVivo}")

                if(vidaMortoVivo1 <= 0):
                    mortovivo1Vivo = False
                if(vidaMortoVivo2 <= 0):
                    mortovivo2Vivo = False
                if(vidaMortoVivo3 <= 0):
                    mortovivo3Vivo = False
                if(vidaMortoVivo1 <= 0 and vidaMortoVivo2 <= 0 and vidaMortoVivo3 <= 0):
                    mortosVivosVivos = False
                    break

                print("\nEles te atacam de volta\n")

                if(mortovivo1Vivo == True):
                    danoMortosVivos = random.randint(4, 8)
                    hp = hp - danoMortosVivos
                    print(f"1º Morto-Vivo: {danoMortosVivos} de dano")
                if(mortovivo2Vivo == True):
                    danoMortosVivos = random.randint(4, 8)
                    hp = hp - danoMortosVivos
                    print(f"2º Morto-Vivo: {danoMortosVivos} de dano")
                if(mortovivo3Vivo == True):
                    danoMortosVivos = random.randint(4, 8)
                    hp = hp - danoMortosVivos
                    print(f"3º Morto-Vivo: {danoMortosVivos} de dano\n")
                print(f"HP: {hp}\n")

            elif(escolha == "2"):
                print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                
                if(mortovivo1Vivo == True):
                    danoMortosVivos = random.randint(4, 8)
                    danoTotal = danoTotal + danoMortosVivos
                    print(f"1º Hit: {danoMortosVivos} de dano")
                if(mortovivo2Vivo == True):
                    danoMortosVivos = random.randint(4, 8)
                    danoTotal = danoTotal + danoMortosVivos
                    print(f"2º Hit: {danoMortosVivos} de dano")
                if(mortovivo3Vivo == True):
                    danoMortosVivos = random.randint(4, 8)
                    danoTotal = danoTotal + danoMortosVivos
                    print(f"3º Hit: {danoMortosVivos} de dano\n")
                danoRecebido = danoTotal - escudo
                if(danoRecebido < 0):
                    danoRecebido = 0
                hp = hp - danoRecebido
                print(f"Dano total: {danoTotal}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                print(f"HP: {hp}\n")
            if(hp<= 0):
                Morte()
            elif(escolha == "3"):
                Inventario()
                continue
            sleep(tempoLoad)
            system('cls')
            print(f"\n\n O\n\n O  O  O [O] O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        
        print("\nVocê encontrou:\n 2x - Poções de vida\n60x - Moedas de Ouro\n")
        PoçõesVida = PoçõesVida + 2
        MoedasOuro = MoedasOuro + 60
        print(F"HP: {hp}\n")
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 3)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 9): #Loja
        Danos()
        #Preços
        preçoPoção = 15
        system('cls')
        print(f"\n\n O\n\n O  O [O] O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
    
        print(F"Ao caminhar, você se depara com uma pequena tenda improvisada e um anão em frente a tenda.\n\n-Boa tarde jovem guerreiro, deseja dar uma olhada em meu estoque? \n Lhe garanto que meus produtos são de qualidade!")
        print(F"\n      Ações: \n\n[1] - Comprar\n[2] - Seguir Viagem\n[3] - Inventário\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            print(F"\n      Itens: \n\n[1] - Poção de vida 30$\n[2] - Sair\n")
            compra = input("Qual item deseja?\n")
            if(compra == "1"):
                if(MoedasOuro > preçoPoção):
                    MoedasOuro -= preçoPoção
                    PoçõesVida += 1
                    print("Você comprou uma poção de vida!")
                    sleep(tempoLoad)
                else:
                    print("\nVocê não tem dinheiro o suficiente")
                    sleep(tempoLoad)
                    pass
            elif(compra == "2"):
                pass
        elif(escolha == "2"):
            print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
            escolha = input("Sua Ação: ")
            if(escolha == "1"):
                dado = random.randint(1, 3)
                print(dado)
                sleep(1)
                posição = posição + dado
            elif(escolha == "2"):
                break
        elif(escolha == "3"):
            Inventario()
            continue
        
    elif(posição == 10): #Minotauro
        Danos()
        system('cls')
        print(f"\n\n O\n\n O [O] O  O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        print(F"Enquanto anda você se encontra dentro de um labirinto, após 20 minutos andando sem parar você chega à uma sala maior.\nParado no centro dela, esta um minotauro raivoso enorme com um machado de dois gumes em suas mãos.\n")
        vidatotalMinotauro = 80
        vidaMinotauro = vidatotalMinotauro

        while minotauroVivo == True:
            danoTotal = 0
            print(F"HP Minotauro: {vidaMinotauro}/{vidatotalMinotauro}\n\nHP: {hp}\n")
            print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                vidaMinotauro -= dano
                print(f"HP Minotauro: {vidaMinotauro}/{vidatotalMinotauro}")

                if(vidaMinotauro <= 0):
                    minotauroVivo = False
                    break

                print("\nEle te ataca de volta\n")

                if(minotauroVivo == True):
                    danoMinotauro = random.randint(8, 16)
                    hp = hp - danoMinotauro
                    print(f"Minotauro: {danoMinotauro} de dano")
                print(f"HP: {hp}\n")

            elif(escolha == "2"):
                print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                
                if(minotauroVivo == True):
                    danoMinotauro = random.randint(8, 16)
                    print(f"Minotauro: {danoMinotauro} de dano")
                danoRecebido = danoMinotauro - escudo
                if(danoRecebido < 0):
                    danoRecebido = 0
                hp = hp - danoRecebido
                print(f"Dano total: {danoMinotauro}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                print(f"HP: {hp}\n")
            if(hp<= 0):
                Morte()
            elif(escolha == "3"):
                Inventario()
                sleep(tempoLoad)
                system('cls')
                print(f"\n\n O\n\n O [O] O  O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
                continue
            sleep(tempoLoad)
            system('cls')
            print(f"\n\n O\n\n O [O] O  O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        
        print("\nVocê encontrou:\n 1x - Poção de vida\n1x - Machado de Dois Gumes\n")
        PoçõesVida = PoçõesVida + 1
        machado = machado + 1
        print(F"HP: {hp}\n")
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 2)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 11): #Bau Bom
        Danos()
        system('cls')
        print(f"\n\n O\n\n[O] O  O  O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        print(F"HP: {hp}\n")
        print(F"Ao entrar em uma sala, ao fundo dela, você encontra um baú dourado.")
        print(F"      Ações: \n\n[1] - Abrir\n[2] - Passar Reto\n[3] - Inventário\n")
        escolha = input("Sua Ação: ")
        

        if(escolha == "1"):
            print("Você Encontra uma Katana e 4x Poções de vida\n")
            katana += 1
            PoçõesVida += 4  
        elif(escolha == "2"):
            pass
        elif(escolha == "3"):
            Inventario()
            continue
        
        print(F"\n      Ações: \n\n[1] - Jogar o dado (D3)\n[2] - Encerrar Sessão\n")
        escolha = input("Sua Ação: ")

        if(escolha == "1"):
            dado = random.randint(1, 1)
            print(dado)
            sleep(1)
            posição = posição + dado
        elif(escolha == "2"):
            break

    elif(posição == 12): #Boss
        Danos()
        system('cls')
        print(f"\n\n[O]\n\n O  O  O  O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        print(F"Você chega na ultima sala da dungeon, uma sala gigantesca e cheia de nevoa, você não enxerga nada,\nde repente uma sombra preta gigantesca se levanta e começa uma ventania, dissipando toda a nevoa.\nQuando a nevoa termina de se dissipar você vê um dragão negro de olhos vermelhos enorme em sua frente.\nLute ou Morra\n")
        vidaTotalDragao = 400
        vidaDragao = vidaTotalDragao

        while dragaoVivo == True:
            danoTotal = 0
            print(F"HP Dragão Negro: {vidaDragao}/{vidaTotalDragao}\n\nHP: {hp}\n")
            print(F"      Ações: \n[1] - Atacar\n[2] - Defender\n[3] - Inventário\n")
            escolha = input("Sua Ação: ")

            if(escolha == "1"):
                vidaDragao = vidaDragao - dano
                print(f"HP Dragão Negro: {vidaDragao}/{vidaTotalDragao}")

                if(vidaDragao <= 0):
                    dragaoVivo = False
                    break

                print("\nEle te ataca de volta\n")

                if(dragaoVivo == True):
                    dragaoDano = random.randint(15, 32)
                    hp = hp - dragaoDano
                    print(f"Dragão Negro: {dragaoDano} de dano")
                print(f"HP: {hp}\n")
            elif(escolha == "2"):
                print("Você ergue seu escudo para se defender dos ataques inimigos, gerando 10 de escudo\n")
                
                if(dragaoVivo == True):
                    dragaoDano = random.randint(15, 32)
                    print(f"Dragão Negro: {dragaoDano} de dano")
                danoRecebido = dragaoDano - escudo
                if(danoRecebido < 0):
                    danoRecebido = 0
                hp = hp - danoRecebido
                print(f"Dano total: {dragaoDano}\nEscudo: {escudo}\nDano recebido: {danoRecebido}")
                print(f"HP: {hp}\n")
            if(hp<= 0):
                Morte()
            elif(escolha == "3"):
                Inventario()
                continue
            sleep(tempoLoad)
            system('cls')
            print(f"\n\n[O]\n\n O  O  O  O  O\n\n             O\n\n O  O  O  O  O\n\n O\n")
        
        print("\nVocê encontrou:\n 1x - Excalibur\n2500x - Moedas de Ouro\n")
        excalibur =+ 1
        MoedasOuro =+ 2500

        jogoCompleto = True

if(jogoCompleto == True):
    print("Após uma àrdua batalha você da seu ultimo golpe no Dragão Negro e ele desaba no chão, Sua vingança está feita.")
    print("\n\nParabéns! Você completou o jogo...Obrigado por Jogar!")
    sleep(20)