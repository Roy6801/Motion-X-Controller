import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5, tipIds=[8]):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = tipIds
    
    def findPosition(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        self.lmList = []
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                hand = []
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(w * lm.x), int(h * lm.y)
                    hand.append([id, cx, cy])
                    if draw:self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                self.lmList.append(hand)
        return self.lmList
    

    def fingersUp(self, handNo=0, rightHandControl=True):
        if len(self.lmList) !=0:
            fingersUp = []
            for tipId in self.tipIds:
                if tipId !=4 and self.lmList[handNo][tipId][2] < self.lmList[handNo][tipId - 2][2]:
                    fingersUp.append(tipId)
            if 4 in self.tipIds and self.lmList[handNo][4][1] < self.lmList[handNo][2][1] and rightHandControl:
                fingersUp.append(4)
            elif 4 in self.tipIds and self.lmList[handNo][4][1] > self.lmList[handNo][2][1] and not rightHandControl:
                fingersUp.append(4)
            fingersUp.sort()
            return fingersUp
        return []
