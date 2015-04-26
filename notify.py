import logging
import notify2
import subprocess
import config

logger = logging.getLogger('notify')


def init(program):
    notify2.init(program)


def send(title, message):
    logger.info('send notify "{}" "{}"'.format(title, message))
    notify2.Notification(title, message).show()
    if config.sounds and config.sound_cmd:
        logger.info('play sound "{}"'.format(config.sound_cmd))
        subprocess.call(config.sound_cmd, shell=True)
