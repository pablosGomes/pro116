import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("resultado", img)
cv2.waitKey(0)

cv2.putText(img
"sol",
(100,80),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"mercurio",
(200,150),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"venus",
(250,150),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"terra",
(300,150),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"marte",
(350,150),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"jupiter",
(400,300),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"saturno",
(450,270),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"urano",
(500,250),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)
cv2.putText(img
"netuno",
(550,250),
cv2.fontFace=FONT_HERSHEY_COMPLEX,
2,
(0,0,255)
)