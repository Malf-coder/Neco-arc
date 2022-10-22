from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random


class Example2(QWidget):
    def __init__(self):
        super().__init__()
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
        self.AlertAnim.setStartValue(QPoint(1900, 760))
        self.AlertAnim.setEndValue(QPoint(1140, 760))
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
        self.AlertAnim.setStartValue(QPoint(1900, 760))
        self.AlertAnim.setEndValue(QPoint(1140, 760))
        self.AlertAnim.setDuration(800)
        self.AlertAnim.start()
        QTimer.singleShot(1000, self.EndAnimationAlert)

    def EndAnimationAlert(self):
        self.EndAlertAnim = QPropertyAnimation(self, b"pos")
        self.EndAlertAnim.setEasingCurve(QEasingCurve.InCubic)
        self.EndAlertAnim.setStartValue(QPoint(1140, 760))
        self.EndAlertAnim.setEndValue(QPoint(1900, 760))
        self.EndAlertAnim.setDuration(1000)
        self.EndAlertAnim.start()
        QTimer.singleShot(1000, lambda: alert.hide())


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.step = 0

        self.dataGif = ["Gif/neco-arc-taunt2.gif", "Gif/necoarc-melty-blood2FastDanse.gif",
                        "Gif/necoarc-melty-blood2.gif", "Gif/neco-arc-class2.gif", "Gif/neco-arc-dance 2.gif",
                        "Gif/neco-arc-lumina2.gif", "Gif/neco-arc-melty-blood2.gif"]

        self.movie_screen = QLabel(self)
        self.movie_screen.setGeometry(200, 50, 250, 400)
        self.movie_screen.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(700, 700)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.movie_screen.setAttribute(Qt.WA_TranslucentBackground)
        self.movie_screen.setScaledContents(True)
        self.movie = QMovie("Gif/neco-arc-melty-blod2.gif")
        # self.movie = QMovie("Gif/neco-arc-laying-down.gif")
        self.movie_screen.setMovie(self.movie)
        self.movie.start()
        self.oldPos = self.pos()

    def showTime(self):
        # print(self.movie.fileName())
        print(self.time)
        self.time += 1  # !!!
        if self.time % 10 == 0:
            self.randgif = random.choice(self.dataGif)
            if self.randgif == "Gif/neco-arc-melty-blood2.gif" or self.randgif == "Gif/neco-arc-class2.gif" or self.randgif == "Gif/necoarc-melty-blood2.gif":
                self.movie_screen.setGeometry(200, 50, 300, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie(self.randgif)
                self.movie_screen.setMovie(self.movie)
                self.movie.start()
            elif self.randgif == "Gif/neco-arc-lumina2.gif" or self.randgif == "Gif/neco-arc-dance 2.gif" or self.randgif == "Gif/neco-arc-taunt2.gif":
                self.movie_screen.setGeometry(200, 50, 400, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie(self.randgif)
                self.movie_screen.setMovie(self.movie)
                self.movie.start()
            elif self.randgif == "Gif/necoarc-melty-blood2FastDanse.gif":
                self.movie_screen.setGeometry(150, 50, 450, 400)
                self.movie_screen.setScaledContents(True)
                self.movie = QMovie(self.randgif)
                self.movie_screen.setMovie(self.movie)
                self.movie.start()
            print("ok")

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Q:
            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-melty-blood2.gif")
            # self.movie = QMovie("Gif/neco-arc-dance.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_W:
            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-lumina2.gif")
            # self.movie = QMovie("Gif/cute-neko.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_E:
            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-dance 2.gif")
            # self.movie = QMovie("Gif/tsukihime-anime.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_R:
            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-class2.gif")
            # self.movie = QMovie("Gif/breakdance-neco-arc.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_T:
            self.movie_screen.setGeometry(200, 50, 300, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/necoarc-melty-blood2.gif")
            # self.movie = QMovie("Gif/neco-arc-laying-down.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_Y:
            self.movie_screen.setGeometry(200, 50, 300, 300)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-neco2.gif")
            # self.movie = QMovie("Gif/neco-arc-laying-down.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_U:
            self.movie_screen.setGeometry(200, 50, 250, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-melty-blod2.gif")
            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_D:
            self.movie_screen.setGeometry(200, 50, 400, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/neco-arc-taunt2.gif")

            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_A:
            self.movie_screen.setGeometry(150, 50, 450, 400)
            self.movie_screen.setScaledContents(True)
            self.movie = QMovie("Gif/necoarc-melty-blood2FastDanse.gif")

            self.movie_screen.setMovie(self.movie)
            self.movie.start()

        if key == Qt.Key_Z:
            self.step += 1
            if self.step == 1:
                alert.show()
                alert.AlertOnAnimation()
                self.timer = QTimer(self)
                self.timer.timeout.connect(self.showTime)
                self.timer.setInterval(1000)  # 1 sec
                self.time = 0
                self.timer.start()
            if self.step == 2:
                alert.show()
                alert.AlertOffAnimation()
                self.timer.stop()
                self.step = 0

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    qApp = QApplication([])
    app = Example()
    alert = Example2()
    app.show()
    qApp.exec()
