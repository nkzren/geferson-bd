package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jdk.jfr.Name;

import javax.persistence.*;
import java.util.List;

@Entity(name = "filmes")
@NamedQuery(
        name = "Filmes.getDisponibilidade",
        query = "SELECT o.nome, COUNT(o) as qtd_plataformas " +
                "FROM filmes f INNER JOIN f.obra as o INNER JOIN f.disponibilidade as ds " +
                "WHERE o.id IN (SELECT ee.obra.id FROM esta_em ee WHERE ee.ator.id IN " +
                "(SELECT a.id FROM ator a WHERE a.nomeAtor = :nomeAtor))" +
                "GROUP BY o.nome ORDER BY COUNT(o) DESC"
)
public class Filmes extends PanacheEntity {

    @OneToOne(targetEntity = Obra.class, cascade = CascadeType.ALL)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    public Obra obra;

    @OneToMany(targetEntity = DisponibilidadeSites.class, fetch = FetchType.LAZY)
    @JoinColumn(name = "obra_id",  referencedColumnName = "obra_id")
    public List<DisponibilidadeSites> disponibilidade;

    public Integer duracao;

}
