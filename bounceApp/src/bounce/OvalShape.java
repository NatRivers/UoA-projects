package bounce;
/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : OvalShape
 *  ============================================================================================
 */
public class OvalShape extends Shape{
	public OvalShape() {
		super();
	}
	
	/**
	 * Creates a Shape object with a specified x and y position.
	 */
	public OvalShape(int x, int y) {
		super(x,y);
	}
	
	/**
	 * Creates a Shape instance with specified x, y, deltaX and deltaY values.
	 * The Shape object is created with a default width and height.
	 */
	public OvalShape(int x, int y, int deltaX, int deltaY) {
		super(x, y, deltaX, deltaY);
	}

	/**
	 * Creates a Shape instance with specified x, y, deltaX, deltaY, width and
	 * height values.
	 */
	public OvalShape(int x, int y, int deltaX, int deltaY, int width, int height) {
		super(x, y, deltaX, deltaY, width, height);
	}
	public OvalShape(int x, int y, int deltaX, int deltaY, int width, int height, String text) {
		super(x, y, deltaX, deltaY, width, height,text);
	}
	protected void doPaint(Painter painter){
	    painter.drawOval(super.x(), super.y(), super.width(), super.height());
	    if (this._text != null){
	        painter.drawCenteredText(this._text, (int)(this._x + this._width/2), (int)(this._y + this._height/2));
	    }
	}
}
