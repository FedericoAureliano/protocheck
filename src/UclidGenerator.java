import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.tree.*;
import java.io.*;

public class UclidGenerator {
    public static void main(String[] args) throws Exception {
        CharStream stream = CharStreams.fromFileName("examples/pingpong/pingpong.p");
        PLexer lexer = new PLexer(stream);
        // create a buffer of tokens pulled from the lexer
        CommonTokenStream tokens = new CommonTokenStream(lexer);
        // create a parser that feeds off the tokens buffer
        PParser parser = new PParser(tokens);
        ParseTree tree = parser.program();
        System.out.println(tree.toStringTree(parser));
    }
}