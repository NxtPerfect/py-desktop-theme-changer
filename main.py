import src.config
import src.backup
import src.change
import src.windowmanager

DEFAULT_PATH = '$XDG_CONFIG_HOME/theme-switcher/config.toml'


def debug():
    try:
        src.backup.create_backup()
    except Exception:
        print('Couldn\'t create backup, Error {e}', flush=True)
        exit()

    try:
        src.windowmanager.read_window_manager()
    except Exception as e:
        print(f'Couln\'t read window manager, Error {e}', flush=True)
        exit()

    theme = 'light'
    try:
        theme = src.config.read_themes_configuration('./config.toml')
    except Exception as e:
        print(f'Couldn\'t find config file, Error {e}', flush=True)
        exit()
    print(f'Config read {theme}')

    try:
        src.config.write_current_theme(
            './config.toml', src.config.read_current_theme('./config.toml'))
    except Exception as e:
        print(f'Couldn\'t write to file, Error {e}', flush=True)

    try:
        src.change.change_wallpaper(theme['wallpaper'])
    except Exception as e:
        print(f'Couldn\'t set wallpaper, Error {e}', flush=True)

    try:
        src.change.change_pointer(theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change pointer, Error {e}', flush=True)

    try:
        src.change.change_icons(theme['icons'])
    except Exception as e:
        print(f'Couldn\'t change icons, Error {e}', flush=True)

    try:
        src.change.change_theme_gtk(theme['theme-gtk'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk, Error {e}', flush=True)

    try:
        src.change.change_theme_qt(theme['theme-qt'])
    except Exception as e:
        print(f'Couldn\'t change theme qt, Error {e}', flush=True)

    try:
        src.change.change_live(theme['theme-gtk'],
                               theme['icons'], theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk LIVE, Error {e}', flush=True)

    return 'Successfully changed theme to {theme[\'current_theme\']}'


if __name__ == "__main__":
    debug()
