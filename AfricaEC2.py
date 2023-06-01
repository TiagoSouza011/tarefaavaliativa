# Criar a tabela 'animais' se ela não existir
create_table_query = '''
    CREATE TABLE IF NOT EXISTS animais (
        id INT AUTO_INCREMENT PRIMARY KEY,
        raca VARCHAR(100),
        quantidade INT,
        risco_extincao ENUM('sim', 'não'),
        area_encontrada ENUM('norte', 'sul', 'leste', 'oeste')
    )
'''

cursor = cnx.cursor()
cursor.execute(create_table_query)
cnx.commit()

# Função para cadastrar um novo animal
def cadastrar_animal():
    raca = input('Raça do animal: ')
    quantidade = int(input('Quantidade: '))
    risco_extincao = input('Risco de extinção (sim ou não): ')
    area_encontrada = input('Área onde é encontrado (norte, sul, leste ou oeste): ')

    insert_query = '''
        INSERT INTO animais (raca, quantidade, risco_extincao, area_encontrada)
        VALUES (%s, %s, %s, %s)
    '''
    data = (raca, quantidade, risco_extincao, area_encontrada)

    cursor.execute(insert_query, data)
    cnx.commit()

    print('Animal cadastrado com sucesso!')

# Função para exibir todos os animais cadastrados
def listar_animais():
    select_query = 'SELECT * FROM animais'
    cursor.execute(select_query)

    for (id, raca, quantidade, risco_extincao, area_encontrada) in cursor:
        print(f'ID: {id}')
        print(f'Raça: {raca}')
        print(f'Quantidade: {quantidade}')
        print(f'Risco de extinção: {risco_extincao}')
        print(f'Área encontrada: {area_encontrada}')
        print()

# Função para editar um animal existente
def editar_animal():
    id_animal = int(input('ID do animal que deseja editar: '))

    select_query = 'SELECT * FROM animais WHERE id = %s'
    cursor.execute(select_query, (id_animal,))
    result = cursor.fetchone()

    if result is None:
        print('Animal não encontrado.')
        return

    print('Digite os novos dados para o animal:')
    raca = input('Raça do animal: ')
    quantidade = int(input('Quantidade: '))
    risco_extincao = input('Risco de extinção (sim ou não): ')
    area_encontrada = input('Área onde é encontrado (norte, sul, leste ou oeste): ')

    update_query = '''
        UPDATE animais
        SET raca = %s, quantidade = %s, risco_extincao = %s, area_encontrada = %s
        WHERE id = %s
    '''
    data = (raca, quantidade, risco_extincao, area_encontrada, id_animal)

    cursor.execute(update_query, data)
    cnx.commit()

    print('Animal atualizado com sucesso!')

# Função para excluir um animal existente
def excluir_animal():
    id_animal = int(input('ID do animal que deseja excluir: '))

    delete_query = 'DELETE FROM animais WHERE id = %s'
    cursor.execute(delete_query, (id_animal,))
    cnx.commit()

    print('Animal excluído com sucesso!')

# Loop principal do programa
while True:
    print('Selecione uma opção:')
    print('1. Cadastrar animal')
    print('2. Listar animais')
    print('3. Editar animal')
    print('4. Excluir animal')
    print('0. Sair')

    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        cadastrar_animal()
    elif opcao == 2:
        listar_animais()
    elif opcao == 3:
        editar_animal()
    elif opcao == 4:
        excluir_animal()
    elif opcao == 0:
        break
    else:
        print('Opção inválida.')

# Fechar a conexão com o banco de dados
cursor.close()
cnx.close()
