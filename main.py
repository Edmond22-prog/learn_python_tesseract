import pytesseract

from PIL import Image


if "__main__" == __name__:
    image_file = "data/images/original-simple-doc_1.jpg"

    image = Image.open(image_file)
    print(image)

    ocr_result = pytesseract.image_to_string(image)
    print(ocr_result)
