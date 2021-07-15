import pyautogui as pyto

class Scale:
    def __init__(self, camDim, scrCount=1):
        camW, camH = camDim
        scrW, scrH = pyto.size()
        print(scrW, scrH)
        self.w = (2 * scrW * scrCount) / camW
        self.h = (2 * scrH) / camH
    
    def fit(self, x, y):
        return self.w * (x - 300), self.h * (y - 150)