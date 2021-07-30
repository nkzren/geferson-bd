package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;

@Entity(name = "posters")
public class Posters extends PanacheEntity {

    @OneToOne(targetEntity = Obra.class, cascade = CascadeType.ALL)
    @JoinColumn(name = "obra_id", referencedColumnName = "id")
    private Obra obra;

    private String path;

    public Obra getObra() {
        return obra;
    }

    public void setObra(Obra obra) {
        this.obra = obra;
    }

    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }
}
