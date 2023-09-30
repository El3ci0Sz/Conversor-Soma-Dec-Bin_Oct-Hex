N1 = int(input())
N2 = int(input())
Representacao = int(input())
#Entrada 2 numeros inteiros a representacao decimal, e mais um sendo a escolha da representacao esperada na saida
#10 decimal, 2 binario, 8 octal e 16 hexadicimal

if  N2 > 512 or N2 <0: 
    print("ERRO")   
    
elif N1 > 512 or N1 < 0:
    print("ERRO")
        
elif Representacao != 10 and Representacao != 2 and Representacao != 8 and Representacao != 16:
    print("ERRO")
       
#Algumas condicoes que caso nao cumprimidas retornaram "ERRO", e encerraram o codigo
else:
    def conversao_binario(N1):
        if N1 == 0:
            return '0'
        
        else:
            A = ''
            while N1 > 1:
                resto_da_divisao_por2 = N1%2
                N1 //= 2
                A += str(resto_da_divisao_por2)
            A += '1'
        return A[::-1]
    
    X=conversao_binario(N1)
    Y=conversao_binario(N2)
#funcao que converte o numero da base decimal para a base binaria, caso seja 0 o binario é zero caso nao.(if) declaro "A" uma variavel em strg, crio um while para repetir o calculo(dividir o numero por 2 e armazenar o resto da divisao)
#Ate o numero a ser divido ser 1, o while para(e vai se armazenando os bits na variavel "A" que cria uma "palavra" de 0 e 1), no final se adiciona mais um 1 no final, no return eu inverto a ordem para ficar do jeito certo
    
    E = str(int(X) + int(Y))
    VetorF = [0] * 11
    G = ''
    g = 10
    
    for i in range(len(E) -1, -1, -1):
        VetorF[g] = int(E[i])
        g -= 1
    g= 10
    
    for i in range(11):    
        if VetorF[g] == 1:
            G = '1' + G 
        if VetorF[g] == 0:
            G = '0' + G
        if VetorF[g] == 2:
            G = '0' + G
            VetorF[g-1] += 1
        if VetorF[g] == 3:
            G = "1" + G
            VetorF[g-1] += 1
        g -= 1
    
    Resultado_da_soma_Binario = G
#Esse bloco faz a soma de 2 numeros binarios, ele pega X e Y, muda de str para int, soma os dois, depois transforma o resultado em str e armazena em E
#Cria um vetor com 11 posições com 11 zeros(VetorF), e uma variavel G(strg), 
#uso um for no range do tamanho de E, ao contrario, para preencher o vetor F, com numeros inteiros, que estavam em E em formato strg
#Depois mais um 'for' dessa vez para formar o numero binario, resultado da soma.
    
    def conversao_decimal(n):
        decimal = 0
        Valor = 1
        count = 0
        
        for i in range(len(n)):
            if n[i] == "0":
                decimal += 0
            elif n[i] == '1':
                    while count < -(i-10):
                        Valor = 2 * Valor
                        count += 1
                    decimal += Valor
                    Valor = 1
                    count = 0        
        
        return decimal 
    Decimal = conversao_decimal(G)
#Depois de ter somado os numeros na base 2(Binario), esse codigo converte o resultado da soma para a base 10 novamente(Decimal)
#Codigo para converter de binario para decimal, usei o while para simular a função pow, de potenciação
#O -(i-10) serve para saber a posição em que o numero esta de tras para frente
    
    def conversao_octal(n):       
        if n == 0:
            Octal = "0000"  
        
        else:     
            Octal = ''
            while n > 0:
                resto_da_divisao_por8 = n%8
                n //= 8
                Octal = str(resto_da_divisao_por8) + Octal
        
        while len(Octal) < 4:
            Octal = "0" + Octal        
        
        return Octal
    Octal = conversao_octal(Decimal)
#Esse codigo converte o resultado da Soma que estava em Decimal para a base 8(Octal)
#Segue a mesma logica da conversão binaria mas desse vez, como é na base 8, as divisões são feitas por 8
#E o while no final serve para preencher "Octal" com 0s, para que fique exatamente 4 digitos, se preciso
               
    def conversao_hexadecimal(n):
        if n == 0:
            return '000'
        
        else:
            numero_hexadecimal = ''
            while n > 0:
                resto_da_divisao_por16 = n%16
                n //= 16
                if (resto_da_divisao_por16) < 10:
                    numero_hexadecimal = str(resto_da_divisao_por16) + numero_hexadecimal
                
                else:
                    Vetor_Letras = ["A","B","C","D","E","F"]
                    J = Vetor_Letras[resto_da_divisao_por16-10]
                    numero_hexadecimal = str(J) + numero_hexadecimal
            
            while len(numero_hexadecimal) < 3:
                numero_hexadecimal = '0' + numero_hexadecimal       
        
        return numero_hexadecimal
    
    Hexadecimal = conversao_hexadecimal(Decimal)
#Esse bloco de codigo converte o resultado da soma que estava em decimal, para Hexadecimal
#Mesma Logica da conversão em Binario, mudando o Fato de que agora a base é 16, então as divisões são feitas por 16
#Então ele divide e armazena o resto da divisão, mA para os numeros de 10-15, o programa substitui por Letras de A-F
    print("Binario1",X)
    print("Binario2",Y)
    print("Soma",Resultado_da_soma_Binario)

    print("Decimal",Decimal)

    print("Octal",Octal)

    print("Hexadecimal",Hexadecimal)
#Aqui estão os prints, cada um com sua base respectiva