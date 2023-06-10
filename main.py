import config
import change

'''Config in a file
read wallpaper-dark
wallpaper-light
theme-dark
theme-light
cursor-dark
cursor-light
change wallpaper with feh
figure out how to change themes
figure out how to change cursor'''

'''We should handle errors either in main or another module
do not write errors already in the modules itself, there\'s no need'''

DEFAULT_PATH = '$XDG_CONFIG_HOME/theme-switcher/config.toml'


def run():
    theme = 'yes'
    try:
        theme = config.read_themes_configuration('./config.toml')
    except:
        print('Couldn\'t find config file')
    print(f'Config read {theme}')

    try:
        config.write_current_theme(
            './config.toml', config.read_current_theme('./config.toml'))
    except:
        print('Couldn\'t write to file')

    print(theme['wallpaper'])

    try:
        change.change_wallpaper(theme['wallpaper'])
    except:
        print('Couldn\'t set wallpaper')

    try:
        change.change_pointer(theme['pointer'])
    except:
        print('Couldn\'t change pointer')

    try:
        change.change_icons_gtk(theme['icons'])
    except:
        print('Couldn\'t change icons gtk')

    try:
        change.change_icons_qt(theme['icons'])
    except:
        print('Couldn\'t change icons qt')

    try:
        change.change_theme_gtk(theme['theme-gtk'])
    except:
        print('Couldn\'t change theme gtk')

    try:
        change.change_theme_qt(theme['theme-qt'])
    except:
        print('Couldn\'t change theme qt')


if __name__ == "__main__":
    run()
