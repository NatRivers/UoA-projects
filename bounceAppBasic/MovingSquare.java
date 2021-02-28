//package Ass1;
/*
 *    ===============================================================================
 *     NAME : THERESA NATHANIA LAN
 *     UPI : TLAN121 (569504563)
 *     DESCRIPTION : MOVINGSQUARE
 *    ===============================================================================
 */
import java.awt.*;

class MovingSquare extends MovingRectangle{
	public MovingSquare() {
		this.width = 50;
		this.height = 50;
	}
	public MovingSquare(int s) {
		super(s);
	}
	public MovingSquare(int x, int y, int h, int mw, int mh, Color bc, Color fc, int pathType){
        super(x,y,h,h,mw,mh,bc,fc,pathType);
    }
	public void setWidth(int w) { width = w; height = w;}
	
	public void setHeight(int h) { height = h; width = h;}

}
