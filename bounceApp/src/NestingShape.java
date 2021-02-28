package bounce;
/*
 *  ============================================================================================
 *  NAME : THERESA NATHANIA LAN
 *  UPI : TLAN121 (569504563)
 *  DESCRIPTION : NestingShape
 *  ============================================================================================
 */
import java.util.List;
import java.util.ArrayList;

public class NestingShape extends Shape{
	private ArrayList<Shape> shapeLst = new ArrayList <Shape>();
	
	public NestingShape() {
		super();
	}
	public NestingShape(int x, int y) {
		super(x, y);
	}
	public NestingShape(int x, int y, int deltaX, int deltaY) {
		super(x, y, deltaX, deltaY);
	}
	public NestingShape(int x, int y, int deltaX, int deltaY, int width, int height) {
		super(x, y, deltaX, deltaY, width, height);
	}
	public NestingShape(int x, int y, int deltaX, int deltaY, int width, int height, String text) {
		super(x, y, deltaX, deltaY, width, height,text);
	}
	public void move(int width, int height) {
		super.move(width, height);
		for (Shape s : shapeLst){
		    s.move(super.width(), super.height());
		}  
		
	}
	protected void doPaint(Painter painter) {
		painter.drawRect(super.x(), super.y(), super.width(), super.height());
		if (this._text != null){
	        painter.drawCenteredText(this._text, (int)(super.x() + super.width()/2), (int)(super.y() + super.height()/2));
	    }
		painter.translate(super.x(), super.y());
		for (Shape s : shapeLst){
		    s.paint(painter);
		}
		painter.translate(0, 0);
		
	}
	void add (Shape shape) throws IllegalArgumentException{
		if (this._width >= shape.width() && this._height >= shape.height() && this._x <= shape.x() && this._y <= shape.y() && this._x + _width >= shape.x() + shape.width() && this._y + _height >= shape.y() + shape.height() && shape.parent() == null){
            this.shapeLst.add(shape);
            shape.setParent(this);
            this.setParent2(shape);
		    super.setLst(shapeLst);
		}
		else {
		    throw new IllegalArgumentException();
		}   
	}
	void remove (Shape shape) {
		this.shapeLst.remove(shape);
		shape.setParent(null);
	}
	public Shape shapeAt (int index) throws IndexOutOfBoundsException{
		if (index < 0 || index >= shapeCount()) {
            throw new IndexOutOfBoundsException();
        } else {
            return shapeLst.get(index);
        }
	}
	public int shapeCount () {
		return shapeLst.size();
	}
	public int indexOf (Shape shape) {
		return shapeLst.indexOf(shape);
	}
	public void setParent2(Shape shape){
	    shape.setParent(this);
	}
	//public boolean contains (Shape shape) {
	//	return shapeLst.contains(shape);	
	//}
	public boolean contains(Shape shape){
	    ArrayList<Shape> tempShapes = this.shapeLst;
	    for (Shape s: tempShapes){
	        if (s == shape){
	            return true;
	        }
	    }return false;
	}
}
