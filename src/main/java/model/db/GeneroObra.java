package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;

@Entity(name = "genero_obra")
public class GeneroObra extends PanacheEntity {

    @ManyToOne(fetch = FetchType.LAZY, targetEntity = Genero.class)
    @JoinColumn(name = "genero_id", referencedColumnName = "id")
    public Genero genero;

    @ManyToOne(fetch = FetchType.LAZY, targetEntity = Obra.class)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    public Obra obra;

}
