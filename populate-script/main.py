import names
import random
from functions import random_date
    

def insert_users(f, qtd):
    f.write("INSERT INTO usuario (nickname, email, data_nascimento) VALUES\n")
    for i in range(qtd):
        nickname = f'{names.get_first_name()}.{names.get_last_name()}'.lower()
        data_nascimento = random_date("1970/01/01", "2009/01/01", random.random())
        # print(f"('{nickname}', '{nickname}@gmail.com', '{data_nascimento}'),")
        f.write(f"('{nickname}', '{nickname}@gmail.com', '{data_nascimento}'){',' if i < qtd-1 else ';' }\n")
    
def insert_ator(f, qtd):
    f.write("INSERT INTO ator (id, nome) VALUES\n")

    for i in range(qtd):
        nome = names.get_full_name()
        f.write(f"('{nome}'){',' if i < qtd-1 else ';' }\n"))


f = open('populate-script/script.sql', 'a')
insert_users(f, 10000)

print(names.get_first_name())
print(random_date("1970/01/01", "2009/01/01", random.random()))
