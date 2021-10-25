import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

url = "12.jpeg"
img = cv2.imread(url)

output = pytesseract.image_to_string(img)

text = open("12.txt","w")
text.write(output)
text.close()
