def convertFrom10(number, numbersystem):
    #10->101(3-ban)
    #17->10001
    eredmeny = ''
    x=number
    while x!=0:
        maradek = x % numbersystem
        x = int(x / numbersystem)
        if maradek==15: 
            eredmeny=f'F{eredmeny}'
        elif maradek==14:
            eredmeny=f'E{eredmeny}'
        elif maradek==13:
            eredmeny=f'D{eredmeny}'
        elif maradek==12:
            eredmeny=f'C{eredmeny}'
        elif maradek==11:
            eredmeny=f'B{eredmeny}'
        elif maradek==10:
            eredmeny=f'A{eredmeny}'
        else:
            eredmeny=f'{maradek}{eredmeny}'


    return eredmeny
     
  