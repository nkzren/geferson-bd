package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;

@Entity(name = "diretores")
public class Diretor extends PanacheEntity {

    @Column(name = "nome_diretor")
    public String nome;
}
