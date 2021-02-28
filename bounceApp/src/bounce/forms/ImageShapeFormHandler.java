package bounce.forms;
/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : ImageShapeFormHandler
 *  ============================================================================================
 */
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.swing.SwingWorker;

import javax.imageio.ImageIO;

import bounce.ImageRectangleShape;
import bounce.NestingShape;
import bounce.ShapeModel;
import bounce.forms.util.Form;
import bounce.forms.util.FormHandler;

public class ImageShapeFormHandler implements FormHandler {
	private ShapeModel _model;
	private NestingShape _parentOfNewShape;
	private Form form;
	private SwingWorker<BufferedImage, Void> sw;
	
	public ImageShapeFormHandler(ShapeModel model,NestingShape parent) {
		_model = model;
		_parentOfNewShape = parent;
	}
	
	@Override
	public void processForm(Form form) {
	    this.form = form;
	    sw = new ImageShapeWorker();
	    sw.execute();
	}
	private class ImageShapeWorker extends SwingWorker<BufferedImage,Void>{
    	protected BufferedImage doInBackground() throws Exception{
    		
    		// Read field values from the form.
    		File imageFile = (File)form.getFieldValue(File.class, ImageFormElement.IMAGE);
    		int width = form.getFieldValue(Integer.class, ShapeFormElement.WIDTH);
    		int deltaX = form.getFieldValue(Integer.class, ShapeFormElement.DELTA_X);
    		int deltaY = form.getFieldValue(Integer.class, ShapeFormElement.DELTA_Y);
    		
    
    		// Load the original image (ImageIO.read() is a blocking call).
    		BufferedImage fullImage = null;
    		try {
    			fullImage = ImageIO.read(imageFile);
    		} catch(IOException e) {
    			System.out.println(e);
    			System.out.println("Error loading image.");
    		}
    		
    		int fullImageWidth = fullImage.getWidth();
    		int fullImageHeight = fullImage.getHeight();
    				
    		BufferedImage scaledImage = fullImage;
    				
    		// Scale the image if necessary.
    		if(fullImageWidth > width) {
    		    long startTime = System.currentTimeMillis();
    			double scaleFactor = (double)width / (double)fullImageWidth;
    			int height = (int)((double)fullImageHeight * scaleFactor);
    					
    			scaledImage = new BufferedImage(width,height,BufferedImage.TYPE_INT_RGB); 
    			Graphics2D g = scaledImage.createGraphics();
    					
    			// Method drawImage() scales an already loaded image. The 
    			// ImageObserver argument is null because we don't need to monitor 
    			// the scaling operation.
    			g.drawImage(fullImage, 0, 0, width, height, null);
    		
        		// Create the new Shape and add it to the model.
        		ImageRectangleShape imageShape = new ImageRectangleShape(deltaX, deltaY, scaledImage);
        		_model.add(imageShape, _parentOfNewShape);
        		
        		long elapsedTime = System.currentTimeMillis() - startTime;
        		//System.out.println("Image loading and scaling took " + elapsedTime + "ms.");
    		}return scaledImage;
    	}
	}
}
