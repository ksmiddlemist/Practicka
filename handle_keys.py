import platform
from PySide6.QtGui import QKeyEvent

IS_WIN = platform.system() == "Windows"


PRESSED_STYLE = "border: 1px solid black; background-color: #00e208; border-radius: 5px; color: black;"
RELEASED_STYLE = "border: 1px solid black; background-color: #00ff09; border-radius: 5px; color: black;"


def setup_physical_keyboard_handlers(window, keyboard_data):
    class KeyHandler:
        def __init__(self):
            self.pressed_keys = set()
            self.vk_map = {} # обратный словарь

            for key, data in keyboard_data.items():
                if IS_WIN:
                    self.vk_map[data["vk"]["win"]] = key
                else:
                    self.vk_map[data["vk"]["mac"]] = key
            
            print(self.vk_map)

        def _get_widget(self, vk, scan_code=None):
            print(vk, scan_code)
            if IS_WIN:
                if vk == 16 and scan_code == 42:
                    return keyboard_data['shift']["widget"]
                elif vk == 13 and scan_code == 28:
                    return keyboard_data['enter']["widget"]
                elif vk == 16 and scan_code == 54:
                    return keyboard_data['shift2']["widget"]
                elif vk == 16 and scan_code == 54:
                    return keyboard_data['shift2']["widget"]
                elif vk == 17 and scan_code == 29:
                    return keyboard_data['ctrl']["widget"]
                elif vk == 17 and scan_code == 57373:
                    return keyboard_data['ctrl2']["widget"]
                elif vk == 18 and scan_code == 56:
                    return  keyboard_data['alt']["widget"]
                elif vk == 18 and scan_code == 57400:
                    return keyboard_data['alt2']["widget"]
                
            key = self.vk_map.get(vk)
            print(key)
            if not key:
                return None

            key_data = keyboard_data[key]
            return key_data["widget"]


        def key_press(self, event: QKeyEvent):
            vk = event.nativeVirtualKey()
            scan_code = event.nativeScanCode()

            widget = self._get_widget(vk, scan_code)
            if widget:
                widget.setStyleSheet(PRESSED_STYLE)
                self.pressed_keys.add((vk, scan_code))

        def key_release(self, event: QKeyEvent):
            vk = event.nativeVirtualKey()
            scan_code = event.nativeScanCode()

            widget = self._get_widget(vk, scan_code)
            if widget and (vk, scan_code) in self.pressed_keys:
                widget.setStyleSheet(RELEASED_STYLE)
                self.pressed_keys.remove((vk, scan_code))

    handler = KeyHandler()

    def key_press_event(event):
        handler.key_press(event)
        event.accept()

    def key_release_event(event):
        handler.key_release(event)
        event.accept()

    window.keyPressEvent = key_press_event
    window.keyReleaseEvent = key_release_event