package gov.copyright.vcc.jpa;

import javax.persistence.Access;
import javax.persistence.AccessType;
import javax.persistence.Entity;
import javax.persistence.Id;
/**
 * 
 * @author William
 *
 */
@Entity(name="Drawers")
@Access(AccessType.PROPERTY)
public class TimeFrames {
	String TimeFrame, TimeFrameDescription;
	@Id
	public String getTimeFrame() {
		return TimeFrame;
	}

	public void setTimeFrame(String timeFrame) {
		TimeFrame = timeFrame;
	}

	public String getTimeFrameDescription() {
		return TimeFrameDescription;
	}

	public void setTimeFrameDescription(String timeFrameDescription) {
		TimeFrameDescription = timeFrameDescription;
	}
	
	
}
