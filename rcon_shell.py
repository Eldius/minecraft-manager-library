
from rcon.commands import execute_rcon_commands

from utils.params_parser import parse_args

if __name__ == '__main__':
    host = parse_args()

    with execute_rcon_commands(host) as mcr:
        cmd = ""
        while cmd != "exit":
            cmd = input("$> ")
            print(mcr.command(cmd))
