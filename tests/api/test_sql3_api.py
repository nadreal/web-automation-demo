import pytest
import sqlite3

@pytest.fixture(scope="session")
def sample_data():
    data = {'a':10, 'b':5}
    print (f"Data is set {data}")
    yield data    
    
@pytest.fixture(scope="module")
def db_connection():
    print("\n[SETUP] Opening SQLite connection...")
    conn = sqlite3.connect(":memory:")  # in-memory DB, no file created
    cursor = conn.cursor()

    # create dummy table
    cursor.execute("CREATE TABLE results (operation TEXT, a INT, b INT, result INT)")
    conn.commit()

    yield conn  # this is passed into tests

    print("\n[TEARDOWN] Closing SQLite connection...")
    conn.close()
    
def test_add_and_store(db_connection, sample_data):    
    result = sample_data['a'] + sample_data['b']
    
    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO results VALUES (?, ?, ?, ?)", ("add", sample_data['a'],sample_data['b'], result))
    db_connection.commit()    

    assert result == 15


def test_subtract_and_store(db_connection, sample_data):    
    result = sample_data['a'] - sample_data['b']

    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO results VALUES (?, ?, ?, ?)", ("Substract", sample_data['a'],sample_data['b'], result))
    db_connection.commit()

    assert result == 5
    
# 🔹 Verify that DB has 2 rows
def test_check_db_entries(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM results")
    rows = cursor.fetchall()

    print("DB rows:", rows)
    assert len(rows) == 2