package resource;

import model.db.Usuario;

import javax.enterprise.context.RequestScoped;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import java.util.List;

@RequestScoped
@Path("user")
public class UserResource {

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Usuario> test(@QueryParam("nickname") String nickname) {
        return Usuario.find("SELECT u FROM usuario u WHERE nickname = ?1", nickname).list();
    }
}
