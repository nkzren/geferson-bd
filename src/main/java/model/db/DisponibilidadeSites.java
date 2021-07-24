package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;
import jdk.jfr.Name;

import javax.persistence.*;

@Entity(name = "disponibilidade_sites")
public class DisponibilidadeSites extends PanacheEntity {

    @ManyToOne(targetEntity = Obra.class, fetch = FetchType.LAZY)
    private Obra obra;

    private Integer sitesId;

    public Integer getSitesId() {
        return sitesId;
    }

    public void setSitesId(Integer sitesId) {
        this.sitesId = sitesId;
    }
}
