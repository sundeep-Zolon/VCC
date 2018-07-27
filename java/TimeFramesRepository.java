package gov.copyright.vcc.repositories;

/**
 * 
 * @author William
 *
 */
import org.springframework.data.repository.CrudRepository;
import gov.copyright.vcc.jpa.TimeFrames;

public interface TimeFramesRepository extends CrudRepository<TimeFrames, String> {
	
	
}
