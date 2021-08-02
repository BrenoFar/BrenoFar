from random import randrange 
def combsort(num):                 #Definindo a função combsort
    gap = len(num)
    while gap > 1:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        for i in range(len(num) - gap):
            j = i+gap
            if num[i] > num[j]:
                num[i], num[j] = num[j], num[i]

 
num_list = [75, 16, 55, 19, 48, 14, 2, 61, 22, 100]
lista = []
print('Defina qual dessas opções você deseja?')
print('1- Lista Pré-definida')
print('2- Definir a lista e o tamanho')
print('3- Lista randomizada com x elementos definidos também pelo usuário')
P1=int(input('\n'))

if P1 ==1 or P1 ==2 or P1==3:

    if P1==1:
        print('Você selecionou a lista pré definida.')
        print('Antes: ',num_list)
        combsort(num_list)
        print('Depois: ',num_list)


    elif P1==2:
        aux = int(input('Defina o tamanho da sua lista (ex: 1/10/50/30/100) \n'))
        contador = 0
        while contador < aux:
            value=int(input('Entre com o {0}° valor \n'.format(contador+1)))
            lista.append(value)
            contador = contador + 1
        print("Antes: ", lista) 
        combsort(lista)                #chamando a função combsort atribuindo a lista (que fica entre parenteses)
        print("Depois:  ", lista)
        print('\n')
    if P1==3:
        aux = int(input('Defina o tamanho da sua lista (ex: 1/10/50/30/100) \n'))
        contador = 0
        rangeusuario=(int(input('Digite até que numero pode ser randomizado: \n')))
        while contador < aux:
            for f in range(1):
                value=randrange(rangeusuario)
                lista.append(value)
                contador= contador + 1
        print("Antes ,",lista)
        combsort(lista)           #Chamando a lista com função combsort randomizada
        print("Depois: ",lista)
        print('\n')

else:
    print('Valor incorreto! FIM DO ALGORITMO.')