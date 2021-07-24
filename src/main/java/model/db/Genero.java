package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.*;

@Entity(name = "genero")
public class Genero extends PanacheEntity {

    @Column(name = "tipo_de_genero")
    private String tipoDeGenero;

    public String getTipoDeGenero() {
        return tipoDeGenero;
    }

    public void setTipoDeGenero(String tipoDeGenero) {
        this.tipoDeGenero = tipoDeGenero;
    }
}
