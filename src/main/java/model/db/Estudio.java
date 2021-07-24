package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;

@Entity(name = "estudio")
public class Estudio extends PanacheEntity {

    @Column(name = "nome_estudio")
    public String nomeEstudio;
}
