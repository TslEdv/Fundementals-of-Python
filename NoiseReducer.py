import cv2
img = cv2.imread("noisy.jpg")
result = cv2.fastNlMeansDenoisingColored(img,None,20,10,7,21)
cv2.imshow("Original Image", img)
cv2.imshow("Noise removed", result)
cv2.waitKey(0)
