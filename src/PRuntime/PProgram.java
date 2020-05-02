package PRuntime;

import java.util.HashSet;

public class PProgram {

    private HashSet<PEvent> eventSet;
    private HashSet<PMachine> machineSet;
    private PMachine mainMachine;

    public PProgram() {
        eventSet = new HashSet<>();
        machineSet = new HashSet<>();
        mainMachine = null;
    }

    public void addEvent(PEvent event) {
        eventSet.add(event);
    }

    public void addMachine(PMachine machine) {
        machineSet.add(machine);
        if (machine.isMain) {
            assert(mainMachine == null);
            mainMachine = machine;
        }
    }
}