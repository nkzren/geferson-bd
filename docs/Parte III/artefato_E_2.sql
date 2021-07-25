SELECT nome_ator FROM obra
INNER JOIN esta_em
ON obra.id = esta_em.obra_id
INNER JOIN ator
ON esta_em.ator_id = ator.id
WHERE obra.nome = 'Brocolis 99'