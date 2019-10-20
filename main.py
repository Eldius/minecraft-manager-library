
from remote.model import HostDef, KeyAuth
from remote.model import HostDef, KeyAuth
from remote.connection_utils import execute_as_ssh, execute_ssh_command, execute_ssh_script_template
from utils.params_parser import parse_args

if __name__ == '__main__':
    host = parse_args()

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
