package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;

@Entity(name = "esta_em")
public class EstaEm extends PanacheEntity {
    @Column(name = "ator_id")
    private Integer atorId;

    @Column(name = "obra_id")
    private Integer obraId;


    public Integer getAtorId() {
        return atorId;
    }

    public void setAtorId(Integer atorId) {
        this.atorId = atorId;
    }

    public Integer getObraId() {
        return obraId;
    }

    public void setObraId(Integer obraId) {
        this.obraId = obraId;
    }
}
