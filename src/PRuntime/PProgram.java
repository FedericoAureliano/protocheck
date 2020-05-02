package PRuntime;

import java.util.HashSet;

public class PProgram {

    private HashSet<PEvent> eventSet;
    private HashSet<PMachine> machineSet;

    public void addEvent(PEvent event) {
        eventSet.add(event);
    }
}