package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.OneToOne;

@Entity(name = "esta_em")
public class EstaEm extends PanacheEntity {

    @OneToOne(targetEntity = Ator.class, fetch = FetchType.LAZY)
    public Ator ator;

    @OneToOne(targetEntity = Obra.class, fetch = FetchType.LAZY)
    public Obra obra;
}
