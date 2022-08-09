import sqlite3 as sql


class TransactionObject():
    database = "clientes.db"
    conn = None
    cur = None
    connected = False

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False


def initDB():
    trans = TransactionObject()
    trans.connect()
    trans.execute(
        "CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nome TEXT, endereco TEXT, vacinas TEXT, data TEXT, telefone TEXT)")
    trans.persist()
    trans.disconnect()


def insert(nome, endereco, vacinas, data, telefone):
    trans = TransactionObject()
    trans.connect()
    trans.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?,?)",
                  (nome, endereco, vacinas, data, telefone))
    trans.persist()
    trans.disconnect()


def view():
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes")
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def search(nome="", endereco="", vacinas="", data="", telefone=""):
    trans = TransactionObject()
    trans.connect()
    trans.execute("SELECT * FROM clientes WHERE nome=? or endereco=? or vacinas=? or data=? or telefone=?",
                  (nome, endereco, vacinas, data, telefone))
    rows = trans.fetchall()
    trans.disconnect()
    return rows


def delete(id):
    trans = TransactionObject()
    trans.connect()
    trans.execute("DELETE FROM clientes WHERE id = ?", (id,))
    trans.persist()
    trans.disconnect()


def update(id, nome, endereco, vacinas, data, telefone):
    trans = TransactionObject()
    trans.connect()
    trans.execute("UPDATE clientes SET nome =?, endereco=?, vacinas=?, data=?, telefone=? WHERE id = ?",
                  (nome, endereco, vacinas, data, telefone, id))
    trans.persist()
    trans.disconnect()


initDB()
