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


class KeyAuth(object):
    def __init__(self, user, key_filename):
        self.user = user
        self.key_filename = key_filename
