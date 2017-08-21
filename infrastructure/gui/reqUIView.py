# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReqView(object):
    def setupUi(self, ReqView):
        ReqView.setObjectName("ReqView")
        ReqView.resize(715, 460)
        ReqView.setStyleSheet("#ReqView { background: rgba(32, 80, 96, 100); }\n"
"\n"
"#topPanel { background-color: qlineargradient(spread:reflect,\n"
"x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100),\n"
"stop:1 rgba(32, 80, 96, 100)); }\n"
"\n"
"\n"
"\n"
"QLineEdit { border-radius: 3px; }\n"
"QTextEdit { border-radius: 3px; }\n"
"QLabel { color: white; }\n"
"\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(ReqView)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.topPanel = QtWidgets.QWidget(ReqView)
        self.topPanel.setObjectName("topPanel")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topPanel)
        self.verticalLayout_2.setContentsMargins(0, 17, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3.addWidget(self.topPanel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableView = QtWidgets.QTableView(ReqView)
        self.tableView.setObjectName("tableView")
        self.horizontalLayout.addWidget(self.tableView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QtWidgets.QPushButton(ReqView)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(ReqView)
        self.editButton.setObjectName("editButton")
        self.verticalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(ReqView)
        self.deleteButton.setObjectName("deleteButton")
        self.verticalLayout.addWidget(self.deleteButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalWidget_2 = QtWidgets.QWidget(ReqView)
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 23, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3.addWidget(self.horizontalWidget_2)

        self.retranslateUi(ReqView)
        QtCore.QMetaObject.connectSlotsByName(ReqView)

    def retranslateUi(self, ReqView):
        _translate = QtCore.QCoreApplication.translate
        ReqView.setWindowTitle(_translate("ReqView", "Form"))
        self.addButton.setText(_translate("ReqView", "Add"))
        self.editButton.setText(_translate("ReqView", "Edit"))
        self.deleteButton.setText(_translate("ReqView", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReqView = QtWidgets.QWidget()
    ui = Ui_ReqView()
    ui.setupUi(ReqView)
    ReqView.show()
    sys.exit(app.exec_())
