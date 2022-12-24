import random
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QDialog, QMessageBox

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()
        self.model = QSqlTableModel(self, db)
        self.model.setTable('coffee')
        self.model.select()
        self.tableView.setModel(self.model)
        self.pushButton.clicked.connect(self.add_row)

    def add_row(self):
        inputDialog = Dialog()
        rez = inputDialog.exec()
        if not rez:
            QMessageBox.information(self, 'Внимание', 'Диалог сброшен.')
            return
        a = inputDialog.lineEdit.text()
        b = inputDialog.lineEdit_2.text()
        c = inputDialog.lineEdit_3.text()
        d = inputDialog.lineEdit_4.text()
        e = inputDialog.lineEdit_5.text()
        f = inputDialog.lineEdit_6.text()
        r = self.model.record()
        r.setValue("sort", a)
        r.setValue("objarka", b)
        r.setValue("type", c)
        r.setValue("vkus", d)
        r.setValue("cost", e)
        r.setValue("size", f)
        self.model.insertRecord(-1, r)
        self.model.select()


class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
