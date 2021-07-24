import io.agroal.api.AgroalDataSource;
import io.quarkus.runtime.Startup;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import java.sql.SQLException;

@ApplicationScoped
@Startup
@Path("health")
@Produces(MediaType.TEXT_PLAIN)
public class HealthCheck {

    @Inject
    AgroalDataSource defaultDataSource;

    @GET
    public String health() {
        return "OK";
    }

    @GET
    @Path("db")
    public String dbHealth() throws SQLException {
        return String.valueOf(defaultDataSource.getConnection().isValid(0));
    }

}
