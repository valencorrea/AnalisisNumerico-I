
def maximos_presa():
    valores_x = []
    maximos_x = []

    # N = 300
    for n in range(1,300):
      # pico de la presa
      if(valores_x[n-1] < valores_x[n] and valores_x[n] > valores_x[n+1]):
        maximos_x.append(n)

    return maximos_x

def maximos_depredador():
    valores_y = []
    maximos_y = []

    # N = 300
    for n in range(1, 300):
        # pico del depredador
        if (valores_y[n - 1] < valores_y[n] and valores_y[n] > valores_y[n + 1]):
            maximos_y.append(n)

    return maximos_y
