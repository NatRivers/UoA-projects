package bounce;
/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : DynamicRectangleShape
 *  ============================================================================================
 */
import java.awt.*;

public class DynamicRectangleShape extends RectangleShape{
	private Color color;
	
	public DynamicRectangleShape(int x, int y, int deltaX, int deltaY, int width, int height) {
		super(x,y,deltaX,deltaY,width,height);
		this.color = Color.RED;
	}
	public DynamicRectangleShape(int x, int y, int deltaX, int deltaY, int width, int height, Color color) {
		super(x,y,deltaX,deltaY,width,height);
		this.color = color;
	}
	public DynamicRectangleShape(int x, int y, int deltaX, int deltaY, int width, int height, String text, Color color) {
		super(x,y,deltaX,deltaY,width,height,text);
		this.color = color;
	}
	protected void doPaint(Painter painter) {
		painter.setColor(this.color);
		if (this.color == Color.BLACK) {
		    painter.drawRect(super.x(), super.y(), super.width(), super.height());
		}else {
			painter.fillRect(super.x(), super.y(), super.width(), super.height());
		}
		if (this._text != null){
	        painter.drawCenteredText(this._text, (int)(this._x + this._width/2), (int)(this._y + this._height/2));
	    }
		painter.setColor(Color.BLACK);
	}
	public void move(int width, int height) {
		int nextX = _x + _deltaX;
		int nextY = _y + _deltaY;
		int tempX = nextX;
		int tempY = nextY;
        
        if (nextX <= 0) {
			this.color = Color.RED;
		} else if (nextX + _width >= width) {
			this.color = Color.RED;
		}

		if (nextY <= 0) {
		    this.color = Color.BLACK;
			if (tempX <= 0 || tempX + _width >= width){
			    this.color = Color.RED;
			}
		} else if (nextY + _height >= height) {
		    this.color = Color.BLACK;
			if (tempX <= 0 || tempX + _width >= width){
			    this.color = Color.RED;
			}
		}
		super.move(width, height);
	}
}
