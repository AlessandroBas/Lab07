from database.DB_connect import ConnessioneDB
from model.artefattoDTO import Artefatto

"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
      def __init__(self):
         pass

      # TODO
      def leggi_artefatti_filtrati(self, museo:str, epoca:str) -> list[Artefatto] | None:
          results = []
          cnx = None
          cursor = None
          try:
              cnx = ConnessioneDB.get_connection()
              if cnx is None:
                  print("Connection failed")
                  return None
              else:
                  cursor = cnx.cursor(dictionary=True)
                  if museo=="Nessun Filtro":
                      museo=None
                  if epoca=="Nessun Filtro":
                      epoca=None

                  query = """SELECT a.*
                             FROM artefatto a, museo m
                             WHERE m.nome=COALESCE(%s,m.nome) 
                             AND a.epoca=COALESCE(%s,a.epoca) 
                             AND a.id_museo=(m.id-14)"""

                  cursor.execute(query,(museo,epoca))
                  for row in cursor:
                      artefatto = Artefatto(row["id"], row["nome"], row["tipologia"], row["epoca"],row["id_museo"])
                      results.append(artefatto)

          except Exception as e:
              print(f"Database error: {e}")
              return None
          finally:
              if cursor:
                  cursor.close()
              if cnx:
                  cnx.close()
          return results

      @staticmethod
      def leggi_epoche():
          print("Executing read from database using SQL query")
          cnx = None
          cursor = None

          try:
              cnx = ConnessioneDB.get_connection()
              if cnx is None:
                  print("Connection failed")
                  return None
              else:
                  cursor = cnx.cursor()
                  query = """SELECT DISTINCT epoca FROM artefatto """
                  cursor.execute(query)
                  results = cursor.fetchall()
          except Exception as e:
            print(f"Database error: {e}")
            return None
          finally:
            if cursor:
                cursor.close()
            if cnx:
                cnx.close()
          return results