from tracker import handTracker
from mouse import Mouse
from scale import Scale
import cv2
import time


def main(cfg):
    fps = 1
    camW = 640
    camH = 480
    pLocX, pLocY = 0, 0
    cLocX, cLocY = 0, 0
    smoothening = cfg[2]
    cap = cv2.VideoCapture(0)
    cap.set(3, camW)
    cap.set(4, camH)
    ht = handTracker(maxHands=1, tipIds=[4, 8, 12, 16, 20])
    ms = Mouse((150, 75, camW - 150, camH - 75))
    if cfg[0] == 0:
        rightHandControl = False
        hand = ms.LeftHandControl
    else:
        rightHandControl = True
        hand = ms.RightHandControl
    
    sc = Scale((camW - 300, camH - 150), scrCount=cfg[1])

    while True:
        start = time.time()
        success, img = cap.read()
        if not success:continue
        img = cv2.flip(img, 1)
        lmList = ht.findPosition(img, draw=True)
        try:
            fingersUp = ht.fingersUp(rightHandControl=rightHandControl)
            scaledX, scaledY = sc.fit(lmList[0][7][1], lmList[0][7][2])
            cLocX = pLocX + (scaledX - pLocX) / smoothening
            cLocY = pLocY + (scaledY - pLocY) / smoothening
            if hand(lmList):
                ms.Action(cLocX, cLocY, fingersUp)
        except Exception as e:
            pass
        if cfg[3] == 1:
            cv2.putText(img, str(int(fps)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)
            cv2.rectangle(img, (150, 75), (camW - 150, camH - 75), (255, 0, 0), 1, cv2.LINE_AA)
            cv2.imshow('Output', img)
        pLocX, pLocY = cLocX, cLocY
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        fps = 1/(time.time() - start)


if __name__ == "__main__":
    try:
        with open("config.txt", "r") as fr:
            cfg = []
            for line in fr:
                cfg.append(int(line))
    except Exception as e:
        pass
    main(cfg)