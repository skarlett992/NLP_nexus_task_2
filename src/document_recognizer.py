import cv2
import numpy as np
import pytesseract
from src.biggestRestangle import biggestRectangle
from src.detect_languages import detect_languages
from src.image_to_text import image_to_text

# open scan and convert it to text
def get_text_from_document(input_file):
    print(f'run get_text_from_document., args: input_file: {input_file}')
    img = cv2.imread(input_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invGamma = 1.0 / 0.3
    table = np.array([((i / 255.0) ** invGamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    # apply gamma correction using the lookup table
    gray = cv2.LUT(gray, table)
    ret, thresh1 = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]

    # find text contours
    indexReturn = biggestRectangle(contours)
    # create a crop mask
    # Create mask where white is what we want, black otherwise
    mask = np.zeros_like(img)
    # Draw filled contour in mask
    cv2.drawContours(mask, contours, indexReturn, 255, -1)
    # Extract out the object and place into output image
    out = np.zeros_like(img)
    out[mask == 255] = img[mask == 255]

    # crop the image
    (y, x, _) = np.where(mask == 255)
    (topy, topx) = (np.min(y), np.min(x))
    (bottomy, bottomx) = (np.max(y), np.max(x))
    out = img[topy: bottomy + 1, topx: bottomx + 1, :]

    # first convert scan to text
    all_predictions = image_to_text(out_rgb=cv2.cvtColor(out, cv2.COLOR_BGR2RGB),
                                    lang='eng',
                                    config="--psm 11 --oem 3",
                                    output_type=pytesseract.Output.DATAFRAME)
    # second convert scan to text using docs language
    all_predictions = image_to_text(out_rgb=cv2.cvtColor(out, cv2.COLOR_BGR2RGB),
                                    lang=f'{detect_languages(all_predictions)}+eng',
                                    config="--psm 11 --oem 3",
                                    output_type=pytesseract.Output.DATAFRAME)
    print(f"finish get_text_from_document., returns: {' '.join(all_predictions)}")

    return ' '.join(all_predictions)