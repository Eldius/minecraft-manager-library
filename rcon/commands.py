from mcrcon import MCRcon

from contextlib import contextmanager

@contextmanager
def execute_rcon_commands(host):
    mcr = MCRcon(host.rcon_port, host.rcon_pass)
    try:
        yield mcr
    except:
        mcr.disconnect()
        raise
    else:
        mcr.disconnect()
