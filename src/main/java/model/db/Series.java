package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;

@Entity(name = "series")
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
