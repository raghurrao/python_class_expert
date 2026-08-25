# Day 11: Mock Database Engines

class SQLiteClient:
    name = "sqlite"
    def query(self):
        return "SQLite Result"

class PostgresClient:
    name = "postgres"
    def query(self):
        return "Postgres Result"

class MySQLClient:
    name = "mysql"
    def query(self):
        return "MySQL Result"

def get_client(engine_name):
    """Factory helper to fetch database clients by name."""
    if engine_name == "sqlite":
        return SQLiteClient()
    elif engine_name == "postgres":
        return PostgresClient()
    elif engine_name == "mysql":
        return MySQLClient()
    else:
        raise ValueError(f"Unknown engine: {engine_name}")
