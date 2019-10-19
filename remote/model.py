from paramiko import SSHClient
import paramiko


class HostDef(object):
    def __init__(self, host, port, auth):
        self.host = host
        self.port = port
        self.auth = auth
        self.ssh = None

    def _is_ssh_connected(self):
        return (
            (self.ssh != None)
            and (ssh.get_transport() is not None)
            and ssh.get_transport().is_active()
        )

    def _connect_ssh(self):
        if not self._is_ssh_connected():
            self.ssh = self.auth.get_connection(self)

    def _disconnect_ssh(self):
        if self._is_ssh_connected():
            self.ssh.close()
        self.ssh = None

    def _get_ssh_connection(self):
        if not self._is_ssh_connected():
            self._connect_ssh()
        return self.ssh

    def execute_as_ssh(self, command):
        if not self._is_ssh_connected():
            _connect_ssh()
        self.ssh.exec_command(command)


class KeyAuth(object):
    def __init__(self, user, key_filename):
        self.user = user
        self.key_filename = key_filename

    def get_connection(self, host):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host.host, port=host.port, username=self.user, key_filename=self.key_filename)
        return ssh
