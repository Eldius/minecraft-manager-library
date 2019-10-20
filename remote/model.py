from paramiko import SSHClient, SFTPClient
import paramiko


class HostDef(object):
    def __init__(
        self,
        host,
        ssh_port,
        auth,
        rcon_port=None,
        rcon_pass=None,
        install_folder='/servers/minecraft',
    ):
        self.host = host
        self.ssh_port = ssh_port
        self.auth = auth
        self.ssh = None
        self.sftp = None
        self.rcon_port = rcon_port
        self.rcon_pass = rcon_pass
        self.install_folder = install_folder

    def is_ssh_connected(self):
        return (
            (self.ssh != None)
            and (self.ssh.get_transport() is not None)
            and self.ssh.get_transport().is_active()
        )

    def connect_ssh(self):
        if not self.is_ssh_connected():
            self.ssh = self.auth._open_ssh_connecion(self)

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

    def is_sftp_connected(self):
        return (
            (self.sftp != None)
            and (self.sftp.get_transport() is not None)
            and self.sftp.get_transport().is_active()
        )

    def connect_sftp(self):
        if not self.is_sftp_connected():
            self.sftp = self.auth._open_sftp_connecion(self)

    def disconnect_sftp(self):
        if self.is_sftp_connected():
            self.sftp.close()
        self.sftp = None

    def _get_sftp_connection(self):
        if not self.is_sftp_connected():
            self.connect_sftp()
        return self.sftp

    def execute_as_sftp(self, command):
        if not self.is_sftp_connected():
            connect_sftp()
        self.sftp.exec_command(command)


class KeyAuth(object):
    def __init__(self, user, key_filename):
        self.user = user
        self.key_filename = key_filename

    def _open_ssh_connecion(self, host):
        ssh = SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host.host, port=host.ssh_port, username=self.user, key_filename=self.key_filename)
        return ssh

    def _open_sftp_connecion(self, host):
        sftp = SFTPClient()
        sftp.load_system_host_keys()
        sftp.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sftp.connect(hostname=host.host, port=host.ssh_port, username=self.user, key_filename=self.key_filename)
        return sftp
