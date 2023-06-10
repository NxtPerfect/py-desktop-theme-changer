import toml
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


def read_themes_configuration(file):
    try:
        with open(file, 'rb') as configfile:
            try:
                data = tomllib.load(configfile)
            except tomllib.TOMLDecodeError as e:
                print(f'failed, {e}')
                return -1
            print(f'{data["runtime"]}')

            return data['light_theme'] if data['runtime']['current_theme'] == 'light_theme' else data['dark_theme']
    except FileNotFoundError:
        return -1  # Couldn't read file


def read_current_theme(file):
    try:
        with open(file, 'rb') as configfile:
            try:
                data = tomllib.load(configfile)
            except tomllib.TOMLDecodeError as e:
                print(f'failed, {e}')
                return -1
            return data['runtime']['current_theme']
    except FileNotFoundError:
        return -1


def write_current_theme(file, theme):
    if theme == 'dark_theme':
        theme = 'light_theme'
    elif theme == 'light_theme':
        theme = 'dark_theme'
    else:
        return -1
    print(theme)

    try:
        with open(file, 'rb') as configfile:
            data = tomllib.load(configfile)
            data['runtime']['current_theme'] = theme
            print('Success!')
    except FileNotFoundError:
        return -1  # Couldn't read file
    try:
        with open(file, 'w') as configfile:
            print(data)
            toml.dump(data, configfile)

    except FileNotFoundError:
        return -2  # Couldn't write to file
