import cv2
import pytesseract

class Image_OCR:
    def __init__(self,image,lang="fas"):
        self.image = image
        self.lang = lang

    def predict(self):
        text = pytesseract.image_to_string(self.image,lang=self.lang)
        print(text)

image = cv2.imread("main-qimg-057fd8bf1928b95dead70fb944e8d794-lq.jpg")
Image_OCR(image).predict()
    