# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Users\unhealthy\Documents\GitHub\myClientPyQt\LoginWidgetQt.ui'
#
# Created: Sun Mar  3 17:22:48 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        loginDialog.setObjectName(_fromUtf8("loginDialog"))
        loginDialog.resize(330, 180)
        loginDialog.setMinimumSize(QtCore.QSize(330, 180))
        loginDialog.setMaximumSize(QtCore.QSize(330, 180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("src/logo_school.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        loginDialog.setWindowIcon(icon)
        loginDialog.setAutoFillBackground(False)
        loginDialog.setSizeGripEnabled(False)
        loginDialog.setModal(False)
        self.frame = QtGui.QFrame(loginDialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 330, 180))
        self.frame.setMinimumSize(QtCore.QSize(330, 180))
        self.frame.setFrameShape(QtGui.QFrame.Box)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(2)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.stackedWidget = QtGui.QStackedWidget(self.frame)
        self.stackedWidget.setGeometry(QtCore.QRect(1, 1, 328, 178))
        self.stackedWidget.setMinimumSize(QtCore.QSize(328, 178))
        self.stackedWidget.setMaximumSize(QtCore.QSize(328, 178))
        self.stackedWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.stackedWidget.setFrameShape(QtGui.QFrame.Box)
        self.stackedWidget.setFrameShadow(QtGui.QFrame.Sunken)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page.sizePolicy().hasHeightForWidth())
        self.page.setSizePolicy(sizePolicy)
        self.page.setMinimumSize(QtCore.QSize(330, 180))
        self.page.setMaximumSize(QtCore.QSize(330, 180))
        self.page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.page.setObjectName(_fromUtf8("page"))
        self.LoginTitleabel = QtGui.QLabel(self.page)
        self.LoginTitleabel.setGeometry(QtCore.QRect(1, 11, 332, 41))
        self.LoginTitleabel.setMinimumSize(QtCore.QSize(332, 41))
        self.LoginTitleabel.setMaximumSize(QtCore.QSize(332, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(22)
        font.setItalic(False)
        self.LoginTitleabel.setFont(font)
        self.LoginTitleabel.setScaledContents(False)
        self.LoginTitleabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LoginTitleabel.setObjectName(_fromUtf8("LoginTitleabel"))
        self.userNamelabel = QtGui.QLabel(self.page)
        self.userNamelabel.setGeometry(QtCore.QRect(60, 60, 48, 22))
        self.userNamelabel.setMinimumSize(QtCore.QSize(48, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userNamelabel.setFont(font)
        self.userNamelabel.setObjectName(_fromUtf8("userNamelabel"))
        self.userCodelabel = QtGui.QLabel(self.page)
        self.userCodelabel.setGeometry(QtCore.QRect(60, 100, 32, 22))
        self.userCodelabel.setMinimumSize(QtCore.QSize(32, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.userCodelabel.setFont(font)
        self.userCodelabel.setObjectName(_fromUtf8("userCodelabel"))
        self.userNameLineEdit = QtGui.QLineEdit(self.page)
        self.userNameLineEdit.setGeometry(QtCore.QRect(130, 60, 140, 22))
        self.userNameLineEdit.setMinimumSize(QtCore.QSize(140, 22))
        self.userNameLineEdit.setMaximumSize(QtCore.QSize(140, 22))
        self.userNameLineEdit.setObjectName(_fromUtf8("userNameLineEdit"))
        self.quitButton = QtGui.QPushButton(self.page)
        self.quitButton.setGeometry(QtCore.QRect(180, 139, 75, 27))
        self.quitButton.setMinimumSize(QtCore.QSize(75, 27))
        self.quitButton.setMaximumSize(QtCore.QSize(75, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName(_fromUtf8("quitButton"))
        self.loginButton = QtGui.QPushButton(self.page)
        self.loginButton.setGeometry(QtCore.QRect(100, 139, 75, 27))
        self.loginButton.setMinimumSize(QtCore.QSize(75, 27))
        self.loginButton.setMaximumSize(QtCore.QSize(75, 27))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.loginButton.setFont(font)
        self.loginButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.userCodeLineEdit = QtGui.QLineEdit(self.page)
        self.userCodeLineEdit.setGeometry(QtCore.QRect(130, 100, 140, 22))
        self.userCodeLineEdit.setMinimumSize(QtCore.QSize(140, 22))
        self.userCodeLineEdit.setMaximumSize(QtCore.QSize(140, 22))
        self.userCodeLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.userCodeLineEdit.setObjectName(_fromUtf8("userCodeLineEdit"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.page_2.sizePolicy().hasHeightForWidth())
        self.page_2.setSizePolicy(sizePolicy)
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.progressBar = QtGui.QProgressBar(self.page_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 140, 281, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(10, 60, 301, 52))
        self.label.setMinimumSize(QtCore.QSize(301, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.loadingQuitButton = QtGui.QToolButton(self.page_2)
        self.loadingQuitButton.setGeometry(QtCore.QRect(290, 0, 31, 21))
        self.loadingQuitButton.setObjectName(_fromUtf8("loadingQuitButton"))
        self.stackedWidget.addWidget(self.page_2)
        self.userNamelabel.setBuddy(self.userNameLineEdit)
        self.userCodelabel.setBuddy(self.userCodeLineEdit)

        self.retranslateUi(loginDialog)
        QtCore.QObject.connect(self.quitButton, QtCore.SIGNAL(_fromUtf8("clicked()")), loginDialog.close)
        QtCore.QMetaObject.connectSlotsByName(loginDialog)
        loginDialog.setTabOrder(self.userNameLineEdit, self.userCodeLineEdit)
        loginDialog.setTabOrder(self.userCodeLineEdit, self.loginButton)
        loginDialog.setTabOrder(self.loginButton, self.quitButton)
        loginDialog.setTabOrder(self.quitButton, self.loadingQuitButton)

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(_translate("loginDialog", "登陆", None))
        self.LoginTitleabel.setText(_translate("loginDialog", "绝望2005第三方登陆器", None))
        self.userNamelabel.setText(_translate("loginDialog", "用户名", None))
        self.userCodelabel.setText(_translate("loginDialog", "密码", None))
        self.quitButton.setText(_translate("loginDialog", "退出", None))
        self.loginButton.setText(_translate("loginDialog", "登陆", None))
        self.label.setText(_translate("loginDialog", "Loading...", None))
        self.loadingQuitButton.setText(_translate("loginDialog", "X", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    loginDialog = QtGui.QDialog()
    ui = Ui_loginDialog()
    ui.setupUi(loginDialog)
    loginDialog.show()
    sys.exit(app.exec_())

