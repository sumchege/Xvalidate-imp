from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from reqUIDialog import Ui_ReqDialog

class ReqDialog(QDialog):
    def __init__(self):
        super(ReqDialog, self).__init__()
        
        self.ui = Ui_ReqDialog()
        self.ui.setupUi(self)
        
        self.ui.saveButton.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.cancel)
    
    def save(self):
        print("Saving")
    
    def cancel(self):
        print("Canceled")
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dia = ReqDialog()
    dia.show()
    sys.exit(app.exec_())
