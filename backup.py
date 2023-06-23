"Create backup of files i'm going to change, load them in case of an error"
import os

HOME = os.environ['HOME']

ICONS_CONFIG_PATH_INDEX = HOME + '/.icons/default/index.theme'
CONFIG_PATH_GTK_2 = HOME + '/.gtkrc-2.0'
CONFIG_PATH_GTK_3 = HOME + '/.config/gtk-3.0/settings.ini'
CONFIG_PATH_QT5 = HOME + '/.config/qt5ct/qt5ct.conf'
CONFIG_PATH_XSETTINGS = HOME + '/.xsettingsd'
FILES = [ICONS_CONFIG_PATH_INDEX, CONFIG_PATH_GTK_2,
         CONFIG_PATH_GTK_3, CONFIG_PATH_QT5, CONFIG_PATH_XSETTINGS]


def create_backup():
    try:
        for backup in FILES:
            print(f'{backup}')
            with open(backup, 'r') as f:
                data = f.read()
            path = backup + ".bak"
            with open(path, 'w') as f:
                f.write(data)
    except Exception as e:
        print('Failed to create backup')
        return e


def delete_backup_files():
    try:
        for backup in FILES:
            backup = backup + '.bak'
            if os.path.exists(backup):
                os.remove(backup)
                print(f'Successfully removed {backup}')
            else:
                print(f"The file {backup} does not exist")
    except Exception as e:
        print('Failed to remove backup')
        return e


def restore_backup():
    try:
        for backup in FILES:
            with open(backup, 'r') as f:
                data = f.read()
            path = backup.removesuffix('.bak')
            with open(path, 'w') as f:
                f.write(data)
    except Exception as e:
        print('Failed to restore backup')
        return e
