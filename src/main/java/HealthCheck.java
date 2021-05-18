import io.quarkus.runtime.Startup;
import model.TestDump;

import javax.enterprise.context.ApplicationScoped;
import javax.ws.rs.GET;
import javax.ws.rs.Path;

@ApplicationScoped
@Startup
@Path("health")
public class HealthCheck {

    @GET
    public String health() {
        return "OK";
    }

    @GET
    @Path("db")
    public String dbHealth() {
        return TestDump.testResource().test;
    }

}
