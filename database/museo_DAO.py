from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""
class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    @staticmethod
    def leggi_musei():
        print("Executing read from database using SQL query")
        results = []
        cnx = None
        cursor = None

        try:
            cnx = ConnessioneDB.get_connection()
            if cnx is None:
                print("Connection failed")
                return None

            cursor = cnx.cursor(dictionary=True)
            query = "SELECT * FROM museo"
            cursor.execute(query)

            for row in cursor:
                museo = Museo(row["id"], row["nome"], row["tipologia"])
                results.append(museo)

        except Exception as e:
            print(f"Database error: {e}")
            return None

        finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
        return results
