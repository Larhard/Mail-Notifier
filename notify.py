import notify2
import subprocess
import config


def init(program):
    notify2.init(program)


def send(title, message):
    notify2.Notification(title, message).show()
    if config.sounds and config.sound_cmd:
        subprocess.call(config.sound_cmd, shell=True)
