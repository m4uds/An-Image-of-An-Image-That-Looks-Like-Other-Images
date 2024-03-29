#current production version
#for assesment 31st Oct 2022
#
#Maud Freeman
#An Image Of An Image That Looks Like Other Images, 2022
#



from base64 import encode
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
volume = engine.getProperty('volume')
engine.setProperty('volume', 2)
print(volume)

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
                
                
            normalized_binary = normalized_binary + " " + encodeed
                    
        
        
        normalized_binary = normalized_binary.split()
        beep_bob = []
        for char in normalized_binary:

            setChar = []
            for byte in char:
                
                if byte == "0":
                    setChar.append("beep")
                else: 
                    setChar.append("bop")
                    
            beep_bob.append(setChar)
        return beep_bob
        
         
def cropImage(_left, _top, _right, _bottom):
    # Opens a image in RGB mode
    im = Image.open('frame.png')
    # Setting the points for cropped image
    left = _left
    top = _top
    right = _right
    bottom = _bottom
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))
    # Shows the image in image viewer
    im1.show()
    im1.save("frame.png")



camera = cv2.VideoCapture(0) # video capture source camera


while True:


  
    ret,frame = camera.read() # return a single frame in variable `frame`
    
    cv2.imwrite('frame.png',frame) # save image
    
    
    #cropImage(50,50,50,50)
    
    caption = generate_image_caption(["frame.png"])[0] 
    
    os.remove("frame.png") #delete image
    caption = convert_text_to_beep_bop(caption)
    
    engine.say("An Image OF AN IMAGE THAT LOOKS LIKE")
    engine.runAndWait()
    for char in caption:
        say = ""
        for x in char:
            say = say + " " + x + ","
        
        print(say)
        engine.say(say)
        engine.runAndWait()
        
    
    
        



