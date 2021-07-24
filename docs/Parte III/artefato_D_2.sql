SELECT DISTINCT o.nome 
FROM obra o WHERE(
	EXISTS (
                SELECT 1 FROM diretores d INNER JOIN avaliacao a 
                ON((o.diretores_id IN (
                            SELECT diretores.id FROM diretores 
                            WHERE diretores.nome_diretor = 'Karole Pickens'
                            )
                 ) AND (
                        o.id IN (
                            SELECT avaliacao.obra_id FROM avaliacao 
                            GROUP BY avaliacao.obra_id 
                            HAVING AVG(avaliacao.nota) > 8
                        )
                    )
                )
	)
)