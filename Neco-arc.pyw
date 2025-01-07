from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random


class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.EndAlertAnim = None
        self.AlertAnim = None

        self.Alert = QLabel(self)
        self.Alert.setGeometry(0, 0, 300, 100)
        self.Alert.setStyleSheet("border-width: 5px; "
                                 "border-radius: 15px;"
                                 "border-style: inset;"
                                 "border-color: #f00 #27496D #27496D #f00;")
        self.Alert.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)

        self.font = QFont()
        self.font.setFamily("FangSong")
        self.font.setPointSize(15)
        self.font.setBold(True)
        self.font.setWeight(75)
        self.Alert.setFont(self.font)
        self.Alert.setAlignment(Qt.AlignCenter)

        self.setFixedSize(300, 100)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def AlertOffAnimation(self):
        self.Alert.setText("Disabled auto mode")
        self.Alert.setStyleSheet("border-width: 5px; "
                                 "border-radius: 15px;"
                                 "border-style: inset;"
                                 "border-color: #f00 #27496D #27496D #f00;"
                                 "color: white;")
        self.AlertAnim = QPropertyAnimation(self, b"pos")
        self.AlertAnim.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim.setStartValue(QPoint(QApplication.desktop().width(), QApplication.desktop().height() - 100))
        self.AlertAnim.setEndValue(QPoint(QApplication.desktop().width() - 500, QApplication.desktop().height() - 100))
        self.AlertAnim.setDuration(800)
        self.AlertAnim.start()
        QTimer.singleShot(1000, self.EndAnimationAlert)

    def AlertOnAnimation(self):
        self.Alert.setText("Enabled auto mode")
        self.Alert.setStyleSheet("border-width: 5px; "
                                 "border-radius: 15px;"
                                 "border-style: inset;"
                                 "border-color: #0f0 #27496D #27496D #0f0;"
                                 "color: white;")
        self.AlertAnim = QPropertyAnimation(self, b"pos")
        self.AlertAnim.setEasingCurve(QEasingCurve.OutCubic)
        self.AlertAnim.setStartValue(QPoint(QApplication.desktop().width(), QApplication.desktop().height() - 100))
        self.AlertAnim.setEndValue(QPoint(QApplication.desktop().width() - 500, QApplication.desktop().height() - 100))
        self.AlertAnim.setDuration(800)
        self.AlertAnim.start()
        QTimer.singleShot(1000, self.EndAnimationAlert)

    def EndAnimationAlert(self):
        self.EndAlertAnim = QPropertyAnimation(self, b"pos")
        self.EndAlertAnim.setEasingCurve(QEasingCurve.InCubic)
        self.EndAlertAnim.setStartValue(
            QPoint(QApplication.desktop().width() - 500, QApplication.desktop().height() - 100))
        self.EndAlertAnim.setEndValue(QPoint(QApplication.desktop().width(), QApplication.desktop().height() - 100))
        self.EndAlertAnim.setDuration(1000)
        self.EndAlertAnim.start()
        QTimer.singleShot(1000, lambda: alert.hide())


class Example(QMainWindow):
    def __init__(self, debug_mode: bool):
        super().__init__()

        self.time_dance = None
        self.DebugMode = debug_mode
        self.randgif = None
        self.step = 0
        self.waitingFlag = False
        self.NecoDanceFlag = False
        self.NecoDrink = False
        self.flag = False
        self.pathMovie = None

        self.dataDanceNecoGif = ["Gif/neco-arc-taunt2.gif", "Gif/necoarc-melty-blood2FastDanse.gif",
                                 "Gif/necoarc-melty-blood2.gif", "Gif/neco-arc-class2.gif", "Gif/neco-arc-dance 2.gif",
                                 "Gif/neco-arc-lumina2.gif", "Gif/neco-arc-melty-blood2.gif"]

        self.movie_screen = QLabel(self)
        self.movie_screen.setGeometry(200, 50, 250, 400)
        self.movie_screen.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(700, 600)

        if self.DebugMode:
            print("On debug mode")
            self.setStyleSheet("background-color: yellow;")

            self.movie_screen_debugText = QLabel(self)
            self.movie_screen_debugText.setGeometry(500, 10, 200, 50)
            self.movie_screen_debugText.setStyleSheet("background: green;")

            self.movie_screen_debugText2 = QLabel(self)
            self.movie_screen_debugText2.setGeometry(500, 60, 200, 50)
            self.movie_screen_debugText2.setStyleSheet("background: green;")

            self.movie_screen_debugText3 = QLabel(self)
            self.movie_screen_debugText3.setGeometry(500, 110, 200, 50)
            self.movie_screen_debugText3.setStyleSheet("background: green;")

            self.movie_screen_debugText4 = QLabel(self)
            self.movie_screen_debugText4.setGeometry(500, 160, 200, 50)
            self.movie_screen_debugText4.setStyleSheet("background: green;")

            self.movie_screen_debug = QLabel(self)
            self.movie_screen_debug.setGeometry(200, 50, 250, 400)
            self.movie_screen_debug.setStyleSheet("background: lightgreen;")

            self.opacity_effect = QGraphicsOpacityEffect()
            self.opacity_effect.setOpacity(0.5)
            self.movie_screen_debug.setGraphicsEffect(self.opacity_effect)

        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.MSWindowsFixedSizeDialogHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        self.movie_screen.setAttribute(Qt.WA_TranslucentBackground)
        self.movie_screen.setScaledContents(True)
        self.movie = QMovie("Gif/neco-arc-melty-blod2.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.oldPos = self.pos()
        self.pathMovie = self.movie.fileName()

    def randomNecoDance(self):
        if self.DebugMode:
            self.movie_screen_debugText4.setText(str(self.time_dance))
        self.time_dance += 1  # !!!
        if self.time_dance % 10 == 0:
            self.randgif = random.choice(self.dataDanceNecoGif)
            if self.randgif == "Gif/neco-arc-melty-blood2.gif" or self.randgif == "Gif/neco-arc-class2.gif" or self.randgif == "Gif/necoarc-melty-blood2.gif":

                if self.DebugMode:
                    self.movie_screen_debug.setGeometry(200, 50, 300, 400)

                self.movie_screen.setGeometry(200, 50, 300, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie(self.randgif)
                self.movie_screen.setMovie(self.movie)
                self.movie.start()

                self.pathMovie = self.movie.fileName()

            elif self.randgif == "Gif/neco-arc-lumina2.gif" or self.randgif == "Gif/neco-arc-dance 2.gif" or self.randgif == "Gif/neco-arc-taunt2.gif":

                if self.DebugMode:
                    self.movie_screen_debug.setGeometry(200, 50, 400, 400)

                self.movie_screen.setGeometry(200, 50, 400, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie(self.randgif)
                self.movie_screen.setMovie(self.movie)
                self.movie.start()

                self.pathMovie = self.movie.fileName()

            elif self.randgif == "Gif/necoarc-melty-blood2FastDanse.gif":

                if self.DebugMode:
                    self.movie_screen_debug.setGeometry(150, 50, 450, 400)

                self.movie_screen.setGeometry(150, 50, 450, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie(self.randgif)
                self.movie_screen.setMovie(self.movie)
                self.movie.start()

                self.pathMovie = self.movie.fileName()


    def waitingNecoTimer(self):
        self.waiting_timer += 1
        if self.DebugMode:
            self.movie_screen_debugText4.setText(str(self.waiting_timer))

        if self.waiting_timer == 30:
            self.movie_screen.setGeometry(200, 50, 250, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-phone.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()
        if self.waiting_timer == 50:
            self.movie_screen.setGeometry(200, 50, 250, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-melty-blod2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()
            self.waiting_timer = 0

    def drinkingNeco(self):

        if self.DebugMode:
            self.movie_screen_debug.setGeometry(165, 31, 335, 417)

        self.movie_screen.setGeometry(165, 31, 335, 417)
        self.movie_screen.setScaledContents(True)
        self.movie = QMovie("Gif/neco-arc-mbtl.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()

        self.pathMovie = self.movie.fileName()

    def keyPressEvent(self, event):
        key = event.key()

        if key:

            if self.waitingFlag:
                self.waiting.stop()
                self.waitingFlag = False
            if self.NecoDrink:
                self.drink.stop()

        if key == Qt.Key_Q:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 400)

            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-melty-blood2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_W:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 400, 400)

            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-lumina2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_E:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 400, 400)

            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-dance 2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_R:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 400)

            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-class2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            self.NecoDrink = True
            self.drink = QTimer()
            self.drink.timeout.connect(self.drinkingNeco)
            self.drink.setSingleShot(True)
            self.drink.start(3000)

        if key == Qt.Key_T:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 400)

            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/necoarc-melty-blood2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_Y:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 300)

            self.movie_screen.setGeometry(200, 50, 300, 300)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-neco2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_U:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 250, 400)

            self.movie_screen.setGeometry(200, 50, 250, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-melty-blod2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            if self.NecoDanceFlag:
                self.timerNecoDance.stop()
                self.NecoDanceFlag = False
                self.step = 0

            self.waitingFlag = True
            self.waiting = QTimer(self)
            self.waiting.timeout.connect(self.waitingNecoTimer)
            self.waiting.setInterval(1000)  # 1 sec
            self.waiting_timer = 0
            self.waiting.start()

        if key == Qt.Key_D:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 400, 400)

            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-taunt2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_A:

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 450, 400)

            self.movie_screen.setGeometry(150, 50, 450, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/necoarc-melty-blood2FastDanse.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

        if key == Qt.Key_Z:
            self.step += 1
            if self.step == 1:
                self.NecoDanceFlag = True
                alert.show()
                alert.AlertOnAnimation()
                self.timerNecoDance = QTimer(self)
                self.timerNecoDance.timeout.connect(self.randomNecoDance)
                self.timerNecoDance.setInterval(1000)  # 1 sec
                self.time_dance = 0
                self.timerNecoDance.start()
            if self.step == 2:
                self.NecoDanceFlag = False
                alert.show()
                alert.AlertOffAnimation()
                self.timerNecoDance.stop()
                self.step = 0

    def chose_size_widget(self):
        if self.pathMovie == "Gif/neco-arc-melty-blood2.gif" or self.pathMovie == "Gif/necoarc-melty-blood2.gif":

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 400)

            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie(self.pathMovie)
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 400)

        elif self.pathMovie == "Gif/neco-arc-lumina2.gif" or self.pathMovie == "Gif/neco-arc-dance 2.gif" or self.pathMovie == "Gif/neco-arc-taunt2.gif":

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 400, 400)

            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie(self.pathMovie)
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(200, 50, 300, 400)

        elif self.pathMovie == "Gif/necoarc-melty-blood2FastDanse.gif":

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(150, 50, 450, 400)

            self.movie_screen.setGeometry(150, 50, 450, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie(self.pathMovie)
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(150, 50, 350, 400)

        elif self.pathMovie == "Gif/neco-arc-melty-blod2.gif" or self.pathMovie == "Gif/neco-arc-phone.gif":  # анимация с таймером

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(150, 50, 250, 400)

            self.movie_screen.setGeometry(150, 50, 250, 400)
            self.movie_screen.setScaledContents(True)

            self.pathMovie = "Gif/neco-arc-melty-blod2.gif"  # для 2-х gif ставится одна

            self.movie = QMovie(self.pathMovie)
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(150, 50, 250, 400)

        elif self.pathMovie == "Gif/neco-arc-neco2.gif":

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(150, 50, 300, 300)

            self.movie_screen.setGeometry(150, 50, 300, 300)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie(self.pathMovie)
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

            self.pathMovie = self.movie.fileName()

            if self.DebugMode:
                self.movie_screen_debug.setGeometry(150, 50, 300, 400)

        elif self.pathMovie == "Gif/neco-arc-class2.gif" or self.pathMovie == "Gif/neco-arc-mbtl.gif":  # анимация с таймером
            self.drinkingNeco()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

        if self.DebugMode:
            self.movie_screen_debugText.setText(str(self.oldPos))

    def mouseReleaseEvent(self, event):
        print(self.pathMovie)
        if self.DebugMode:
            self.movie_screen_debugText2.setText(str(self.pathMovie))

        if self.flag:
            self.flag = False
            self.chose_size_widget()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        if delta.x() > 5 or delta.y() > 5 or delta.x() < -5 or delta.y() < -5:
            if not self.flag:
                print(delta)
                self.flag = True

                if self.DebugMode:
                    self.movie_screen_debug.setGeometry(100, 50, 350, 400)
                    self.movie_screen_debugText3.setText(f"{str(delta.x())},{str(delta.y())}")

                self.movie_screen.setGeometry(100, 50, 350, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie("Gif/neco-arc.gif")
                self.movie_screen.setMovie(self.movie)
                self.movie.start()

        self.oldPos = event.globalPos()


if __name__ == "__main__":
    qApp = QApplication([])
    app = Example(debug_mode=False)
    alert = Example2()
    app.show()
    qApp.exec()
