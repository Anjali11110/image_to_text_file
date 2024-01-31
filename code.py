import pytesseract as pyt
from PIL import Image

img=Image.open("text.jpg")
pyt.pytesseract.tesseract_cmd="C:\\Users\\Anjali Tulabandala\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
text=pyt.image_to_string(img)
print(text)
with open("text.txt","w+") as f:
    f.write(text)