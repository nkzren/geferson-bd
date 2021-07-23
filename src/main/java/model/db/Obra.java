package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;
import java.time.LocalDate;

@Entity(name = "obra")
public class Obra extends PanacheEntity {

    @Column(name = "estudio_id")
    private Integer estudioId;

    @Column(name = "diretores_id")
    private Integer diretoresId;

    @Column(name = "pais_id")
    private Integer paisId;

    private String nome;

    private String descricao;

    @Column(name = "data_lancamento")
    private LocalDate dataLancamento;

    public Integer getEstudioId() {
        return estudioId;
    }

    public void setEstudioId(Integer estudioId) {
        this.estudioId = estudioId;
    }

    public Integer getDiretoresId() {
        return diretoresId;
    }

    public void setDiretoresId(Integer diretoresId) {
        this.diretoresId = diretoresId;
    }

    public Integer getPaisId() {
        return paisId;
    }

    public void setPaisId(Integer paisId) {
        this.paisId = paisId;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public LocalDate getDataLancamento() {
        return dataLancamento;
    }

    public void setDataLancamento(LocalDate dataLancamento) {
        this.dataLancamento = dataLancamento;
    }
}
