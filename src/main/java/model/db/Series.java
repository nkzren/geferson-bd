package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;

@Entity(name = "series")
@NamedQuery(
        name = "Series.maxEpisodesWithAndWithoutGender",
        query = "SELECT s.obra.nome, s.nEpisodios, s.temporadas, (s.nEpisodios * s.temporadas) as totalEpisodios " +
                "FROM series s WHERE (s.nEpisodios * s.temporadas) < 50 " +
                "AND s.obra.id IN     (SELECT gob.obra.id FROM genero_obra gob INNER JOIN gob.genero g WHERE g.tipoDeGenero = :gender)" +
                "AND s.obra.id NOT IN (SELECT gob.obra.id FROM genero_obra gob INNER JOIN gob.genero g WHERE g.tipoDeGenero = :notGender)"
)
public class Series extends PanacheEntity {

    @OneToOne(fetch = FetchType.LAZY, targetEntity = Obra.class)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    private Obra obra;

    @Column(name = "n_episodios")
    private Integer nEpisodios;

    private Integer temporadas;

    public Obra getObra() {
        return obra;
    }

    public void setObra(Obra obra) {
        this.obra = obra;
    }

    public Integer getnEpisodios() {
        return nEpisodios;
    }

    public void setnEpisodios(Integer nEpisodios) {
        this.nEpisodios = nEpisodios;
    }

    public Integer getTemporadas() {
        return temporadas;
    }

    public void setTemporadas(Integer temporadas) {
        this.temporadas = temporadas;
    }
}
