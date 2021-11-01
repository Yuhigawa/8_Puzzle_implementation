def escolha():
    selection = input("manual(True) ou Randomico(False): ")

    if str(selection) != "True":
        print("Seu merda, foi randomico então")
        return False

    return True

def manual():  # preenchimento do tabuleiro manual
    Lista = []

    while len(Lista) < 9: 
        num = input("digite um valor :")

        if num.isnumeric() and jata(int(num),Lista) == True:
            if int(num) >= 0 and int(num) <=8:
                Lista.append(int(num))
            else:
                print("mas é burro")
        else:
            print("Eh numero neh meu confrade")
                
    return Lista

def jata(n,Lista):  #função ve se já há o elemmento no tabuleiro
    numta = True
    for i in Lista:
        if n == i:
            numta = False
            print("é igual")
    return numta