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
@Entity(name="Cards")
@Access(AccessType.PROPERTY)
public class Cards {
	public String CardID, DrawerID, CardText, CardNumber, CardGroup, RegistrationNumber, RegistrationDate, Title, Author, Claimant, TimeFrame, DrawerDescription;
	@Id
	public String getCardID() {
		return CardID;
	}

	public void setCardID(String cardID) {
		CardID = cardID;
	}

	public String getDrawerID() {
		return DrawerID;
	}

	public void setDrawerID(String drawerID) {
		DrawerID = drawerID;
	}

	public String getCardText() {
		return CardText;
	}

	public void setCardText(String cardText) {
		CardText = cardText;
	}

	public String getCardNumber() {
		return CardNumber;
	}

	public void setCardNumber(String cardNumber) {
		CardNumber = cardNumber;
	}

	public String getCardGroup() {
		return CardGroup;
	}

	public void setCardGroup(String cardGroup) {
		CardGroup = cardGroup;
	}

	public String getRegistrationNumber() {
		return RegistrationNumber;
	}

	public void setRegistrationNumber(String registrationNumber) {
		RegistrationNumber = registrationNumber;
	}

	public String getRegistrationDate() {
		return RegistrationDate;
	}

	public void setRegistrationDate(String registrationDate) {
		RegistrationDate = registrationDate;
	}

	public String getTitle() {
		return Title;
	}

	public void setTitle(String title) {
		Title = title;
	}

	public String getAuthor() {
		return Author;
	}

	public void setAuthor(String author) {
		Author = author;
	}

	public String getClaimant() {
		return Claimant;
	}

	public void setClaimant(String claimant) {
		Claimant = claimant;
	}

	public String getTimeFrame() {
		return TimeFrame;
	}

	public void setTimeFrame(String timeFrame) {
		TimeFrame = timeFrame;
	}

	public String getDrawerDescription() {
		return DrawerDescription;
	}

	public void setDrawerDescription(String drawerDescription) {
		DrawerDescription = drawerDescription;
	}

}
