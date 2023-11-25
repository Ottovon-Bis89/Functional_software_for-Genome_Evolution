#Logger written by Caitlins short :)

import logging

log = logging.getLogger("applogger")
log.setLevel(logging.ERROR)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)
formatter = logging.Formatter("L%(lineno)d [%(filename)s] > %(message)s",)
consoleHandler.setFormatter(formatter)
log.addHandler(consoleHandler)
