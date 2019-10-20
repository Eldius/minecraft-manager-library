from mcrcon import MCRcon

from contextlib import contextmanager

@contextmanager
def execute_rcon_commands(host):
    mcr = MCRcon(host=host.host, password=host.rcon_pass, port=host.rcon_port)
    mcr.connect()
    try:
        yield mcr
    except:
        mcr.disconnect()
        raise
    else:
        mcr.disconnect()
