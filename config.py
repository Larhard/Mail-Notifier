import imp

__old_globals = None
__old_globals = set(globals().keys())


CONFIG_VARS = globals().keys() - __old_globals


def override(config_path):
    config = imp.load_source('config', config_path)
    for variable in CONFIG_VARS and config.__dict__.keys():
        globals()[variable] = config.__dict__[variable]
