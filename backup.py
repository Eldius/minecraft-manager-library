from remote.model import HostDef, KeyAuth
from remote.connection_utils import execute_as_ssh, execute_ssh_command, execute_ssh_script_template, execute_as_sftp
from rcon.commands import execute_rcon_commands
import argparse

import sys

def backup_minecraft_server(host):
    with execute_rcon_commands(host) as mcr:
        print("---")
        print(f"save-all:")
        print(mcr.command("/save-all"))
        print("---")
        print(f"save-off:")
        print(mcr.command("/save-off"))

    with execute_as_ssh(host) as ssh:
        print("###")
        print("create package")
        execute_ssh_script_template(
            ssh=ssh,
            template_file="create_minecraft_backup_package.sh",
            host=host,
        )
    with execute_as_sftp(host) as sftp:
        print("###")
        print("get package")
        sftp.get(f"{host.install_folder}/../minecraft.tar.bz2", args.dest_folder)
        print("###")
        print("remove package")
        sftp.remove(f"{host.install_folder}/../minecraft.tar.bz2")
        print("###")

    with execute_rcon_commands(host) as mcr:
        print("---")
        print(f"save-on:")
        print(mcr.command("/save-on"))


if __name__ == '__main__':
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
        "--dest-folder",
        type=str,
        help="The folder to put backup package",
    )
    parser.add_argument(
        "--install-folder",
        type=str,
        help="The folder where Minecraft was installed",
    )
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

    backup_minecraft_server(host)
