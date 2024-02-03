import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        openAction = QAction(QIcon("open.png"), 'Open', self)
        openAction.triggered.connect(self.openFile)
        saveAction = QAction(QIcon("save.png"), 'Save', self)
        saveAction.triggered.connect(self.saveFile)
        fontAction= QAction(QIcon("font.png"), 'Font', self)
        fontAction.triggered.connect(self.changeFont)
        
        toolbar = self.addToolBar('Toolbar')
        toolbar.addAction(openAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(fontAction)

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)


    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", "", "(*.txt)")
        if fileName:
            with open(fileName, 'r') as file:
                data = file.read()
                self.textEdit.setPlainText(data)

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "(*.txt)")
        if fileName:
            with open(fileName, 'w') as file:
                text = self.textEdit.toPlainText()
                file.write(text)

    def changeFont(self):   
        font, ok = QFontDialog.getFont()
        if ok:
            self.textEdit.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())