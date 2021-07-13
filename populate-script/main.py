import names
import random
from functions import random_date, randomstring

def insert_users(f, qtd):
    f.write("INSERT INTO usuario (nickname, email, data_nascimento) VALUES\n")
    for i in range(qtd):
        nickname = f'{names.get_first_name()}.{names.get_last_name()}'.lower()
        data_nascimento = random_date("1970/01/01", "2009/01/01", random.random())
        # print(f"('{nickname}', '{nickname}@gmail.com', '{data_nascimento}'),")
        f.write(f"('{nickname}', '{nickname}@gmail.com', '{data_nascimento}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")
    
def insert_ator(f, qtd):
    f.write("INSERT INTO ator (nome) VALUES\n")

    for i in range(qtd):
        nome = names.get_full_name()
        f.write(f"('{nome}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


generos = ['romance', 'sci-fi', 'adventure', 'horror', 'fantasy', 'humor']
estudios = ['Ghibli', 'Herbert Richer', 'Alamo', 'Roberto', 'Adam Sandler Animations', 'Warner', 'Bros', 'Dream', 'Works', 'Daora Studios']

def insert_obra(f, qtd):
    f.write("INSERT INTO obra (estudio_id, diretores_id, pais_id, nome, descricao, data_lancamento) VALUES\n")

def insert_estudio(f): 
    qtd = len(estudios)
    for i in range():
        f.write(f"('{estudios[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_genero(f, qtd):
    f.write("INSERT INTO genero (tipo_de_genero) VALUES\n")

    for i in range(qtd):
        tipo_de_genero = random.choice(generos)
        f.write(f"('{tipo_de_genero}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_pais(f):
    f.write("INSERT INTO pais (nome_pais) VALUES\N")

    paises = [ 'Brasil', 'Congo', 'Bangladesh', 'Paquistao', 'Taiwan', 'Cingapura', 'Romenia']
    qtd = len(paises)
    for i in range(qtd):
        f.write(f"('{paises[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_categorias(f):
    f.write("INSERT INTO categorias (nome_pais) VALUES\N")

    categorias = [ 'Assistir com a família', 'Crianças grandes', 'em alta', 'Campeões de bilheteria', 'filmes policiais']
    qtd = len(categorias)
    for i in range(qtd):
        f.write(f"('{categorias[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

    


f = open('populate-script/script.sql', 'a')
# insert_pais(f)

print(randomstring(20))