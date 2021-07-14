/* Table 'obra' */
CREATE TABLE obra (
id SERIAL,
estudio_id integer NOT NULL,
diretores_id integer NOT NULL,
pais_id integer NOT NULL,
nome text,
descricao text,
data_lancamento date,
PRIMARY KEY(id));

/* Table 'genero' */
CREATE TABLE genero (
id SERIAL,
tipo_de_genero text,
PRIMARY KEY(id));

/* Table 'disponibilidade_sites' */
CREATE TABLE disponibilidade_sites (
sites_id integer NOT NULL,
obra_id integer NOT NULL,
PRIMARY KEY (sites_id, obra_id));

/* Table 'plataforma' */
CREATE TABLE plataforma (
id SERIAL,
nome_site text,
PRIMARY KEY(id));

/* Table 'diretores' */
CREATE TABLE diretores (
id SERIAL,
nome_diretor text,
PRIMARY KEY(id));

/* Table 'estudio' */
CREATE TABLE estudio (
id SERIAL,
nome_estudio text,
PRIMARY KEY(id));

/* Table 'usuario' */
CREATE TABLE usuario (
id SERIAL,
nickname text,
email text,
data_nascimento date,
deletado bool DEFAULT FALSE,
PRIMARY KEY(id));

/* Table 'watchlist' */
CREATE TABLE watchlist (
usuario_id integer NOT NULL,
obra_id integer NOT NULL,
publico bool,
PRIMARY KEY (usuario_id, obra_id));

/* Table 'avaliacao' */
CREATE TABLE avaliacao (
id SERIAL,
usuario_id integer,
obra_id integer NOT NULL,
comentario text,
nota integer,
data_avaliacao date,
PRIMARY KEY(id));

/* Table 'ator' */
CREATE TABLE ator (
id SERIAL,
nome_ator text,
PRIMARY KEY(id));

/* Table 'esta_em' */
CREATE TABLE esta_em (
ator_id integer NOT NULL,
obra_id integer NOT NULL,
PRIMARY KEY (ator_id, obra_id));

/* Table 'posters' */
CREATE TABLE posters (
path text,
obra_id integer NOT NULL);

/* Table 'pais' */
CREATE TABLE pais (
id SERIAL,
nome_pais text,
PRIMARY KEY(id));

/* Table 'avaliadores' */
CREATE TABLE avaliadores (
id SERIAL,
"tipoDeNota_id" integer NOT NULL,
nome_site text,
path text,
PRIMARY KEY(id));

/* Table 'avaliacao_exterior' */
CREATE TABLE avaliacao_exterior (
sites_avaliacao_id integer NOT NULL,
obra_id integer NOT NULL,
PRIMARY KEY(sites_avaliacao_id, obra_id));

/* Table 'categorias' */
CREATE TABLE categorias (
id SERIAL,
categoria_nome text,
descricao text,
PRIMARY KEY(id));

/* Table 'categorias_obra' */
CREATE TABLE categorias_obra (
categorias_id integer NOT NULL,
obra_id integer NOT NULL,
PRIMARY KEY (categorias_id, obra_id));

/* Table 'tipoDeNota' */
CREATE TABLE "tipoDeNota" (
"tipoDeNota" text NOT NULL,
id SERIAL,
PRIMARY KEY(id));

/* Table 'genero_obra' */
CREATE TABLE genero_obra (
genero_id integer NOT NULL,
obra_id integer NOT NULL,
PRIMARY KEY (genero_id, obra_id));

/* Table 'series' */
CREATE TABLE series (
obra_id integer NOT NULL,
n_episodios integer,
temporadas integer);

/* Table 'filmes' */
CREATE TABLE filmes (
obra_id integer NOT NULL,
duracao integer);

/* Table 'is_blocked' */
CREATE TABLE is_blocked (
usuario_id integer NOT NULL,
data_de_bloqueio text);

/* Relation 'sites-disponibilidade_sites' */
ALTER TABLE disponibilidade_sites ADD CONSTRAINT "sites-disponibilidade_sites"
FOREIGN KEY (sites_id)
REFERENCES plataforma(id);

/* Relation 'obra-disponibilidade_sites' */
ALTER TABLE disponibilidade_sites ADD CONSTRAINT "obra-disponibilidade_sites"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'diretores-obra' */
ALTER TABLE obra ADD CONSTRAINT "diretores-obra"
FOREIGN KEY (diretores_id)
REFERENCES diretores(id);

/* Relation 'estudio-obra' */
ALTER TABLE obra ADD CONSTRAINT "estudio-obra"
FOREIGN KEY (estudio_id)
REFERENCES estudio(id);

/* Relation 'usuario-watchlist' */
ALTER TABLE watchlist ADD CONSTRAINT "usuario-watchlist"
FOREIGN KEY (usuario_id)
REFERENCES usuario(id);

/* Relation 'obra-watchlist' */
ALTER TABLE watchlist ADD CONSTRAINT "obra-watchlist"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'usuario-avaliacao' */
ALTER TABLE avaliacao ADD CONSTRAINT "usuario-avaliacao"
FOREIGN KEY (usuario_id)
REFERENCES usuario(id);

/* Relation 'obra-avaliacao' */
ALTER TABLE avaliacao ADD CONSTRAINT "obra-avaliacao"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'ator-esta_em' */
ALTER TABLE esta_em ADD CONSTRAINT "ator-esta_em"
FOREIGN KEY (ator_id)
REFERENCES ator(id);

/* Relation 'obra-esta_em' */
ALTER TABLE esta_em ADD CONSTRAINT "obra-esta_em"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'obra-table1' */
ALTER TABLE posters ADD CONSTRAINT "obra-table1"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'pais-obra' */
ALTER TABLE obra ADD CONSTRAINT "pais-obra"
FOREIGN KEY (pais_id)
REFERENCES pais(id);

/* Relation 'sites_avaliacao-avaliacao_exterior' */
ALTER TABLE avaliacao_exterior ADD CONSTRAINT "sites_avaliacao-avaliacao_exterior"
FOREIGN KEY (sites_avaliacao_id)
REFERENCES avaliadores(id);

/* Relation 'obra-avaliacao_exterior' */
ALTER TABLE avaliacao_exterior ADD CONSTRAINT "obra-avaliacao_exterior"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'categorias-table1' */
ALTER TABLE categorias_obra ADD CONSTRAINT "categorias-table1"
FOREIGN KEY (categorias_id)
REFERENCES categorias(id);

/* Relation 'obra-table1' */
ALTER TABLE categorias_obra ADD CONSTRAINT "obra-table1"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'tipoDeNota-avaliadores' */
ALTER TABLE avaliadores ADD CONSTRAINT "tipoDeNota-avaliadores"
FOREIGN KEY ("tipoDeNota_id")
REFERENCES "tipoDeNota"(id);

/* Relation 'genero-genero_obra' */
ALTER TABLE genero_obra ADD CONSTRAINT "genero-genero_obra"
FOREIGN KEY (genero_id)
REFERENCES genero(id);

/* Relation 'obra-genero_obra' */
ALTER TABLE genero_obra ADD CONSTRAINT "obra-genero_obra"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'obra-filmes' */
ALTER TABLE filmes ADD CONSTRAINT "obra-filmes"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'obra-series' */
ALTER TABLE series ADD CONSTRAINT "obra-series"
FOREIGN KEY (obra_id)
REFERENCES obra(id);

/* Relation 'usuario-is_blocked' */
ALTER TABLE is_blocked ADD CONSTRAINT "usuario-is_blocked"
FOREIGN KEY (usuario_id)
REFERENCES usuario(id);