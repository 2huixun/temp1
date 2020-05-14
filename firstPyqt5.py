import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Example(QMainWindow):
    def __init__(self,parent =None):
        super(Example,self).__init__(parent)
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage("Please see here.")
        self.setWindowTitle('good morning')
        self.initUI()
    def initUI(self):
        title = QLabel('Title')
        author =QLabel('Author')
        review =QLabel('Review')
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit =QTextEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title,1,0)
        grid.addWidget(titleEdit,1,1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1,5,1)

        self.setLayout(grid)
        self.show()
app =QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())