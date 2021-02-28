//package Ass1;
/*
 *    ===============================================================================
 *     NAME : THERESA NATHANIA LAN
 *     UPI : TLAN121 (569504563)
 *     DESCRIPTION : MOVINGPYRAMID
 *    ===============================================================================
 */
import java.awt.Color;
import java.awt.Graphics;
import java.awt.*;

class MovingPyramid extends MovingRectangle{
	private int xSize, ySize;
	public static int NUMBER_OF_ROWS = 5;
	
	public MovingPyramid() {
		super();
		setUp();
	}
	public MovingPyramid(int s) {
		super(s);
		setUp();
	}
	public MovingPyramid(int x, int y, int w, int h, int mw, int mh, Color bc, Color fc, int pathType){
        super(x,y,w,h,mw,mh,bc,fc,pathType);
        setUp();
    }
	private void setUp() {
		int col = getXSize();
		int row = getYSize();
		
		//row 1 (1 square)
		int x1 = this.x + col * 4;
		int y1 = this.y;
		
		//row 2 (3 squares)
		int x2_1 = this.x + col * 3;
		int x2_2 = this.x + col * 4;
		int x2_3 = this.x + col * 5;
		int y2 = this.y + row;
		
		//row 3 (5 squares)
		int x3_1 = this.x + col * 2;
		int x3_2 = this.x + col * 3;
		int x3_3 = this.x + col * 4;
		int x3_4 = this.x + col * 5;
		int x3_5 = this.x + col * 6;
		int y3 = this.y + row * 2;
		
		//row 4 (7 squares)
		int x4_1 = this.x + col;
		int x4_2 = this.x + col * 2;
		int x4_3 = this.x + col * 3;
		int x4_4 = this.x + col * 4;
		int x4_5 = this.x + col * 5;
		int x4_6 = this.x + col * 6;
		int x4_7 = this.x + col * 7;
		int y4 = this.y + row * 3;
		
		//row 5 (9 squares)
		int x5_1 = this.x;
		int x5_2 = this.x + col;
		int x5_3 = this.x + col * 2;
		int x5_4 = this.x + col * 3;
		int x5_5 = this.x + col * 4;
		int x5_6 = this.x + col * 5;
		int x5_7 = this.x + col * 6;
		int x5_8 = this.x + col * 7;
		int x5_9 = this.x + col * 8;
		int y5 = this.y + row * 4;
	}
	public void draw(Graphics g) {
		final Graphics2D g2d = (Graphics2D) g;
		int c = getXSize();
		int r = getYSize();
		
		g2d.setPaint(this.borderColor);
		g2d.drawRect(this.x, this.y, this.width, this.height);
		
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 4, this.y, c, r);
		
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 3, this.y + r, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 4, this.y + r, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 5, this.y + r, c, r);
		
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 2, this.y + r * 2, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 3, this.y + r * 2, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 4, this.y + r * 2, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 5, this.y + r * 2, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 6, this.y + r * 2, c, r);
		
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c, this.y + r * 3, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 2, this.y + r * 3, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 3, this.y + r * 3, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 4, this.y + r * 3, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 5, this.y + r * 3, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 6, this.y + r * 3, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 7, this.y + r * 3, c, r);
		
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x, this.y + r * 4, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c, this.y + r * 4, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 2, this.y + r * 4, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 3, this.y + r * 4, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 4, this.y + r * 4, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 5, this.y + r * 4, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 6, this.y + r * 4, c, r);
		g2d.setPaint(this.fillColor);
		g2d.fillRect(this.x + c * 7, this.y + r * 4, c, r);
		g2d.setPaint(Color.WHITE);
		g2d.fillRect(this.x + c * 8, this.y + r * 4, c, r);
	}
	public void setHeight(int h) {
		this.height = h;
	}
	public void setWidth(int w) {
		this.width = w;
	}
	public int getXSize() {
		xSize = (int) (this.width / 9);
		return xSize;
	}
	public int getYSize() {
		ySize = (int) (this.height / 5);
		return ySize;
	}
	//private setUp() calculates dimention (Q6)

}
