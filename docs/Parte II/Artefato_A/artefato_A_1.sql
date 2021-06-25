CREATE FUNCTION obra_nota_media() RETURNS TRIGGER AS $$
BEGIN
  UPDATE obra
  SET nota_media = (
    SELECT COALESCE(avg(nota), 0) 
    FROM avaliacao a WHERE obra_id = 1
  ) 
  WHERE obra.id = new.obra_id;
  RETURN NULL;
END $$ LANGUAGE PLPGSQL;

CREATE TRIGGER trigger_obra_nota_media
AFTER INSERT ON avaliacao
FOR EACH ROW
EXECUTE PROCEDURE obra_nota_media()


-- SQL Padrao
CREATE TRIGGER obra_nota_media AFTER INSERT ON avaliacao
AS
BEGIN
  UPDATE obra
  SET nota_media = (
    SELECT COALESCE(avg(nota), 0) 
    FROM avaliacao a WHERE obra_id = 1
  ) 
  WHERE obra.id = new.obra_id;
END;