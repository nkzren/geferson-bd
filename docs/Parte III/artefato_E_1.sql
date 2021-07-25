SELECT nome_ator
FROM ator
WHERE EXISTS(
	SELECT obra.nome
	FROM obra
	INNER JOIN esta_em	
	ON esta_em.obra_id = obra.id
	WHERE ator.id = esta_em.ator_id
	AND obra.nome = 'Brocolis 99'
)