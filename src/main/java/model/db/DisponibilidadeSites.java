package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jdk.jfr.Name;

import javax.persistence.*;

@Entity(name = "disponibilidade_sites")
public class DisponibilidadeSites extends PanacheEntity {

    @ManyToOne(targetEntity = Obra.class, fetch = FetchType.LAZY)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    public Obra obra;

    @Column(name = "sites_id")
    public Integer sitesId;

}
