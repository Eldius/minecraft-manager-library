
from remote.model import HostDef, KeyAuth

import peewee

# Aqui criamos o banco de dados
db = peewee.SqliteDatabase('minecraft_hosts.db')


def from_model(model):
    if isinstance(model, HostDef):
        result = HostDefEntity()
        result.host = model.host
        result.ssh_port = model.ssh_port
        result.query_port = model.query_port
        result.rcon_port = model.rcon_port
        result.rcon_pass = model.rcon_pass
        result.install_folder = model.install_folder
        result.auth = from_model(model.auth)
        return result
    elif isinstance(model, KeyAuth):
        result = KeyAuthEntity()
        result.user = model.user
        result.key_filename = model.key_filename
        return result
    else:
        return None


def to_model(entity):
    if isinstance(entity, HostDefEntity):
        return HostDef(
            host=entity.host,
            ssh_port=entity.ssh_port,
            query_port=entity.query_port,
            rcon_port=entity.rcon_port,
            rcon_pass=entity.rcon_pass,
            install_folder=entity.install_folder,
            auth=to_model(entity.auth),
        )
    elif isinstance(entity, KeyAuthEntity):
        return KeyAuth(
            user=entity.user,
            key_filename=entity.key_filename
        )


class BaseModel(peewee.Model):
    class Meta:
        database = db


class KeyAuthEntity(BaseModel):
    user = peewee.CharField()
    key_filename = peewee.CharField()


class HostDefEntity(BaseModel):
    host = peewee.CharField()
    ssh_port = peewee.IntegerField()
    query_port = peewee.IntegerField()
    rcon_port = peewee.IntegerField()
    rcon_pass = peewee.CharField()
    install_folder = peewee.CharField()

    auth = peewee.ForeignKeyField(KeyAuthEntity)


try:
    KeyAuthEntity.create_table()
    print("KeyAuth table created with success...")
except peewee.OperationalError:
    print("KeyAuth table already exists...")

try:
    HostDefEntity.create_table()
    print("HostDef table created with success...")
except peewee.OperationalError:
    print("HostDef table already exists...")
