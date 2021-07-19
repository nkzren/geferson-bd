import names
import lorem
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
    f.write("INSERT INTO ator (nome_ator) VALUES\n")

    for i in range(qtd):
        nome = names.get_full_name()
        atores.append(nome)
        f.write(f"('{nome}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")


def insert_obra(f, qtd, tipo, start):
    f.write("INSERT INTO obra (estudio_id, diretores_id, pais_id, nome, descricao, data_lancamento) VALUES\n")
    if (tipo == 'filmes'):
        nomes = obras[tipo]
        for i in range(qtd): 
            nome_base = random_item(list(nomes.keys()))
            nome_obra = f'{nome_base} {nomes[nome_base]}'
            nomes[nome_base]+=1

            data_lancamento = random_date("1970/01/01", "2009/01/01")
            f.write(f"({random_id(estudios)}, {random_id(diretores)}, {random_id(paises)}, '{nome_obra}', '{lorem.paragraph()}', '{data_lancamento}'){',' if i < qtd-1 else ';' }\n")
    elif (tipo == 'series'): 
        nomes = obras[tipo]

        for i in range(len(nomes)):
            nome_obra = nomes[i]
            data_lancamento = random_date("1970/01/01", "2009/01/01")
            f.write(f"({random_id(estudios)}, {random_id(diretores)}, {random_id(paises)}, '{nome_obra}', '{lorem.paragraph()}', '{data_lancamento}'){',' if i < qtd-1 else ';' }\n")

    insert_especializacao(f, qtd, tipo, start)


def insert_especializacao(f, qtd, tipo, start):
    if (tipo == 'filmes'): 
        f.write(f"\nINSERT INTO {tipo} (obra_id, duracao) VALUES\n")
        for i in range(qtd):
            f.write(f"({start+i}, {random_number(90, 130)}){',' if i < qtd-1 else ';' }\n")
    else:
        f.write(f"\nINSERT INTO {tipo} (obra_id, n_episodios, temporadas) VALUES\n")
        for i in range(qtd):
            f.write(f"({start+i}, {random_number(12, 25)}, {random_number(1, 10)}){',' if i < qtd-1 else ';' }\n")
    
    f.write("\n")

def insert_estudio(f): 
    f.write("INSERT INTO estudio (nome_estudio) VALUES\n")
    qtd = len(estudios)
    for i in range(qtd):
        f.write(f"('{estudios[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_diretores(f, qtd):
    f.write("INSERT INTO diretores (nome_diretor) VALUES\n")
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
        f.write(f"('{categorias[i]}', '{lorem.paragraph()}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_plataforma(f):
    f.write("INSERT INTO plataforma (nome_site) VALUES\n")

    qtd = len(plataformas)
    for i in range(qtd):
        f.write(f"('{plataformas[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_tipo_nota(f):
    f.write("INSERT INTO tipo_de_nota (tipo_de_nota) VALUES \n")
    qtd = len(tipo_nota)
    for i in range(qtd):
        f.write(f"('{tipo_nota[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_avaliadores(f):
    f.write("INSERT INTO avaliadores (tipo_de_nota_id, nome_site, path) VALUES \n")

    qtd = len(avaliadores)
    for i in range(qtd):
        f.write(f"('{random_id(tipo_nota)}', '{avaliadores[i]}', '{avaliadoresPath[i]}'){',' if i < qtd-1 else ';' }\n")
    f.write("\n")

def insert_avaliacao_exterior(f, qtd_obras):
    f.write("INSERT INTO avaliacao_exterior (sites_avaliacao_id, obra_id, nota) VALUES \n")
    entry_set = set()
    
    for i in range(qtd_obras):
        obra_id = random_number(1, qtd_obras)
        site_avaliacao_id = random_number(1, qtd_obras)
        set_key = f'{obra_id}_{site_avaliacao_id}'
        if (set_key not in entry_set):
            entry_set.add(set_key)
            f.write(f"({obra_id}, {site_avaliacao_id}, {random_number(1,10)}){',' if i < qtd_obras-1 else ';' }\n")
    
    f.write("\n")

def insert_watchlist(f, qtd_usuarios, qtd_obras): 
    f.write("INSERT INTO watchlist (usuario_id, obra_id) VALUES \n")

    entry_set = set()
    # Cria em media 5 itens na watchlist dos usuarios
    num_iterations = qtd_usuarios * 5
    for i in range(num_iterations):
        usuario_id = random_number(1, qtd_usuarios)
        obra_id = random_number(1, qtd_obras)
        set_key = f'{obra_id}_{usuario_id}'
        if (set_key not in entry_set):
            entry_set.add(set_key)
            f.write(f"({usuario_id}, {obra_id}){',' if i < num_iterations-1 else ';' }\n")

def insert_disponibilidade_sites(f, qtd_obras):
    f.write("INSERT INTO disponibilidade_sites (sites_id, obra_id) VALUES \n")

    entry_set = set()
    # as obras estarao disponiveis em 3 plataformas em media
    num_iterations = qtd_obras * 3
    for i in range(num_iterations):
        id_obra = random_number(1, qtd_obras)
        id_plataforma = random_number(1, 2)
        set_key = f'{id_obra}_{id_plataforma}'
        if (set_key not in entry_set):
            entry_set.add(set_key)
            f.write(f"({id_plataforma}, {id_obra}){',' if i < num_iterations-1 else ';' }\n")



def main():
    f = open(f'{current_dir}/_ignoreTest.sql', 'a')
    qtd_filmes = 100
    qtd_series = len(obras['series'])
    qtd_obras = qtd_filmes + qtd_series
    qtd_usuarios = 100

    insert_tipo_nota(f)
    insert_users(f, qtd_usuarios)
    insert_ator(f, 10)
    insert_estudio(f)
    insert_genero(f)
    insert_pais(f)
    insert_diretores(f, 20)
    insert_plataforma(f)
    insert_avaliadores(f)
    insert_categorias(f)
    

    insert_obra(f, qtd_series, 'series', 1)
    insert_obra(f, qtd_filmes, 'filmes', qtd_series+1)

    insert_disponibilidade_sites(f, qtd_obras)
    insert_watchlist(f, qtd_usuarios, qtd_obras)

main()


