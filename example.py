import cv2
import numpy as np

gray_img = cv2.imread('./322868_1100-1100x628.png', cv2.IMREAD_GRAYSCALE)
unchanged_img = cv2.imread('./322868_1100-1100x628.png', cv2.IMREAD_UNCHANGED)

cv2.imwrite('gray_test.png', gray_img)
cv2.imwrite('unchanged_test.png', unchanged_img)

print('='*40)
print('img_save!!')
print('Enter command =>  ls')
print('gray_test.png & unchanged_test.png')
print('='*40)
