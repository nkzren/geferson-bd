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
    private Integer usuarioId;

    @ManyToOne(targetEntity = Obra.class, fetch = FetchType.LAZY)
    private Obra obra;

    @Column(name = "obra_id")
    private Integer obraId;

    private String comentario;

    private Integer nota;

    @Column(name = "data_avaliacao")
    private LocalDate dataAvaliacao;

    public Integer getUsuarioId() {
        return usuarioId;
    }

    public void setUsuarioId(Integer usuarioId) {
        this.usuarioId = usuarioId;
    }

    public Obra getObra() {
        return obra;
    }

    public void setObra(Obra obra) {
        this.obra = obra;
    }

    public String getComentario() {
        return comentario;
    }

    public void setComentario(String comentario) {
        this.comentario = comentario;
    }

    public Integer getNota() {
        return nota;
    }

    public void setNota(Integer nota) {
        this.nota = nota;
    }

    public LocalDate getDataAvaliacao() {
        return dataAvaliacao;
    }

    public void setDataAvaliacao(LocalDate dataAvaliacao) {
        this.dataAvaliacao = dataAvaliacao;
    }
}
