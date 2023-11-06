import cv2
x = cv2.imread('./logo.png')
h, w, _ = x.shape
x = cv2.resize(x,(h//2,w//2))
u = cv2.imwrite('./logo_.png', x)
print(u)