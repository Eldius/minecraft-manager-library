from contextlib import contextmanager

@contextmanager
def execute_as_ssh(host):
    ssh = host._get_ssh_connection()
    try:
        yield ssh
    except:
        ssh.close()
        raise
    else:
        ssh.close()
