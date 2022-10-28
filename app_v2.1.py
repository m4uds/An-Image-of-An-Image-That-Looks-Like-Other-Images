#current production version
#for assesment 31st Oct 2022
#
#Maud Freeman
#An Image Of An Image That Looks Like Other Images, 2022
#



from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image
import torch
import pyttsx3
import cv2
import time
import os

#voice engine init
engine = pyttsx3.init() # object creation
engine.setProperty('rate',100)

#init model
model = VisionEncoderDecoderModel.from_pretrained("model/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("model/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("model/vit-gpt2-image-captioning")

#inti pytorch
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# model settings
max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def generate_image_caption(image_paths):
    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
    if i_image.mode != "RGB":
      i_image = i_image.convert(mode="RGB")
    images.append(i_image)
    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    print(preds)
    return preds
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
        
        for byte in normalized_binary:
            
            if byte == "0":
                beep_bob = beep_bob + " beep,"
            else: 
                beep_bob = beep_bob + " bop,"
        return beep_bob 

camera = cv2.VideoCapture(0) # video capture source camera 

while True:
  
    ret,frame = camera.read() # return a single frame in variable `frame`
    
    cv2.imwrite('frame.png',frame) # save image
    caption = generate_image_caption(['frame.png'])[0] 
    print(caption)
    os.remove("frame.png") #delete image
    caption = convert_text_to_beep_bop("LEts test this").split()
    print(caption)

    i = 0
    for char in caption:
        if i % 8 == 0:
            time.sleep(4)
        engine.say(char)
        engine.runAndWait()
 
  
    time.sleep(10)



