__old_globals = None
__old_globals = set(globals().keys())

sounds = None
sound_cmd = None

CONFIG_VARS = globals().keys() - __old_globals


def override(config):
    for variable in CONFIG_VARS & config.keys():
        globals()[variable] = config[variable]
