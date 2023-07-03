import src.config
from src.change import HOME

if __name__ == "__main__":
    match src.config.read_current_theme(HOME + '/.config/polybar/config.toml'):
        case 'dark_theme':
            print('dark')
        case 'light_theme':
            print('light')
        case _:
            print('no theme')
