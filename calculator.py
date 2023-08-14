import cv2
from cvzone.HandTrackingModule import HandDetector
#import pyttsx3


class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        self.text = cv2.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv2.FONT_HERSHEY_PLAIN,
                                2, (50, 50, 50), 2)


# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)  # height
detector = HandDetector(detectionCon=0.8, maxHands=1)
size = 80
margin = 850

buttonList = []


def Cal_Button():
    # Creating Buttons
    for x in range(4):
        for y in range(4):
            xpos = x * size + margin
            ypos = y * size + 150
            buttonList.append(Button((xpos, ypos), size, size, '9'))


Cal_Button()
# Loop
while True:
    # Get image from Webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # Detection of Hand
    hands, img = detector.findHands(img, flipType=False)

    # cv2.rectangle(img, (650, 50), (550 + 580, 80 + 70),
    #               (230, 230, 230), cv2.FILLED)
    #
    # cv2.rectangle(img, (650, 50), (550 + 580, 80 + 70),
    #               (50, 50, 50), 3)

    # Draw all Buttons
    for button in buttonList:
        button.draw(img)

    # Display Image
    cv2.imshow("Image", img)
    cv2.waitKey(1)
