package model.util;

public class Queries {
    public static String obrasWithDiretorAndAvg() {
        return "SELECT o.nome, AVG(a.nota) " +
               "FROM avaliacao a, obra o, diretores d " +
               "WHERE d.id = SOME (SELECT id FROM diretores WHERE nome = :nomeDiretor)" +
               "GROUP BY o.nome HAVING AVG(a.nota) > :nota";
    }
}
