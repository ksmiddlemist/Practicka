from qtui.keyboard2 import Ui_MainWindowK2
from qtui.menu import Ui_MainWindow


def macos_key_map(ui: Ui_MainWindowK2):
    return {
        # Первый ряд
        (None,53): ui.key_Esc,
        (None,122,): ui.key_f1,
        (None,120,): ui.key_f2,
        (None,99,): ui.key_f3,
        (None,118,): ui.key_f4,
        (None,96,): ui.key_f5,
        (None,97,): ui.key_f6,
        (None,98,): ui.key_f7,
        (None,100,): ui.key_f8,
        (None,101,): ui.key_f9,
        (None,109,): ui.key_f10,
        (None,103,): ui.key_f10_2,
        (None,111,): ui.key_f12,
        (None, 117,): ui.key_Backspace,

# нету
        (None, 111,): ui.key_f13,
        (None, 111,): ui.key_f14,
        (None, 111,): ui.key_f15,
        (None, 111,): ui.key_f16,
        (None, 111,): ui.key_f17,
        (None, 111,): ui.key_f18,

        # Второй ряд
        (None,50,): ui.key_tilda,
        (None,18,): ui.key_t_1,         # 1
        (None,19,): ui.key_t_2,         # 2
        (None,20,): ui.key_t_3,         # 3
        (None,21,): ui.key_t_4,         # 4
        (None,23,): ui.key_t_5,         # 5
        (None,22,): ui.key_t_6,         # 6
        (None,26,): ui.key_t_7,         # 7
        (None,28,): ui.key_t_8,         # 8
        (None,25,): ui.key_t_9,         # 9
        (None,29,): ui.key_t_0,         # 0
        (None,27,): ui.key_underscore,  # - (минус/подчёркивание)
        (None,24,): ui.key_plus,        # = (плюс)

        (None,51,): ui.key_Delete_2,
        (None, 115): ui.key_Home,
        (None, 116): ui.key_PageUp,

        # нету

        #
        # Третий ряд (Q-P)
        (None, 48,): ui.key_Tab,         # Tab
        (None, 12,): ui.key_Q,           # Q
        (None, 13,): ui.key_W,           # W
        (None, 14,): ui.key_E,           # E
        (None, 15,): ui.key_R,           # R
        (None, 17,): ui.key_T,           # T
        (None, 16,): ui.key_Y,           # Y
        (None, 32,): ui.key_U,           # U
        (None, 34,): ui.key_I,           # I
        (None, 31,): ui.key_O,           # O
        (None, 35,): ui.key_P,           # P
        (None, 33,): ui.key_l_bracket,   # [
        (None, 30,): ui.key_R_bracket,   # ]
        (0xDC, 42): ui.key_backslash,
        (0x2E, 117): ui.key_Delete,
        (0x23, 119): ui.key_End,
        (0x22, 121): ui.key_PageDown,

        # Четвёртый ряд
        (0x14, 57): ui.key_Capslock,
        (0x41, 0): ui.key_A,
        (0x53, 1): ui.key_S,
        (0x44, 2): ui.key_D,
        (0x46, 3): ui.key_F,
        (0x47, 5): ui.key_G,
        (0x48, 4): ui.key_H,
        (0x4A, 38): ui.key_J,
        (0x4B, 40): ui.key_K,
        (0x4C, 37): ui.key_L,
        (0xBA, 41): ui.key_colon,
        (0xDE, 39): ui.key_backtick,
        (0x0D, 36): ui.key_Return,
        #
        # # Пятый ряд (Z-M)
        (0xA0, 56): ui.key_Shift,
        (0x5A, 6): ui.key_Z,
        (0x58, 7): ui.key_X,
        (0x43, 8): ui.key_C,
        (0x56, 9): ui.key_V,
        (0x42, 11): ui.key_B,
        (0x4E, 45): ui.key_N,
        (0x4D, 46): ui.key_M,
        (0xBC, 43): ui.key_comma,
        (0xBE, 47): ui.key_point,
        (0xBF, 44): ui.key_slash,
        (0xA1, 60): ui.key_Shift_2,
        (0x26, 126): ui.key_up,

        # Шестой ряд (модификаторы и стрелки)
        (None, 59,): ui.key_Control,        # Control (левая)
        (None, 55,): ui.key_Command,         # Command (⌘) (левая)
        (None, 58,): ui.key_Option,         # Option (⌥) (левая)
        (None, 49,): ui.key_Space,       # Space
        (None, 61,): ui.key_Option_2,       # Option (правая)
        (None, 54,): ui.key_Command_2,       # Command (правая)
        (None, 62,): ui.key_Control_2,      # Control (правая)

        (None, 123,): ui.key_left,       # Стрелка влево
        (None, 125,): ui.key_down,       # Стрелка вниз
        (None, 124,): ui.key_right,      # Стрелка вправо
        #
        # # NumPad (если нужно, зависит от устройства)
        # (71,): ui.key_NumLock,
        # (75,): ui.key_division,
        # (67,): ui.key_multiplication,
        # (78,): ui.key_minus,
        # (69,): ui.key_plus_2,
        # (76,): ui.key_Enter_2,
        # (65,): ui.key_Del,
        # (114,): ui.key_Ins,
        # (None, 116): ui.key_Clear,
        #
        # (83,): ui.key_seven,
        # (84,): ui.key_eight,
        # (85,): ui.key_nine,
        # (80,): ui.key_four,
        # (81,): ui.key_five,
        # (82,): ui.key_six,
        # (77,): ui.key_one,
        # (78,): ui.key_two,
        # (79,): ui.key_three,
    }
