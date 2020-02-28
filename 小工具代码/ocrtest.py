
import pytesseract
from PIL import Image
img = Image.open('C:/Users/Shanzhen/Desktop/test.png')
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
s = pytesseract.image_to_string(img)  #不加lang参数的话，默认进行英文识别


print(s)
