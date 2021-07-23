SELECT nome 
FROM obra WHERE EXISTS(
	SELECT obra_id FROM avaliacao 
	GROUP BY obra_id 
	HAVING AVG(nota) > 8 
	AND obra.id = avaliacao.obra_id)
AND
EXISTS(
	SELECT d.id FROM diretores d
	WHERE d.nome_diretor = 'Karole Pickens'
	AND obra.diretores_id = d.id)
;
	