import mysql.connector

con = mysql.connector.connect(host='localhost', database='atv2python', user='root', password='root')


table_author = """
    CREATE TABLE IF NOT EXISTS Author(
    id INT, nome VARCHAR(50), Primary Key(id)
    )
"""

table_post = """
    CREATE TABLE IF NOT EXISTS Post(
    id INT, title VARCHAR(50), created DATE, author_id INT, Primary Key(id), 
    Foreign Key(author_id) References Author(id)
    )
    """

cursor = con.cursor()
cursor.execute(table_author)
cursor.execute(table_post)


while True:

    soun = int(input("Deseja continuar? 1- Sim, 2- Não --> "))

    if soun == 1:

        ind = int(input("Qual tabela deseja utilizar? 1- Author, 2- Post --> "))

        ind2 = int(input("Digite a funcionalidade desejada: 1- Inserir, 2- Consultar, 3- Deletar, 4- Atualizar --> "))


        if ind == 1 and ind2 == 1:
            
            x = int(input("Digite o id do autor-->"))
            y = input("Digite o nome do autor-->")

            cursor.execute('INSERT INTO Author (id, nome) VALUES(%s,%s) ', (x, y))

            print("Autor inserido com sucesso!")

        elif ind == 2 and ind2 == 1:

            x = int(input("Digite o id do post-->"))
            y = input("Digite o título do post-->")
            z = input("Digite a data de criação do post-->")
            w = int(input("Digite o id do autor do post-->"))

            cursor.execute('INSERT INTO Post (id, title, created, author_id) VALUES(%s,%s,%s,%s) ', (x, y, z, w))

            print("Post inserido com sucesso!")

        elif ind == 1 and ind2 == 2:

            cursor.execute('SELECT * FROM Author')

            for author in cursor.fetchall():
                print(author)

        elif ind == 2 and ind2 == 2:

            cursor.execute('SELECT * FROM Post')

            for post in cursor.fetchall():
                print(post)

        elif ind == 1 and ind2 == 3:

            x = input("Digite o id do autor que será excluído-->")

            cursor.execute('DELETE FROM Post WHERE author_id = ' + x)
            cursor.execute('DELETE FROM Author WHERE id = ' + x)

            print("Autor excluído com sucesso!")

        elif ind == 2 and ind2 == 3:

            x = input("Digite o id do post que será excluído-->")

            cursor.execute('DELETE FROM Post WHERE id = ' + x)

            print("Post excluído com sucesso!")

        elif ind == 1 and ind2 == 4:

            x = int(input("Digite o id do autor que será atualizado-->"))
            y = input("Digite o nome do autor-->")

            cursor.execute('UPDATE Author SET nome = %s WHERE id = %s', (y, x))

            print("Autor atualizado com sucesso!")

        elif ind == 2 and ind2 == 4:

            x = int(input("Digite o id do post que será atualizado-->"))
            y = input("Digite o título do post-->")
            z = input("Digite a data de criação do post-->")

            cursor.execute('UPDATE Post SET title = %s, created = %s WHERE id = %s', (y, z, x))

            print("Post atualizado com sucesso!")

        con.commit()

    elif soun == 2:
        print("Operação encerrada!")
        break
     
