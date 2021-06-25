CREATE FUNCTION update_aval_reverso() RETURNS TRIGGER AS $update_aval_reverso$
    DECLARE
        contador NUMERIC;
        divisor NUMERIC;

    BEGIN
        SELECT CAST(SUM(nota) AS NUMERIC) 
        INTO contador
        FROM avaliacao
        WHERE old.obra_id = avaliacao.obra_id;

        SELECT CAST(COUNT(nota) AS NUMERIC)
        INTO divisor
        FROM avaliacao
        WHERE old.obra_id = avaliacao.obra_id;
    
        UPDATE obra
        SET nota_media = contador/divisor
        WHERE obra.id = old.obra_id;
    RETURN NULL;
    END;
$update_aval_reverso$ LANGUAGE plpgsql;

CREATE TRIGGER obra_nota_update_reverso
AFTER DELETE
ON avaliacao
FOR EACH ROW
EXECUTE PROCEDURE update_aval_reverso();
