import mysql.connector

#Conectar ao banco de dados MySQL no RDS
cnx = mysql.connector.connect(
    host='endereco_do_seu_RDS',
    user='seu_usuario',
    password='sua_senha',
    database='nome_do_banco_de_dados'
)