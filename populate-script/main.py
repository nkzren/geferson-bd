import names
from functions import random_date, random_number, randomstring, random_item, random_id, get_movies
import os
current_dir = os.path.dirname(os.path.realpath(__file__))

def insert_users(f, qtd):
    f.write("INSERT INTO usuario (nickname, email, data_nascimento) VALUES\n")
    for i in range(qtd):
        nickname = f'{names.get_first_name()}.{names.get_last_name()}'.lower()
        data_nascimento = random_date("1970/01/01", "2009/01/01")
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
# filmes_imdb = get_movies()
paises = [ 'Brasil', 'Congo', 'Bangladesh', 'Paquistao', 'Taiwan', 'Cingapura', 'Romenia']


def insert_obra(f, qtd, tipo):
    f.write("INSERT INTO obra (estudio_id, diretores_id, pais_id, nome, descricao, data_lancamento) VALUES\n")
    obras = {
        'filmes': {
            'Harry Potter': 1,
            'Duro de Matar': 1,
            'Senhor dos Aneis': 1,
            'Rapidos e Pistolassos': 1,
            'Star Wars': 1,
            'Jaime Bonde': 1,
            'Arranjo de Arranjos (Matrix)': 1,
            'A viagem de Chico Liro': 1,
        },
        'series': [ 
            'Casa', 'Quimica Braba', 'Doutor Quem', 'Brocolis 99', 'Jogo das Cadeiras',
            'O Inverno esta chegando', 'Bruxeiro: Geraldo de Ribeirao', 'Serie de medico com 20 mil temporadas',
            'Melhor chamar o Saulao', 'Bagulhos Esquisitos'
        ]
    }

    if (tipo == 'filmes'):
        for i in range(qtd): 
            nomes = obras[tipo]

            nome_base = random_item(list(nomes.keys()))
            nome_obra = f'{nome_base} {nomes[nome_base]}'
            nomes[nome_base]+=1

            data_lancamento = random_date("1970/01/01", "2009/01/01")
            f.write(f"('{random_id(estudios)}', '{random_number(1, 20)}', '{random_id(paises)}', '{nome_obra}', '{randomstring(30)}', '{data_lancamento}'){',' if i < qtd-1 else ';' }\n")
    elif (tipo == 'series'): 
        nomes = obras[tipo]

        for i in range(len(nomes)):
            nome_obra = nomes[i]
            data_lancamento = random_date("1970/01/01", "2009/01/01")
            f.write(f"('{random_id(estudios)}', '{random_number(1, 20)}', '{random_id(paises)}', '{nome_obra}', '{randomstring(30)}', '{data_lancamento}'){',' if i < qtd-1 else ';' }\n")

    insert_especializacao(f, qtd, tipo)

def insert_especializacao(f, qtd, tipo):
    if (tipo == 'filmes'): 
        f.write(f"\nINSERT INTO {tipo} (obra_id, duracao) VALUES\n")
        for i in range(qtd):
            f.write(f"('{i}', '{random_number(90, 130)}'){',' if i < qtd-1 else ';' }\n")
    else:
        f.write(f"\nINSERT INTO {tipo} (obra_id, n_episodios, temporadas) VALUES\n")
        for i in range(qtd):
            f.write(f"('{i}', '{random_number(12, 25)}', '{random_number(1, 10)}'){',' if i < qtd-1 else ';' }\n")

def insert_estudio(f): 
    qtd = len(estudios)
    for i in range(qtd):
        f.write(f"('{estudios[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_diretor(f, qtd):
    f.write("INSERT INTO diretor (nome_diretor) VALUES\n")
    nome_diretor = f'{names.get_first_name()}.{names.get_last_name()}'
    for i in range(qtd):
        f.write(f"('{nome_diretor}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_genero_obra(f, qtd):
    f.write("INSERT INTO genero (tipo_de_genero) VALUES\n")

    for i in range(qtd):
        tipo_de_genero = random_item(generos)
        f.write(f"('{tipo_de_genero}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_pais(f):
    f.write("INSERT INTO pais (nome_pais) VALUES\n")

    qtd = len(paises)
    for i in range(qtd):
        f.write(f"('{paises[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_categorias(f):
    f.write("INSERT INTO categorias (nome_pais) VALUES\n")

    categorias = [ 'Assistir com a família', 'Crianças grandes', 'em alta', 'Campeões de bilheteria', 'filmes policiais']
    qtd = len(categorias)
    for i in range(qtd):
        f.write(f"('{categorias[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")
    


f = open(f'{current_dir}/test.sql', 'a')

qtd_filmes = 100
qtd_obras = 100

# insert_ator(f, 1000)
# insert_genero_obra(f, qtd_obras)

insert_obra(f, 10, 'series')