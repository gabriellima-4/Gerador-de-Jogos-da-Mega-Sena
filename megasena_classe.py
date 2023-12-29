###################################################
## Gerador de números para a Mega Sena da Virada ##
###################################################

# O jogo da Mega Sena (no final do ano sendo a Mega Sena da Virada) é amplamente conhecido por todo o Brasil. Consiste numa aposta
    # de 6 a 20 números, visando acertar os 6 (a sena) sorteados oficialmente.

# A cada execução deste código, a saída será uma lista de inteiros gerados aleatoriamente e em ordem crescente, ou seja, 
    # um 'jogo' da Mega. O tamanho dessa lista irá variar dependendo de quantos números quer apostar (de 6 a 20).

# Além disso, o programa já possui funções para armazenar todos os
    # jogos gerados num arquivo .txt, como também mostrar a quantia de dinheiro que deveria ser paga em relação ao tamanho da aposta.

# A premiação da Mega da Virada de 2023 será de 570 Milhões de Reais, e as apostas só podem ser feitas até
    # o dia 31/12/2023 às 17:00h.

# Lembre-se de jogar com responsabilidade e dentro de suas possibiliadades financeiras.


# Bibliotecas Utilizadas:
import random

# Classes e Métodos:

class MegaSena:

    def mega_sena(self, quantidade_numeros):
        if quantidade_numeros < 6:
            raise ValueError("Para jogar, devem ser escolhidas no mínimo 6 dezenas.")
            
        else:
            self.numeros_a_jogar = []
            dezenas = list(range(1, 61))  # Números possíveis para aposta (01 a 60)

            selecao = random.choices(dezenas, k=quantidade_numeros) # A quantidade de números escolhidos será igual ao
                                                                        # desejado pelo usuário.

            self.numeros_a_jogar.extend(selecao)
            self.numeros_a_jogar = list(set(self.numeros_a_jogar)) # Primeira remoção de números duplicados.
            random.shuffle(self.numeros_a_jogar) # Garantia de que a cada execução do código será um 'jogo' novo.
            
            while (len(self.numeros_a_jogar) != quantidade_numeros):
                self.numeros_a_jogar.extend(random.choices(dezenas, k=(quantidade_numeros - len(self.numeros_a_jogar))))
                self.numeros_a_jogar = list(set(self.numeros_a_jogar)) # caso o número (ou números) adicionado já esteja na lista, ele será removido.
                
                # Caso após a remoção dos numeros duplicados fique faltando um ou mais números em 'numeros_a_jogar',
                    # outros números serão aleatóriamente escolhidos para repor, até que a lista tenha o tamanho desejado e não tenha
                    # nenhum número duplicado.

                # Depois do laço de repetição, a função retornará a lista em ordem crescente.
            
            return sorted(self.numeros_a_jogar)
        

    def custo_jogo_mega(self, tamanho): # preço do jogo em relação ào _tamanho_ da aposta (quantidade de números)
        if tamanho == 6:
            return "R$ 5,00"
        if tamanho == 7:
            return "R$ 35,00"
        if tamanho == 8:
            return "R$ 140,00"
        if tamanho == 9:
            return "R$ 420,00"
        if tamanho == 10:
            return "R$ 1.050,00"
        if tamanho == 11:
            return "R$ 2.310,00"
        if tamanho == 12:
            return "R$ 4.620,00"
        if tamanho == 13:
            return "R$ 8.580,00"
        if tamanho == 14:
            return "R$ 15.015,00"
        if tamanho == 15:
            return "R$ 25.035,00"
        if tamanho == 16:
            return "R$ 40.040,00"
        if tamanho == 17:
            return "R$ 61.880,00"
        if tamanho == 18:
            return "R$ 92.820,00"
        if tamanho == 19:
            return "R$ 135.600,00"
        if tamanho == 20:
            return "R$ 193.800,00"
        

    def gravar_jogos(self):

        jogo = open("megasena_virada.txt", "a")
        jogo.write("     Jogo para a Mega da Virada     \n")
        jogo.write("                 |                  \n")
        jogo.write("------------------------------------\n")
        jogo.write("    {}    ".format(sorted(self.numeros_a_jogar)) + "\n")
        jogo.write("------------------------------------\n")
        jogo.write("\n")
        jogo.close()


    def ler_jogos(self):
        with open("megasena_virada.txt", "r") as arquivo:
            lista_jogos = arquivo.readlines()
        return lista_jogos


########################
## Execução do Código ##
########################

ms = MegaSena()
num_jogos = int(input("Digite quantos jogos de Mega Sena quer fazer: "))

for _ in range(num_jogos):
    print("Novo jogo!")
    qtd_numeros = int(input("Digite a quantidade de dezenas que quer apostar na Mega-Sena: "))
    
    print(f"""
        Seu jogo da Mega está pronto! Aqui estão seus números : | {ms.mega_sena(qtd_numeros)} |
        Sua aposta foi de {qtd_numeros} números e o total à pagar será de {ms.custo_jogo_mega(qtd_numeros)}.
    """)
    print("\n")

    ms.gravar_jogos()

ms.ler_jogos()

