# py-desktop-theme-changer
## This script is made to automate changing themes to one button for window manager Linux users

### How does it work?
To your polybar config, add new module/script, with

```python:
label = %output%
exec = /usr/bin/python /path/to/startup.py
click-left = /usr/bin/python /path/to/main.py
```

Your config.toml file should be inside your polybar folder ~/.config/polybar/config.toml, If config file is correctly configured, your themes should change to ones in that file, and restart your window manager display.

### How to install

### Supported WM
- bspwm
- i3
- dwm
- xmonad

### Dependencies
- xsettingsd
- gtk3/gtk4
- qt5
- python
- python toml
Install xsettingsd with your distro's package manager

Fedora
```sudo dnf install xsettingsd```

Install toml for python
```pip install toml```

### Why?
I wanted to create a script that would change my themes with a press of a button on my bspwm, that i could then run from polybar.

### Is it overengineered, way too complicated, and I could've just used something else?
Yea, most likely yes, the code probably can be optimized or written way better but honestly, so what? It's a project I've taken all on my own and I just wanted to make it for myself. If anyone wants to improve it, sees some issue or wants to suggest set of features, you're free to use github issues.
