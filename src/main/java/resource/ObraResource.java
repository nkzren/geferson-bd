package resource;

import model.db.Obra;

import javax.enterprise.context.RequestScoped;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.QueryParam;
import java.util.List;

@RequestScoped
@Path("obra")
public class ObraResource {

    @GET
    public List<Obra> findByPeriod(@QueryParam("from") Integer from, @QueryParam("to") Integer to) {
        return null;
    }
}
