def main():


    print('-'*30)
    print("Sequência de Fibanacci")
    print('-'*30)
    n = int(input('Quantos termos você quer mostar?'))
    t1 = 0
    t2 = 1

    print('-'*30)
    print('{}, {}'.format(t1, t2), end='')
    cont = 3 
    while cont <= n:
        t3 = t1 + t2
        print(', {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
    
    Fn = int(input('\n\n Digite um valor. '))
    Fn = Fn - 1 + Fn + 2
    if n == 0:
        print ('Erro.')
    if n != Fn :
        print (Fn)
    else:
        print('Ok')
    


if __name__ =="__main__":
    main()