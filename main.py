#!/usr/bin/python

import sys, sqlite3

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore    import QCoreApplication, QSize, Qt

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class SoundBoard(QMainWindow):
    def __init__(self)
        super().__init__()
        self.title = 'Hell\'s Bells'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.load_db()

    def load_db():
        this.db = sqlite3.connect('hellsbells.db')
        this.db.row_factory = dict_factory

    def init_sound_grid(self, window):
        soundGrid = QGridLayout()

        # If no database tables exist, create them...
        cursor = this.db.cursor()
        cursor.execute('''
            CREATE IF NOT EXISTS bells.tabs (
                id INTEGER PRIMARY KEY,
                label VARCHAR(64),
                sortOrder INTEGER
                );
                
            CREATE IF NOT EXISTS bells.buttons (
                id INTEGER PRIMARY KEY,
                label VARCHAR(64),
                tabId INTEGER,
                row INTEGER,
                col INTEGER,
                file VARCHAR(1024)
                );
            ''');
        this.db.commit()

        # If no rows exist in the tabs table, create a default
        # tab...
        cursor.execute('SELECT COUNT(*) AS items FROM bells.tabs;')
        if cursor.fetchone()['items'] == 0:
            cursor.execute('''INSERT INTO tabs (label, sortOrder)
                                        VALUES ('Tab',1);'''
  
    def remove_all_tabs(self):
        while self.tabbar.count() > 0:
            self.tabbar.removeTab(0)
        
    def draw_sound_grid(self, window):
        self.remove_all_tabs()
        cursor = this.db.cursor()
        for row in cursor.execute("SELECT 
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sb = SoundBoard()
    sys.exit(app.exec_())
    
