import sqlite3

class VagasDatabase:
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            print("Conexao com banco de dados feita com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao conectar com banco de dados: ", e)
            
    def create_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS vagas (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    vaga TEXT,
                                    empresa TEXT,
                                    description TEXT,
                                    contact TEXT
                                );""")
            print("Tabela criada com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao criar tabela: ", e)
            
    def add_pet(self, pet_data):
        try:
            # Check if all form data is present before adding to the database
            if 'vaga' in pet_data and 'empresa' in pet_data and 'description' in pet_data and 'contact' in pet_data:
                sql = "INSERT INTO vagas (vaga, empresa, description, contact) VALUES (?, ?, ?, ?)"
                self.cursor.execute(sql, (pet_data['vaga'], pet_data['empresa'], pet_data['description'], pet_data['contact']))
                self.connection.commit()
                print("Vaga adicionada com sucesso.")
                return True
            else:
                print("Dados incompletos da vaga.")
                return False
        except sqlite3.Error as e:
            print("Erro ao adicionar vaga: ", e)
            return False

    def delete_pet(self, pet_id):
        try:
            self.cursor.execute("DELETE FROM pets WHERE id=?", (pet_id,))
            self.connection.commit()
            print(f"Pet with id {pet_id} deleted successfully.")
            return True
        except sqlite3.Error as e:
            print("Erro ao deletar pet: ", e)
            return False

    def disconnect(self):
        self.connection.close()
        print("Conexao com banco de dados finalizada com sucesso.")

    def delete_pet_table(self):
        self.cursor.execute("DROP TABLE IF EXISTS pets")
        self.connection.commit()
