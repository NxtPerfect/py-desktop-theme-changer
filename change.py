import re
import os

HOME = os.environ['HOME']

ICONS_CONFIG_PATH_INDEX = HOME + '/.icons/default/index.theme'
CONFIG_PATH_GTK_2 = HOME + '/.gtkrc-2.0'
CONFIG_PATH_GTK_3 = HOME + '/.config/gtk-3.0/settings.ini'
CONFIG_PATH_QT5 = HOME + '/.config/qt5ct/qt5ct.conf'
CONFIG_PATH_XSETTINGS = HOME + '/.xsettingsd'

#  On a X11 wm you need a xsettings daemon running, every DE comes with one, you should install xsettingsd as the lightweight wm agnostic one.
#
# ~/.config/xsettingsd/xsettingsd.conf
#
#     Net/ThemeName "Adwaita"
#
# Make this conf file, launch the daemon and every gtk app will listen to it, if you want to live reload change Adwaita to a different theme and force reload of the config with killall -HUP xsettingsd


def change_wallpaper(wallpaper):
    try:
        wallpaper = str(wallpaper)
    except Exception as e:
        print('Wrong wallpaper path')
        return e

    try:
        command = 'feh --bg-fill ' + wallpaper
        os.system(command)
        return 0
    except Exception as e:
        return e


def change_pointer(pointer):
    # print('Changed pointer')
    # return 'Success'
    try:
        with open(ICONS_CONFIG_PATH_INDEX, 'r') as f:
            data = f.read()
        with open(ICONS_CONFIG_PATH_INDEX, 'w') as f:
            print(data)
            data = re.sub('Inherits=.+?(?=\n)',
                          f'Inherits={pointer}', data, 1)
            f.write(data)
    except FileNotFoundError:
        return -1

    try:
        with open(CONFIG_PATH_GTK_3, 'r+') as f:
            data = f.read()
        with open(CONFIG_PATH_GTK_3, 'w') as f:
            data = re.sub('gtk-cursor-theme-name=.+?(?=\n)',
                          f'gtk-cursor-theme-name={pointer}', data)
            f.write(data)
    except FileNotFoundError:
        return -1


def change_icons_gtk(icons_gtk):
    # print('Changed icons gtk')
    # return 'Success'
    try:
        with open(CONFIG_PATH_GTK_3, 'r+') as f:
            data = f.read()
        with open(CONFIG_PATH_GTK_3, 'w') as f:
            data = re.sub('gtk-icon-theme-name=.+?(?=\n)',
                          f'gtk-icon-theme-name={icons_gtk}', data)
            f.write(data)
    except FileNotFoundError:
        return -1


def change_icons_qt(icons_qt):
    # print('Changed icons qt')
    # return 'Success'
    try:
        with open(CONFIG_PATH_QT5, 'r+') as f:
            data = f.read()
        with open(CONFIG_PATH_QT5, 'w') as f:
            data = re.sub('icon_theme=.+?(?=\n)',
                          f'icon_theme={icons_qt}', data)
            f.write(data)
    except FileNotFoundError:
        return -1


def change_theme_gtk(theme_gtk):
    # print('Changed theme gtk')
    # return 'Success'
    try:
        with open(CONFIG_PATH_GTK_3, 'r+') as f:
            data = f.read()
        with open(CONFIG_PATH_GTK_3, 'w') as f:
            data = re.sub('gtk-theme-name=.+?(?=\n)',
                          f'gtk-theme-name={theme_gtk}', data)
            f.write(data)
    except FileNotFoundError:
        return -1


def change_theme_qt(theme_qt):
    # print('Changed theme qt')
    # return 'Success'
    try:
        with open(CONFIG_PATH_QT5, 'r+') as f:
            data = f.read()
        with open(CONFIG_PATH_QT5, 'w') as f:
            data = re.sub('style=.+?(?=\n)', f'style={theme_qt}', data)
            f.write(data)
    except FileNotFoundError:
        return -1


def change_theme_gtk_live(theme_gtk):
    try:
        with open(CONFIG_PATH_XSETTINGS, 'r+') as f:
            data = f.read()
        with open(CONFIG_PATH_XSETTINGS, 'w') as f:
            data = re.sub('Net/ThemeName+.+?(?=\n)',
                          f'Net/ThemeName \"{theme_gtk}\"', data)
            f.write(data)
    except FileNotFoundError:
        return -1

    try:
        command = 'killall -HUP xsettingsd'
        os.system(command)
        return 0
    except Exception as e:
        return e


def change_polybar_theme(theme):
    pass
