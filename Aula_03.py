import mysql.connector

# Conectando ao banco de dados
con = mysql.connector.connect(host='localhost', database='sakila', user='root', password='root')

tabela_contatos = """
    CREATE TABLE IF NOT EXISTS contatos(
        nome VARCHAR(50),tel varchar(40)
    )
"""

tabela_emails = """ 
    CREATE TABLE IF NOT EXISTS emails(
        id INT AUTO_INCREMENT PRIMARY KEY,
        dono VARCHAR(50)
    )
"""

cursor = con.cursor()
cursor.execute(tabela_contatos)
cursor.execute(tabela_emails)

sql = 'INSERT INTO contatos (nome, tel) VALUES (%s, %s)'
args = ('joao', '1234-56789')

cursor.execute(sql, args)

cursor.execute('INSERT INTO contatos (nome, tel) VALUES(%s,%s) ', ('maria', '9876-54321'))
cursor.execute('INSERT INTO contatos (nome, tel) VALUES(%s,%s) ', ('jose', '4567-8901'))
cursor.execute('INSERT INTO contatos (nome, tel) VALUES(%s,%s) ', ('ana', '6543-2109'))

con.commit()

sql= 'SELECT tel, nome FROM contatos'

cursor.execute(sql)

for contato in cursor.fetchall():
    print(contato)

con.close()
print("conectado")