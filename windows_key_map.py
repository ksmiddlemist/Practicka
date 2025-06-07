def windows_key_map(ui):
    return {
        # Первый ряд (функциональные клавиши)
        "esc": {
            "vk": {"win": 0x1B, "mac": 0x35},
            "widget": ui.key_Esc,
            
        },
        "f1": {
            "vk": {"win": 0x70, "mac": 0x7A},
            "widget": ui.key_f1,
            
        },
        "f2": {
            "vk": {"win": 0x71, "mac": 0x78},
            "widget": ui.key_f2,
            
        },
        "f3": {
            "vk": {"win": 0x72, "mac": 0x63},
            "widget": ui.key_f3,
            
        },
        "f4": {
            "vk": {"win": 0x73, "mac": 0x76},
            "widget": ui.key_f4,
            
        },
        "f5": {
            "vk": {"win": 0x74, "mac": 0x60},
            "widget": ui.key_f5,
            
        },
        "f6": {
            "vk": {"win": 0x75, "mac": 0x61},
            "widget": ui.key_f6,
            
        },
        "f7": {
            "vk": {"win": 0x76, "mac": 0x62},
            "widget": ui.key_f7,
            
        },
        "f8": {
            "vk": {"win": 0x77, "mac": 0x64},
            "widget": ui.key_f8,
            
        },
        "f9": {
            "vk": {"win": 0x78, "mac": 0x65},
            "widget": ui.key_f9,
            
        },
        "f10": {
            "vk": {"win": 0x79, "mac": 0x6D},
            "widget": ui.key_f10,
            
        },
        "f11": {
            "vk": {"win": 0x7A, "mac": 0x67},
            "widget": ui.key_f11,
            
        },
        "f12": {
            "vk": {"win": 0x7B, "mac": 0x6F},
            "widget": ui.key_f12,
            
        },
        "prtscr": {
            "vk": {"win": 0x2C, "mac": 0x69},  # Mac: F13
            "widget": ui.key_PrtScr,
            
        },
        "scroll_lock": {
            "vk": {"win": 0x91, "mac": 0x6B},  # Mac: F14
            "widget": ui.key_ScrollLock,
            
        },
        "pause": {
            "vk": {"win": 0x13, "mac": 0x71},  # Mac: F15
            "widget": ui.key_PauseBreak,
            
        },

        # Второй ряд (цифры)
        "backtick": {
            "vk": {"win": 0xC0, "mac": 0x32},
            "widget": ui.key_tilda,
            
        },
        "1": {
            "vk": {"win": 0x31, "mac": 0x12},
            "widget": ui.key_t_1,
            
        },
        "2": {
            "vk": {"win": 0x32, "mac": 0x13},
            "widget": ui.key_t_2,
            
        },
        "3": {
            "vk": {"win": 0x33, "mac": 0x14},
            "widget": ui.key_t_3,
            
        },
        "4": {
            "vk": {"win": 0x34, "mac": 0x15},
            "widget": ui.key_t_4,
            
        },
        "5": {
            "vk": {"win": 0x35, "mac": 0x17},
            "widget": ui.key_t_5,
            
        },
        "6": {
            "vk": {"win": 54, "mac": 0x16},
            "widget": ui.key_t_6,
            
        },
        "7": {
            "vk": {"win": 0x37, "mac": 0x1A},
            "widget": ui.key_t_7,
            
        },
        "8": {
            "vk": {"win": 0x38, "mac": 0x1C},
            "widget": ui.key_t_8,
            
        },
        "9": {
            "vk": {"win": 0x39, "mac": 0x19},
            "widget": ui.key_t_9,
            
        },
        "0": {
            "vk": {"win": 0x30, "mac": 0x1D},
            "widget": ui.key_t_0,
            
        },
        "minus": {
            "vk": {"win": 0xBD, "mac": 0x1B},
            "widget": ui.key_underscore,
            
        },
        "equal": {
            "vk": {"win": 0xBB, "mac": 0x18},
            "widget": ui.key_plus,
            
        },
        "backspace": {
            "vk": {"win": 0x08, "mac": 0x33},
            "widget": ui.key_backspace,
            
        },

        # Навигационные клавиши
        "insert": {
            "vk": {"win": 0x2D, "mac": 0x72},
            "widget": ui.key_Insert,
            
        },
        "insert2": {
            "vk": {"win": 0xE052, "mac": 0x72},
            "widget": ui.key_Ins,
            
        },
        "home": {
            "vk": {"win": 0x24, "mac": 0x73},
            "widget": ui.key_Home,
            
        },
        "page_up": {
            "vk": {"win": 0x21, "mac": 0x74},
            "widget": ui.key_PageUp,
            
        },

        # Третий ряд (буквы Q-P)
        "tab": {
            "vk": {"win": 0x09, "mac": 0x30},
            "widget": ui.key_Tab,
            
        },
        "q": {
            "vk": {"win": 0x51, "mac": 0x0C},
            "widget": ui.key_Q,
            
        },
        "w": {
            "vk": {"win": 0x57, "mac": 0x0D},
            "widget": ui.key_W,
            
        },
        "e": {
            "vk": {"win": 0x45, "mac": 0x0E},
            "widget": ui.key_E,
            
        },
        "r": {
            "vk": {"win": 0x52, "mac": 0x0F},
            "widget": ui.key_R,
            
        },
        "t": {
            "vk": {"win": 0x54, "mac": 0x11},
            "widget": ui.key_T,
            
        },
        "y": {
            "vk": {"win": 0x59, "mac": 0x10},
            "widget": ui.key_Y,
            
        },
        "u": {
            "vk": {"win": 0x55, "mac": 0x20},
            "widget": ui.key_U,
            
        },
        "i": {
            "vk": {"win": 0x49, "mac": 0x22},
            "widget": ui.key_I,
            
        },
        "o": {
            "vk": {"win": 0x4F, "mac": 0x1F},
            "widget": ui.key_O,
            
        },
        "p": {
            "vk": {"win": 0x50, "mac": 0x23},
            "widget": ui.key_P,
            
        },
        "left_bracket": {
            "vk": {"win": 0xDB, "mac": 0x21},
            "widget": ui.key_l_bracket,
            
        },
        "right_bracket": {
            "vk": {"win": 0xDD, "mac": 0x1E},
            "widget": ui.key_R_bracket,
            
        },
        "backslash": {
            "vk": {"win": 0xDC, "mac": 0x2A},
            "widget": ui.key_backslash,
            
        },
        "delete": {
            "vk": {"win": 0x2E, "mac": 0x75},
            "widget": ui.key_Delete,
            
        },
        "end": {
            "vk": {"win": 0x23, "mac": 0x77},
            "widget": ui.key_End,
            
        },
        "page_down": {
            "vk": {"win": 0x22, "mac": 0x79},
            "widget": ui.key_PageDown,
            
        },

        # Четвертый ряд (буквы A-L)
        "caps": {
            "vk": {"win": 0x14, "mac": 0x39},
            "widget": ui.key_Caps,
            
        },
        "a": {
            "vk": {"win": 0x41, "mac": 0x00},
            "widget": ui.key_A,
            
        },
        "s": {
            "vk": {"win": 0x53, "mac": 0x01},
            "widget": ui.key_S,
            
        },
        "d": {
            "vk": {"win": 0x44, "mac": 0x02},
            "widget": ui.key_D,
            
        },
        "f": {
            "vk": {"win": 0x46, "mac": 0x03},
            "widget": ui.key_F,
            
        },
        "g": {
            "vk": {"win": 0x47, "mac": 0x05},
            "widget": ui.key_G,
            
        },
        "h": {
            "vk": {"win": 0x48, "mac": 0x04},
            "widget": ui.key_H,
            
        },
        "j": {
            "vk": {"win": 0x4A, "mac": 0x26},
            "widget": ui.key_J,
            
        },
        "k": {
            "vk": {"win": 0x4B, "mac": 0x28},
            "widget": ui.key_K,
            
        },
        "l": {
            "vk": {"win": 0x4C, "mac": 0x25},
            "widget": ui.key_L,
            
        },
        "semicolon": {
            "vk": {"win": 0xBA, "mac": 0x29},
            "widget": ui.key_colon,
            
        },
        "quote": {
            "vk": {"win": 0xDE, "mac": 0x27},
            "widget": ui.key_backtick,
            
        },
        "enter": {
            "vk": {"win": 0x0D, "mac": 36},
            "widget": ui.key_Enter,
            
        },
        "enter2": {
            "vk": {"win": 0xE01C, "mac": 76},
            "widget": ui.key_Enter_2,
            
        },

        # Пятый ряд (буквы Z-M)
        "shift": {
            "vk": {"win": 0x10, "mac": 0x38},
            "widget": ui.key_Shift,
            
        },
        "shift2": {
            "vk": {"win": 16, "mac": 0x3C},
            "widget": ui.key_Shift_2,
            
        },
        "z": {
            "vk": {"win": 0x5A, "mac": 0x06},
            "widget": ui.key_Z,
            
        },
        "x": {
            "vk": {"win": 0x58, "mac": 0x07},
            "widget": ui.key_X,
            
        },
        "c": {
            "vk": {"win": 0x43, "mac": 0x08},
            "widget": ui.key_C,
            
        },
        "v": {
            "vk": {"win": 0x56, "mac": 0x09},
            "widget": ui.key_V,
            
        },
        "b": {
            "vk": {"win": 0x42, "mac": 0x0B},
            "widget": ui.key_B,
            
        },
        "n": {
            "vk": {"win": 0x4E, "mac": 0x2D},
            "widget": ui.key_N,
            
        },
        "m": {
            "vk": {"win": 0x4D, "mac": 0x2E},
            "widget": ui.key_M,
            
        },
        "comma": {
            "vk": {"win": 0xBC, "mac": 0x2B},
            "widget": ui.key_comma,
            
        },
        "period": {
            "vk": {"win": 0xBE, "mac": 0x2F},
            "widget": ui.key_point,
            
        },
        "slash": {
            "vk": {"win": 0xBF, "mac": 0x2C},
            "widget": ui.key_slash,
            
        },
        "up": {
            "vk": {"win": 0x26, "mac": 0x7E},
            "widget": ui.key_up,
            
        },

        # Шестой ряд (модификаторы и пробел)
        "ctrl": {
            "vk": {"win": 0x11, "mac": 0x3B},
            "widget": ui.key_Ctrl,
            
        },
        "ctrl2": {
            "vk": {"win": 0xE01D, "mac": 0x3E},
            "widget": ui.key_Ctrl_2,
            
        },
        "win": {
            "vk": {"win": 0x5B, "mac": 0x37},
            "widget": ui.key_Win,
            
        },
        "win2": {
            "vk": {"win": 0x5C, "mac": 0x36},
            "widget": ui.key_Win_2,
            
        },
        "alt": {
            "vk": {"win": 0x12, "mac": 0x3A},
            "widget": ui.key_Alt,
            
        },
        "alt2": {
            "vk": {"win": 0xE038, "mac": 0x3D},
            "widget": ui.key_Alt_2,
            
        },
        "space": {
            "vk": {"win": 0x20, "mac": 0x31},
            "widget": ui.key_Space,
            
        },
        "menu": {
            "vk": {"win": 0x5D, "mac": 0x6E},  # Mac: Right Click
            "widget": ui.key_buffer,
            
        },
        "left": {
            "vk": {"win": 0x25, "mac": 0x7B},
            "widget": ui.key_left,
            
        },
        "down": {
            "vk": {"win": 0x28, "mac": 0x7D},
            "widget": ui.key_down,
        },
        "right": {
            "vk": {"win": 0x27, "mac": 0x7C},
            "widget": ui.key_right,
        },

        # Numpad
        "num_lock": {
            "vk": {"win": 0x90, "mac": 0x47},
            "widget": ui.key_NumLock,
        },
        "num_divide": {
            "vk": {"win": 0x6F, "mac": 0x4B},
            "widget": ui.key_division,
            
        },
        "num_multiply": {
            "vk": {"win": 0x6A, "mac": 0x43},
            "widget": ui.key_multiplication,
            
        },
        "num_subtract": {
            "vk": {"win": 0x6D, "mac": 0x4E},
            "widget": ui.key_minus,
            
        },
        "num_add": {
            "vk": {"win": 0x6B, "mac": 0x45},
            "widget": ui.key_plus_2,
            
        },
        "num_enter": {
            "vk": {"win": 0x0D, "mac": 0x4C},
            "widget": ui.key_Enter_2,
            
        },
        "num_decimal": {
            "vk": {"win": 0x6E, "mac": 0x41},
            "widget": ui.key_Del,
            
        },
        "num_0": {
            "vk": {"win": 0x60, "mac": 0x52},
            "widget": ui.key_Ins,
            
        },
        "num_1": {
            "vk": {"win": 0x61, "mac": 0x53},
            "widget": ui.key_one,
            
        },
        "num_2": {
            "vk": {"win": 0x62, "mac": 0x54},
            "widget": ui.key_two,
            
        },
        "num_3": {
            "vk": {"win": 0x63, "mac": 0x55},
            "widget": ui.key_three,
            
        },
        "num_4": {
            "vk": {"win": 0x64, "mac": 0x56},
            "widget": ui.key_four,
            
        },
        "num_5": {
            "vk": {"win": 0x65, "mac": 0x57},
            "widget": ui.key_five,
            
        },
        "num_6": {
            "vk": {"win": 0x66, "mac": 0x58},
            "widget": ui.key_six,
            
        },
        "num_7": {
            "vk": {"win": 0x67, "mac": 0x59},
            "widget": ui.key_seven,
            
        },
        "num_8": {
            "vk": {"win": 0x68, "mac": 0x5B},
            "widget": ui.key_eight,
            
        },
        "num_9": {
            "vk": {"win": 0x69, "mac": 0x5C},
            "widget": ui.key_nine,
            
        }
    }