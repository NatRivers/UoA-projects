package bounce.views;
/*
*  ============================================================================================
*  NAME : THERESA NATHANIA LAN
*  UPI : TLAN121 (569504563)
*  DESCRIPTION : TreeModelAdapterWithShapeModelListener
*  ============================================================================================
*/
import java.util.*;
import javax.swing.event.*;
import javax.swing.tree.*;

import bounce.NestingShape;
import bounce.Shape;
import bounce.ShapeModel;
import bounce.ShapeModelEvent;
import bounce.ShapeModelListener;

public class TreeModelAdapterWithShapeModelListener extends TreeModelAdapter implements ShapeModelListener{
    private ArrayList<TreeModelListener> TML_lst = new ArrayList<TreeModelListener>();
    public TreeModelAdapterWithShapeModelListener(ShapeModel shape){
        super(shape);
    }
    public void addTreeModelListener(TreeModelListener t){
        TML_lst.add(t);
    }
    public void removeTreeModelListener(TreeModelListener t){
        TML_lst.remove(t);
    }
    public void update(ShapeModelEvent event){
        ShapeModelEvent.EventType event_type = event.eventType();
        Shape operand;
        Object[] o;
        NestingShape ns = event.parent();
        int index;
        int[] i;
        TreeModelEvent e;
        
        switch (event_type){
            case ShapeAdded:
                operand = event.operand();
                o = new Object[] {operand};
                index = event.index();
                i = new int[] {index};
                e = new TreeModelEvent(this, ns.path().toArray(), i, o);
                for (TreeModelListener tml : TML_lst){
                    tml.treeNodesInserted(e);
                }break;
            case ShapeRemoved:
                operand = event.operand();
                o = new Object[]{operand};
                index = event.index();
                i = new int[] {index};
                e = new TreeModelEvent(this, ns.path().toArray(), i, o);
                for (TreeModelListener tml : TML_lst){
                    tml.treeNodesRemoved(e);
                }break;
            case ShapeMoved:
                break;
        }
    }
}
