package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;

@Entity(name = "disponibilidade_sites")
public class DisponibilidadeSites extends PanacheEntity {
    private Integer sites_id;

    @Column(name = "obra_id")
    private Integer obraId;

    public Integer getSites_id() {
        return sites_id;
    }

    public void setSites_id(Integer sites_id) {
        this.sites_id = sites_id;
    }

    public Integer getObraId() {
        return obraId;
    }

    public void setObraId(Integer obraId) {
        this.obraId = obraId;
    }
}
