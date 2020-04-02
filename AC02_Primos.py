def primo (n):
    if n != 0 and n !=1:
        if n>3:
            for i in range(2,n):
                if n %i==0:
                    return False
        return True
    return


i=1
cont =0
while True:
    primo(i)
    i+=1
    if primo(i) == True:
        cont+=1
        print(i)
    if cont == 100:
        break
