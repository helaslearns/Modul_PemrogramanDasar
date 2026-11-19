import os
import sys

# Agar `import validasi`, `import main`, `from repository...` bisa ditemukan
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest


class FakeCursor:
    def __init__(self, conn):
        self.conn = conn
        self.lastrowid = conn.lastrowid
        self.rowcount = conn.rowcount

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def execute(self, sql, params=None):
        self.conn.executed.append((sql, params))
        if self.conn.fail_on == len(self.conn.executed):
            raise self.conn.error

    def fetchall(self):
        return self.conn.rows

    def fetchone(self):
        return self.conn.rows[0] if self.conn.rows else None


class FakeConnection:
    def __init__(self, lastrowid=1, rowcount=1, rows=None,
                 fail_on=None, error=None):
        self.lastrowid = lastrowid
        self.rowcount = rowcount
        self.rows = rows or []
        self.fail_on = fail_on          # execute() ke-n yang akan gagal (mulai 1)
        self.error = error or RuntimeError("gagal")
        self.executed = []
        self.committed = False
        self.rolled_back = False
        self.closed = False

    def cursor(self):
        return FakeCursor(self)

    def commit(self):
        self.committed = True

    def rollback(self):
        self.rolled_back = True

    def close(self):
        self.closed = True


class FakeDatabase:
    def __init__(self, conn):
        self.conn = conn
        self.jumlah_connect = 0

    def connect(self):
        self.jumlah_connect += 1
        return self.conn


@pytest.fixture
def buat_db():
    """Pemakaian: db, conn = buat_db(rowcount=0)"""
    def _buat(**kwargs):
        conn = FakeConnection(**kwargs)
        return FakeDatabase(conn), conn
    return _buat