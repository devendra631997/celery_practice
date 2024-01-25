import duckdb
con = duckdb.connect("storage/duck_db/duck_db_staorage_file.db")
def execute_query(query:str):
        return con.sql(query)