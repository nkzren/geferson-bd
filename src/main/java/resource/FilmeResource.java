package resource;

import model.db.Filmes;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import java.util.List;

@Path("filmes")
public class FilmeResource {

    @GET
    public List<Filmes> getDisponibilidade() {
        return null;
    }
}
