import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets

import browser as ui


class MyBrowserApplication(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = ui.Ui_Browser()
        self.ui.setupUi(self)
        self.ui.urlBar.returnPressed.connect(self._load_page)

    def _load_page(self):
        url = QtCore.QUrl(self.ui.urlBar.text())
        self.ui.webView.setUrl(url)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyBrowserApplication()
    myapp.show()
    sys.exit(app.exec_())
