package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;
import java.time.LocalDate;
import java.util.Collection;
import java.time.LocalDate;

@Entity(name = "obra")
public class Obra extends PanacheEntity {

    @Column(name = "estudio_id")
    private Integer estudioId;

    @OneToOne(fetch = FetchType.LAZY, targetEntity = Diretor.class)
    @JoinColumn(name = "diretores_id", referencedColumnName = "id")
    private Diretor diretor;

    @OneToMany(fetch = FetchType.LAZY, targetEntity = Avaliacao.class)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    private Collection<Avaliacao> avaliacoes;

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

    public Collection<Avaliacao> getAvaliacoes() {
        return avaliacoes;
    }

    public void setAvaliacoes(Collection<Avaliacao> avaliacoes) {
        this.avaliacoes = avaliacoes;
    }

    public Diretor getDiretor() {
        return diretor;
    }

    public void setDiretor(Diretor diretor) {
        this.diretor = diretor;
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
