CREATE VIEW busca_obra_por_ator_diretor AS
SELECT 	o.id AS obra_id, o.nome AS obra_nome, 
		a.id AS ator_id, a.nome_ator AS ator_nome, 
		d.id AS diretor_id, d.nome_diretor AS diretor_nome 
FROM ator a 
INNER JOIN esta_em e ON a.id = e.ator_id 
RIGHT JOIN obra o ON e.obra_id = o.id
LEFT JOIN diretores d ON d.id = o.diretores_id 
WHERE a.id IS NOT NULL AND d.id IS NOT NULL;