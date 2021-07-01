import pyautogui

class Scale:
    def __init__(self, camDim):
        camW, camH = camDim
        scrW, scrH = pyautogui.size()
        print(scrW, scrH)
        self.w = (1.5*scrW)/camW
        self.h = (1.5*scrH)/camH
    
    def fit(self, x, y):
        return self.w * (x - 300), self.h * (y - 150)