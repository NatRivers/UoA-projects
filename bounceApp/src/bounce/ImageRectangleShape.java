package bounce;
/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : ImageRectangleShape
 *  ============================================================================================
 */
import java.awt.Image;
import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import java.awt.Color;
import java.awt.*;


public class ImageRectangleShape extends RectangleShape{
	private Image image;
	private int deltaX, deltaY;

	public ImageRectangleShape(int deltaX, int deltaY, Image image) {
		this.deltaX = deltaX;
		this.deltaY = deltaY;
		this.image = image;
	}
	public static Image makeImage(String imageFileName, int shapeWidth) {
	    int w = 0, h = 0, sh = 0;
	    double sf = 0;
	    File f;
	    BufferedImage b= null, b2 = null;
	    Graphics2D g;
	    
		f = new File(imageFileName);
		try{b = ImageIO.read(f);}
		catch(Exception e){}
		b2 = b;
		w = b.getWidth();
		h = b.getHeight();
		
		if (w > shapeWidth){
		    sf = (double) shapeWidth / (double) w;
		    sh = (int) (h * sf);
		    b2 = new BufferedImage(shapeWidth, sh, BufferedImage.TYPE_INT_RGB);
		    g = b2.createGraphics();
		    g.drawImage(b, 0, 0, shapeWidth, sh, null);
		}
		return b2;
	}
	public void paint(Painter painter){
	    int w, h;
	    w = this.image.getWidth(null);
	    h = this.image.getHeight(null);

		painter.drawImage(image, super.x(), super.y(), w, h);
	}
	public void move(int width, int height) {
		int w, h;
	    w = this.image.getWidth(null);
	    h = this.image.getHeight(null);
	    
		int nextX = _x + _deltaX;
		int nextY = _y + _deltaY;

		if (nextX <= 0) {
			nextX = 0;
			_deltaX = -_deltaX;
		} else if (nextX + w >= width) {
			nextX = width - w;
			_deltaX = -_deltaX;
		}

		if (nextY <= 0) {
			nextY = 0;
			_deltaY = -_deltaY;
		} else if (nextY + h >= height) {
			nextY = height - h;
			_deltaY = -_deltaY;
		}

		_x = nextX;
		_y = nextY;
	}
}
