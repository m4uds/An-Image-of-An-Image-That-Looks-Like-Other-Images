
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image
import torch
import pyttsx3
import cv2
import time
import os

#voice engine init

engine = pyttsx3.init() # object creation
#voices = engine.getProperty('voices')
#print(voices)


model = VisionEncoderDecoderModel.from_pretrained("model/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("model/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("model/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)



max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}
def predict_step(image_paths):
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
  print(preds)
  preds = [pred.strip() for pred in preds]
  return preds

camera = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop)
while True:
    
  ret,frame = camera.read() # return a single frame in variable `frame`
  #cv2.imshow('img1',frame) #display the captured image
  cv2.imwrite('frame.png',frame) # 
  caption = predict_step(['frame.png'])[0] # ['a woman in a hospital bed with a woman in a hospital bed']
  os.remove("frame.png")
  print(caption)
  engine.say(caption)
  engine.runAndWait()
  
  time.sleep(1)
  #cv2.destroyAllWindows()