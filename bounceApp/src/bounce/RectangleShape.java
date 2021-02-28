package bounce;

/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : RectangleShape
 *  ============================================================================================
 */
public class RectangleShape extends Shape {
	/**
	 * Default constructor that creates a RectangleShape instance whose instance
	 * variables are set to default values.
	 */
	public RectangleShape() {
		super();
	}
	
	/**
	 * Creates a RectangleShape object with a specified x and y position.
	 */
	public RectangleShape(int x, int y) {
		super(x,y);
	}

	/**
	 * Creates a RectangleShape instance with specified values for instance 
	 * variables.
	 * @param x x position.
	 * @param y y position.
	 * @param deltaX speed and direction for horizontal axis.
	 * @param deltaY speed and direction for vertical axis.
	 */
	public RectangleShape(int x, int y, int deltaX, int deltaY) {
		super(x,y,deltaX,deltaY);
	}
	
	/**
	 * Creates a RectangleShape instance with specified values for instance 
	 * variables.
	 * @param x x position.
	 * @param y y position.
	 * @param deltaX speed (pixels per move call) and direction for horizontal 
	 *        axis.
	 * @param deltaY speed (pixels per move call) and direction for vertical 
	 *        axis.
	 * @param width width in pixels.
	 * @param height height in pixels.
	 */
	public RectangleShape(int x, int y, int deltaX, int deltaY, int width, int height) {
		super(x,y,deltaX,deltaY,width,height);
	}
	
	public RectangleShape(int x, int y, int deltaX, int deltaY, int width, int height, String text) {
		super(x,y,deltaX,deltaY,width,height,text);
	}
	
	/**
	 * Paints the rectangle using the supplied Painter.
	 */

	protected void doPaint(Painter painter){
	    painter.drawRect(_x,_y,_width,_height);
	    if (this._text != null){
	        painter.drawCenteredText(this._text, (int)(this._x + this._width/2), (int)(this._y + this._height/2));
	    }
	}
}
