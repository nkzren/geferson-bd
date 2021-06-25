CREATE FUNCTION update_aval_reverso() RETURNS TRIGGER AS $update_aval_reverso$
BEGIN
  UPDATE obra
  SET nota_media = (
    SELECT COALESCE(avg(nota), 0) 
    FROM avaliacao a WHERE obra_id = 1
  ) 
  WHERE obra.id = new.obra_id;
  RETURN NULL;
END $update_aval_reverso$ LANGUAGE plpgsql;

CREATE TRIGGER obra_nota_update_reverso
AFTER DELETE ON avaliacao
FOR EACH ROW
EXECUTE PROCEDURE update_aval_reverso();

-- SQL Padrao
CREATE TRIGGER obra_nota_media AFTER DELETE ON avaliacao
AS
DECLARE
  contador NUMERIC;
  divisor NUMERIC;
BEGIN
  UPDATE obra
  SET nota_media = (
    SELECT COALESCE(avg(nota), 0) 
    FROM avaliacao a WHERE obra_id = 1
  ) 
  WHERE obra.id = new.obra_id;
END;