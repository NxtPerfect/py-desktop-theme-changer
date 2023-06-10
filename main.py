import config

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


if __name__ == "__main__":
    run()
