def convert_text_to_beep_bop(text):
    beep_bob = ""
    a_bytes = bytes(text, "utf8")
    binary = ' '.join(["{0:b}".format(x) for x in a_bytes])
    binary = binary.replace(" ","")

    for byte in binary:
        
        if byte == "0":
            beep_bob = beep_bob + " beep"
        else: 
            beep_bob = beep_bob + " bop"
    
    return beep_bob 


print(convert_text_to_beep_bop("apple and co"))