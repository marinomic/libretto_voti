import mysql.connector
from modello.voto_dto import VotoDto

class VotiDao:

    def get_all_voti(self):
        try:
            cnx = mysql.connector.connect(user='root',
                                          password='In@zMar&dB!',
                                          host='127.0.0.1',
                                          database='libretto')
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT *
                            FROM voti"""
            cursor.execute(query)
            result = []
            for row in cursor.fetchall():
                result.append(VotoDto(row["nome"],
                                                row["CFU"],
                                                row["punteggio"],
                                                bool(row["lode"]),
                                                row["data"]))
            cursor.close()
            return result
            # print(cursor.fetchall())

        except mysql.connector.Error as err:
            print(err)
        else:
             cnx.close


if __name__ == '__main__':
    voti_dao = VotiDao()
    voti_dao.get_all_voti()
