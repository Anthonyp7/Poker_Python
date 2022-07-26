from module_tirage import machine, premier_tirage
from module_gain import gain

def video_poker():
    age = int(input("Age? "))
    if age < 18:
        print("les jeux d'argent sont interdits aux mineurs!")
        exit()
    else:
        bankroll = int(input("Combien voulez vous mettre dans la machine? "))
        mise = int(input("Votre mise : "))

        while bankroll > 0:
            if mise > bankroll:
                print('Mise trop haute, votre bankroll: ' + str(bankroll))
                mise = int(input("Votre mise : "))
            else :
                main = machine()
                g, resultat = gain(main, mise)
                bankroll = bankroll - mise
                bankroll += g
                print(resultat)
                print('Bankroll: ' + str(bankroll))

                restart = input("Voulez vous rejouer? (o/n) ")
                if restart == 'n' or restart == 'non':
                    print('Cashout: ' + str(bankroll))
                    exit()
                else :
                    mise = int(input("Votre mise : "))

        print("Bankroll à sec, retentez votre chance")

video_poker()
