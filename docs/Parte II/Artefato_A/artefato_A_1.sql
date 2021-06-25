CREATE FUNCTION obra_nota_media()
  RETURNS TRIGGER
  LANGUAGE PLPGSQL
AS $$
BEGIN
  SELECT CAST(SUM(nota) AS NUMERIC)
  INTO contador
  IN avaliacao
  WHERE new.obra_id = avaliacao.obra_id;

  SELECT CAST(COUNT(nota) AS NUMERIC)
  INTO divisor
  IN avaliacao
  WHERE new.obra_id = avaliacao.obra_id;

  UPDATE obra
  SET nota_media = contador/divisor
  WHERE obra.id = new.obra_id;
END;

CREATE TRIGGER trigger_obra_nota_media
  AFTER INSERT, DELETE ON avaliacao
  FOR EACH ROW
  EXECUTE PROCEDURE obra_nota_media()


-- SQL Padrao
CREATE TRIGGER obra_nota_media AFTER INSERT, DELETE ON avaliacao
AS
DECLARE
  contador NUMERIC;
  divisor NUMERIC;
BEGIN
  SELECT CAST(SUM(nota) AS NUMERIC)
  INTO contador
  IN avaliacao
  WHERE new.obra_id = avaliacao.obra_id;

  SELECT CAST(COUNT(nota) AS NUMERIC)
  INTO divisor
  IN avaliacao
  WHERE new.obra_id = avaliacao.obra_id;

  UPDATE obra
  SET nota_media = contador/divisor
  WHERE obra.id = new.obra_id;
END;