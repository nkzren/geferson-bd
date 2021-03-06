package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;
import java.time.LocalDate;
import java.util.List;

@Entity(name = "obra")
@NamedQuery(name = "Obra.findPosterByName",
        query = "SELECT o.nome, p.path, o.id " +
                "FROM posters p INNER JOIN p.obra as o " +
                "WHERE o.nome = :nomeObra "
)
public class Obra extends PanacheEntity {

    @OneToOne(fetch = FetchType.LAZY, targetEntity = Estudio.class)
    @JoinColumn(name = "estudio_id", referencedColumnName = "id")
    public Estudio estudio;

    @OneToOne(fetch = FetchType.LAZY, targetEntity = Diretor.class)
    @JoinColumn(name = "diretores_id", referencedColumnName = "id")
    public Diretor diretor;

    @OneToMany(fetch = FetchType.LAZY, targetEntity = Avaliacao.class)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    public List<Avaliacao> avaliacoes;

    @OneToMany(fetch = FetchType.LAZY, targetEntity = GeneroObra.class)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    public List<GeneroObra> generos;

    @Column(name = "pais_id")
    public Integer paisId;

    public String nome;

    public String descricao;

    @Column(name = "data_lancamento")
    public LocalDate dataLancamento;

}
