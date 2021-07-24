package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.NamedQuery;

@Entity(name = "estudio")
@NamedQuery(
        name = "Estudio.avgRatingByYear",
        query = "SELECT year(f.obra.dataLancamento) AS ano, avg(a.nota) " +
                "FROM filmes f INNER JOIN f.obra.avaliacoes a " +
                "WHERE f.obra.estudio.nomeEstudio = :nomeEstudio " +
                "GROUP BY ano ORDER BY ano"
)
public class Estudio extends PanacheEntity {

    @Column(name = "nome_estudio")
    public String nomeEstudio;
}
