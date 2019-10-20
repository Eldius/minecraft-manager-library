from contextlib import contextmanager

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
