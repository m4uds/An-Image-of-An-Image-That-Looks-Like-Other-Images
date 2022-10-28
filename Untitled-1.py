import time
def convert_text_to_beep_bop(text)
caption = convert_text_to_beep_bop("LEts test this").split()
print(caption)

i = 0
for char in caption:
    if i % 8 == 0:
        time.sleep(4)
engine.say(char)
engine.runAndWait()
 
    