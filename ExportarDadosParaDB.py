# Biblioteca responsável pelo processamento de dataframes
import pandas as pd
# Responsável por conectar ao banco de dados MySQL
import mysql.connector
import entidade_entrega
# Entidade Entregas no modelo de arquitetura de sistemas em 3 camadas
from entidade_entrega import Entrega
# Entidade Banco de dados - Responsável pela string de conexão ao banco de dados mysql
from entidade_bancodedados import BancoDeDados
from datetime import datetime

if __name__ == '__main__':
    # String de conexão do servidor SQL
    dbConfig = {
        'user': 'sa',
        'password': '@database123',
        'host': 'localhost',
        'port': 3306,
        'database': 'salexpress',
        'raise_on_warnings': True
    }
    # Extrair dados da planilha de Excel
    # Arquivo do Excel
    filename = 'AMOSTRA.xlsx'
    file = pd.read_excel(filename)
    # Abrir conexão com o servidor
    connection = mysql.connector.connect(**dbConfig)
    if connection.is_connected():
        cursor = connection.cursor()
        for index, row in file.iterrows():
            try:
                custoAdicional = row[9].strip()
                custoAdicional = float(custoAdicional) if custoAdicional else 0.0
            except:
                custoAdicional = 0.0

            # Criar objeto do tipo dicionário
            novaEntrega = {
                'origem': row[0].strip(),
                'destino': row[1].strip(),
                'tipo': row[2].strip(),
                'valor': float(row[3]),
                'data_contratacao': row[4].strftime('%Y-%m-%d') if not pd.isnull(row[4]) else None,
                'data_entrega': row[5].strftime('%Y-%m-%d') if not pd.isnull(row[5]) else None,
                'tempo': int(row[6]) if not pd.isnull(row[6]) else None,
                'forma_pagamento': row[7].strip(),
                'status': row[8].strip(),
                'custo_adicional': custoAdicional,
                'obs': row[10] if not pd.isnull(row[10]) else ''
            }

            # Chamar a stored procedure para salvar a entrega no banco de dados SQL
            sqlQuery = """
                    CALL AdicionarEntrega(
                        %(origem)s,
                        %(destino)s,
                        %(tipo)s, 
                        %(valor)s,
                        %(data_contratacao)s,
                        %(data_entrega)s, 
                        %(tempo)s, 
                        %(forma_pagamento)s,
                        %(status)s,
                        %(custo_adicional)s,
                        %(obs)s
                    );
                """
            try:
                cursor.execute(sqlQuery, novaEntrega)
                connection.commit()
            except mysql.connector.Error as err:
                print(f"Erro: {err}")
                connection.rollback()

            print(novaEntrega)
        # Fechar a conexão
        cursor.close()
        connection.close()




