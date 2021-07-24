SELECT ano, avg(medias) FROM (
SELECT date_part('year',data_lancamento) as ano, avg(nota) as medias, obra.id FROM avaliacao
INNER JOIN obra
ON avaliacao.obra_id = obra.id
GROUP BY ano, obra.id
) as t
WHERE
EXISTS
( SELECT obra.id FROM estudio
 INNER JOIN obra
 ON obra.estudio_id = estudio.id 
 WHERE nome_estudio = 'Ghibli'
 AND t.id = obra.id
 GROUP BY t.ano, obra.id
)
GROUP BY t.ano;