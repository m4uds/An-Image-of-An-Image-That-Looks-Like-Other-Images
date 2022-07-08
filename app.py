
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
from PIL import Image
import torch
import pyttsx3
import cv2
import time

#voice engine init
engine = pyttsx3.init() # object creation


model = VisionEncoderDecoderModel.from_pretrained("vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("vit-gpt2-image-captioning")

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
  preds = [pred.strip() for pred in preds]
  return preds


while True:
  cap = cv2.VideoCapture(0) # video capture source camera (Here webcam of laptop) 
  ret,frame = cap.read() # return a single frame in variable `frame`
  cv2.imshow('img1',frame) #display the captured image
  cv2.imwrite('c1.png',frame)

        

  cap.release()

  a = predict_step(['c1.png']) # ['a woman in a hospital bed with a woman in a hospital bed']
  print(a)
  engine.say(a)
  engine.runAndWait()
  
  time.sleep(15)
  cv2.destroyAllWindows()