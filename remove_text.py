import cv2
from pytesseract import pytesseract
from pytesseract import Output

pytesseract.tesseract_cmd = "C:\\Tesseract-OCR\\tesseract.exe"

class remove_text:
    def remove(self, file_path):
        img = cv2.imread(file_path)

        img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        inv = cv2.bitwise_not(img2)

        ret, thresh1 = cv2.threshold(img2, 125, 255, cv2.THRESH_BINARY)

        ret, thresh2 = cv2.threshold(inv, 250, 255, cv2.THRESH_BINARY)

        add_thresh = thresh1|thresh2

        image_data = pytesseract.image_to_data(add_thresh, output_type=Output.DICT)

        for i, word in enumerate(image_data['text']):
            if word!="" and not word.isspace():
                x, y, w, h = image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i]
                r = int(img[y-1][x-1][0])
                g = int(img[y-1][x-1][1])
                b = int(img[y-1][x-1][2])
                cv2.rectangle(img, (x, y), (x+w, y+h), color=(r, g, b), thickness=-1) #colour: (0,255,0)

        cv2.imshow("Text Removed (press any key to close)", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
