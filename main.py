import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Users\Przemek\Desktop\tmp\zaawansowane programowanie\programs\tesseract\tesseract.exe'


def get_text_from_img(img_path: str):
    img = cv2.imread(img_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    converted_img = cv2.threshold(cv2.medianBlur(img_gray, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return pytesseract.image_to_string(converted_img)


if __name__ == '__main__':
    print(get_text_from_img('data/img_1.jpg'))
    print(get_text_from_img('data/img_2.jpg'))
    print(get_text_from_img('data/img_3.jpg'))
    print(get_text_from_img('data/img_4.jpg'))
    print(get_text_from_img('data/img_5.jpg'))
