import src.config
import src.backup
import src.change
import src.windowmanager

HOME = src.change.HOME
CONFIG_PATH = HOME + '/.config/polybar/config.toml'


def run():
    try:
        src.backup.create_backup()
    except Exception:
        print('Couldn\'t create backup, Error {e}')
        exit()

    try:
        src.windowmanager.read_window_manager()
    except Exception as e:
        print(f'Couldn\'t read window manager, Error {e}')
        exit()

    theme = 'light'
    try:
        theme = src.config.read_themes_configuration(CONFIG_PATH)
    except Exception as e:
        print(f'Couldn\'t find config file, Error {e}')
        exit()

    try:
        src.config.write_current_theme(
            CONFIG_PATH, src.config.read_current_theme(CONFIG_PATH))
    except Exception as e:
        print(f'Couldn\'t write to file, Error {e}')

    modules = []
    try:
        modules = src.config.read_modules(CONFIG_PATH)
    except Exception as e:
        print(f'Couldn\'t read modules, Error {e}')

    # Determine what live change should happen
    is_wallpaper: bool = False
    is_pointer: bool = False
    is_icons: bool = False

    for module in modules:
        match module:
            case 'wallpaper':
                try:
                    src.change.change_wallpaper(theme['wallpaper'])
                except Exception as e:
                    print(f'Couldn\'t change wallpaper, Error {e}')
                is_wallpaper = True
            case 'pointer':
                try:
                    src.change.change_pointer(theme['pointer'])
                except Exception as e:
                    print(f'Couldn\'t change pointer, Error {e}')
                is_pointer = True
            case 'icons':
                try:
                    src.change.change_icons(theme['icons'])
                except Exception as e:
                    print(f'Couldn\'t change icons, Error {e}')
                is_icons = True
            case 'gtk':
                try:
                    src.change.change_theme_gtk(theme['theme-gtk'])
                except Exception as e:
                    print(f'Couldn\'t change theme gtk, Error {e}')
            case 'qt':
                try:
                    src.change.change_theme_qt(theme['theme-qt'])
                except Exception as e:
                    print(f'Couldn\'t change theme qt, Error {e}')
            case 'polybar':
                try:
                    src.change.change_polybar(theme['polybar-colors'])
                except Exception as e:
                    print(f'Couldn\'t change polybar colors, Error {e}')

    try:
        src.change.change_live(is_wallpaper, is_pointer, is_icons, theme)
        # src.change.change_live(theme['theme-gtk'],
        #                        theme['icons'], theme['pointer'])
    except Exception as e:
        print(f'Couldn\'t change theme gtk LIVE, Error {e}')

    try:
        src.windowmanager.reset_display(
            src.windowmanager.read_window_manager())
    except Exception:
        print('Couldn\'t reload window manager')


if __name__ == "__main__":
    run()
