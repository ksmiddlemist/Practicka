import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication

from handle_windows import  setup_physical_keyboard_handlers
from macos_key_map import macos_key_map
from qtui.keyboard1 import Ui_MainWindowK1
from qtui.keyboard2 import Ui_MainWindowK2
from qtui.menu import Ui_MainWindow
from windows_key_map import windows_key_map


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screen = None # none или 'windows' или 'macos'
        self.w_size = None

        self.main_render()


    def main_render(self):
        if self.centralWidget():
            self.w_size = self.size()
            self.centralWidget().deleteLater()

        if self.screen is None:
            self.render_menu()
        elif self.screen == 'windows':
            self.render_windows()
        elif self.screen == 'macos':
            self.render_macos()

        if self.w_size is not None:
            self.resize(self.w_size)
        else:
            self.resize(1000, 600)

    def render_macos(self):
        main_ui = Ui_MainWindowK2()
        main_ui.setupUi(self)
        main_ui.Button_keyboard.clicked.connect(self._go_home)
        setup_physical_keyboard_handlers(self, macos_key_map(main_ui))
        main_ui.Button_reset.clicked.connect(self.render_macos)


    def render_windows(self):
        main_ui = Ui_MainWindowK1()
        main_ui.setupUi(self)
        main_ui.Button_keyboard.clicked.connect(self._go_home)
        setup_physical_keyboard_handlers(self, windows_key_map(main_ui))
        main_ui.Button_reset.clicked.connect(self.render_windows)

    def render_menu(self):
        main_ui = Ui_MainWindow()
        main_ui.setupUi(self)
        main_ui.Button_MacOS.mousePressEvent = self._MacOSPressEvent
        main_ui.Button_Windows.mousePressEvent = self._WindowsPressEvent

    def _go_home(self):
        self.screen = None
        self.main_render()

    
    def _MacOSPressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.screen = 'macos'
            self.main_render()

    def _WindowsPressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.screen = 'windows'
            self.main_render()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle('Тестер для клавиатуры')
    window.show()
    sys.exit(app.exec())