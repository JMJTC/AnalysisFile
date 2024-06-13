import sqlite3


class DatabaseHandler:
    def __init__(self, db_name="data_analysis.db"):
        self.db_name = db_name
        self.conn = self.connect_db()
        self.create_table()

    def connect_db(self):
        """Connect to the SQLite database. If the database does not exist, it will be created."""
        try:
            conn = sqlite3.connect(self.db_name)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the table if it does not exist."""
        try:
            query = """
            CREATE TABLE IF NOT EXISTS Data (
                id INTEGER PRIMARY KEY,
                field1 TEXT,
                field2 TEXT,
                field3 TEXT,
                field4 TEXT
            )
            """
            self.conn.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def save_data(self, data):
        """Save data from a DataFrame to the SQLite database."""
        try:
            for _, row in data.iterrows():
                query = "INSERT INTO Data (field1, field2, field3, field4) VALUES (?, ?, ?, ?)"
                self.conn.execute(query, tuple(row))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error saving data: {e}")

    def filter_data(self, conditions):
        """Filter data from the database based on conditions."""
        try:
            query = "SELECT * FROM Data WHERE " + " AND ".join(conditions)
            cursor = self.conn.execute(query)
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error filtering data: {e}")
            return []

    def close(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
