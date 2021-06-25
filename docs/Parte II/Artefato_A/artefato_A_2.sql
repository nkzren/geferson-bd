CREATE FUNCTION deletar_avaliacoes_usuario() 
  RETURNS TRIGGER 
  LANGUAGE PLPGSQL
AS $$
BEGIN
  DELETE FROM avaliacao a
  WHERE a.usuario_id = NEW.id;
END;
RETURN NULL;

CREATE TRIGGER trigger_deletar_avaliacoes_usuario
  AFTER UPDATE ON usuario
  FOR EACH ROW
  WHEN (NEW.deletado = TRUE)
  EXECUTE PROCEDURE deletar_avaliacoes_usuario()
deletar_avaliacoes_usuario()
