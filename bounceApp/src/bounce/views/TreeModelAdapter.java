package bounce.views;

/*
*  ============================================================================================
*  NAME : THERESA NATHANIA LAN
*  UPI : TLAN121 (569504563)
*  DESCRIPTION : TreeModelAdapter
*  ============================================================================================
*/
import bounce.NestingShape;
import bounce.Shape;
import bounce.ShapeModel;

import javax.swing.event.*;
import javax.swing.tree.*;

public class TreeModelAdapter implements TreeModel{
    private ShapeModel adaptee;
    public TreeModelAdapter(ShapeModel shape){
        adaptee = shape;
    }
    public Object getRoot(){
        return adaptee.root();
    }
    public Object getChild(Object parent, int index){
        if (parent instanceof NestingShape){
            NestingShape s = (NestingShape) parent;
            try{return s.shapeAt(index);}
            catch (IndexOutOfBoundsException e){return null;}
        }return null;
    }
    public int getChildCount(Object parent){
        if (parent instanceof NestingShape){
            NestingShape s = (NestingShape) parent;
            return s.shapeCount();
        }return 0;
    }
    public boolean isLeaf(Object parent){
        return !(parent instanceof NestingShape);
    }
    public int getIndexOfChild( Object parent, Object child ){ 
        int indexOfChild = -1;
        if ( parent instanceof NestingShape ){
            NestingShape s = ( NestingShape ) parent; 
            indexOfChild = s.indexOf((Shape)child);
        }
        return indexOfChild; 
    }
    public void addTreeModelListener(TreeModelListener t){;}
    public void removeTreeModelListener(TreeModelListener t){;}
    public void valueForPathChanged(TreePath p, Object s){;}
}
