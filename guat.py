from myro import *
from time import *
from photo import RobotPic
from threading import Thread
import urllib2
import ast

# Robot class
class Guatmobile:

    url = "http://myro-robot.appspot.com"
    key = "/?key=6969"
    check = "?check="

    # Logic Variables
    beginTime = 0
    timeElapsed = 0

    # Functions to calculate how long it took to turn at the beginning
    def startTime(self):
        self.beginTime = time()

    def endTime(self):
        self.timeElapsed = time() - self.beginTime
        return self.timeElapsed

    # Delaying functions
    def checkBright(self):

        done = 0;

        while done == 0:
            if (getObstacle('center') > 4000):
                speak("Alarm on")
                request = urllib2.Request(self.url + self.key)
                response = urllib2.urlopen(request)
                html = response.read()
                html = ast.literal_eval(html)
                self.startTime()
                beep(0.2, 880)
                beep(0.1, 880)
                beep(0.1, 880)
                return self.checkTimer(html)

    # Delaying functions
    def checkTimer(self, html):
        while True:
            beep(0.1, 1280)
            beep(0.1, 1280)
            beep(0.1, 1280)
            if(getObstacle('center') > 0):
                sleep(1)
                speak("Taking Picture")
                robotPic = RobotPic()
                robotPic.picTake("gray")
                robotPic = RobotPic(robotPic.filterGray(100, 100))
                robotPic.findSquares(120, 20, 10)
                code = robotPic.getCode(3)
                print code
                print html
                if code == html:
                    request = urllib2.Request("http://myro-robot.appspot.com/2?check=1")
                    response = urllib2.urlopen(request)
                    return True

            if (time() - self.beginTime >= 60):
                request = urllib2.Request("http://myro-robot.appspot.com/2?check=0")
                response = urllib2.urlopen(request)
                beep(3, 880)
                self.endTime()
                return False

    # When an interuder is found
    def intruder(self):
        while True:
            speak("Intruder")
            beep(0.3, 960)
            beep(0.3, 960)
            beep(0.3, 960)
            if(getObstacle('center') > 0):
                return True