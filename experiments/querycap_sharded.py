import requests
from PIL import Image

from transformers import BlipProcessor, Blip2ForConditionalGeneration

model_name = "ethzanalytics/blip2-flan-t5-xl-sharded"
processor = BlipProcessor.from_pretrained(model_name)
model = Blip2ForConditionalGeneration.from_pretrained(model_name, device_map="auto", offload_folder="offload")

print("Finished loading model")

img_url = 'https://storage.googleapis.com/sfr-vision-language-research/BLIP/demo.jpg' 
raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

while True:
    question = input(">> ")
    inputs = processor(raw_image, question, return_tensors="pt")
    out = model.generate(**inputs)

    print(processor.decode(out[0], skip_special_tokens=True))

