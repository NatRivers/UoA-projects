package bounce.forms.util;
/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : FormHandler
 *  ============================================================================================
 */
/**
 * Interface to be implemented by classes that process Form data.
 * 
 * Implementing classes typically implement process() by reading data from the
 * supplied form, and performing some action based on the data.
 * 
 * @author Ian Warren
 *
 */
public interface FormHandler {
	void processForm(Form form);
}
