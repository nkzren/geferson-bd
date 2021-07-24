SELECT obra.nome, series.n_episodios, series.temporadas FROM (obra INNER JOIN series on obra.id = series.obra_id) WHERE
EXISTS(
	SELECT obra_id
	FROM series
	WHERE (n_episodios * temporadas) < 50
	AND obra.id = series.obra_id
)
AND
EXISTS(	
	SELECT DISTINCT obra_id
	FROM genero_obra
	INNER JOIN genero
	ON genero.id = genero_obra.genero_id
	WHERE genero.tipo_de_genero = 'adventure' AND genero.tipo_de_genero != 'horror'
	AND obra.id = genero_obra.obra_id
	
)
;