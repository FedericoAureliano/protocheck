package PRuntime;

import java.util.HashSet;
import java.util.LinkedList;

public class PMachine {
    private HashSet<PMachineState> stateSet;
    private HashSet<PMachineVar> varSet;
    private PMachineState currentState;
    protected boolean alive;
    protected boolean isMain;
    private String name;

    public PMachine(String name, boolean isMain) {
        stateSet = new HashSet<>();
        varSet = new HashSet<>();
        this.name = name;
        this.isMain = isMain;
    }

    public void AddMachineVar(PRuntimeType type, String name) {
        varSet.add(new PMachineVar(type, name));
    }

    public void AddMachineState(PMachineState state) {
        stateSet.add(state);
    }

    private class PMachineState {
        private boolean isStart;
        private String name;

        public PMachineState(boolean isStart, String name) {
            this.isStart = isStart;
            this.name = name;
        }

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
