from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtGui import QPixmap
from PIL import Image
from random import randint
from PyQt5.QtCore import Qt
import subprocess


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


def scale_image(self):
    image = Image.open(self.background)
    width, height = X, Y
    image = image.resize((width, height))
    image.save(self.background)


class Building(QWidget):
    def __init__(self, id):
        super().__init__()
        self.main = QVBoxLayout()
        self.setStyleSheet('.Building {background-image: url(text.png);}')
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        building = cursor.execute("SELECT * FROM `buildings` WHERE `id` = ?", (id,)).fetchall()[0]

        self.row = QHBoxLayout()
        self.txt = QLabel()
        self.txt.setText(building[2])
        self.txt.setFont(QtGui.QFont("Arial", 40, QtGui.QFont.Bold))
        self.txt.adjustSize()
        self.image = QLabel()
        self.image.setPixmap(QPixmap("buildings/" + building[4] + ".jpg"))
        self.row.addWidget(self.txt)
        self.row.addWidget(self.image)

        self.info = QVBoxLayout()

        text = building[3].split("\\n")
        for elem in text:
            label = QLabel(elem)
            self.info.addWidget(label)

        self.main.addLayout(self.row)
        self.main.addLayout(self.info)
        self.setLayout(self.main)


class Buildings(QWidget):
    def __init__(self, id_fraction):
        super().__init__()

        self.setStyleSheet("""
                .QPushButton{
                    background-color: #403a3a;
                    color: white;
                    font-size: 23px;
                    border-radius: 5px;
                }
                .QPushButton:hover{
                    background-color: #5c5353;
                }
                .QLabel{
                font-size: 30px;
                }""")

        # БД
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        buildings = cursor.execute("SELECT * FROM `buildings` WHERE `id_fraction` = ?", (id_fraction,)).fetchall()

        self.main = QVBoxLayout()

        self.btns = QVBoxLayout()
        for building in buildings:
            btn = QPushButton()
            btn.setText(building[2])
            btn.clicked.connect(self.handler)
            self.btns.addWidget(btn)

        self.txt = QLabel()
        self.txt.setText("Постройки")
        self.txt.setAlignment(Qt.AlignCenter)

        self.main.addWidget(self.txt)
        self.main.addLayout(self.btns)

        self.setLayout(self.main)

    def handler(self):
        name = self.sender().text()
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        id = cursor.execute("SELECT `id` FROM `buildings` WHERE `name` = ?", (name,)).fetchall()[0][0]
        self.building = Building(id)
        self.building.showMaximized()


class Spell(QWidget):
    def __init__(self, id):
        super().__init__()
        self.main = QVBoxLayout()

        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        spell = cursor.execute("SELECT * FROM `spells` WHERE `id` = ?", (id,)).fetchall()[0]

        self.row = QHBoxLayout()
        self.txt = QLabel()
        self.txt.setText(spell[2])
        self.txt.setFont(QtGui.QFont("Arial", 40, QtGui.QFont.Bold))
        self.txt.adjustSize()
        self.image = QLabel()
        self.image.setPixmap(QPixmap("spells/" + spell[4] + ".jpg"))
        self.row.addWidget(self.txt)
        self.row.addWidget(self.image)

        self.info = QVBoxLayout()

        text = spell[3].split("\\n")
        for elem in text:
            label = QLabel(elem)
            self.info.addWidget(label)

        self.main.addLayout(self.row)
        self.main.addLayout(self.info)
        self.setLayout(self.main)


class Spells(QWidget):
    def __init__(self, id_fraction):
        super().__init__()

        self.setStyleSheet("""
                .QPushButton{
                    background-color: #403a3a;
                    color: white;
                    font-size: 23px;
                    border-radius: 5px;
                }
                .QPushButton:hover{
                    background-color: #5c5353;
                }
                .QLabel{
                font-size: 30px;
                }""")

        # БД
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        spells = cursor.execute("SELECT * FROM `spells` WHERE `id_fraction` = ?", (id_fraction,)).fetchall()

        self.main = QVBoxLayout()

        self.btns = QVBoxLayout()
        for spell in spells:
            btn = QPushButton()
            btn.setText(spell[2])
            btn.clicked.connect(self.handler)
            self.btns.addWidget(btn)

        self.txt = QLabel()
        self.txt.setText("Заклинания")
        self.txt.setAlignment(Qt.AlignCenter)

        self.main.addWidget(self.txt)
        self.main.addLayout(self.btns)

        self.setLayout(self.main)

    def handler(self):
        name = self.sender().text()
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        id = cursor.execute("SELECT `id` FROM `spells` WHERE `name` = ?", (name,)).fetchall()[0][0]
        self.spell = Spell(id)
        self.spell.show()


class Army(QWidget):
    def __init__(self, id):
        super().__init__()
        self.main = QVBoxLayout()

        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        army = cursor.execute("SELECT * FROM `armies` WHERE `id` = ?", (id,)).fetchall()[0]

        self.row = QHBoxLayout()
        self.txt = QLabel()
        self.txt.setText(army[2])
        self.txt.setFont(QtGui.QFont("Arial", 40, QtGui.QFont.Bold))
        self.txt.adjustSize()
        self.image = QLabel()
        self.image.setPixmap(QPixmap("armies/" + army[4] + ".jpg"))
        self.row.addWidget(self.txt)
        self.row.addWidget(self.image)

        self.info = QVBoxLayout()

        text = army[3].split("\\n")
        for elem in text:
            label = QLabel(elem)
            self.info.addWidget(label)

        self.main.addLayout(self.row)
        self.main.addLayout(self.info)
        self.setLayout(self.main)


class Armies(QWidget):
    def __init__(self, id_fraction):
        super().__init__()

        self.setStyleSheet("""
                .QPushButton{
                    background-color: #403a3a;
                    color: white;
                    font-size: 23px;
                    border-radius: 5px;
                }
                .QPushButton:hover{
                    background-color: #5c5353;
                }
                .QLabel{
                font-size: 30px;
                }""")

        # БД
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        armies = cursor.execute("SELECT * FROM `armies` WHERE `id_fraction` = ?", (id_fraction,)).fetchall()

        self.main = QVBoxLayout()

        self.btns = QVBoxLayout()
        for army in armies:
            btn = QPushButton()
            btn.setText(army[2])
            btn.clicked.connect(self.handler)
            self.btns.addWidget(btn)

        self.txt = QLabel()
        self.txt.setText("Войска")
        self.txt.setAlignment(Qt.AlignCenter)

        self.main.addWidget(self.txt)
        self.main.addLayout(self.btns)

        self.setLayout(self.main)

    def handler(self):
        name = self.sender().text()
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        id = cursor.execute("SELECT `id` FROM `armies` WHERE `name` = ?", (name,)).fetchall()[0][0]
        self.army = Army(id)
        self.army.show()


class Hero(QWidget):
    def __init__(self, id):
        super().__init__()
        self.main = QVBoxLayout()

        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        hero = cursor.execute("SELECT * FROM `heroes` WHERE `id` = ?", (id,)).fetchall()[0]

        self.row = QHBoxLayout()
        self.txt = QLabel()
        self.txt.setText(hero[2])
        self.txt.setFont(QtGui.QFont("Arial", 40, QtGui.QFont.Bold))
        self.txt.adjustSize()
        self.image = QLabel()
        self.image.setPixmap(QPixmap("heroes/" + hero[4] + ".jpg"))
        self.row.addWidget(self.txt)
        self.row.addWidget(self.image)

        self.info = QVBoxLayout()

        text = hero[3].split("\\n")
        for elem in text:
            label = QLabel(elem)
            self.info.addWidget(label)

        self.main.addLayout(self.row)
        self.main.addLayout(self.info)
        self.setLayout(self.main)


class Heroes(QWidget):
    def __init__(self, id_fraction):
        super().__init__()

        self.setStyleSheet("""
                .QPushButton{
                    background-color: #403a3a;
                    color: white;
                    font-size: 23px;
                    border-radius: 5px;
                }
                .QPushButton:hover{
                    background-color: #5c5353;
                }
                .QLabel{
                    font-size: 30px;
                }
                """)

        # БД
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        heroes = cursor.execute("SELECT * FROM `heroes` WHERE `id_fraction` = ?", (id_fraction,)).fetchall()

        self.main = QVBoxLayout()

        self.btns = QVBoxLayout()
        for hero in heroes:
            btn = QPushButton()
            btn.setText(hero[2])
            btn.clicked.connect(self.handler)
            self.btns.addWidget(btn)

        self.txt = QLabel()
        self.txt.setText("Герои")
        self.txt.setAlignment(Qt.AlignCenter)

        self.main.addWidget(self.txt)
        self.main.addLayout(self.btns)

        self.setLayout(self.main)

    def handler(self):
        name = self.sender().text()
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        id = cursor.execute("SELECT `id` FROM `heroes` WHERE `name` = ?", (name,)).fetchall()[0][0]
        self.hero = Hero(id)
        self.hero.show()


class MenuProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выберите картинку")
        self.main = QVBoxLayout()
        self.btn_image = QPushButton("Выбрать фоновое изображение")
        self.main.addWidget(self.btn_image)
        self.setLayout(self.main)


class Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
                .QPushButton {
                    cursor: pointer;
                    background: url(buttons/butt2.png);vs
                    width: 230px; height: 60px;
                    background-repeat: no-repeat;
                    display: flex;
                    background-color: none;
                    border: none;
                    transition: all 0.2s;
                    color: white;
                    font-size: 23px;
                    font-family: Arial;
                }
                .QPushButton:hover {
                    background: url(buttons/butt1.png);
                }
                .QLabel {
                    color: white;
                    font-size: 25px;
                }
                """)

        self.setContentsMargins(
            0, int(QApplication.desktop().height() / 1.3), 0, 0)

        # Меню
        self.main = QVBoxLayout()
        self.menu = QHBoxLayout()
        self.warning = QLabel()
        self.warning.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.warning.setAlignment(Qt.AlignCenter)
        spacer_item0 = QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn1 = QPushButton('Википедия')
        self.btn1.setFixedSize(230, 60)
        spacer_item1 = QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn2 = QPushButton('Запуск')
        self.btn2.setFixedSize(230, 60)
        spacer_item2 = QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.btn3 = QPushButton('Ожидание...')
        self.btn3.setFixedSize(230, 60)
        spacer_item4 = QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.menu.addItem(spacer_item0)
        self.menu.addWidget(self.btn1)
        self.menu.addItem(spacer_item1)
        self.menu.addWidget(self.btn2)
        self.menu.addItem(spacer_item2)
        self.menu.addWidget(self.btn3)
        self.menu.addItem(spacer_item4)
        self.main.addLayout(self.menu)
        self.main.addWidget(self.warning)
        self.setLayout(self.main)


class Fraction(QWidget):
    def __init__(self, id):
        super().__init__()
        self.resize(X, Y - 30)
        self.move(0, 0)
        id = id[0]
        self.id = id
        self.section = ''
        self.main = QHBoxLayout()
        self.heroes = QVBoxLayout()
        self.armies = QVBoxLayout()
        self.buildings = QVBoxLayout()
        self.spells = QVBoxLayout()

        self.setStyleSheet("""
        .QPushButton{
            background-color: #403a3a;
            color: white;
            font-size: 23px;
            border-radius: 5px;
        }
        .QPushButton:hover{
            background-color: #5c5353;
        }""")

        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()

        heroes = cursor.execute("SELECT `image_heroes` FROM `fractions` WHERE `id` = ?", (id,)).fetchall()[0][0]
        print(heroes)
        self.heroes_image = QLabel()
        self.heroes_image.setPixmap(QPixmap(f"backgrounds/{heroes}.png"))
        self.heroes_btn = QPushButton("Герои")
        self.heroes_btn.setFixedSize(200, 30)
        self.heroes.addWidget(self.heroes_image)
        self.heroes.addWidget(self.heroes_btn)

        armies = cursor.execute("SELECT `image_armies` FROM `fractions` WHERE `id` = ?", (id,)).fetchall()[0][0]
        self.armies_image = QLabel()
        self.armies_image.setPixmap(QPixmap(f"backgrounds/{armies}.png"))
        self.armies_btn = QPushButton("Войска")
        self.armies_btn.setFixedSize(200, 30)
        self.armies.addWidget(self.armies_image)
        self.armies.addWidget(self.armies_btn)

        buildings = cursor.execute("SELECT `image_buildings` FROM `fractions` WHERE `id` = ?", (id,)).fetchall()[0][0]
        self.buildings_image = QLabel()
        self.buildings_image.setPixmap(QPixmap(f"backgrounds/{buildings}.png"))
        self.buildings_btn = QPushButton("Постройки")
        self.buildings_btn.setFixedSize(200, 30)
        self.buildings.addWidget(self.buildings_image)
        self.buildings.addWidget(self.buildings_btn)

        spells = cursor.execute("SELECT `image_spells` FROM `fractions` WHERE `id` = ?", (id,)).fetchall()[0][0]
        self.spells_image = QLabel()
        self.spells_image.setPixmap(QPixmap(f"backgrounds/{spells}.png"))
        self.spells_btn = QPushButton("Заклинания")
        self.spells_btn.setFixedSize(200, 30)
        self.spells.addWidget(self.spells_image)
        self.spells.addWidget(self.spells_btn)

        self.main.addLayout(self.heroes)
        self.main.addLayout(self.armies)
        self.main.addLayout(self.buildings)
        self.main.addLayout(self.spells)

        self.armies_btn.clicked.connect(self.handler)
        self.buildings_btn.clicked.connect(self.handler)
        self.heroes_btn.clicked.connect(self.handler)
        self.spells_btn.clicked.connect(self.handler)

        self.setLayout(self.main)

    def handler(self):
        section = self.sender().text()
        if section == "Герои":
            self.section = Heroes(self.id)
        elif section == "Войска":
            self.section = Armies(self.id)
        elif section == "Постройки":
            self.section = Buildings(self.id)
        else:
            self.section = Spells(self.id)
        self.section.setMinimumSize(400, 75)
        self.section.show()


class Wiki(QWidget):
    def __init__(self):
        super().__init__()
        # Вики
        self.main = QVBoxLayout()
        self.fractions = QHBoxLayout()

        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        fractions = cursor.execute("SELECT * FROM `fractions`").fetchall()
        for info in fractions:
            # Фракции
            self.fraction = QVBoxLayout()
            self.fraction_image = QLabel()
            self.fraction_image.setFixedSize(300, 300)
            self.fraction_image.setPixmap(QPixmap(f"fractions/{info[2]}-main-image.png"))
            self.fraction_btn = QPushButton(info[1])
            self.fraction_btn.setFixedSize(300, 50)
            self.fraction_btn.clicked.connect(self.handler)
            self.setStyleSheet("""
            .QPushButton{
                background-color: #403a3a;
                color: white;
                font-size: 23px;
                border-radius: 5px;
            }
            .QPushButton:hover{
                background-color: #5c5353;
            }""")
            self.fraction.addWidget(self.fraction_image)
            self.fraction.addWidget(self.fraction_btn)
            self.fractions.addLayout(self.fraction)
        self.back_layout = QHBoxLayout()
        self.back = QPushButton("Назад")
        self.back_layout.addWidget(self.back)
        self.back.setFixedSize(300, 50)

        self.main.addLayout(self.back_layout)
        self.main.addLayout(self.fractions)

        self.setLayout(self.main)

    def handler(self):
        query = sqlite3.connect("ennorath.sqlite")
        cursor = query.cursor()
        id = cursor.execute("SELECT `id` FROM `fractions` WHERE `name` = ?", (self.sender().text(),)).fetchall()[0]
        self.fraction = Fraction(id)
        self.fraction.showMaximized()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ennorath Launcher")

        self.move(0, 0)

        self.background = ''  # Чтобы компилятор не ругался
        self.update_background()

        self.menu = Menu()
        self.wiki = Wiki()
        self.menu.btn1.clicked.connect(self.handler)
        self.menu.btn2.clicked.connect(self.handler)
        self.wiki.back.clicked.connect(self.handler)
        self.setCentralWidget(self.menu)

        self.menu_program_action = QAction("Меню")
        self.menu_program_action.triggered.connect(self.open_menu_program)
        self.menu_program = MenuProgram()
        self.menu_program.btn_image.clicked.connect(self.select_image)
        self.menuBar().addAction(self.menu_program_action)

    def update_background(self):
        try:
            self.background = "user-background.jpg"
            scale_image(self)
        except FileNotFoundError:
            self.background = f"backgrounds/menu-background-{randint(1, 2)}.jpg"  # рандомное фоновое изображение
            scale_image(self)
        self.setStyleSheet("""
            .Main {
                background-image: url(""" + self.background + """);
                background-size: contain;
            }
        """)

    def select_image(self):
        file_name = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            '*.jpg;;*.png;;*.bmp;;*.jpeg')[0]
        image = Image.open(file_name)
        image.save("user-background.jpg", "JPEG")
        self.update_background()
        self.menu_program.hide()

    def handler(self):
        action = self.sender().text()
        if action == 'Википедия':
            self.menu = self.takeCentralWidget()
            self.setCentralWidget(self.wiki)
        elif action == 'Назад':
            self.wiki = self.takeCentralWidget()
            self.setCentralWidget(self.menu)
        elif action == "Запуск":
            try:
                subprocess.call('../lotrbfme2ep1.exe')
            except FileNotFoundError:
                self.menu.warning.setText(
                    "Для нормальной работы лаунчера необходимо поместить его в папку EP1 игры")

    def open_menu_program(self):
        self.menu_program.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = QDesktopWidget().availableGeometry()
    X, Y = q.width(), q.height()
    form = Main()
    form.showMaximized()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
