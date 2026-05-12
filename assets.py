def get_asset_config(gui) -> dict:
    return {
        "buttons": {
            "numbers": {
                "9": {
                    "master": gui.app,
                    "text": "9",
                    "command": lambda: gui.append("9")
                },

                "8": {
                    "master": gui.app,
                    "text": "8",
                    "command": lambda: gui.append("8")
                },

                "7": {
                    "master": gui.app,
                    "text": "7",
                    "command": lambda: gui.append("7")
                },

                "6": {
                    "master": gui.app,
                    "text": "6",
                    "command": lambda: gui.append("6")
                },

                "5": {
                    "master": gui.app,
                    "text": "5",
                    "command": lambda: gui.append("5")
                },

                "4": {
                    "master": gui.app,
                    "text": "4",
                    "command": lambda: gui.append("4")
                },

                "3": {
                    "master": gui.app,
                    "text": "3",
                    "command": lambda: gui.append("3")
                },

                "2": {
                    "master": gui.app,
                    "text": "2",
                    "command": lambda: gui.append("2")
                },

                "1": {
                    "master": gui.app,
                    "text": "1",
                    "command": lambda: gui.append("1")
                },

                "0": {
                    "master": gui.app,
                    "text": "0",
                    "command": lambda: gui.append("0")
                }
            },

            "operators": {
                "/": {
                    "master": gui.app,
                    "text": "/",
                    "command": lambda: gui.append("/")
                },

                "*": {
                    "master": gui.app,
                    "text": "*",
                    "command": lambda: gui.append("*")
                },

                "+": {
                    "master": gui.app,
                    "text": "+",
                    "command": lambda: gui.append("+")
                },

                "-": {
                    "master": gui.app,
                    "text": "-",
                    "command": lambda: gui.append("-")
                }
            },

            "special": {
                "=": {
                    "master": gui.app,
                    "text": "=",
                    "command": lambda: gui.calculate()
                },

                "back": {
                    "master": gui.app,
                    "text": "back",
                    "command": lambda: gui.remove_last_char()
                },

                "(": {
                    "master": gui.app,
                    "text": "(",
                    "command": lambda: gui.append("(")
                },

                ")": {
                    "master": gui.app,
                    "text": ")",
                    "command": lambda: gui.append(")")
                },

                ".": {
                    "master": gui.app,
                    "text": ".",
                    "command": lambda: gui.append(".")
                }
            }
        }
    }