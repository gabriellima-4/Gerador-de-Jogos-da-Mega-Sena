# Gerador de Jogos da Mega Sena
![Imagem de jogo físico da Mega](https://s2-g1.glbimg.com/HNy8l536EI7MfCIQSIAuv0v8RVI=/0x0:600x371/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_59edd422c0c84a879bd37670ae4f538a/internal_photos/bs/2022/C/z/amTaqnTaydr4gig5wCyg/fta20181204045-b.jpg)

   O jogo da Mega Sena (no final do ano sendo a Mega Sena da Virada) é amplamente conhecido por todo o Brasil. Consiste numa aposta de 6 a 20 números, visando acertar os 6 (a sena) sorteados oficialmente.

   
   Os códigos neste repositório utilizaram por pura e simples inspiração este jogo de apostas, e seu escritor (no caso, eu) não possui nenhuma relação com a Caixa Econômica Federal.
   A criação de todo esse repositório tem objetivo puramente de aprendizagem e exercício de conhecimentos de programação, que estou aprendendo dentro e fora da Universidade.
   
   Lembre-se de jogar com responsabilidade e dentro de suas possibiliadades financeiras!
   
   **Observação**:
   Como este README foi feito **bem** depois do sorteio oficial, transmitido ao vivo em rede nacional, já não se pode mais disputar pelo prêmio recorde de 588 milhões. Houveram 5 ganhadores da sena, cada um faturando aproximadamente 118 milhões de Reais.
   Os números sorteados foram **21 - 24 - 33 - 41 - 48 - 56** .

   A expectativa para o ano de 2024 é que o prêmio da Mega da Virada seja ainda maior, podendo muito bem passar da casa dos 600 milhões de Reais.

   É dinheiro pra c******.

## Linguagem Utilizada:
![Python](https://logowik.com/content/uploads/images/python.jpg=300x300)


## Como funciona o código:
  #### Arquivo megasena_classe.py
  O usuário escolhe primeiramente quantos jogos da Mega ele quer que o código gere. Depois disso, o usuário deve fornecer manualmente como entrada a quantidade de dezenas que CADA jogo deve ter.
  Lembrando, o mínimo de dezenas na Mega Sena são 6. Portanto, caso peça um jogo de 5 ou menos números, o código levantará um erro, e você terá de recomeçar o processo.
  
  
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
        
  

  Após isso, o código exibirá os números gerados após cada iteração e o custo que cada um teria na vida real.

## Funcionalidades:
  O código escrito por mim tem _todas as explicações mais detalhadas_ dentro dele, em forma de **comentários**, quase que a cada linha, explicando passo-a-passo. Por favor, leia-o.
  
  De forma geral, o código apresenta:
  * Informações sobre o preço de cada jogo, levando em conta a quantidade de números escolhidos.
  * Escritura e salvamento em arquivo do tipo .txt
  * Randomização garantida à cada execução.

