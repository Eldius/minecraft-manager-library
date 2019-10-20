
from remote.model import HostDef, KeyAuth
from remote.ssh import execute_as_ssh
import sys

if __name__ == '__main__':
    auth = KeyAuth(user='root', key_filename='/home/eldius/.ssh/id_rsa.pub')
    host = HostDef(host='159.65.160.193', ssh_port=22, auth=auth)

    def execute_cmd(ssh, cmd):
        stdin,stdout,stderr = ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print(stderr.read().decode('utf-8'), file=sys.stderr)
        else:
            print(stdout.read().decode('utf-8'))

    with execute_as_ssh(host) as ssh:
        print("---")
        execute_cmd(ssh, "ls -la")
        print("---")
        execute_cmd(ssh, "ls -la /")
        print("---")
        execute_cmd(ssh, "ls -la /servers")
        print("---")
        execute_cmd(ssh, "ls -la /servers/minecraft")
        print("---")
        execute_cmd(ssh, "ls -la /servers_with_error")
        print("---")

    print(f"Still connected? {host.is_ssh_connected()}")
