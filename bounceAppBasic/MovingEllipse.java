//package Ass1;
/*
 *    ===============================================================================
 *     NAME : THERESA NATHANIA LAN
 *     UPI : TLAN121 (569504563)
 *     DESCRIPTION : MOVINGELLIPSE
 *    ===============================================================================
 */
import java.awt.*;
//import MovingShape.MovingShape;

public class MovingEllipse extends MovingShape{
    public MovingEllipse() {
        super();
    }
    public MovingEllipse(int s) {
        super(s);
    }
    public MovingEllipse(int x, int y, int w, int h, int mw, int mh, Color bc, Color fc, int pathType){
        super(x,y,w,h,mw,mh,bc,fc,pathType);
    }
    public void draw(Graphics g){
    	final Graphics2D g2d = (Graphics2D) g;
    	g2d.setPaint(this.fillColor);
        g2d.fillOval(this.x, this.y, this.width, this.height);
        
        g2d.setPaint(this.borderColor);
        g2d.drawOval(this.x, this.y, this.width, this.height);
        g2d.drawRect(this.x, this.y, this.width, this.height);
    }
    public double getArea(){
        return Math.PI * (this.width/2) * (this.height/2);
    }
    public boolean contains(Point mousePt){
    	double dx, dy;
    	Point EndPt = new Point(x + width, y + height);
    	dx = (2 * mousePt.x - x - EndPt.x) / (double) width; 
    	dy = (2 * mousePt.y - y - EndPt.y) / (double) height; 
    	return dx * dx + dy * dy < 1.0;
    }
    public static void main(String[] args) {
    	MovingEllipse r1 = new MovingEllipse(10,20,30,40,500,600,Color.orange,Color.pink,0);
    	System.out.println(r1);
    	System.out.printf("%.2f\n",r1.getArea());
    }

}
