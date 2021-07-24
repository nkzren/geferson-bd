SELECT obra.nome, series.n_episodios, series.temporadas FROM (obra INNER JOIN series on obra.id = series.obra_id) WHERE
id IN
(SELECT obra_id FROM series WHERE (n_episodios * temporadas) < 50)
AND id
IN
((SELECT obra_id FROM genero_obra WHERE genero_id = 3) EXCEPT (SELECT obra_id FROM genero_obra WHERE genero_id = 6))
;


