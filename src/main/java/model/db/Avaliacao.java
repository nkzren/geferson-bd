package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;
import java.time.LocalDate;

@Entity(name = "avaliacao")
@NamedQuery(name = "Avaliacao.getAverageRatingsFromDirector",
        query = "SELECT o.nome, AVG(a.nota) " +
                "FROM avaliacao a INNER JOIN a.obra as o " +
                "WHERE o.diretor.nome = :nomeDiretor " +
                "GROUP BY o.nome HAVING AVG(a.nota) > :nota"
)
public class Avaliacao extends PanacheEntity {

    @Column(name = "usuario_id")
    public Integer usuarioId;

    @ManyToOne(targetEntity = Obra.class, fetch = FetchType.LAZY)
    public Obra obra;

    public String comentario;

    public Integer nota;

    @Column(name = "data_avaliacao")
    public LocalDate dataAvaliacao;

}
