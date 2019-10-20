from paramiko import SSHClient
import paramiko


class HostDef(object):
    def __init__(self, host, ssh_port, auth):
        self.host = host
        self.ssh_port = ssh_port
        self.auth = auth
        self.ssh = None

    def is_ssh_connected(self):
        return (
            (self.ssh != None)
            and (self.ssh.get_transport() is not None)
            and self.ssh.get_transport().is_active()
        )

    def connect_ssh(self):
        if not self.is_ssh_connected():
            self.ssh = self.auth.get_connection(self)

    def disconnect_ssh(self):
        if self.is_ssh_connected():
            self.ssh.close()
        self.ssh = None

    def _get_ssh_connection(self):
        if not self.is_ssh_connected():
            self.connect_ssh()
        return self.ssh

    def execute_as_ssh(self, command):
        if not self.is_ssh_connected():
            connect_ssh()
        self.ssh.exec_command(command)


class KeyAuth(object):
    def __init__(self, user, key_filename):
        self.user = user
        self.key_filename = key_filename

    def get_connection(self, host):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host.host, port=host.ssh_port, username=self.user, key_filename=self.key_filename)
        return ssh
