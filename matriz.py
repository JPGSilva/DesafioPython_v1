import numpy as np

# Criando a matriz 2D de inteiros de 8 bits (valores aleatórios para demonstração)
matriz = np.random.randint(0, 256, size=(3, 3), dtype=np.uint8)
print("Matriz 2D de Entrada:")
print(matriz)

# Selecionando a primeira, segunda e terceira linha da matriz
primeira_linha = matriz[0]
segunda_linha  = matriz[1]
terceira_linha = matriz[2]

# Calculando desvio padrão de cada linha
desvio_padrao1 = np.std(primeira_linha)
desvio_padrao2 = np.std(segunda_linha)
desvio_padrao3 = np.std(terceira_linha)

# Definindo os limites do intervalo desejado
limite_inferior1 =  np.mean(primeira_linha) - np.std(primeira_linha)
limite_inferior2 =  np.mean(segunda_linha) - np.std(segunda_linha)
limite_inferior3 =  np.mean(terceira_linha) - np.std(terceira_linha)


limite_superior1 = np.mean(primeira_linha) + np.std(primeira_linha)
limite_superior2 = np.mean(segunda_linha) + np.std(segunda_linha)
limite_superior3 = np.mean(terceira_linha) + np.std(terceira_linha)

# Aplicando o range à primeira linha
primeira_linha_range = np.round(np.clip(primeira_linha, limite_inferior1, limite_superior1),decimals=2)
segunda_linha_range = np.round(np.clip(segunda_linha, limite_inferior2, limite_superior2), decimals=2)
terceira_linha_range = np.round(np.clip(terceira_linha, limite_inferior3, limite_superior3), decimals=2)


matriz_2d = np.vstack((primeira_linha_range, segunda_linha_range, terceira_linha_range))

# Imprimir os resultados
print("Matriz 2D de saida após aplicar os ranges:")
print(matriz_2d ) # feito em 20 linhas de codigo