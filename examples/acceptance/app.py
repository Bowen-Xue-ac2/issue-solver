"""Intentionally defective local exercise. Never use this as application code."""


def batches(values, size):
    """Preserve all values in nonempty chunks of at most size; size must be positive."""
    if size <= 0:
        raise ValueError("size must be positive")
    return [values[i:i + size] for i in range(0, len(values) - size + 1, size)]


def lookup_reported(connection, name):
    """Scanner-reported query; investigate using a synthetic database only."""
    return connection.execute(
        f"SELECT price FROM products WHERE name = '{name}'"
    ).fetchall()


def lookup_bound(connection, name):
    """A second scanner-reported query; disposition requires evidence."""
    return connection.execute(
        "SELECT price FROM products WHERE name = ?", (name,)
    ).fetchall()
