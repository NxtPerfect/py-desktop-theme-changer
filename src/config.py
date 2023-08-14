import toml


def read_themes_configuration(file):
    try:
        with open(file, 'r') as configfile:
            try:
                data = toml.load(configfile)
            except Exception as e:
                print(f'failed, {e}')
                return -1
            return data['dark_theme'] if data['runtime']['current_theme'] == 'light_theme' else data['light_theme']
    except FileNotFoundError or PermissionError:
        return -1


def read_modules(file):
    try:
        with open(file, 'r') as configfile:
            try:
                data = toml.load(configfile)
            except Exception as e:
                print(f'failed modules, {e}')
                return -1
            return data['runtime']['modules']
    except FileNotFoundError or PermissionError:
        return -1


def read_current_theme(file):
    try:
        with open(file, 'r') as configfile:
            try:
                data = toml.load(configfile)
            except Exception as e:
                print(f'failed, {e}')
                return -2
            return data['runtime']['current_theme']
    except FileNotFoundError or PermissionError:
        return -1


def write_current_theme(file, theme):
    match theme:
        case 'dark_theme':
            theme = 'light_theme'
        case 'light_theme':
            theme = 'dark_theme'
        case _:
            return -1

    try:
        with open(file, 'r') as configfile:
            data = toml.load(configfile)
            data['runtime']['current_theme'] = theme
    except FileNotFoundError or PermissionError:
        return -1

    try:
        with open(file, 'w') as configfile:
            toml.dump(data, configfile)
    except FileNotFoundError or PermissionError:
        return -1
