
from remote.model import HostDef, KeyAuth
from remote.ssh import execute_as_ssh

if __name__ == '__main__':
    auth = KeyAuth(user='root', key_filename='/home/eldius/.ssh/id_rsa.pub')
    host = HostDef(host='159.65.160.193', port=22, auth=auth)

    with execute_as_ssh(host) as ssh:
        cmd = "ls -la"
        stdin,stdout,stderr = ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            #print(stderr.read().replace("\n", "\\n"))
            print(stderr.read().decode('utf-8'))
        else:
            #print(stdout.read().replace("\n", "\\n"))
            print(stdout.read().decode('utf-8'))
