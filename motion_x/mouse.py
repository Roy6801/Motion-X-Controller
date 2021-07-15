import pyautogui as pyto
import win32api as wapi
import time

holdDown = 3
lockMode = False
drag = False
pItr = 0
cItr = 0

class Mouse:
    def __init__(self, mousePad, handNo=0):
        self.handNo = handNo
        self.padX1, self.padY1, self.padX2, self.padY2 = mousePad
        pyto.FAILSAFE = False

    def MousePad(self, tipId, lmList):
        if lmList[self.handNo][tipId][1] > self.padX1 and lmList[
                self.handNo][tipId][1] < self.padX2 and lmList[
                    self.handNo][tipId][2] > self.padY1 and lmList[
                        self.handNo][tipId][2] < self.padY2:
            return True
        else:
            return False

    def LeftHandControl(self, lmList):
        if lmList[self.handNo][2][1] > lmList[self.handNo][17][1] and lmList[
                self.handNo][0][2] > lmList[self.handNo][9][2]:
            return True
        else:
            return False

    def RightHandControl(self, lmList):
        if lmList[self.handNo][2][1] < lmList[self.handNo][17][1] and lmList[
                self.handNo][0][2] > lmList[self.handNo][9][2]:
            return True
        else:
            return False

    def Action(self, x, y, fingersUp):
        global holdDown, drag, lockMode, pItr, cItr

        if fingersUp == [4, 8, 12, 16]:
            lockMode = not lockMode
            time.sleep(1.0)


        if not lockMode:
            if fingersUp == []:
                holdDown = 3
                pItr = 0
                cItr = 0
            

            if fingersUp == [4]:
                drag = not drag
                if drag:
                    pyto.mouseDown(button="left")
                else:
                    pyto.mouseUp(button="left")
                time.sleep(1.0)
            
            
            if fingersUp == [4, 8]:
                pyto.leftClick()
            elif fingersUp == [8, 12]:
                pyto.rightClick()
            elif fingersUp == [8, 20]:
                pyto.doubleClick()
            elif fingersUp == [8]:
                wapi.SetCursorPos((int(x), int(y)))

            if fingersUp == [4, 20]:
                pyto.hotkey('win', 'd')
                time.sleep(1.0)

            if fingersUp == [8, 12, 16, 20]:
                pyto.hotkey('alt', 'tab')
                time.sleep(1.0)

            if fingersUp == [12, 16, 20]:
                pyto.scroll(200)
            elif fingersUp == [16, 20]:
                pyto.scroll(50)
            elif fingersUp == [12, 20]:
                pyto.scroll(-200)
            elif fingersUp == [20]:
                pyto.scroll(-50)

            cItr = time.time()

            if fingersUp == [4, 8, 12, 16, 20]:
                if int(cItr) - int(pItr) == 1:
                    print(holdDown)
                    holdDown -= 1
                    pItr = cItr
                if holdDown == 3:
                    pItr = cItr
                if holdDown == 0:
                    pyto.hotkey('alt', 'f4')
                    holdDown = 3

            if fingersUp == [4, 8, 12]:
                if int(cItr) - int(pItr) == 1:
                    print(holdDown)
                    holdDown -= 1
                    pItr = cItr
                if holdDown == 3:
                    pItr = cItr
                if holdDown == 0:
                    exit(1)
