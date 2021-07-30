package resource;

import io.quarkus.panache.common.Parameters;
import model.db.Avaliacao;
import model.db.Obra;
import model.db.Usuario;

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

    @GET
    public List<Avaliacao> findPosterByName(@QueryParam("nomeObra") String nomeObra) {
        Parameters params = Parameters
                .with("nomeObra", nomeObra);
        return Avaliacao.find("#Obra.findPosterByName", params).list();
    }
}
