# import sys
# from PyQt5 import QtWidgets, QtGui, QtCore

# class GUI(QtWidgets.QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         # Set background color
#         self.setAutoFillBackground(True)
#         p = self.palette()
#         p.setColor(self.backgroundRole(), QtGui.QColor(0, 0, 0))
#         self.setPalette(p)

#         # Set GIF
#         movie = QtGui.QMovie("audio_gif.gif")
#         movie.setScaledSize(QtCore.QSize(1366, 720))
#         movie.start()

#         label = QtWidgets.QLabel(self)
#         label.setMovie(movie)
#         label.setAlignment(QtCore.Qt.AlignCenter)
#         self.setCentralWidget(label)

#         self.show()

#     def keyPressEvent(self, event):
#         if event.modifiers() == QtCore.Qt.WindowMaximized and event.key() == QtCore.Qt.Key_Up:
#             # Set window size to half of screen size
#             screen_size = QtWidgets.QDesktopWidget().screenGeometry()
#             self.setGeometry(0, 0, screen_size.width() // 2, screen_size.height() // 2)
#         else:
#             super().keyPressEvent(event)
       

#     def closeEvent(self, event):
#         # End program when GUI is closed
#         QtWidgets.QApplication.quit()

# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     gui = GUI()
    
#     sys.exit(app.exec_())








import sys
from PyQt5 import QtWidgets, QtGui, QtCore


class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set full screen
        self.setWindowState(QtCore.Qt.WindowFullScreen)

        # Set background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QtGui.QColor(0, 0, 0))
        self.setPalette(p)

        # Set GIF
        movie = QtGui.QMovie("audio_gif.gif")
        movie.setScaledSize(QtCore.QSize(1366, 720))
        movie.start()

        label = QtWidgets.QLabel(self)
        label.setMovie(movie)
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.setCentralWidget(label)

        self.show()

    def closeEvent(self, event):
        # End program when GUI is closed
        QtWidgets.QApplication.quit()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = GUI()
    sys.exit(app.exec_())
