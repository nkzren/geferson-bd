package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.OneToOne;

@Entity(name = "esta_em")
public class EstaEm extends PanacheEntity {

    @OneToOne(targetEntity = Ator.class, fetch = FetchType.LAZY)
    private Ator ator;

    @OneToOne(targetEntity = Obra.class, fetch = FetchType.LAZY)
    private Obra obra;

    public Ator getAtor() {
        return ator;
    }

    public void setAtor(Ator ator) {
        this.ator = ator;
    }

    public Obra getObra() {
        return obra;
    }

    public void setObra(Obra obra) {
        this.obra = obra;
    }
}
