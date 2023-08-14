import subprocess as sb
import os


def read_window_manager():
    output = sb.run(['wmctrl', '-m'], text=True,
                    stdout=sb.PIPE, stderr=sb.PIPE)
    namestr = output.stdout.split('\n')[0]
    return namestr.split(' ')[1]


def reset_display(window_manager):
    match window_manager:
        case 'bspwm':
            command = 'bspc wm -r'
        case 'i3':
            command = 'i3-msg reload'
            # command = 'i3-msg restart'
        case 'dwm':
            command = 'pkill dwm; dwm'
        case 'xmonad':
            command = 'xmonad --restart'
        case _:
            print(
                f'Unsupported window manager of type {window_manager}, this script doesn\'t work with wayland.')
            print(
                'Check github of the project to see which window managers are supported')
            return -1

    try:
        os.system(command)
    except Exception as e:
        return e
