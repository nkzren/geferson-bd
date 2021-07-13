import names
import random
from functions import random_date
    

def insert_users(file, qtd):
    for i in range(qtd):
        nickname = f'{names.get_first_name()}.{names.get_last_name()}'.lower()
        data_nascimento = random_date("1970/01/01", "2009/01/01", random.random())
        print(f"INSERT INTO usuario VALUES ('{nickname}', '{nickname}@gmail.com', '{data_nascimento}');")
        file.write(f"INSERT INTO usuario VALUES ('{nickname}', '{nickname}@gmail.com', '{data_nascimento}');\n")



file = open('script.sql', 'a')

insert_users(file, 5)

print(names.get_first_name())
print(random_date("1970/01/01", "2009/01/01", random.random()))

