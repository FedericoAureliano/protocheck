package PRuntime;

import java.util.HashSet;
import java.util.LinkedList;

public class PMachine {
    private HashSet<PMachineState> stateSet;
    private LinkedList<PMachineVar> varList;


    private class PMachineState {
        private boolean isStart;
        private String name;

        public void entry(PEvent event, PMachineState state) {
            
        }

        public void onGoto(PEvent event, PMachineState state) {

        }

    }

    private class PMachineVar {
        private PRuntimeType type;
        private String name;

        public PMachineVar(PRuntimeType type, String name) {
            this.type = type;
            this.name = name;
        }

    }
}
