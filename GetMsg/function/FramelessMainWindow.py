import sys

import qtawesome
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QPainter, QPen, QColor, QEnterEvent, QIcon, QBrush, QPixmap, QPalette
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QDesktopWidget, QSystemTrayIcon, QAction, QMenu, QMessageBox

from function.MainWindow import UI_MainWindow
from function.TitleBar import UI_TitleBar

Left, Top, Right, Bottom, LeftTop, RightTop, LeftBottom, RightBottom = range(8)

class FramelessMainWindow(QWidget):

    Margins = 5

    def __init__(self, mailusr,clisock):
        super(FramelessMainWindow, self).__init__()
        # self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        layout = QVBoxLayout(self, spacing=0)
        layout.setContentsMargins(self.Margins, self.Margins, self.Margins, self.Margins)
        self.titlebar = UI_TitleBar()
        self.mainwindow = UI_MainWindow(mailusr, clisock)
        # self.mainwindow.install
        layout.addWidget(self.titlebar)
        self.setWidget(self.mainwindow)
        self.setBackgroundPicture()
        self.connectButtons()
        self.titlebar.windowMoved.connect(self.move)
        self.titlebar.windowNormaled.connect(self.windowRestore)
        self.titlebar.windowMaximumed.connect(self.windowMaximum)
        self.mainwindow.signOut.connect(self.quitApp)
        self.systemTrayIconInitial()
        self.setMinimumSize(1000, 600)

    def systemTrayIconInitial(self):
        # 在系统托盘处显示图标
        self.tray = QSystemTrayIcon(self)
        self.tray.setIcon(QIcon('timg.jpg'))
        self.tray.show()
        # 设置系统托盘图标的菜单
        # 设定显示和退出两个选项
        self.op1 = QAction('&显示(Show)', triggered=self.show)
        self.op2 = QAction('&退出(Exit)', triggered=self.quitApp)

        # 创建菜单并添加选项
        self.trayMenu = QMenu()
        self.trayMenu.addAction(self.op1)
        self.trayMenu.addAction(self.op2)
        self.tray.setContextMenu(self.trayMenu)

        # 设置后台运行时的提示信息
        self.tray.showMessage('九龙湖邮管', '已在后台运行', icon=0)
        # 鼠标双击点击或左键单击点击会唤出主界面
        self.tray.activated.connect(self.act)

        # 退出程序
    def quitApp(self):
        self.show()  # w.hide() #隐藏
        re = QMessageBox.question(self, "提示", "退出系统", QMessageBox.Yes |
                                      QMessageBox.No, QMessageBox.No)
        if re == QMessageBox.Yes:
            # 关闭窗体程序
            QCoreApplication.instance().quit()
            # 在应用程序全部关闭后，TrayIcon其实还不会自动消失，
            # 直到你的鼠标移动到上面去后，才会消失，
            # 这是个问题，（如同你terminate一些带TrayIcon的应用程序时出现的状况），
            # 这种问题的解决我是通过在程序退出前将其setVisible(False)来完成的。
            self.tray.setVisible(False)

    def act(self, reason):
        # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def connectButtons(self):
        self.titlebar.closewidget.clicked.connect(self.hide)
        self.titlebar.minimum.clicked.connect(self.showMinimized)
        self.titlebar.maximum.clicked.connect(self.windowMaximum)

    def windowMaximum(self):
        self.showMaximized()
        self.titlebar.maximum.setIcon(qtawesome.icon("fa5.window-restore", color="black"))
        self.titlebar.maximum.clicked.disconnect(self.windowMaximum)
        self.titlebar.maximum.clicked.connect(self.windowRestore)

    def windowRestore(self):
        self.showNormal()
        self.titlebar.maximum.setIcon(qtawesome.icon("fa5.window-maximize", color="black"))
        self.titlebar.maximum.clicked.disconnect(self.windowRestore)
        self.titlebar.maximum.clicked.connect(self.windowMaximum)

    def showCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setBackgroundPicture(self):
        palette = self.palette()
        palette.setBrush(self.backgroundRole(), QBrush(QPixmap("background.jpg")))
        self.setPalette(palette)

    def resizeEvent(self, event):
        palette = QPalette()
        pix = QPixmap("background.jpg")
        pix = pix.scaled(self.width(), self.height())
        palette.setBrush(QPalette.Background, QBrush(pix))
        self.setPalette(palette)

    def setWidget(self, widget):
        """设置自己的控件"""
        if hasattr(self, '_widget'):
            return
        # self._widget = widget
        # 设置默认背景颜色,否则由于受到父窗口的影响导致透明
        # self._widget.setAutoFillBackground(True)
        # palette = self._widget.palette()
        # palette.setColor(palette.Window, QColor(240, 240, 240))
        # self._widget.setPalette(palette)
        # self._widget.installEventFilter(self)
        widget.installEventFilter(self)
        self.layout().addWidget(widget)

    def move(self, pos):
        if self.windowState() == Qt.WindowMaximized or self.windowState() == Qt.WindowFullScreen:
            # 最大化或者全屏则不允许移动
            return
        super(FramelessMainWindow, self).move(pos)

    def showMaximized(self):
        """最大化,要去除上下左右边界,如果不去除则边框地方会有空隙"""
        super(FramelessMainWindow, self).showMaximized()
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.titlebar.maxOrNormal = False

    def showNormal(self):
        """还原,要保留上下左右边界,否则没有边框无法调整"""
        super(FramelessMainWindow, self).showNormal()
        self.showCenter()
        self.layout().setContentsMargins(self.Margins, self.Margins, self.Margins, self.Margins)
        self.titlebar.maxOrNormal = True

    def eventFilter(self, obj, event):
        """事件过滤器,用于解决鼠标进入其它控件后还原为标准鼠标样式"""
        if isinstance(event, QEnterEvent):
            self.setCursor(Qt.ArrowCursor)
            return True
        return super(FramelessMainWindow, self).eventFilter(obj, event)

    def paintEvent(self, event):
        """由于是全透明背景窗口,重绘事件中绘制透明度为1的难以发现的边框,用于调整窗口大小"""
        super(FramelessMainWindow, self).paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(255, 255, 255, 1), 2 * self.Margins))
        painter.drawRect(self.rect())

    def mousePressEvent(self, event):
        """鼠标点击事件"""
        super(FramelessMainWindow, self).mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self._mpos = event.pos()
            self._pressed = True

    def mouseReleaseEvent(self, event):
        '''鼠标弹起事件'''
        super(FramelessMainWindow, self).mouseReleaseEvent(event)
        self._pressed = False
        self.Direction = None

    def mouseMoveEvent(self, event):
        """鼠标移动事件"""
        super(FramelessMainWindow, self).mouseMoveEvent(event)
        pos = event.pos()
        xPos, yPos = pos.x(), pos.y()
        wm, hm = self.width() - self.Margins, self.height() - self.Margins
        if self.isMaximized() or self.isFullScreen():
            self.Direction = None
            self.setCursor(Qt.ArrowCursor)
            return
        if event.buttons() == Qt.LeftButton and self._pressed:
            self._resizeWidget(pos)
            return
        if xPos <= self.Margins and yPos <= self.Margins:
            # 左上角
            self.Direction = LeftTop
            self.setCursor(Qt.SizeFDiagCursor)
        elif wm <= xPos <= self.width() and hm <= yPos <= self.height():
            # 右下角
            self.Direction = RightBottom
            self.setCursor(Qt.SizeFDiagCursor)
        elif wm <= xPos and yPos <= self.Margins:
            # 右上角
            self.Direction = RightTop
            self.setCursor(Qt.SizeBDiagCursor)
        elif xPos <= self.Margins and hm <= yPos:
            # 左下角
            self.Direction = LeftBottom
            self.setCursor(Qt.SizeBDiagCursor)
        elif 0 <= xPos <= self.Margins and self.Margins <= yPos <= hm:
            # 左边
            self.Direction = Left
            self.setCursor(Qt.SizeHorCursor)
        elif wm <= xPos <= self.width() and self.Margins <= yPos <= hm:
             # 右边
            self.Direction = Right
            self.setCursor(Qt.SizeHorCursor)
        elif self.Margins <= xPos <= wm and 0 <= yPos <= self.Margins:
            # 上面
            self.Direction = Top
            self.setCursor(Qt.SizeVerCursor)
        elif self.Margins <= xPos <= wm and hm <= yPos <= self.height():
            # 下面
            self.Direction = Bottom
            self.setCursor(Qt.SizeVerCursor)

    def _resizeWidget(self, pos):
        """调整窗口大小"""
        if self.Direction == None:
            return
        mpos = pos - self._mpos
        xPos, yPos = mpos.x(), mpos.y()
        geometry = self.geometry()
        x, y, w, h = geometry.x(), geometry.y(), geometry.width(), geometry.height()
        if self.Direction == LeftTop:  # 左上角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
        elif self.Direction == RightBottom:  # 右下角
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
        elif self.Direction == RightTop:  # 右上角
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos.setX(pos.x())
        elif self.Direction == LeftBottom:  # 左下角
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos.setY(pos.y())
        elif self.Direction == Left:  # 左边
            if w - xPos > self.minimumWidth():
                x += xPos
                w -= xPos
            else:
                return
        elif self.Direction == Right:  # 右边
            if w + xPos > self.minimumWidth():
                w += xPos
                self._mpos = pos
            else:
                return
        elif self.Direction == Top:  # 上面
            if h - yPos > self.minimumHeight():
                y += yPos
                h -= yPos
            else:
                return
        elif self.Direction == Bottom:  # 下面
            if h + yPos > self.minimumHeight():
                h += yPos
                self._mpos = pos
            else:
                return
        self.setGeometry(x, y, w, h)

    def getmainwindow(self):
        return self.mainwindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    # app.setStyleSheet(StyleSheet)
    mainWnd = FramelessMainWindow()
    # mainWnd.setWindowTitle('测试标题栏')
    # mainWnd.setWindowIcon(QIcon('Qt.ico'))
    mainWnd.resize(QSize(1250,780))
    mainWnd.setWidget(UI_MainWindow())  # 把自己的窗口添加进来
    mainWnd.show()
    #
    # a = TitleBar()
    # a.show()
    sys.exit(app.exec_())