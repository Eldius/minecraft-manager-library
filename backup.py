from remote.model import HostDef, KeyAuth
from remote.connection_utils import execute_as_ssh, execute_ssh_command, execute_ssh_script_template
import sys

if __name__ == '__main__':
    auth = KeyAuth(user='root', key_filename='/home/eldius/.ssh/id_rsa.pub')
    host = HostDef(host='159.65.160.193', ssh_port=22, auth=auth)

    with execute_as_ssh(host) as ssh:
        print("###")
        execute_ssh_script_template(ssh=ssh, template_file="test_script.sh", host=host, extra_parameters=dict(servers_folder='/servers/minecraft'))
        print("###")

    print(f"Still connected? {host.is_ssh_connected()}")
