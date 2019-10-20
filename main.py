
from remote.model import HostDef, KeyAuth
from remote.model import HostDef, KeyAuth
from remote.connection_utils import execute_as_ssh, execute_ssh_command, execute_ssh_script_template

import argparse

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
    )

    with execute_as_ssh(host) as ssh:
        print("---")
        execute_ssh_command(ssh, "ls -la")
        print("---")
        execute_ssh_command(ssh, "ls -la /")
        print("---")
        execute_ssh_command(ssh, "ls -la /servers")
        print("---")
        execute_ssh_command(ssh, "ls -la /servers/minecraft")
        print("---")
        execute_ssh_command(ssh, "ls -la /servers_with_error")
        print("---")
        print("###")
        execute_ssh_script_template(ssh=ssh, template_file="test_script.sh", host=host, extra_parameters=dict(servers_folder='/servers/minecraft'))
        print("###")
