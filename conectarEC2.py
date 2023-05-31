import pymysql

# Conectar ao banco de dados MariaDB no EC2
cnx = pymysql.connect(
    host='endereco_do_seu_EC2',
    user='seu_usuario',
    password='sua_senha',
    database='nome_do_banco_de_dados'
)

# Criar a tabela 'animais' se ela não existir
create_table_query = '''
    CREATE TABLE IF NOT EXISTS animais (
        id INT AUTO_INCREMENT PRIMARY KEY,
        raca VARCHAR(100),
        quantidade INT,
        risco_extincao ENUM('sim', 'não'),
        area_encontrada ENUM('norte', 'sul', 'leste', 'oeste')
    )