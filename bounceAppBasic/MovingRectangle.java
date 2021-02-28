//package Ass1;
/*
 *    ===============================================================================
 *     NAME : THERESA NATHANIA LAN
 *     UPI : TLAN121 (569504563)
 *     DESCRIPTION : MOVINGRECTANGLE
 *    ===============================================================================
 */
import java.awt.*;
class MovingRectangle extends MovingShape{

    public MovingRectangle() {
        super();
    }
    public MovingRectangle(int s) {
        super(s);
    }
    public MovingRectangle(int x, int y, int w, int h, int mw, int mh, Color bc, Color fc, int pathType){
        super(x,y,w,h,mw,mh,bc,fc,pathType);
    }
    public void draw(Graphics g){
    	final Graphics2D g2d = (Graphics2D) g;
    	g2d.setPaint(this.fillColor);
        g2d.fillRect(this.x, this.y, this.width, this.height);
        
        g2d.setPaint(this.borderColor);
        g2d.drawRect(this.x, this.y, this.width, this.height);
    }
    public double getArea(){
        return this.width * this.height;
    }
    public boolean contains(Point mousePt){
    	if ((mousePt.x >= this.x && mousePt.x <= (this.x + this.width)) || (mousePt.x <= this.x && mousePt.x >= (this.x - this.width))) { 
        	if((mousePt.y >= this.y && mousePt.y <= (this.y + this.height)) || (mousePt.y <= this.y && mousePt.y >= (this.y - this.height))){
        		return true;
        	}
        }return false;
    }
	

}
