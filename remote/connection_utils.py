from contextlib import contextmanager
from jinja2 import Template

from paramiko import SSHClient, SFTPClient
import paramiko

import jinja2
import sys

def _open_ssh_connection(host):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host.host,
        port=host.ssh_port,
        username=host.auth.user,
        key_filename=host.auth.key_filename,
    )
    return ssh


def _open_sftp_connection(host):
    return _open_ssh_connection(host).open_sftp()


def parse_template(host, file, extra_parameters=dict(), searchpath="./templates"):
    templateLoader = jinja2.FileSystemLoader(searchpath=searchpath)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template(file)
    parameters = extra_parameters.copy()
    parameters['host'] = host
    return template.render(parameters)


def execute_ssh_command(ssh, cmd):
    stdin,stdout,stderr = ssh.exec_command(cmd)
    if stderr.channel.recv_exit_status() != 0:
        print(stderr.read().decode('utf-8'), file=sys.stderr)
    else:
        print(stdout.read().decode('utf-8'))


def execute_ssh_script_template(ssh, template_file, host, extra_parameters=dict()):
    rendered_script = parse_template(
        host=host,
        file=template_file,
        extra_parameters=extra_parameters,
    )
    stdin,stdout,stderr = ssh.exec_command(rendered_script)
    if stderr.channel.recv_exit_status() != 0:
        print(stderr.read().decode('utf-8'), file=sys.stderr)
    else:
        print(stdout.read().decode('utf-8'))


@contextmanager
def execute_as_ssh(host):
    ssh = _open_ssh_connection(host)
    try:
        yield ssh
    except:
        ssh.close()
        raise
    else:
        ssh.close()

@contextmanager
def execute_as_sftp(host):
    sftp = _open_sftp_connection(host)
    try:
        yield sftp
    except:
        sftp.close()
        raise
    else:
        sftp.close()
