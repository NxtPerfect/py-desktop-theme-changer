import src.config
import src.backup
import src.change
import src.windowmanager


def run():
    try:
        src.backup.create_backup()
    except Exception:
        print('Couldn\'t create backup, Error {e}')
        exit()

    try:
        src.windowmanager.read_window_manager()
    except Exception as e:
        print(f'Couln\'t read window manager, Error {e}')
        exit()

    theme = 'light'
    try:
        theme = src.config.read_themes_configuration(
            src.change.HOME + '/.config/polybar/config.toml')
    except Exception as e:
        print(f'Couldn\'t find config file, Error {e}')
        exit()

    try:
        src.config.write_current_theme(
            src.change.HOME + '/.config/polybar/config.toml', src.config.read_current_theme(src.change.HOME + '/.config/polybar/config.toml'))
    except Exception as e:
        print(f'Couldn\'t write to file, Error {e}')

    try:
        src.change.change_wallpaper(theme['wallpaper'])
    except Exception as e:
        print(f'Couldn\'t set wallpaper, Error {e}')

    try:
        src.change.change_pointer(theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change pointer, Error {e}')

    try:
        src.change.change_icons(theme['icons'])
    except Exception as e:
        print(f'Couldn\'t change icons, Error {e}')

    try:
        src.change.change_theme_gtk(theme['theme-gtk'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk, Error {e}')

    try:
        src.change.change_theme_qt(theme['theme-qt'])
    except Exception as e:
        print(f'Couldn\'t change theme qt, Error {e}')

    try:
        src.change.change_live(theme['theme-gtk'],
                               theme['icons'], theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk LIVE, Error {e}')


if __name__ == "__main__":
    run()
