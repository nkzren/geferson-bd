package model.db;

import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;
import java.time.LocalDate;

@Entity(name = "usuario")
public class Usuario extends PanacheEntity {

    public String nickname;
    public String email;

    @Column(name = "data_nascimento")
    public LocalDate dataNascimento;

    public Boolean deletado;
}
