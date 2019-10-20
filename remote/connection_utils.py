from contextlib import contextmanager
from jinja2 import Template

import jinja2
import sys

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
    ssh = host._get_ssh_connection()
    try:
        yield ssh
    except:
        ssh.close()
        host.disconnect_ssh()
        raise
    else:
        ssh.close()
        host.disconnect_ssh()

@contextmanager
def execute_as_sftp(host):
    sftp = host._get_sftp_connection()
    try:
        yield sftp
    except:
        sftp.close()
        host.disconnect_sftp()
        raise
    else:
        sftp.close()
        host.disconnect_sftp()
