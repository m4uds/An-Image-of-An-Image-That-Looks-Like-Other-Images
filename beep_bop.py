from locale import normalize


def convert_text_to_beep_bop(text):
    beep_bob = ""
    normalized_binary = ""
    a_bytes = bytes(text, "utf8")
    binary = ' '.join(["{0:b}".format(x) for x in a_bytes])
    binary = binary.split(" ")
    #binary = binary.replace(" ","")

    for encodeed in binary:
        print(encodeed)
        if len(encodeed) < 8:
            print(encodeed)
            print(len(encodeed))
            numZ = 8 - len(encodeed)
            i = 0
            while i < numZ:
                encodeed = "0" + encodeed
                i = i+1
                
        print(encodeed)
        print(len(encodeed))
        normalized_binary = normalized_binary + encodeed
    
    

    for byte in normalized_binary:
        
        if byte == "0":
            beep_bob = beep_bob + " beep"
        else: 
            beep_bob = beep_bob + " bop"
    return beep_bob 


print(convert_text_to_beep_bop("chair is a man who is not normal"))