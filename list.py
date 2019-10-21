
import persistence.database

from persistence.database import HostDefEntity, KeyAuthEntity

from mcstatus import MinecraftServer

def ping(host):
    return MinecraftServer.lookup(f"{host.host}:{host.query_port}").ping()


def display_host(host):
    print(f"""## Server #####
    host: {host.host}
    ping: {ping(host)}
    """)

def list_hosts():
    print("Listing data...")
    return HostDefEntity.select().join(KeyAuthEntity)

if __name__ == '__main__':
    for host in list_hosts():
        display_host(host)
