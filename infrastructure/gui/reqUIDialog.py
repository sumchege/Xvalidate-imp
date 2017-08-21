# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reqdialog.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReqDialog(object):
    def setupUi(self, ReqDialog):
        ReqDialog.setObjectName("ReqDialog")
        ReqDialog.resize(481, 461)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ReqDialog.sizePolicy().hasHeightForWidth())
        ReqDialog.setSizePolicy(sizePolicy)
        ReqDialog.setStyleSheet("#ReqDialog { background: rgba(32, 80, 96, 100); }\n"
"\n"
"#topPanel { background-color: qlineargradient(spread:reflect,\n"
"x1:0.5, y1:0, x2:0, y2:0, stop:0 rgba(91, 204, 233, 100),\n"
"stop:1 rgba(32, 80, 96, 100)); }\n"
"\n"
"#formWidget\n"
"{\n"
"background: rgba(0, 0, 0, 80);\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit { border-radius: 3px; }\n"
"QTextEdit { border-radius: 3px; }\n"
"QLabel { color: white; }\n"
"\n"
"")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ReqDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.topPanel = QtWidgets.QWidget(ReqDialog)
        self.topPanel.setObjectName("topPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.topPanel)
        self.verticalLayout.setContentsMargins(0, 31, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addWidget(self.topPanel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.formWidget = QtWidgets.QWidget(ReqDialog)
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.req_name = QtWidgets.QLineEdit(self.formWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.req_name.sizePolicy().hasHeightForWidth())
        self.req_name.setSizePolicy(sizePolicy)
        self.req_name.setMinimumSize(QtCore.QSize(0, 25))
        self.req_name.setText("")
        self.req_name.setObjectName("req_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.req_name)
        self.label_2 = QtWidgets.QLabel(self.formWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.req_type = QtWidgets.QComboBox(self.formWidget)
        self.req_type.setMinimumSize(QtCore.QSize(0, 25))
        self.req_type.setObjectName("req_type")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.req_type)
        self.label_3 = QtWidgets.QLabel(self.formWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.req_description = QtWidgets.QTextEdit(self.formWidget)
        self.req_description.setObjectName("req_description")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.req_description)
        self.verticalLayout_2.addWidget(self.formWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cancelButton = QtWidgets.QPushButton(ReqDialog)
        self.cancelButton.setMinimumSize(QtCore.QSize(0, 25))
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.saveButton = QtWidgets.QPushButton(ReqDialog)
        self.saveButton.setMinimumSize(QtCore.QSize(0, 25))
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)

        self.retranslateUi(ReqDialog)
        QtCore.QMetaObject.connectSlotsByName(ReqDialog)

    def retranslateUi(self, ReqDialog):
        _translate = QtCore.QCoreApplication.translate
        ReqDialog.setWindowTitle(_translate("ReqDialog", "Form"))
        self.label.setText(_translate("ReqDialog", "Name"))
        self.label_2.setText(_translate("ReqDialog", "Type"))
        self.label_3.setText(_translate("ReqDialog", "Description"))
        self.cancelButton.setText(_translate("ReqDialog", "Cancel"))
        self.saveButton.setText(_translate("ReqDialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ReqDialog = QtWidgets.QWidget()
    ui = Ui_ReqDialog()
    ui.setupUi(ReqDialog)
    ReqDialog.show()
    sys.exit(app.exec_())
