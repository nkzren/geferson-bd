package service;

import io.agroal.api.AgroalDataSource;
import io.quarkus.runtime.Startup;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;

@ApplicationScoped
@Startup
public class PostgresService {

    @Inject
    AgroalDataSource defaultDatasource;

}
