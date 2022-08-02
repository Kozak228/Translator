from PyQt6.QtWidgets import QApplication
from GUI import mainWindow
from sys import exit, argv

def main():
    app = QApplication(argv)
    appl = mainWindow()
    appl.show()

    try:
        exit(app.exec())
    except:
        pass

if __name__ == '__main__':
    main()