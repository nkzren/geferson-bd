import names
import os
from functions import random_date, random_number, randomstring, random_item, random_id, get_movies
from values import generos, estudios, paises, obras, categorias, diretores, plataformas, atores, avaliadores, tipo_nota, avaliadoresPath
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
        atores.append(nome)
        f.write(f"('{nome}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_obra(f, qtd, tipo):
    f.write("INSERT INTO obra (estudio_id, diretores_id, pais_id, nome, descricao, data_lancamento) VALUES\n")

    if (tipo == 'filmes'):
        nomes = obras[tipo]
        for i in range(qtd): 

            nome_base = random_item(list(nomes.keys()))
            nome_obra = f'{nome_base} {nomes[nome_base]}'
            nomes[nome_base]+=1

            data_lancamento = random_date("1970/01/01", "2009/01/01")
            f.write(f"('{random_id(estudios)}', '{random_id(diretores)}', '{random_id(paises)}', '{nome_obra}', '{randomstring(30)}', '{data_lancamento}'){',' if i < qtd-1 else ';' }\n")
    elif (tipo == 'series'): 
        nomes = obras[tipo]

        for i in range(len(nomes)):
            nome_obra = nomes[i]
            data_lancamento = random_date("1970/01/01", "2009/01/01")
            f.write(f"('{random_id(estudios)}', '{random_id(diretores)}', '{random_id(paises)}', '{nome_obra}', '{randomstring(30)}', '{data_lancamento}'){',' if i < qtd-1 else ';' }\n")

    insert_especializacao(f, qtd, tipo)

def insert_especializacao(f, qtd, tipo):
    if (tipo == 'filmes'): 
        f.write(f"\nINSERT INTO {tipo} (obra_id, duracao) VALUES\n")
        for i in range(qtd):
            f.write(f"('{i + 1}', '{random_number(90, 130)}'){',' if i < qtd-1 else ';' }\n")
    else:
        f.write(f"\nINSERT INTO {tipo} (obra_id, n_episodios, temporadas) VALUES\n")
        for i in range(qtd):
            f.write(f"('{i + 1}', '{random_number(12, 25)}', '{random_number(1, 10)}'){',' if i < qtd-1 else ';' }\n")
    
    f.write("\n")

def insert_estudio(f): 
    f.write("INSERT INTO estudio (nome_estudio) VALUES\n")
    qtd = len(estudios)
    for i in range(qtd):
        f.write(f"('{estudios[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_diretor(f, qtd):
    f.write("INSERT INTO diretor (nome_diretor) VALUES\n")
    for i in range(qtd):
        nome_diretor = f'{names.get_first_name()} {names.get_last_name()}'
        diretores.append(nome_diretor)
        f.write(f"('{nome_diretor}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_genero(f):
    f.write("INSERT INTO genero (tipo_de_genero) VALUES\n")

    qtd = len(generos)
    for i in range(qtd):
        tipo_de_genero = generos[i]
        f.write(f"('{tipo_de_genero}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_pais(f):
    f.write("INSERT INTO pais (nome_pais) VALUES\n")

    qtd = len(paises)
    for i in range(qtd):
        f.write(f"('{paises[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_categorias(f):
    f.write("INSERT INTO categorias (categoria_nome, descricao) VALUES\n")

    qtd = len(categorias)
    for i in range(qtd):
        f.write(f"('{categorias[i]}', '{randomstring(30)}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_plataforma(f):
    f.write("INSERT INTO plataforma (nome_site) VALUES\n")

    qtd = len(plataformas)
    for i in range(qtd):
        f.write(f"('{plataformas[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_tipo_nota(f):
    f.write("INSERT INTO 'tipoDeNota' (tipoDeNota)")
    qtd = len(tipo_nota)
    for i in range(qtd):
        f.write(f"('{tipo_nota[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_avaliadores(f):
    f.write("INSERT INTO avaliadores (tipoDeNota_id, nome_site, path)")

    qtd = len(avaliadores)
    for i in range(qtd):
        f.write(f"('{avaliadores[i]}', '{tipo_nota[i]}', '{avaliadoresPath[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

f = open(f'{current_dir}/_ignoreTest.sql', 'a')

qtd_filmes = 100
qtd_series = len(obras['series'])
qtd_obras = qtd_filmes + qtd_series
qtd_usuarios = 100

insert_users(f, qtd_usuarios)
insert_ator(f, 10)
insert_estudio(f)
insert_genero(f)
insert_pais(f)
insert_diretor(f, 20)
insert_plataforma(f)

insert_obra(f, qtd_series, 'series')
insert_obra(f, qtd_filmes, 'filmes')
