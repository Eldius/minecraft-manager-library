
import persistence.database

from persistence.database import HostDefEntity, KeyAuthEntity, from_model, db

from utils.params_parser import parse_args

from mcstatus import MinecraftServer

def persist(host):
    print("Persisting data...")
    entity = from_model(host)
    entity.auth.save(force_insert=True)
    entity.save(force_insert=True)


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
    with db.atomic() as txn:
        persist(parse_args())
        for host in list_hosts():
            display_host(host)
