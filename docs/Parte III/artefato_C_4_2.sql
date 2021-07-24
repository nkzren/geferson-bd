SELECT ano, avg(medias) FROM (
SELECT date_part('year',data_lancamento) as ano, avg(nota) as medias, obra.id, obra.estudio_id AS estd FROM avaliacao
INNER JOIN obra
ON avaliacao.obra_id = obra.id
GROUP BY ano, obra.id
) as t
WHERE estd IN
(SELECT id FROM estudio WHERE nome_estudio = 'Ghibli'	
)
GROUP BY t.ano;