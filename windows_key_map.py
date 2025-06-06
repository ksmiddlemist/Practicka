def windows_key_map(ui):
    return {
        # Одиночные клавиши (is_pair=False)
        0x1B: {"is_pair": False, "widget": ui.key_Esc},  # Esc
        0x70: {"is_pair": False, "widget": ui.key_f1},   # F1
        0x71: {"is_pair": False, "widget": ui.key_f2},   # F2
        0x72: {"is_pair": False, "widget": ui.key_f3},   # F3
        0x73: {"is_pair": False, "widget": ui.key_f4},   # F4
        0x74: {"is_pair": False, "widget": ui.key_f5},   # F5
        0x75: {"is_pair": False, "widget": ui.key_f6},   # F6
        0x76: {"is_pair": False, "widget": ui.key_f7},   # F7
        0x77: {"is_pair": False, "widget": ui.key_f8},   # F8
        0x78: {"is_pair": False, "widget": ui.key_f9},   # F9
        0x79: {"is_pair": False, "widget": ui.key_f10},  # F10
        0x7A: {"is_pair": False, "widget": ui.key_f11},  # F11
        0x7B: {"is_pair": False, "widget": ui.key_f12},  # F12
        0x2C: {"is_pair": False, "widget": ui.key_PrtScr},  # PrtScr
        0x91: {"is_pair": False, "widget": ui.key_ScrollLock},  # ScrollLock
        0x13: {"is_pair": False, "widget": ui.key_PauseBreak},  # PauseBreak

        # Второй ряд
        0xC0: {"is_pair": False, "widget": ui.key_tilda},  # ~
        0x31: {"is_pair": False, "widget": ui.key_t_1},    # 1
        0x32: {"is_pair": False, "widget": ui.key_t_2},    # 2
        0x33: {"is_pair": False, "widget": ui.key_t_3},    # 3
        0x34: {"is_pair": False, "widget": ui.key_t_4},    # 4
        0x35: {"is_pair": False, "widget": ui.key_t_5},    # 5
        0x36: {"is_pair": False, "widget": ui.key_t_6},    # 6
        0x37: {"is_pair": False, "widget": ui.key_t_7},    # 7
        0x38: {"is_pair": False, "widget": ui.key_t_8},    # 8
        0x39: {"is_pair": False, "widget": ui.key_t_9},    # 9
        0x30: {"is_pair": False, "widget": ui.key_t_0},    # 0
        0xBD: {"is_pair": False, "widget": ui.key_underscore},  # -
        0xBB: {"is_pair": False, "widget": ui.key_plus},  # +
        0x08: {"is_pair": False, "widget": ui.key_backspace},  # Backspace
        0x2D: {"is_pair": True, "widgets": {  # Insert
            "default": ui.key_Insert,
            "pairs": [
                {"scan_code": 0x52, "widget": ui.key_Insert},
                {"scan_code": 0xE052, "widget": ui.key_Ins}
            ]
        }},
        0x24: {"is_pair": False, "widget": ui.key_Home},  # Home
        0x21: {"is_pair": False, "widget": ui.key_PageUp},  # PageUp

        # Третий ряд
        9: {"is_pair": False, "widget": ui.key_Tab},  # Tab
        0x51: {"is_pair": False, "widget": ui.key_Q},    # Q
        0x57: {"is_pair": False, "widget": ui.key_W},    # W
        0x45: {"is_pair": False, "widget": ui.key_E},    # E
        0x52: {"is_pair": False, "widget": ui.key_R},    # R
        0x54: {"is_pair": False, "widget": ui.key_T},    # T
        0x59: {"is_pair": False, "widget": ui.key_Y},    # Y
        0x55: {"is_pair": False, "widget": ui.key_U},    # U
        0x49: {"is_pair": False, "widget": ui.key_I},    # I
        0x4F: {"is_pair": False, "widget": ui.key_O},    # O
        0x50: {"is_pair": False, "widget": ui.key_P},    # P
        0xDB: {"is_pair": False, "widget": ui.key_l_bracket},  # [
        0xDD: {"is_pair": False, "widget": ui.key_R_bracket},  # ]
        0xDC: {"is_pair": False, "widget": ui.key_backslash},  # \
        0x2E: {"is_pair": False, "widget": ui.key_Delete},  # Delete
        0x23: {"is_pair": False, "widget": ui.key_End},  # End
        0x22: {"is_pair": False, "widget": ui.key_PageDown},  # PageDown

        # Четвертый ряд
        0x14: {"is_pair": False, "widget": ui.key_Caps},  # Caps
        0x41: {"is_pair": False, "widget": ui.key_A},    # A
        0x53: {"is_pair": False, "widget": ui.key_S},    # S
        0x44: {"is_pair": False, "widget": ui.key_D},    # D
        0x46: {"is_pair": False, "widget": ui.key_F},    # F
        0x47: {"is_pair": False, "widget": ui.key_G},    # G
        0x48: {"is_pair": False, "widget": ui.key_H},    # H
        0x4A: {"is_pair": False, "widget": ui.key_J},    # J
        0x4B: {"is_pair": False, "widget": ui.key_K},    # K
        0x4C: {"is_pair": False, "widget": ui.key_L},    # L
        0xBA: {"is_pair": False, "widget": ui.key_colon},  # ;
        0xDE: {"is_pair": False, "widget": ui.key_backtick},  # '
        0x0D: {"is_pair": True, "widgets": {  # Enter
            "default": ui.key_Enter,
            "pairs": [
                {"scan_code": 0x1C, "widget": ui.key_Enter},
                {"scan_code": 0xE01C, "widget": ui.key_Enter_2}
            ]
        }},

        # Пятый ряд (модификаторы)
        16: {"is_pair": True, "widgets": {  # LShift/RShift
            "default": ui.key_Shift,
            "pairs": [
                {"scan_code": 0x2A, "widget": ui.key_Shift},
                {"scan_code": 0x36, "widget": ui.key_Shift_2}
            ]
        }},
        0x5A: {"is_pair": False, "widget": ui.key_Z},    # Z
        0x58: {"is_pair": False, "widget": ui.key_X},    # X
        0x43: {"is_pair": False, "widget": ui.key_C},    # C
        0x56: {"is_pair": False, "widget": ui.key_V},    # V
        0x42: {"is_pair": False, "widget": ui.key_B},    # B
        0x4E: {"is_pair": False, "widget": ui.key_N},    # N
        0x4D: {"is_pair": False, "widget": ui.key_M},    # M
        0xBC: {"is_pair": False, "widget": ui.key_comma},  # ,
        0xBE: {"is_pair": False, "widget": ui.key_point},  # .
        0xBF: {"is_pair": False, "widget": ui.key_slash},  # /
        38: {"is_pair": False, "widget": ui.key_up},    # Up

        # Шестой ряд (модификаторы)
        0x11: {"is_pair": True, "widgets": {  # LCtrl/RCtrl
            "default": ui.key_Ctrl,
            "pairs": [
                {"scan_code": 0x1D, "widget": ui.key_Ctrl},
                {"scan_code": 0xE01D, "widget": ui.key_Ctrl_2}
            ]
        }},
        0x5B: {"is_pair": True, "widgets": {  # LWin/RWin
            "default": ui.key_Win,
            "pairs": [
                {"scan_code": 0x5B, "widget": ui.key_Win},
                {"scan_code": 0x5C, "widget": ui.key_Win_2}
            ]
        }},
        0x12: {"is_pair": True, "widgets": {  # LAlt/RAlt
            "default": ui.key_Alt,
            "pairs": [
                {"scan_code": 0x38, "widget": ui.key_Alt},
                {"scan_code": 0xE038, "widget": ui.key_Alt_2}
            ]
        }},
        0x20: {"is_pair": False, "widget": ui.key_Space},  # Space
        0x5C: {"is_pair": False, "widget": ui.key_buffer},  # Menu/Buffer
        0x25: {"is_pair": False, "widget": ui.key_left},  # Left
        0x28: {"is_pair": False, "widget": ui.key_down},  # Down
        0x27: {"is_pair": False, "widget": ui.key_right},  # Right

        # Numpad
        0x90: {"is_pair": False, "widget": ui.key_NumLock},  # NumLock
        0x6F: {"is_pair": False, "widget": ui.key_division},  # /
        0x6A: {"is_pair": False, "widget": ui.key_multiplication},  # *
        0x6D: {"is_pair": False, "widget": ui.key_minus},  # -
        0x6B: {"is_pair": False, "widget": ui.key_plus_2},  # +
        0x6E: {"is_pair": False, "widget": ui.key_Del},    # NumDel
        0x67: {"is_pair": False, "widget": ui.key_seven},  # 7
        0x68: {"is_pair": False, "widget": ui.key_eight},  # 8
        0x69: {"is_pair": False, "widget": ui.key_nine},  # 9
        0x64: {"is_pair": False, "widget": ui.key_four},  # 4
        0x65: {"is_pair": False, "widget": ui.key_five},  # 5
        0x66: {"is_pair": False, "widget": ui.key_six},  # 6
        0x61: {"is_pair": False, "widget": ui.key_one},  # 1
        0x62: {"is_pair": False, "widget": ui.key_two},  # 2
        0x63: {"is_pair": False, "widget": ui.key_three},  # 3
        0x60: {"is_pair": False, "widget": ui.key_Ins}  # 0
    }