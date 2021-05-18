package model;


import io.quarkus.hibernate.orm.panache.PanacheEntity;

import javax.persistence.Column;
import javax.persistence.Entity;

@Entity
public class TestDump extends PanacheEntity {

    @Column
    public String test;

    public static TestDump testResource() {
        return find("test", "TAPIOCA").firstResult();
    }
}
