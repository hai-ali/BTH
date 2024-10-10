# 1) Du behöver definiera dessa 3 variabler:

server_hostname = 'adb-6283305705355295.15.azuredatabricks.net'
http_path = '/sql/1.0/warehouses/43943fff51032788'
token = {du hämtar denna under Settings > Developer > Access tokens}

# 2) Sedan få ut en connection string, ska ha följande format:

def get_connection_string(self):
    return (f"databricks://token:{self._tkn}@{self._server_hostname}:443?http_path={self._http_path}")


# 3) Skicka in connection string i sqlalchemy & kör den
engine = sqlalchemy.create_engine(storage.get_connection_string())
engine.connect().execution_options(stream_results=True)