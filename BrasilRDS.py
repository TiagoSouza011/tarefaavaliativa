# Criar a tabela 'tribos' se ela não existir
create_table_query = '''
    CREATE TABLE IF NOT EXISTS tribos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        habitantes INT,
        renda_media FLOAT,
        escolaridade ENUM('fundamental', 'médio', 'superior'),
        trabalho_assalariado ENUM('sim', 'não')
    )
'''

cursor = cnx.cursor()
cursor.execute(create_table_query)
cnx.commit()

# Função para cadastrar uma nova tribo
def cadastrar_tribo():
    nome = input('Nome da tribo: ')
    habitantes = int(input('Número de habitantes: '))
    renda_media = float(input('Renda média mensal: '))
    escolaridade = input('Escolaridade (fundamental, médio ou superior): ')
    trabalho_assalariado = input('Possui trabalho assalariado (sim ou não): ')

    insert_query = '''
        INSERT INTO tribos (nome, habitantes, renda_media, escolaridade, trabalho_assalariado)
        VALUES (%s, %s, %s, %s, %s)
    '''
    data = (nome, habitantes, renda_media, escolaridade, trabalho_assalariado)

    cursor.execute(insert_query, data)
    cnx.commit()

    print('Tribo cadastrada com sucesso!')

# Função para exibir todas as tribos cadastradas
def listar_tribos():
    select_query = 'SELECT * FROM tribos'
    cursor.execute(select_query)

    for (id, nome, habitantes, renda_media, escolaridade, trabalho_assalariado) in cursor:
        print(f'ID: {id}')
        print(f'Nome: {nome}')
        print(f'Habitantes: {habitantes}')
        print(f'Renda média mensal: {renda_media}')
        print(f'Escolaridade: {escolaridade}')
        print(f'Trabalho assalariado: {trabalho_assalariado}')
        print()

# Função para editar uma tribo existente
def editar_tribo():
    id_tribo = int(input('ID da tribo que deseja editar: '))

    select_query = 'SELECT * FROM tribos WHERE id = %s'
    cursor.execute(select_query, (id_tribo,))
    result = cursor.fetchone()

    if result is None:
        print('Tribo não encontrada.')
        return

    print('Digite os novos dados para a tribo:')
    nome = input('Nome da tribo: ')
    habitantes = int(input('Número de habitantes: '))
    renda_media = float(input('Renda média mensal: '))
    escolaridade = input('Escolaridade (fundamental, médio ou superior): ')
    trabalho_assalariado = input('Possui trabalho assalariado (sim ou não): ')

    update_query = '''
        UPDATE tribos
        SET nome = %s, habitantes = %s, renda_media = %s, escolaridade = %s, trabalho_assalariado = %s
        WHERE id = %s
    '''
    data = (nome, habitantes, renda_media, escolaridade, trabalho_assalariado, id_tribo)

    cursor.execute(update_query, data)
    cnx.commit()

    print('Tribo atualizada com sucesso!')

# Função para excluir uma tribo existente
def excluir_tribo():
    id_tribo = int(input('ID da tribo que deseja excluir: '))

    delete_query = 'DELETE FROM tribos WHERE id = %s'
    cursor.execute(delete_query, (id_tribo,))
    cnx.commit()

    print('Tribo excluída com sucesso!')

# Loop principal do programa
while True:
    print('Selecione uma opção:')
    print('1. Cadastrar tribo')
    print('2. Listar tribos')
    print('3. Editar tribo')
    print('4. Excluir tribo')
    print('0. Sair')

    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        cadastrar_tribo()
    elif opcao == 2:
        listar_tribos()
    elif opcao == 3:
        editar_tribo()
    elif opcao == 4:
        excluir_tribo()
    elif opcao == 0:
        break
    else:
        print('Opção inválida.')

# Fechar a conexão com o banco de dados
cursor.close()
cnx.close()