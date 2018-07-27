package gov.copyright.vcc.jpa;

import javax.persistence.Access;
import javax.persistence.AccessType;
import javax.persistence.Entity;
import javax.persistence.ForeignKey;
import javax.persistence.Id;
/**
 * 
 * @author William
 *
 */
@Entity(name="Drawers")
@Access(AccessType.PROPERTY)
public class Drawers {
	String DrawerID, DrawerPath, DrawerDescription, TimeFrame;
	@Id
	public String getDrawerID() {
		return DrawerID;
	}

	public void setDrawerID(String drawerID) {
		DrawerID = drawerID;
	}

	public String getDrawerPath() {
		return DrawerPath;
	}

	public void setDrawerPath(String drawerPath) {
		DrawerPath = drawerPath;
	}

	public String getDrawerDescription() {
		return DrawerDescription;
	}

	public void setDrawerDescription(String drawerDescription) {
		DrawerDescription = drawerDescription;
	}
	
	public String getTimeFrame() {
		return TimeFrame;
	}

	public void setTimeFrame(String timeFrame) {
		TimeFrame = timeFrame;
	}
	
}
