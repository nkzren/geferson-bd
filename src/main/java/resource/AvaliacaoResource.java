package resource;

import io.quarkus.panache.common.Parameters;
import model.db.Avaliacao;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import java.util.List;

@Path("avaliacao")
@Produces(MediaType.APPLICATION_JSON)
public class AvaliacaoResource {

    @GET
    public List<Avaliacao> getAverageRatingsFromDirector(
            @QueryParam("nomeDiretor") String nomeDiretor,
            @QueryParam("nota") Double nota
    ) {

        Parameters params = Parameters
                .with("nomeDiretor", nomeDiretor)
                .and("nota", nota);

        return Avaliacao.find("#Avaliacao.getAverageRatingsFromDirector", params).list();
    }
}
