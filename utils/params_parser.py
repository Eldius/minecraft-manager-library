import argparse

from remote.model import HostDef, KeyAuth

def _common_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--host",
        type=str,
        help="The server host",
    )
    parser.add_argument(
        "--ssh-user",
        type=str,
        help="The server SSH user",
    )
    parser.add_argument(
        "--ssh-key",
        type=str,
        help="The server SSH key file",
    )
    parser.add_argument(
        "--ssh-port",
        type=int,
        help="The server SSH port",
    )
    parser.add_argument(
        "--rcon-pass",
        type=str,
        help="The RCON pass",
    )
    parser.add_argument(
        "--rcon-port",
        type=int,
        help="The RCON port",
    )
    parser.add_argument(
        "--install-folder",
        type=str,
        help="The folder where Minecraft was installed",
    )
    return parser


def parse_args():
    parser = _common_args()
    args = parser.parse_args()

    auth = KeyAuth(
        user=args.ssh_user,
        key_filename=args.ssh_key,
    )
    host = HostDef(
        host=args.host,
        ssh_port=args.ssh_port,
        auth=auth,
        rcon_port=args.rcon_port,
        rcon_pass=args.rcon_pass,
        install_folder=args.install_folder,
    )
    return host


def parse_backup_args():
    parser = _common_args()
    parser.add_argument(
        "--dest-folder",
        type=str,
        help="The folder to put backup package",
    )
    return parser.parse_args()
