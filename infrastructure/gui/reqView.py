from PyQt5.QtWidgets import QWidget, QApplication
from reqUIView import Ui_ReqView
from reqDialog import ReqDialog

class ReqView(QWidget):
    def __init__(self):
        super(ReqView, self).__init__()
        
        self.ui = Ui_ReqView()
        self.ui.setupUi(self)
        
        self.ui.addButton.clicked.connect(self.add)
        self.ui.editButton.clicked.connect(self.edit)
        self.ui.deleteButton.clicked.connect(self.delete)
        
    
    def add(self):
        dialog = ReqDialog()
        dialog.setWindowTitle("Adding Requirement")
        dialog.exec_()
    
    def edit(self):
        print("Canceled")
    
    def delete(self):
        print("Deleted")
    

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    dia = ReqView()
    dia.show()
    sys.exit(app.exec_())
