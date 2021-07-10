# Motion-X-Controller

About
---
A motion gesture mouse and hotkey control using Computer Vision (for Windows).
This software uses OpenCV-Python. A webcam is required to be connected to run this program.
Run Setup.bat for installing dependencies.
Run MotionX.bat for launching the Program.


Configuration
---
Edit config.txt for preferences.

Enter a number on each line such that:

Line 1: Enter 1 for Right Hand Control and 0 for Left Hand Control.

Line 2: Enter number of Monitors used.

Line 3: Mouse Cursor Smoothness Factor (Greater than 1).

Line 4: Enter 1 to display Web Cam Input and Hand Detection Screen.


Controls
---

Lock Mode   :   This Mode allows to keep the program running in background
                while not detecting any unnecessary gestures and cursor
                movements unless gesture to turn off Lock Mode is made.

Drag Mode   :   This Mode enables you to click and drag a window.

Gestures:-

Raise a closed fist infront of camera.

1) Move Cursor  :   Lift and Move Index Finger.

2) Left Click   :   While Index Finger Lifted, stretch the thumb out quickly and close
                    it back.

3) Right Click  :   While Index Finger Lifted, stretch the Middle Finger out quickly and
                    put it down back.

4) Slow Scroll Down :   Lift Pinky Finger.

5) Slow Scroll Up   :   Lift Ring Finger and Pinky Finger.

6) Fast Scroll Down :   Lift Long Finger with Gesture 4.

7) Fast Scroll Up   :   Lift Long Finger with Gesture 5.

8) Perform ALT + TAB Hotkey :   Lift all four fingers (Thumb closed) and
                                put all down quickly.

9) Perform ALT + F4 Hotkey  :   Stretch all fingers out and hold down 3 seconds
                                to close a window.

10) Show Desktop (WIN + D Hotkey)    :   Stretch out Thumb and Pinky Finger
                                            quickly and fold down.

11) Drag Mode   :   Stetch out thumb and fold it down quickly (while cursor
                    is on the title bar of required window). Use Gesture 1
                    to move the cursor. This time the window will be dragged
                    wherever you want. Perform the thumb gesture once again
                    to exit Drag Mode. This Mode can be used for selecting
                    texts as well.

12) Lock Mode   :   Stretch out all fingers except Pinky Finger quickly
                    and fold down to enter/exit this Mode.

13) Close Motion-X-Controller   :   Stretch and hold down Thumb, Index Finger
                                    and Long Finger for 3 seconds to turn off
                                    the program.

14) Cooldown    :   Drag Mode, Lock Mode and Close have a 3 seconds countdown that
                    can be reset or cancel any of the above three actions by
                    showing a closed fist.