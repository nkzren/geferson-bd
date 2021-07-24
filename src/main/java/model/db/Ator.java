package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;

@Entity(name = "ator")
public class Ator extends PanacheEntity {
    public Integer id;

    @Column(name = "nome_ator")
    public String nomeAtor;

}
