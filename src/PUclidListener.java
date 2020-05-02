import org.antlr.v4.gui.SystemFontMetrics;

import PRuntime.PEvent;
import PRuntime.PProgram;

public class PUclidListener extends PParserBaseListener {
    private PProgram program;

    public PUclidListener() {
        this.program = new PProgram();
    }

    @Override
    public void enterEventDecl(PParser.EventDeclContext ctx) {
        String eventName = ctx.name.Iden().getText();
        System.out.println("Found event declaration: " + eventName);
        System.out.println("-----------------------------");
        program.addEvent(new PEvent(eventName));
    }

    @Override
    public void enterImplMachineDecl(PParser.ImplMachineDeclContext ctx) {
        String machineName = ctx.name.Iden().getText();
        boolean isMain = ctx.MAIN() != null;
        System.out.println("Found impl machine declaration: " + machineName);
        System.out.println("is main machine? " + isMain);
        System.out.println("-----------------------------");
    }

}
