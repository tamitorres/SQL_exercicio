import sqlite3  #import de biblioteca

conexao = sqlite3.connect('alunos_exercicio') #indicando qual arquivo vai utilizar
cursor = conexao.cursor() #passando para uma nova varíavel

#cursor.execute('CREATE TABLE alunos_novos (ID INT, Nome VARCHAR (100), Idade INT, Curso  VARCHAR(100));') 

#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (1, "Danilo" ,25 ,"Engenharia")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (2,"Maria",22,"Direito")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (3,"Paulo",26,"Engenharia")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (4,"Marcia",25,"Biologia")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (5,"Diego",25,"Filosofia")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (6,"Pedro",25,"Engenharia")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (7,"Joana",25,"Engenharia")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (8,"Vanessa",25,"Artes")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (9,"Eliana",25,"Direito")')
#cursor.execute('INSERT INTO alunos_novos (ID, Nome, Idade, Curso) VALUES (10,"Thais",25,"Biologia")')

#selecao = cursor.execute('SELECT *FROM alunos_novos')
#for alunos_novos in selecao:
#    print(alunos_novos)

#selecao_nome_idade = cursor.execute('SELECT Nome, Idade FROM alunos_novos WHERE Idade >20')
#for alunos_novos in selecao:
#    print(alunos_novos)

#selecao_engenharia = cursor.execute('SELECT Nome, Curso FROM alunos_novos WHERE Curso = "Engenharia" GROUP BY Nome')
#for alunos_novos in selecao:
#    print(alunos_novos)

#Contagem = cursor.execute('SELECT COUNT (*) FROM alunos_novos')
#for alunos_novos in selecao:
#    print(alunos_novos)

#cursor.execute('UPDATE alunos_novos SET IDADE = 35 WHERE Nome = "Vanessa"')
#cursor.execute('DELETE FROM alunos_novos WHERE ID = 5')

#cursor.execute('CREATE TABLE clientes (ID INT, Nome VARCHAR (100), Idade INT, Saldo  FLOAT);') 

#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (1, "Rafael" ,45 , 750)')
#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (2, "Geane" ,35 , 950)')
#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (3, "Tamiris" ,55 , 1000)')
#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (4, "Miguel" ,25 , 2700)')
#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (5, "Roberta" ,25 , 3700)')
#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (6, "Lorena" ,45 , 7500)')
#cursor.execute('INSERT INTO clientes (ID, Nome, Idade, Saldo) VALUES (7, "Joana" ,35 , 9500)')

#selecao_clientes = cursor.execute('SELECT Nome, Idade FROM clientes WHERE Idade > 30 ')
#for clientes in selecao_clientes:
#    print(clientes)

#calculo_media = cursor.execute('SELECT AVG(Saldo) FROM clientes')
#for clientes in calculo_media:
#    print(clientes)

#maior_saldo = cursor.execute('SELECT Nome, Saldo FROM clientes ORDER BY Saldo DESC LIMIT 1')
#for clientes in maior_saldo:
#    print(clientes)

#Contagem = cursor.execute('SELECT COUNT (*) FROM clientes WHERE Saldo > 1000')
#for clientes in Contagem:
#    print(clientes)

#cursor.execute('UPDATE clientes SET Saldo = 4500 WHERE Nome = "Geane"')
#cursor.execute('DELETE FROM clientes WHERE ID = 3')

cursor.execute('CREATE TABLE compras (ID INTEGER PRIMARY KEY, cliente_id INTEGER, produto VARCHAR(100), valor FLOAT, FOREIGN KEY (cliente_id) REFERENCES clientes (Nome));') 
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (1, "copo", 200.00)')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (2, "pratos", 100.00)')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (3, "talheres", 90.00)')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (4, "copo", 80.00)')
cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (5, "panelas", 100.00)')

cursor.execute('SELECT clientes.nome, compras.produto FROM compras JOIN clientes ON compras.cliente_id = clientes.id')

conexao.commit() 
conexao.close 