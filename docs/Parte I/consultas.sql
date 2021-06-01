-- Encontre o nome de todas as obras de um diretor específico que receberam nota
-- média maior que 8 nas avaliações dos usuários 
SELECT o.nome 
FROM obra o 
	INNER JOIN diretores d ON o.diretores_id IN (
		SELECT id 
		FROM diretores 
		WHERE nome_diretor = 'Ricardo Milos'
	)
	INNER JOIN avaliacao a ON o.id IN (
		SELECT obra_id
		FROM avaliacao
		GROUP BY obra_id
		HAVING AVG(nota) > 8
	);


-- Lista os 5 filmes com maior disponibilidade nas plataformas que contém um ator específico
SELECT o.nome, COUNT(*) AS qtde_plataformas
FROM filmes f 
	INNER JOIN obra o ON f.obra_id = o.id
	INNER JOIN disponibilidade_sites ds ON o.id = ds.obra_id
WHERE o.id IN (
	SELECT obra_id 
	FROM esta_em ee 
	WHERE ator_id IN (
		SELECT id 
		FROM ator a
		WHERE a.nome_ator = 'Kevin Bacon'
	)
)
GROUP BY o.nome 
ORDER BY COUNT(*) DESC 
LIMIT 5
OFFSET 0;


-- Seleciona todas as séries com menos de 50 episódios do gênero comédia e sem o gênero romance
WITH t AS (
	SELECT g.tipo_de_genero, gob.obra_id 
	FROM genero_obra gob
		INNER JOIN genero g ON g.id = gob.genero_id 
)

SELECT o.nome, s.n_episodios, s.temporadas, (s.n_episodios * s.temporadas) AS total_episodios FROM series s 
	INNER JOIN obra o ON o.id = s.obra_id
WHERE (s.n_episodios * s.temporadas) < 50
AND o.id IN (
	SELECT t.obra_id 
	FROM t 
	WHERE t.tipo_de_genero = 'Comédia'
)
AND o.id NOT IN (
	SELECT t.obra_id 
	FROM t
	WHERE t.tipo_de_genero = 'Romance'
);

-- Lista ano a ano a média da nota das avaliações de todos os filmes de um estúdio, ordenado cronologicamente
WITH medias AS (
	SELECT o.id AS id, AVG(a.nota) AS media, date_part('year', o.data_lancamento) AS ano
	FROM obra o 
		INNER JOIN filmes f ON o.id = f.obra_id 
		INNER JOIN avaliacao a ON o.id = a.obra_id
	GROUP BY o.id, ano
)

SELECT date_part('year', o.data_lancamento) AS ano, m.media
FROM estudio e 
	INNER JOIN obra o ON e.id = o.estudio_id
	LEFT JOIN medias m ON o.id = m.id
WHERE m.media NOTNULL
	AND e.nome_estudio = 'Studio Ghibli'
ORDER BY date_part('year', o.data_lancamento);
