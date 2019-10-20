from remote.model import HostDef, KeyAuth
from remote.connection_utils import execute_as_ssh, execute_ssh_command, execute_ssh_script_template, execute_as_sftp
from rcon.commands import execute_rcon_commands
from utils.params_parser import parse_backup_args

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
    args = parse_backup_args()

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
