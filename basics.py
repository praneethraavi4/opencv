import cv2


# Reading an image
img = cv2.imread(r"D:\repos\OpenCV\datasets\cat.jpg")
cv2.imshow("cat",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)

# Reading a video

capture = cv2.VideoCapture(r"D:\repos\OpenCV\datasets\dog.mp4")
while True:
    istrue, frame = capture.read()
    cv2.imshow("video",frame)
    if cv2.waitKey(20) & 0xFF == ord("d"):
        break
capture.release()
cv2.destroyAllWindows()

