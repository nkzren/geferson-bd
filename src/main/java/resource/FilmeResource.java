package resource;

import io.quarkus.panache.common.Parameters;
import model.db.Filmes;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("filmes")
@Produces(MediaType.APPLICATION_JSON)
public class FilmeResource {

    @GET
    public List<Filmes> getDisponibilidade(
            @QueryParam("nomeAtor") String nomeAtor
    ) {

        Parameters params = Parameters.with("nomeAtor", "Helen Rogers");


        return Filmes.find("#Filmes.getDisponibilidade", params)
                .range(0, 4) // Limit 5
                .list();
    }
}
