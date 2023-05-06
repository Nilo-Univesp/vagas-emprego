import sqlite3

class PetDatabase:
    
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
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS pets (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    breed TEXT,
                                    description TEXT,
                                    photo BLOB,
                                    contact TEXT
                                );""")
            print("Tabela criada com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao criar tabela: ", e)
            
    def add_pet(self, pet_data):
        try:
            sql = "INSERT INTO pets (name, breed, description, photo, contact) VALUES (?, ?, ?, ?, ?)"
            self.cursor.execute(sql, (pet_data['name'], pet_data['breed'], pet_data['description'], pet_data['photo'], pet_data['contact']))
            self.connection.commit()
            print("Pet adicionado com sucesso.")
        except sqlite3.Error as e:
            print("Erro ao adicionar pet: ", e)

    def disconnect(self):
        self.connection.close()
        print("Conexao com banco de dados finalizada com sucesso.")
