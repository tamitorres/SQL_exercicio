import sqlite3  #import de biblioteca

conexao = sqlite3.connect('banco_dados') #indicando qual arquivo vai utilizar
cursor = conexao.cursor() #passando para uma nova varíavel

#cursor.execute('CREATE TABLE usuarios_novos (id INT, nome VARCHAR (100), endereco VARCHAR(100), email VARCHAR(100));') #execução de comandos
#cursor.execute('ALTER TABLE usuarios_novos RENAME TO usuarios_novo_rede')
#cursor.execute('ALTER TABLE usuarios_novos_rede ADD COLUMN telefoni INT')

#cursor.execute('CREATE TABLE teste_table (id INT, nome VARCHAR (100), endereco VARCHAR(100), email VARCHAR(100));') 
cursor.execute ('DROP TABLE teste_table')

conexao.commit() #envio de informações, as infos só são enviadas quando chega nesse ponto
conexao.close #para não conflitar o sistema gerenciador do computador, garante que o processe será encerrado