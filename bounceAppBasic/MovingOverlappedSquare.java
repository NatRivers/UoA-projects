//package Ass1;
/*
 *    ===============================================================================
 *     NAME : THERESA NATHANIA LAN
 *     UPI : TLAN121 (569504563)
 *     DESCRIPTION : MOVINGOVERLAPPEDSQUARE
 *    ===============================================================================
 */
import java.util.Random;
import java.awt.*;

class MovingOverlappedSquare extends MovingRectangle{
	private boolean isOverlapped;
	private Random rand;
	private Rectangle square1, square2;
	public static int SIZE = 30;
	private int bound_w = (int) 2 * SIZE;
	private int bound_h = (int) SIZE;
    //********************
	private boolean c, valid;
	private int x1, y1, x2, y2;
	
	public MovingOverlappedSquare(Random r) {
		super();
		this.rand = r;
		setUp();
	}
	public MovingOverlappedSquare(int s, Random r) {
	    super(s);
	    this.c = true;
	    setWidth(s);
	    this.c = true;
		setHeight(s);
		this.rand = r;
	    setUp();
	    this.c = false;
	}
	public MovingOverlappedSquare(int x, int y, int w, int h, int mw, int mh, Color bc, Color fc, int pathType, Random r) {
		super(x,y,w,h,mw,mh,bc,fc,pathType);
		this.c = true;
		setWidth(w);
		this.c = true;
		setHeight(h);
		this.rand = r;
		setUp();
		this.c = false;
	}
	public boolean isRandomReady() {
		return rand != null;
	}
	public void draw(Graphics g) {
		final Graphics2D g2d = (Graphics2D) g;

		if (this.isOverlapped == true) {
			g2d.setPaint(this.fillColor);
			g2d.fillRect(square1.x, square1.y, square1.width, square1.height);
			g2d.fillRect(square2.x, square2.y, square2.width, square2.height);
		}
		g2d.setPaint(this.borderColor);
		g2d.drawRect(square1.x, square1.y, square1.width, square1.height);
		g2d.drawRect(square2.x, square2.y, square2.width, square2.height);
		g2d.drawRect(this.x, this.y, this.width, this.height);
	}
	private void setUp(){
	    int w = this.width - SIZE;
	    int h = this.height - SIZE;
	    this.x1 = rand.nextInt(w) + this.x;
	    this.y1 = rand.nextInt(h) + this.y;
	    this.x2 = rand.nextInt(w) + this.x;
	    this.y2 = rand.nextInt(h) + this.y;
	    this.square1 = new Rectangle(this.x1, this.y1, SIZE, SIZE);
	    this.square2 = new Rectangle(this.x2, this.y2, SIZE, SIZE);
	    if ((this.x1 >= this.x2 && this.x1 <= this.x2 + SIZE) || (this.x1 <= this.x2 && this.x1 >= (this.x2 - SIZE))){
            if((this.y1 >= this.y2 && this.y1 <= this.y2 + SIZE) || (this.y1 <= this.y2 && this.y1 >= (this.y2 - SIZE))){
	            this.isOverlapped = true;
            }else{
                this.isOverlapped = false;
            }
	    }
	}
	public boolean getIsOverlapped(){
	    return this.isOverlapped;
	}
	public Rectangle getSquare1(){
	    return this.square1;
	}
	public Rectangle getSquare2(){
	    return this.square2;
	}
	public void move() {
		super.move();
		if (path instanceof BouncingPath) {
			this.x1 = this.x1 + path.deltaX;
			this.y1 = this.y1 + path.deltaY;
			this.x2 = this.x2 + path.deltaX;
			this.y2 = this.y2 + path.deltaY;

	        if ((this.x < 0) && (path.deltaX < 0)) {
	        	path.deltaX = -path.deltaX;
	        	this.x1 = 0;
	        	this.x2 = 0;
	        }
	        else if ((this.x + width > marginWidth) && (path.deltaX > 0)) {
	        	path.deltaX = -path.deltaX;
	            this.x1 = marginWidth - width;
	            this.x2 = marginWidth - width;
	        }
	        if ((this.y< 0) && (path.deltaY < 0)) {
	        	path.deltaY = -path.deltaY;
	            this.y1 = 0;
	            this.y2 = 0;
	        }
	        else if((this.y + height > marginHeight) && (path.deltaY > 0)) {
	        	path.deltaY = -path.deltaY;
	        	this.y1 = marginHeight - height;
	        	this.y2 = marginHeight - height;
	        }this.square1 = new Rectangle(this.x1, this.y1, SIZE, SIZE);
	        this.square2 = new Rectangle(this.x2, this.y2, SIZE, SIZE);
		}
		if (path instanceof FallingPath) {
			int temp_y1 = this.y1;
			int temp_y2 = this.y2;
			int temp_yy1 = 0;
			int temp_yy2 = 0;
			int temp_y1y2 = 0;
			int temp_delt = path.deltaY;
			
			if (this.y1 <= this.y2) {
				temp_yy1 = this.y1 - this.y;
				temp_y1y2 = this.y2 - this.y1;
			}else {
				temp_yy2 = this.y2 - this.y;
				temp_y1y2 = this.y1 - this.y2;
			}
	        int yh = height + y;
	        this.y1 += 2;
	        this.y2 += 2;
	        if (this.y + this.height >= marginHeight - 1){
	        	if (temp_y1 <= temp_y2) {
	        		this.y1 = 0;
		            this.y1 += temp_yy1;
		            this.y2 = 0;
		            this.y2 += this.y1 + temp_y1y2;
	        	}else {
	        		this.y2 = 0;
		            this.y2 += temp_yy2;
		            this.y1 = 0;
		            this.y1 += this.y2 + temp_y1y2;
	        	}
	        }this.square1 = new Rectangle(this.x1, this.y1, SIZE, SIZE);
	         this.square2 = new Rectangle(this.x2, this.y2, SIZE, SIZE);
		}
        
    }
    public void setHeight(int h) { 
        int temp_h = h;
        if (h > bound_h){
            this.height = h;
            this.valid = true;
        }else{
            if (this.height >= bound_h){
                this.height = this.height;
                //this.valid = true;
            }else{
                if(this.c == true){
                    this.height = bound_h + 1;
                    //this.c = false;
                }
            }
        }if (this.c == false && this.valid == true){
            setUp();
        }//this.c = false;
        this.valid = false;
    }
    public void setWidth(int w){
        int temp_w = this.width;
        if (w > bound_w){
            this.width = w; 
            this.valid = true;
        }else{
            if (this.width >= bound_w){
                this.width = this.width;
                //this.valid = true;
            }else{
                if (this.c == true){
                    this.width = bound_w + 1;
                    //this.c = false;
                }
            }
        }if (this.c == false && this.valid == true){
            setUp();
        }this.valid = false;
    }
}