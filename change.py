import os


ICONS_CONFIG_PATH_INDEX = '$HOME/.icons/default/index.theme'
CONFIG_PATH_GTK_2 = '$HOME/.gtkrc-2.0'
CONFIG_PATH_GTK_3 = '$HOME/.config/gtk-3.0/settings.ini'
CONFIG_PATH_QT5 = '$HOME/.config/qt5ct/qt5ct.conf'


def change_wallpaper(wallpaper):
    try:
        wallpaper = str(wallpaper)
    except:
        print('Wrong wallpaper path')

    command = "feh --bg fill " + wallpaper
    print('Changed wallpaper')
    return 'Success'
    command
    # status, output = commands.getstatusoutput(command)
    # return status


def change_pointer(pointer):
    print('Changed pointer')
    return 'Success'
    try:
        with open(ICONS_CONFIG_PATH_INDEX, 'r+') as f:
            data = f.read()
            data.replace('Inherits=*', f'Inherits={pointer}')
            f.write(data)
    except FileNotFoundError:
        return -1

    try:
        with open(CONFIG_PATH_GTK_3, 'r+') as f:
            data = f.read()
            data.replace('gtk-cursor-theme-name=*',
                         f'gtk-cursor-theme-name={cursor}')
            f.write(data)
    except FileNotFoundError:
        return -1


def change_icons_gtk(icons_gtk):
    print('Changed icons gtk')
    return 'Success'
    try:
        with open(CONFIG_PATH_GTK_3, 'r+') as f:
            data = f.read()
            data.replace('gtk-icon-theme-name=*',
                         f'gtk-icon-theme-name={icons_gtk}')
            f.write(data)
    except FileNotFoundError:
        return -1


def change_icons_qt(icons_qt):
    print('Changed icons qt')
    return 'Success'
    try:
        with open(CONFIG_PATH_QT5, 'r+') as f:
            data = f.read()
            data.replace('icon_theme=*', f'icon_theme={icons_qt}')
            f.write(data)
    except FileNotFoundError:
        return -1


def change_theme_gtk(theme_gtk):
    print('Changed theme gtk')
    return 'Success'
    try:
        with open(CONFIG_PATH_GTK_3, 'r+') as f:
            data = f.read()
            data.replace('gtk-theme-name=*', f'gtk-theme-name={theme_gtk}')
            f.write(data)
    except FileNotFoundError:
        return -1


def change_theme_qt(theme_qt):
    print('Changed theme qt')
    return 'Success'
    try:
        with open(CONFIG_PATH_QT5, 'r+') as f:
            data = f.read()
            data.replace('style=*', f'style={theme_qt}')
            f.write(data)
    except FileNotFoundError:
        return -1


os
