from src.change import CONFIG_PATH_GTK_2, CONFIG_PATH_GTK_3, CONFIG_PATH_POLYBAR_COLORS, CONFIG_PATH_QT5, CONFIG_PATH_XSETTINGS, ICONS_CONFIG_PATH_INDEX

FILES = [ICONS_CONFIG_PATH_INDEX, CONFIG_PATH_GTK_2,
         CONFIG_PATH_GTK_3, CONFIG_PATH_QT5, CONFIG_PATH_XSETTINGS, CONFIG_PATH_POLYBAR_COLORS]


def create_backup():
    for backup in FILES:
        print(f'{backup}')
        try:
            with open(backup, 'r') as f:
                data = f.read()
        except FileNotFoundError or PermissionError:
            print(f'File {backup} not found', flush=True)
            return -1
        path = backup + ".bak"
        try:
            with open(path, 'w') as f:
                f.write(data)
        except PermissionError:
            print(
                f'Insufficient permission to create {path} backup file', flush=True)
            return -2


def restore_backup():
    for backup in FILES:
        try:
            with open(backup, 'r') as f:
                data = f.read()
        except FileNotFoundError or PermissionError:
            return -1
        path = backup.removesuffix('.bak')
        try:
            with open(path, 'w') as f:
                f.write(data)
        except PermissionError:
            return -2
