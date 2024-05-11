import os
os.adddlldirectory('path/to/site-packages/clidriver/bin')
import json
import ibm_db

def main():
    try:
        with open('./db2.json') as f:
            data = json.load(f)
        print("Read the file successfully\n")
    except Exception as e:
        print("Error reading the file:", e)
        return
    database = data["database"]
    hostname = data["host"]
    port = data["port"]
    uid = data["user"]
    pwd = data["password"]
    conn_str = f"DATABASE={database};HOSTNAME={hostname};PORT={port};UID={uid};PWD={pwd};security=ssl"
    try:
        print("Trying to connect...")
        conn = ibm_db.connect(conn_str, '', '')
        print("Connected successfully!")
        ibm_db.close(conn)
    except Exception:
        errorMsg = ibm_db.conn_errormsg()
        print(errorMsg)
if __name__ == "__main__":
    main()