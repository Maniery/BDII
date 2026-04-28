import psycopg2

def executar_tarefa_sql():
    try:
        # Conexão com o banco do Docker
        conn = psycopg2.connect(
            dbname="AtividadesBD",
            user="admin",
            password="password123",
            host="localhost",
            port="5432"
        )
        cur = conn.cursor()

        # 5.a Inserir uma atividade (Exemplo: Atividade ID 1 no Projeto 1)
        cur.execute("INSERT INTO atividade (id, nome, projeto_id) VALUES (%s, %s, %s)", (1, 'Nova Atividade SQL', 1))
        
        # 5.b Atualizar o líder de um projeto
        cur.execute("UPDATE projeto SET lider_id = %s WHERE id = %s", (2, 1))
        
        # 5.c Listar projetos e atividades
        cur.execute("""
            SELECT p.nome, a.nome 
            FROM projeto p 
            LEFT JOIN atividade a ON p.id = a.projeto_id
        """)
        for row in cur.fetchall():
            print(f"Projeto: {row[0]} | Atividade: {row[1]}")

        conn.commit()
        cur.close()
        conn.close()
        print("Questão 5 executada com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    executar_tarefa_sql()