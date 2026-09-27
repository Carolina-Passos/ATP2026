import random

def utilizador_adivinha ():
    print ("Vou pensar num número de 0 a 100 tenta adivinhar em que número pensei")

    numero_secreto = random.randint(0,100)  
    tentativas = 0

    while True:
        resposta = int(input("Qual é o teu palpite? "))
        tentativas = tentativas + 1

        if resposta == numero_secreto:
            print ("Muito bem, era mesmo esse número!")
            print (f"número de tentativas: {tentativas}")
            break

        elif resposta > numero_secreto:
            print ("O meu número é menor")

        else:
            print ("o meu número é maior")



def computador_adivinha ():
    print ("Pensa num número de 0 a 100.")
    print ("Responda apenas com:")
    print ("Acertaste")
    print ("Maior")
    print ("Menor")

    minimo = 0 
    maximo = 100
    tentativas = 0

    while True:
        palpite = (minimo + maximo) // 2
        tentativas = tentativas + 1

        resposta = (input(f"O teu número é {palpite}?"))

        if resposta == "Acertaste":
                print (f"Sou mesmo bom, acertei em {tentativas} tentativas!")
                break

        elif resposta == "Maior":
                minimo = palpite + 1

        elif resposta == "Menor":
                maximo = palpite - 1
                
print ("Vamos jogar ao Adivinha o Número!")
print ("1- Eu adivinho e tu pensas no número")
print ("2- Eu penso no número e tu adivinhas")

opção = input("Escolhe uma opção: ")
if opção == "1":
    computador_adivinha ()
elif opção == "2":
    utilizador_adivinha ()
else: 
    print ("opção inválida")