# user_profile_pyqt6.py
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QFont, QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 700)
        self.setWindowTitle("2.1 - User Profile GUI (PyQt6)")
        self.setUpMainWindow()
        self.show()

    def createImageLabels(self):
        images = ["images/images.jpg"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == "images/images.jpg":
                        label.move(30, 400)
            except FileNotFoundError as error:
                print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        self.createImageLabels()

        user_label = QLabel(self)
        user_label.setText("Иван Драго")
        user_label.setFont(QFont("Arial", 20))
        user_label.move(50, 30)

        bio_label = QLabel(self)
        bio_label.setText("Биография")
        bio_label.setFont(QFont("Arial", 17))
        bio_label.move(15, 70)

        about_label = QLabel(self)
        about_label.setText("Я инженер-программист с 10-летним опытом создания потрясающего кода.")
        about_label.setWordWrap(True)
        about_label.move(15, 100)

        skills_label = QLabel(self)
        skills_label.setText("Умения")
        skills_label.setFont(QFont("Arial", 17))
        skills_label.move(15, 140)

        languages_label = QLabel(self)
        languages_label.setText("Python | PHP | SQL | JavaScript")
        languages_label.move(15, 170)

        experience_label = QLabel(self)
        experience_label.setText("Опыт")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 200)

        developer_label = QLabel(self)
        developer_label.setText("Python Разработчик")
        developer_label.move(15, 230)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("Март 2011 - настоящее время")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 260)

        driver_label = QLabel(self)
        driver_label.setText("Водитель доставки пиццы")
        driver_label.move(15, 290)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Авг 2015 - Дек 2017")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 320)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
