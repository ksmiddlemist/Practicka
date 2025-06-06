import platform
from PySide6.QtGui import QKeyEvent

IS_WIN = platform.system() == "Windows"

# Стили для нажатых и отпущенных клавиш
PRESSED_STYLE = "border: 1px solid black; background-color: #00e208; border-radius: 5px; color: black;"
RELEASED_STYLE = "border: 1px solid black; background-color: #00ff09; border-radius: 5px; color: black;"

def setup_physical_keyboard_handlers(window, keyboard_data):
    
    class KeyHandler:
        def __init__(self):
            self.pressed_keys = set()  # Храним (vk, scan_code) для отслеживания нажатий
            

        def _get_widget(self, vk_win, scan_code=None, is_extended=False):
            print(vk_win)
            key_data = keyboard_data.get(vk_win)
            print(key_data)
            if not key_data:
                return None
            
            if not key_data["is_pair"]:
                print('dsfsd')
                return key_data["widget"]
            
            # Для парных клавиш обрабатываем scan_code
            if scan_code is not None:
                # Формируем полный scan_code с учетом E0 префикса
                
                # Ищем точное совпадение scan_code
                for pair in key_data["widgets"]["pairs"]:
                    if pair["scan_code"] == scan_code:
                        return pair["widget"]
            
            # Возвращаем виджет по умолчанию, если не нашли точного совпадения
            return key_data["widgets"].get("default")
           

        def key_press(self, event: QKeyEvent):
            vk = event.nativeVirtualKey()
            scan_code = event.nativeScanCode()
            print(f"KeyPress: vk={vk}, scan_code={scan_code}")
            
            widget = self._get_widget(vk, scan_code)
            if widget:
                widget.setStyleSheet(PRESSED_STYLE)
                self.pressed_keys.add((vk, scan_code))  # Запоминаем нажатую клавишу

        def key_release(self, event: QKeyEvent):
            vk = event.nativeVirtualKey()
            scan_code = event.nativeScanCode()
            
            widget = self._get_widget(vk, scan_code)
            if widget and (vk, scan_code) in self.pressed_keys:
                widget.setStyleSheet(RELEASED_STYLE)
                self.pressed_keys.remove((vk, scan_code))

    handler = KeyHandler()

    # Переопределяем обработчики событий окна
    def key_press_event(event):
        handler.key_press(event)
        event.accept()

    def key_release_event(event):
        handler.key_release(event)
        event.accept()

    window.keyPressEvent = key_press_event
    window.keyReleaseEvent = key_release_event