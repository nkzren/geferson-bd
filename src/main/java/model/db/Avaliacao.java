package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;
import java.time.LocalDate;

@Entity(name = "avaliacao")
public class Avaliacao extends PanacheEntity {

    @Column(name = "usuario_id")
    private Integer usuarioId;

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

    public Integer getObraId() {
        return obraId;
    }

    public void setObraId(Integer obraId) {
        this.obraId = obraId;
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
