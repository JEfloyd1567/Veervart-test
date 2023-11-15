from sys import stdin

def conflict(T, r, c, v):
    # Inicializa las variables
    ans, i, T[r][c] = False, 0, 0

    # Comprueba si el valor v coincide con algún valor en la misma columna o fila
    while ans == False and i != 9:
        ans, i = T[r][i] == v or T[i][c] == v, i + 1

    # Encuentra la esquina superior izquierda de la subcuadrícula
    i, rr, cc = 0, (r // 3) * 3, (c // 3) * 3

    # Comprueba si el valor v coincide con algún valor en la misma subcuadrícula
    while ans == False and i != 3:
        j = 0
        while ans == False and j != 3:
            ans, j = T[rr+i][cc+j] == v, j + 1
        i += 1

    # Establece el valor en la posición (r, c) del tablero T a v
    T[r][c] = v
    return ans

def solve(T, r, c):
    ans = None

    # Si se alcanzó el final del tablero, se ha encontrado una solución válida
    if r == 9: ans = True
    else:
        # Si se alcanzó el final de la fila, pasa a la siguiente fila
        if c == 9: ans = solve(T, r + 1, 0)
        else:
            # Si el valor ya está establecido en la posición (r, c)
            if T[r][c] != 0:
                # Comprueba si no hay conflictos con el valor actual
                if conflict(T, r, c, T[r][c]) == False:
                    # Llama recursivamente para la siguiente columna
                    ans = solve(T, r, c + 1)
                else:
                    ans = False
            else:
                ans, v = False, 1
                # Prueba todos los valores posibles
                while ans == False and v != 10:
                    # Comprueba si no hay conflictos con el valor v
                    if conflict(T, r, c, v) == False:
                        T[r][c] = v
                        # Llama recursivamente para la siguiente columna
                        ans = solve(T, r, c + 1)
                    v += 1
                # Si no se encontró una solución, deshace el cambio
                if ans == False:
                    T[r][c] = 0
    return ans

def print_board(T):
    #Esta Funcion se encarga de imprimir el tablero
    for i in range(9):
        for j in range(9):
            print(T[i][j], end=' ')
        print()

def main():
    T = [] #tablero general
    for i in range(9):
        line = list(map(int, stdin.readline().strip().split())) #lee cada subtablero
        T.append(line) #se agrega cada subtablero al tablero principal
    if(solve(T,0,0)): #se soluciona el tablero
        print_board(T) #se imprime el tablero ya resuelto
    else:
        print('No solution :(')
main()