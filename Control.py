from Model import Model

class Control:
    def __init__(self):
        self.metodo = Model() #Instanciando a Classe Model
        self.opcao = -1


    def menu(self):
        print("Escolha umas das opções abaixo:  \n\n" +
              "0. Sair \n" +
              "1. Exercicio 1\n" +
              "2. Exercicio 2\n" +
              "3. Exercicio 3\n" +
              "4. Exercicio 4\n" +
              "5. Exercicio 5\n" +
              "6. Exercicio 6\n" +
              "7. Exercicio 7\n" +
              "8. Exercicio 8\n" +
              "9. Exercicio 9\n" +
              "10. Exercicio 10\n" +
              "11. Exercicio 11\n" +
              "12. Exercicio 12\n" +
              "13. Exercicio 13\n" +
              "14. Exercicio 14\n" +
              "15. Exercicio 15\n" +
              "16. Exercicio 16\n" +
              "17. Exercicio 17\n" +
              "18. Exercicio 18\n" +
              "19. Exercicio 19\n" +
              "20. Exercicio 20\n")

        self.opcao = int(input())

    def operacao(self):
        while(self.opcao != 0):
            self.menu() #Chamando o Menu

            if self.opcao == 0:
                print("Obrigado!")

            elif self.opcao == 1:
                print("A: 10\n"
                      "B: 20")
                print(self.metodo.exercicio1())

            elif self.opcao == 2:
                print("Digite um valor inteiro: \n")
                num1 = int(input())
                print("o Numero antecessor ao numero digitado é: ")
                print(self.metodo.exercicio2(num1))

            elif self.opcao == 3:
                print("Digite a Base do Retângulo: \n")
                base = float(input())
                print("Digite a Altura do Retângulo: \n")
                altura = float(input())
                print("A área do Retângulo é: ")
                print((self.metodo.exercicio3(base, altura)))

            elif self.opcao == 4:
                print("Digite a sua idade em Anos: \n")
                ano = int(input())
                print("Mes: \n")
                mes = int(input())
                print("Dias: \n")
                dia = int(input())
                print("Sua idade em dias é: ")
                print(self.metodo.exercicio4(ano, mes, dia))

            elif self.opcao == 5:
                print("Digite o numero total de eleitores: \n")
                eleitores = float(input())
                print("Digite o total de votos Brancos: \n")
                brancos = float(input())
                print("Digite o total de votos nulos: \n")
                nulos = float(input())
                print("Digite o total de votos válidos: \n")
                validos = float(input())
                print(self.metodo.exercicio5(eleitores, brancos, nulos, validos))

            elif self.opcao == 6:
