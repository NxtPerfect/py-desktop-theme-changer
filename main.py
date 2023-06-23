import config
import backup
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


def debug():
    # TODO: only recreate backup if deleted
    backup
    # try:
    #     backup.create_backup()
    # except:
    #     print('Couldn\'t create backup')
    #     exit()

    # try:
    #     backup.delete_backup_files()
    # except:
    #     print('Couldn\'t remove backup')
    #     exit()

    theme = 'light'
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

    try:
        change.change_wallpaper(theme['wallpaper'])
    except Exception as e:
        print(f'Couldn\'t set wallpaper, Error {e}')

    try:
        change.change_pointer(theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change pointer, Error {e}')

    try:
        change.change_icons(theme['icons'])
    except Exception as e:
        print(f'Couldn\'t change icons, Error {e}')

    try:
        change.change_theme_gtk(theme['theme-gtk'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk, Error {e}')

    try:
        change.change_theme_qt(theme['theme-qt'])
    except Exception as e:
        print(f'Couldn\'t change theme qt, Error {e}')

    try:
        change.change_live(theme['theme-gtk'],
                           theme['icons'], theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk LIVE, Error {e}')

    # TODO: Function that reads window manager, and restarts the display

    # os.system('bspc wm -r')

    return 'Successfully changed theme to {theme[\'current_theme\']}'


if __name__ == "__main__":
    debug()
