import cv2

# detect text and words contours
def biggestRectangle(contours):
    print(f'run biggestRectangle., args: contours: {contours}')
    biggest = None
    max_area = 0
    indexReturn = -1
    for index in range(len(contours)):
        i = contours[index]
        area = cv2.contourArea(i)
        if area > 100:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.1 * peri, True)
            if area > max_area:  # and len(approx)==4:
                biggest = approx
                max_area = area
                indexReturn = index
    print(f'finish biggestRectangle., returns: {indexReturn}')
    return indexReturn