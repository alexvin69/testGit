
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *

import dbSQL
import sys, time


class QueryRunner(QThread):
    def __init__(self, query, parent=None):
        super(QueryRunner, self).__init__(parent)
        self.query = query
        return
    
    def run(self):
         dbSQL.query_get(self.query)

class test(): 
    def __init__(self, parent=None):
        self.db = QSqlDatabase.addDatabase('QODBC')
        self.db.setDatabaseName(dbSQL.connstr_get())
        self.db.open()
        # self.query = QSqlQuery(self.db)
        self.query = QSqlQuery("exec Stakan_Slice_Create @createOnly = 1 select * from Stakan_Slice", self.db)
        self.sql = "exec Stakan_Slice_Create @createOnly = 1 select * from Stakan_Slice"
        # self.query.prepare("exec Stakan_Slice_Create @createOnly = 1 select * from Stakan_Slice")

    def test1(self):
        self.query.exec_()
        self.showQueryResult()

    def test2(self):
        self.tr = QueryRunner(self.sql)
        self.tr.finished.connect(self.showQueryResult)
        self.tr.start()
        for i in range(0,100):
            print(str(i))
            time.sleep(1)

    def showQueryResult(self):
        print("----------------------")
        self.query.first()
        print(self.query.value(0))
        self.query.last()
        print(self.query.value(0))
        print("----------------------")


################################################################################
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    # Устанавливаем соединение с базой данных

    win = test()
    win.test2()

    # win.show()
    # sys.exit(app.exec_())



        