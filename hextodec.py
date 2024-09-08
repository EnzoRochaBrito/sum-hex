_hexhash = {
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15,
}

def hextodec(Hexnum: str) -> int:
    """Returns the decimal value of an hexadecimal number

    Args:
        Hexnum (str): Hexadecimal value. Ex: "0xff" or "e3ff"

    Returns:
        int: Decimal value of an hexadecimal number
    """    
    
    hexv = Hexnum.removeprefix('0x')
    counter = 0
    arr = []
    mirrowed = []
    
    for i in hexv:
        mirrowed.insert(0, i)
    
    for i in mirrowed:
        try:
            j = int(i) * (16**counter)
        except:
            j = _hexhash[i] * (16**counter)
            
        counter+=1
        arr.append(j)
        
    return sum(arr)

def rgb(Hex: str) -> list:
    """Returns the value of every hexadecimal pair to its respective RGB color

    Args:
        hex (str): Hexadecimal value. Ex: "#fe9a3e"

    Returns:
        tuple: Decimal value of the hexadecimal pairs. Ex: (254, 154, 62)
    """
    _Hex = Hex.removeprefix("#")
    
    dec_values = [] #List who will hold the RGB values
    
    pointer = 0 #Points to an digit of the hexadecimal number
    
    hholder = '' #Hold the current pair
    
    if len(_Hex) == 3:
        for i in _Hex:
            
            hholder += (i*2)
            
            dec_values.append(hextodec(hholder))
            
            hholder = ''
            
        return dec_values
    
    elif len(_Hex) != 6:
        return False
       
    else:
        for _ in range(0, 3):
                
            hholder += _Hex[pointer]
            hholder += _Hex[pointer+1]
            
            pointer += 2 #Go to the nert pair
            
            dec_values.append(hextodec(hholder))
            
            hholder = ''
            
        return dec_values