import mysql.connector

con = mysql.connector.connect(host='localhost', database='school', user='root', password='root')

cursor = con.cursor()


while True:

    soun = int(input("Deseja continuar? 1- Sim, 2- Não --> "))

    if soun == 1:

        ind = int(input("Qual tabela deseja utilizar? 1- Course, 2- Student --> "))

        ind2 = int(input("Digite a funcionalidade desejada: 1- Inserir, 2- Consultar, 3- Deletar, 4- Atualizar --> "))


        if ind == 1 and ind2 == 1:
            
            x = int(input("Digite o id do curso-->"))
            y = input("Digite o nome do curso-->")
            z = input("Digite a área de estudo do curso-->")

            cursor.execute('INSERT INTO Course (CourseID, Name, StudyArea) VALUES(%s,%s,%s) ', (x, y,z))

            print("Curso inserido com sucesso!")

        elif ind == 2 and ind2 == 1:

            x = int(input("Digite o id do estudante-->"))
            y = int(input("Digite o id do curso-->"))
            n = input("Digite o nome do estudante-->")
            z = input("Data de matrícula do estudante (YYYY-MM-DD)-->")
            w = int(input("Digite a idade do estudante-->"))
            v = input("Digite o CPF do estudante-->")

            cursor.execute('INSERT INTO Student (StudentID, CourseID, Name, Created, Age, CPF) VALUES(%s,%s,%s,%s,%s,%s) ', (x, y, n, z, w,v))

            print("Estudante cadastrado com sucesso!")

        elif ind == 1 and ind2 == 2:

            x = input("Digite o id do curso que deseja consultar-->")

            cursor.execute('SELECT * FROM course LEFT JOIN student ON course.CourseID = student.CourseID WHERE course.CourseID = ' + x)

            for course in cursor.fetchall():
                print(course)

        elif ind == 2 and ind2 == 2:

            cursor.execute('SELECT * FROM Student')

            for student in cursor.fetchall():
                print(student)

        elif ind == 1 and ind2 == 3:

            x = input("Digite o id do curso que será excluído-->")

            cursor.execute('DELETE FROM Student WHERE CourseID = ' + x)
            cursor.execute('DELETE FROM Course WHERE CourseID = ' + x)

            print("Curso excluído com sucesso!")

        elif ind == 2 and ind2 == 3:

            x = input("Digite o id do estudante que será excluído-->")

            cursor.execute('DELETE FROM Student WHERE StudentID = ' + x)

            print("Estudante excluído com sucesso!")

        elif ind == 1 and ind2 == 4:

            x = int(input("Digite o id do curso que será atualizado-->"))
            y = input("Digite o nome do curso-->")
            z = input("Digite a área de estudo do curso-->")

            cursor.execute('UPDATE Course SET Name = %s, StudyArea = %s WHERE CourseID = %s', (y,z,x))

            print("Curso atualizado com sucesso!")

        elif ind == 2 and ind2 == 4:

            x = int(input("Digite o id do estudante que será atualizado-->"))
            y = input("Digite o nome do estudante-->")
            z = input("Digite a data de matrícula do estudante-->")
            w = int(input("Digite a idade do estudante-->"))
            v = input("Digite o CPF do estudante-->")

            cursor.execute('UPDATE Student SET Name = %s, Created = %s, Age = %s, CPF = %s WHERE StudentID = %s', (y, z, w, v, x))

            print("Estudante atualizado com sucesso!")

        con.commit()

    elif soun == 2:
        print("Operação encerrada!")
        break
