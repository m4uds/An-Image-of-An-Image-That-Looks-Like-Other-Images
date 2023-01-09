from locale import normalize


def convert_text_to_beep_bop(text):
    beep_bob = ""
    normalized_binary = ""
    a_bytes = bytes(text, "utf8")
    binary = ' '.join(["{0:b}".format(x) for x in a_bytes])
    binary = binary.split(" ")
    #binary = binary.replace(" ","")

    for encodeed in binary:
        
        if len(encodeed) < 8:
            numZ = 8 - len(encodeed)
            i = 0
            while i < numZ:
                encodeed = "0" + encodeed
                i = i+1
        
        normalized_binary = encodeed + " "
                
    
    print(normalized_binary)
    
    beep_bob_array = []
    
    for binary in normalized_binary:
        print(binary)
        for byte in binary:
            if byte == "0":
                beep_bob = beep_bob + " beep"
            else: 
                beep_bob = beep_bob + " bop"
        
        beep_bob_array.append(beep_bob)
    
    return beep_bob_array 


print(convert_text_to_beep_bop("chair is a man who is not normal"))