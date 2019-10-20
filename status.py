from utils.params_parser import parse_args
from mcstatus import MinecraftServer

if __name__ == '__main__':
    host = parse_args()
    print(f"Host: {host.host}")

    server = MinecraftServer.lookup(f"{host.host}:{host.query_port}")
    query = server.query()
    status = server.status()

    print(f"The server has {status.players.online} players and replied in {status.latency} ms")
    print(f"server latency: {server.ping()} ms")
    print(f"The server has the following players online: {', '.join(query.players.names)}")
