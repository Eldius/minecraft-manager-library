
from remote.model import HostDef, KeyAuth, execute_as_ssh

if __name__ == '__main__':
    auth = KeyAuth(user='root', key_filename='~/.ssh/id_rsa.pub')
    host = HostDef(host='159.65.160.193', port=22, auth=auth)

with execute_as_ssh(host) as ssh:
    cmd = "ls -la"
    stdin,stdout,stderr = ssh.exec_command(cmd)
    if stderr.channel.recv_exit_status() != 0:
        print(stderr.read())
    else:
        print(stdout.read())
