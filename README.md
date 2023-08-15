# py-desktop-theme-changer

## This script is made to automate changing themes to one button for window manager Linux users

### How does it work?

To your polybar config, add new module/script, with

```
label = %output%
exec = /usr/bin/python /path/to/startup.py
click-left = /usr/bin/python /path/to/main.py
```

Your config.toml file should be inside your polybar folder ~/.config/polybar/config.toml, If config file is correctly configured, your themes should change to ones in that file, and restart your window manager display.

### How to install

```
git clone https://github.com/NxtPerfect/py-desktop-theme-changer
cd py-desktop-theme-changer
pip install -r requirements.txt
sudo your-package-manager install-command xsettingsd feh
mkdir ~/.config/polybar/theme-changer
mv ./* ~/.config/polybar/theme-changer
```

You have to install xsettingsd and feh, which depends on what distribution you're running you have to find appropriate package on your own, for arch linux and fedora, it's xsettingsd, feh
now all you need to do is add new module/script into your polybar like in section [How does it work?](#how-does-it-work).
**Remember to change your example.toml file name to config.toml and change file paths, as well as put valid cursor, icon, theme and wallpaper.**

### Modularity

Inside `config.toml` there's a section `[runtime]`, inside of which you can find `modules` field, this determines what the script will change, available options:

- wallpaper - changes wallpaper with feh
- pointer - changes pointer
- icons - changes icons
- gtk - changes gtk theme
- qt - changes qt theme
- polybar - changes polybar color scheme (changes colors.ini, you should `include-file='./colors.ini'` inside of your polybar config, and use these colors for your bar for it to work)

### Supported WM

- bspwm
- i3
- dwm
- xmonad

### Dependencies

- xsettingsd
- feh
- gtk3/gtk4
- qt5
- python
- python toml

### Fedora

`sudo dnf install xsettingsd`

### Why?

I wanted to create a script that would change my themes with a press of a button on my bspwm, that i could then run from polybar.

### Is it overengineered, way too complicated, and I could've just used something else?

Yea, most likely yes, the code probably can be optimized or written way better but honestly, so what? It's a project I've taken all on my own and I just wanted to make it for myself. If anyone wants to improve it, sees some issue or wants to suggest set of features, you're free to use github issues.
