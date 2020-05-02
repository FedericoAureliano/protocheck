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
        program.addEvent(new PEvent(eventName));
    }

    
}
