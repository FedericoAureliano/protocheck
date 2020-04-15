from PModel import *
from PParserListener import PParserListener
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PParser import PParser
else:
    from PParser import PParser
# Customized listener


class PUclidParserListener(PParserListener):

    # need parser to extract token stream
    def __init__(self, parser: PParser, model: PModel):
        self.parser = parser
        self.model = model

    # Enter a parse tree produced by PParser#program.
    def enterProgram(self, ctx: PParser.ProgramContext):
        pass

    # Exit a parse tree produced by PParser#program.
    def exitProgram(self, ctx: PParser.ProgramContext):
        pass

    # Enter a parse tree produced by PParser#iden.
    def enterIden(self, ctx: PParser.IdenContext):
        pass

    # Exit a parse tree produced by PParser#iden.
    def exitIden(self, ctx: PParser.IdenContext):
        pass

    # Enter a parse tree produced by PParser#int_rule.
    def enterInt_rule(self, ctx: PParser.Int_ruleContext):
        pass

    # Exit a parse tree produced by PParser#int_rule.
    def exitInt_rule(self, ctx: PParser.Int_ruleContext):
        pass

    # Enter a parse tree produced by PParser#SeqType.
    def enterSeqType(self, ctx: PParser.SeqTypeContext):
        pass

    # Exit a parse tree produced by PParser#SeqType.
    def exitSeqType(self, ctx: PParser.SeqTypeContext):
        pass

    # Enter a parse tree produced by PParser#SetType.
    def enterSetType(self, ctx: PParser.SetTypeContext):
        pass

    # Exit a parse tree produced by PParser#SetType.
    def exitSetType(self, ctx: PParser.SetTypeContext):
        pass

    # Enter a parse tree produced by PParser#MapType.
    def enterMapType(self, ctx: PParser.MapTypeContext):
        pass

    # Exit a parse tree produced by PParser#MapType.
    def exitMapType(self, ctx: PParser.MapTypeContext):
        pass

    # Enter a parse tree produced by PParser#TupleType.
    def enterTupleType(self, ctx: PParser.TupleTypeContext):
        pass

    # Exit a parse tree produced by PParser#TupleType.
    def exitTupleType(self, ctx: PParser.TupleTypeContext):
        pass

    # Enter a parse tree produced by PParser#NamedTupleType.
    def enterNamedTupleType(self, ctx: PParser.NamedTupleTypeContext):
        pass

    # Exit a parse tree produced by PParser#NamedTupleType.
    def exitNamedTupleType(self, ctx: PParser.NamedTupleTypeContext):
        pass

    # Enter a parse tree produced by PParser#PrimitiveType.
    def enterPrimitiveType(self, ctx: PParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by PParser#PrimitiveType.
    def exitPrimitiveType(self, ctx: PParser.PrimitiveTypeContext):
        pass

    # Enter a parse tree produced by PParser#NamedType.
    def enterNamedType(self, ctx: PParser.NamedTypeContext):
        pass

    # Exit a parse tree produced by PParser#NamedType.
    def exitNamedType(self, ctx: PParser.NamedTypeContext):
        pass

    # Enter a parse tree produced by PParser#idenTypeList.
    def enterIdenTypeList(self, ctx: PParser.IdenTypeListContext):
        pass

    # Exit a parse tree produced by PParser#idenTypeList.
    def exitIdenTypeList(self, ctx: PParser.IdenTypeListContext):
        pass

    # Enter a parse tree produced by PParser#idenType.
    def enterIdenType(self, ctx: PParser.IdenTypeContext):
        pass

    # Exit a parse tree produced by PParser#idenType.
    def exitIdenType(self, ctx: PParser.IdenTypeContext):
        pass

    # Enter a parse tree produced by PParser#funParamList.
    def enterFunParamList(self, ctx: PParser.FunParamListContext):
        pass

    # Exit a parse tree produced by PParser#funParamList.
    def exitFunParamList(self, ctx: PParser.FunParamListContext):
        pass

    # Enter a parse tree produced by PParser#funParam.
    def enterFunParam(self, ctx: PParser.FunParamContext):
        pass

    # Exit a parse tree produced by PParser#funParam.
    def exitFunParam(self, ctx: PParser.FunParamContext):
        pass

    # Enter a parse tree produced by PParser#topDecl.
    def enterTopDecl(self, ctx: PParser.TopDeclContext):
        pass

    # Exit a parse tree produced by PParser#topDecl.
    def exitTopDecl(self, ctx: PParser.TopDeclContext):
        pass

    # Enter a parse tree produced by PParser#ForeignTypeDef.
    def enterForeignTypeDef(self, ctx: PParser.ForeignTypeDefContext):
        pass

    # Exit a parse tree produced by PParser#ForeignTypeDef.
    def exitForeignTypeDef(self, ctx: PParser.ForeignTypeDefContext):
        pass

    # Enter a parse tree produced by PParser#PTypeDef.
    def enterPTypeDef(self, ctx: PParser.PTypeDefContext):
        pass

    # Exit a parse tree produced by PParser#PTypeDef.
    def exitPTypeDef(self, ctx: PParser.PTypeDefContext):
        pass

    # Enter a parse tree produced by PParser#enumTypeDefDecl.
    def enterEnumTypeDefDecl(self, ctx: PParser.EnumTypeDefDeclContext):
        pass

    # Exit a parse tree produced by PParser#enumTypeDefDecl.
    def exitEnumTypeDefDecl(self, ctx: PParser.EnumTypeDefDeclContext):
        pass

    # Enter a parse tree produced by PParser#enumElemList.
    def enterEnumElemList(self, ctx: PParser.EnumElemListContext):
        pass

    # Exit a parse tree produced by PParser#enumElemList.
    def exitEnumElemList(self, ctx: PParser.EnumElemListContext):
        pass

    # Enter a parse tree produced by PParser#enumElem.
    def enterEnumElem(self, ctx: PParser.EnumElemContext):
        pass

    # Exit a parse tree produced by PParser#enumElem.
    def exitEnumElem(self, ctx: PParser.EnumElemContext):
        pass

    # Enter a parse tree produced by PParser#numberedEnumElemList.
    def enterNumberedEnumElemList(self, ctx: PParser.NumberedEnumElemListContext):
        pass

    # Exit a parse tree produced by PParser#numberedEnumElemList.
    def exitNumberedEnumElemList(self, ctx: PParser.NumberedEnumElemListContext):
        pass

    # Enter a parse tree produced by PParser#numberedEnumElem.
    def enterNumberedEnumElem(self, ctx: PParser.NumberedEnumElemContext):
        pass

    # Exit a parse tree produced by PParser#numberedEnumElem.
    def exitNumberedEnumElem(self, ctx: PParser.NumberedEnumElemContext):
        pass

    # Enter a parse tree produced by PParser#eventDecl.
    def enterEventDecl(self, ctx: PParser.EventDeclContext):
        event_payload = ctx.iden().Iden()
        self.model.add_event(PEvent(event_payload))

    # Exit a parse tree produced by PParser#eventDecl.

    def exitEventDecl(self, ctx: PParser.EventDeclContext):
        pass

        # Enter a parse tree produced by PParser#cardinality.
    def enterCardinality(self, ctx: PParser.CardinalityContext):
        pass

    # Exit a parse tree produced by PParser#cardinality.
    def exitCardinality(self, ctx: PParser.CardinalityContext):
        pass

    # Enter a parse tree produced by PParser#eventSetDecl.
    def enterEventSetDecl(self, ctx: PParser.EventSetDeclContext):
        pass

    # Exit a parse tree produced by PParser#eventSetDecl.
    def exitEventSetDecl(self, ctx: PParser.EventSetDeclContext):
        pass

    # Enter a parse tree produced by PParser#eventSetLiteral.
    def enterEventSetLiteral(self, ctx: PParser.EventSetLiteralContext):
        pass

    # Exit a parse tree produced by PParser#eventSetLiteral.
    def exitEventSetLiteral(self, ctx: PParser.EventSetLiteralContext):
        pass

    # Enter a parse tree produced by PParser#interfaceDecl.
    def enterInterfaceDecl(self, ctx: PParser.InterfaceDeclContext):
        pass

    # Exit a parse tree produced by PParser#interfaceDecl.
    def exitInterfaceDecl(self, ctx: PParser.InterfaceDeclContext):
        pass

    # Enter a parse tree produced by PParser#implMachineDecl.
    def enterImplMachineDecl(self, ctx: PParser.ImplMachineDeclContext):
        new_machine = Pmachine(ctx.iden().Iden())
        machineBody = ctx.machineBody()
        if machineBody != None:
            machineEntry = machineBody.machineEntry() 
            print(machineEntry.varDecl())
        self.model.add_machine(new_machine)

    # Exit a parse tree produced by PParser#implMachineDecl.
    def exitImplMachineDecl(self, ctx: PParser.ImplMachineDeclContext):
        pass

    # Enter a parse tree produced by PParser#idenList.
    def enterIdenList(self, ctx: PParser.IdenListContext):
        pass

    # Exit a parse tree produced by PParser#idenList.
    def exitIdenList(self, ctx: PParser.IdenListContext):
        pass

    # Enter a parse tree produced by PParser#MachineReceive.
    def enterMachineReceive(self, ctx: PParser.MachineReceiveContext):
        pass

    # Exit a parse tree produced by PParser#MachineReceive.
    def exitMachineReceive(self, ctx: PParser.MachineReceiveContext):
        pass

    # Enter a parse tree produced by PParser#MachineSend.
    def enterMachineSend(self, ctx: PParser.MachineSendContext):
        pass

    # Exit a parse tree produced by PParser#MachineSend.
    def exitMachineSend(self, ctx: PParser.MachineSendContext):
        pass

    # Enter a parse tree produced by PParser#specMachineDecl.
    def enterSpecMachineDecl(self, ctx: PParser.SpecMachineDeclContext):
        pass

    # Exit a parse tree produced by PParser#specMachineDecl.
    def exitSpecMachineDecl(self, ctx: PParser.SpecMachineDeclContext):
        pass

    # Enter a parse tree produced by PParser#machineBody.
    def enterMachineBody(self, ctx: PParser.MachineBodyContext):
        pass

    # Exit a parse tree produced by PParser#machineBody.
    def exitMachineBody(self, ctx: PParser.MachineBodyContext):
        pass

    # Enter a parse tree produced by PParser#machineEntry.
    def enterMachineEntry(self, ctx: PParser.MachineEntryContext):
        pass

    # Exit a parse tree produced by PParser#machineEntry.
    def exitMachineEntry(self, ctx: PParser.MachineEntryContext):
        pass

    # Enter a parse tree produced by PParser#varDecl.
    def enterVarDecl(self, ctx: PParser.VarDeclContext):
        pass

    # Exit a parse tree produced by PParser#varDecl.
    def exitVarDecl(self, ctx: PParser.VarDeclContext):
        pass

    # Enter a parse tree produced by PParser#ForeignFunDecl.
    def enterForeignFunDecl(self, ctx: PParser.ForeignFunDeclContext):
        pass

    # Exit a parse tree produced by PParser#ForeignFunDecl.
    def exitForeignFunDecl(self, ctx: PParser.ForeignFunDeclContext):
        pass

    # Enter a parse tree produced by PParser#PFunDecl.
    def enterPFunDecl(self, ctx: PParser.PFunDeclContext):
        pass

    # Exit a parse tree produced by PParser#PFunDecl.
    def exitPFunDecl(self, ctx: PParser.PFunDeclContext):
        pass

    # Enter a parse tree produced by PParser#group.
    def enterGroup(self, ctx: PParser.GroupContext):
        pass

    # Exit a parse tree produced by PParser#group.
    def exitGroup(self, ctx: PParser.GroupContext):
        pass

    # Enter a parse tree produced by PParser#groupItem.
    def enterGroupItem(self, ctx: PParser.GroupItemContext):
        pass

    # Exit a parse tree produced by PParser#groupItem.
    def exitGroupItem(self, ctx: PParser.GroupItemContext):
        pass

    # Enter a parse tree produced by PParser#stateDecl.
    def enterStateDecl(self, ctx: PParser.StateDeclContext):
        pass

    # Exit a parse tree produced by PParser#stateDecl.
    def exitStateDecl(self, ctx: PParser.StateDeclContext):
        pass

    # Enter a parse tree produced by PParser#StateEntry.
    def enterStateEntry(self, ctx: PParser.StateEntryContext):
        pass

    # Exit a parse tree produced by PParser#StateEntry.
    def exitStateEntry(self, ctx: PParser.StateEntryContext):
        pass

    # Enter a parse tree produced by PParser#StateExit.
    def enterStateExit(self, ctx: PParser.StateExitContext):
        pass

    # Exit a parse tree produced by PParser#StateExit.
    def exitStateExit(self, ctx: PParser.StateExitContext):
        pass

    # Enter a parse tree produced by PParser#StateDefer.
    def enterStateDefer(self, ctx: PParser.StateDeferContext):
        pass

    # Exit a parse tree produced by PParser#StateDefer.
    def exitStateDefer(self, ctx: PParser.StateDeferContext):
        pass

    # Enter a parse tree produced by PParser#StateIgnore.
    def enterStateIgnore(self, ctx: PParser.StateIgnoreContext):
        pass

    # Exit a parse tree produced by PParser#StateIgnore.
    def exitStateIgnore(self, ctx: PParser.StateIgnoreContext):
        pass

    # Enter a parse tree produced by PParser#OnEventDoAction.
    def enterOnEventDoAction(self, ctx: PParser.OnEventDoActionContext):
        pass

    # Exit a parse tree produced by PParser#OnEventDoAction.
    def exitOnEventDoAction(self, ctx: PParser.OnEventDoActionContext):
        pass

    # Enter a parse tree produced by PParser#OnEventPushState.
    def enterOnEventPushState(self, ctx: PParser.OnEventPushStateContext):
        pass

    # Exit a parse tree produced by PParser#OnEventPushState.
    def exitOnEventPushState(self, ctx: PParser.OnEventPushStateContext):
        pass

    # Enter a parse tree produced by PParser#OnEventGotoState.
    def enterOnEventGotoState(self, ctx: PParser.OnEventGotoStateContext):
        pass

    # Exit a parse tree produced by PParser#OnEventGotoState.
    def exitOnEventGotoState(self, ctx: PParser.OnEventGotoStateContext):
        pass

    # Enter a parse tree produced by PParser#nonDefaultEventList.
    def enterNonDefaultEventList(self, ctx: PParser.NonDefaultEventListContext):
        pass

    # Exit a parse tree produced by PParser#nonDefaultEventList.
    def exitNonDefaultEventList(self, ctx: PParser.NonDefaultEventListContext):
        pass

    # Enter a parse tree produced by PParser#nonDefaultEvent.
    def enterNonDefaultEvent(self, ctx: PParser.NonDefaultEventContext):
        pass

    # Exit a parse tree produced by PParser#nonDefaultEvent.
    def exitNonDefaultEvent(self, ctx: PParser.NonDefaultEventContext):
        pass

    # Enter a parse tree produced by PParser#eventList.
    def enterEventList(self, ctx: PParser.EventListContext):
        pass

    # Exit a parse tree produced by PParser#eventList.
    def exitEventList(self, ctx: PParser.EventListContext):
        pass

    # Enter a parse tree produced by PParser#eventId.
    def enterEventId(self, ctx: PParser.EventIdContext):
        pass

    # Exit a parse tree produced by PParser#eventId.
    def exitEventId(self, ctx: PParser.EventIdContext):
        pass

    # Enter a parse tree produced by PParser#stateName.
    def enterStateName(self, ctx: PParser.StateNameContext):
        pass

    # Exit a parse tree produced by PParser#stateName.
    def exitStateName(self, ctx: PParser.StateNameContext):
        pass

    # Enter a parse tree produced by PParser#functionBody.
    def enterFunctionBody(self, ctx: PParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by PParser#functionBody.
    def exitFunctionBody(self, ctx: PParser.FunctionBodyContext):
        pass

    # Enter a parse tree produced by PParser#CompoundStmt.
    def enterCompoundStmt(self, ctx: PParser.CompoundStmtContext):
        pass

    # Exit a parse tree produced by PParser#CompoundStmt.
    def exitCompoundStmt(self, ctx: PParser.CompoundStmtContext):
        pass

    # Enter a parse tree produced by PParser#PopStmt.
    def enterPopStmt(self, ctx: PParser.PopStmtContext):
        pass

    # Exit a parse tree produced by PParser#PopStmt.
    def exitPopStmt(self, ctx: PParser.PopStmtContext):
        pass

    # Enter a parse tree produced by PParser#AssertStmt.
    def enterAssertStmt(self, ctx: PParser.AssertStmtContext):
        pass

    # Exit a parse tree produced by PParser#AssertStmt.
    def exitAssertStmt(self, ctx: PParser.AssertStmtContext):
        pass

    # Enter a parse tree produced by PParser#PrintStmt.
    def enterPrintStmt(self, ctx: PParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by PParser#PrintStmt.
    def exitPrintStmt(self, ctx: PParser.PrintStmtContext):
        pass

    # Enter a parse tree produced by PParser#ReturnStmt.
    def enterReturnStmt(self, ctx: PParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by PParser#ReturnStmt.
    def exitReturnStmt(self, ctx: PParser.ReturnStmtContext):
        pass

    # Enter a parse tree produced by PParser#BreakStmt.
    def enterBreakStmt(self, ctx: PParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by PParser#BreakStmt.
    def exitBreakStmt(self, ctx: PParser.BreakStmtContext):
        pass

    # Enter a parse tree produced by PParser#ContinueStmt.
    def enterContinueStmt(self, ctx: PParser.ContinueStmtContext):
        pass

    # Exit a parse tree produced by PParser#ContinueStmt.
    def exitContinueStmt(self, ctx: PParser.ContinueStmtContext):
        pass

    # Enter a parse tree produced by PParser#AssignStmt.
    def enterAssignStmt(self, ctx: PParser.AssignStmtContext):
        pass

    # Exit a parse tree produced by PParser#AssignStmt.
    def exitAssignStmt(self, ctx: PParser.AssignStmtContext):
        pass

    # Enter a parse tree produced by PParser#InsertStmt.
    def enterInsertStmt(self, ctx: PParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by PParser#InsertStmt.
    def exitInsertStmt(self, ctx: PParser.InsertStmtContext):
        pass

    # Enter a parse tree produced by PParser#AddStmt.
    def enterAddStmt(self, ctx: PParser.AddStmtContext):
        pass

    # Exit a parse tree produced by PParser#AddStmt.
    def exitAddStmt(self, ctx: PParser.AddStmtContext):
        pass

    # Enter a parse tree produced by PParser#RemoveStmt.
    def enterRemoveStmt(self, ctx: PParser.RemoveStmtContext):
        pass

    # Exit a parse tree produced by PParser#RemoveStmt.
    def exitRemoveStmt(self, ctx: PParser.RemoveStmtContext):
        pass

    # Enter a parse tree produced by PParser#WhileStmt.
    def enterWhileStmt(self, ctx: PParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by PParser#WhileStmt.
    def exitWhileStmt(self, ctx: PParser.WhileStmtContext):
        pass

    # Enter a parse tree produced by PParser#IfStmt.
    def enterIfStmt(self, ctx: PParser.IfStmtContext):
        pass

    # Exit a parse tree produced by PParser#IfStmt.
    def exitIfStmt(self, ctx: PParser.IfStmtContext):
        pass

    # Enter a parse tree produced by PParser#CtorStmt.
    def enterCtorStmt(self, ctx: PParser.CtorStmtContext):
        pass

    # Exit a parse tree produced by PParser#CtorStmt.
    def exitCtorStmt(self, ctx: PParser.CtorStmtContext):
        pass

    # Enter a parse tree produced by PParser#FunCallStmt.
    def enterFunCallStmt(self, ctx: PParser.FunCallStmtContext):
        pass

    # Exit a parse tree produced by PParser#FunCallStmt.
    def exitFunCallStmt(self, ctx: PParser.FunCallStmtContext):
        pass

    # Enter a parse tree produced by PParser#RaiseStmt.
    def enterRaiseStmt(self, ctx: PParser.RaiseStmtContext):
        pass

    # Exit a parse tree produced by PParser#RaiseStmt.
    def exitRaiseStmt(self, ctx: PParser.RaiseStmtContext):
        pass

    # Enter a parse tree produced by PParser#SendStmt.
    def enterSendStmt(self, ctx: PParser.SendStmtContext):
        pass

    # Exit a parse tree produced by PParser#SendStmt.
    def exitSendStmt(self, ctx: PParser.SendStmtContext):
        pass

    # Enter a parse tree produced by PParser#AnnounceStmt.
    def enterAnnounceStmt(self, ctx: PParser.AnnounceStmtContext):
        pass

    # Exit a parse tree produced by PParser#AnnounceStmt.
    def exitAnnounceStmt(self, ctx: PParser.AnnounceStmtContext):
        pass

    # Enter a parse tree produced by PParser#GotoStmt.
    def enterGotoStmt(self, ctx: PParser.GotoStmtContext):
        pass

    # Exit a parse tree produced by PParser#GotoStmt.
    def exitGotoStmt(self, ctx: PParser.GotoStmtContext):
        pass

    # Enter a parse tree produced by PParser#ReceiveStmt.
    def enterReceiveStmt(self, ctx: PParser.ReceiveStmtContext):
        pass

    # Exit a parse tree produced by PParser#ReceiveStmt.
    def exitReceiveStmt(self, ctx: PParser.ReceiveStmtContext):
        pass

    # Enter a parse tree produced by PParser#NoStmt.
    def enterNoStmt(self, ctx: PParser.NoStmtContext):
        pass

    # Exit a parse tree produced by PParser#NoStmt.
    def exitNoStmt(self, ctx: PParser.NoStmtContext):
        pass

    # Enter a parse tree produced by PParser#TupleLvalue.
    def enterTupleLvalue(self, ctx: PParser.TupleLvalueContext):
        pass

    # Exit a parse tree produced by PParser#TupleLvalue.
    def exitTupleLvalue(self, ctx: PParser.TupleLvalueContext):
        pass

    # Enter a parse tree produced by PParser#NamedTupleLvalue.
    def enterNamedTupleLvalue(self, ctx: PParser.NamedTupleLvalueContext):
        pass

    # Exit a parse tree produced by PParser#NamedTupleLvalue.
    def exitNamedTupleLvalue(self, ctx: PParser.NamedTupleLvalueContext):
        pass

    # Enter a parse tree produced by PParser#MapOrSeqLvalue.
    def enterMapOrSeqLvalue(self, ctx: PParser.MapOrSeqLvalueContext):
        pass

    # Exit a parse tree produced by PParser#MapOrSeqLvalue.
    def exitMapOrSeqLvalue(self, ctx: PParser.MapOrSeqLvalueContext):
        pass

    # Enter a parse tree produced by PParser#VarLvalue.
    def enterVarLvalue(self, ctx: PParser.VarLvalueContext):
        pass

    # Exit a parse tree produced by PParser#VarLvalue.
    def exitVarLvalue(self, ctx: PParser.VarLvalueContext):
        pass

    # Enter a parse tree produced by PParser#recvCase.
    def enterRecvCase(self, ctx: PParser.RecvCaseContext):
        pass

    # Exit a parse tree produced by PParser#recvCase.
    def exitRecvCase(self, ctx: PParser.RecvCaseContext):
        pass

    # Enter a parse tree produced by PParser#anonEventHandler.
    def enterAnonEventHandler(self, ctx: PParser.AnonEventHandlerContext):
        pass

    # Exit a parse tree produced by PParser#anonEventHandler.
    def exitAnonEventHandler(self, ctx: PParser.AnonEventHandlerContext):
        pass

    # Enter a parse tree produced by PParser#noParamAnonEventHandler.
    def enterNoParamAnonEventHandler(self, ctx: PParser.NoParamAnonEventHandlerContext):
        pass

    # Exit a parse tree produced by PParser#noParamAnonEventHandler.
    def exitNoParamAnonEventHandler(self, ctx: PParser.NoParamAnonEventHandlerContext):
        pass

    # Enter a parse tree produced by PParser#StringExpr.
    def enterStringExpr(self, ctx: PParser.StringExprContext):
        pass

    # Exit a parse tree produced by PParser#StringExpr.
    def exitStringExpr(self, ctx: PParser.StringExprContext):
        pass

    # Enter a parse tree produced by PParser#KeywordExpr.
    def enterKeywordExpr(self, ctx: PParser.KeywordExprContext):
        pass

    # Exit a parse tree produced by PParser#KeywordExpr.
    def exitKeywordExpr(self, ctx: PParser.KeywordExprContext):
        pass

    # Enter a parse tree produced by PParser#ChooseExpr.
    def enterChooseExpr(self, ctx: PParser.ChooseExprContext):
        pass

    # Exit a parse tree produced by PParser#ChooseExpr.
    def exitChooseExpr(self, ctx: PParser.ChooseExprContext):
        pass

    # Enter a parse tree produced by PParser#SeqAccessExpr.
    def enterSeqAccessExpr(self, ctx: PParser.SeqAccessExprContext):
        pass

    # Exit a parse tree produced by PParser#SeqAccessExpr.
    def exitSeqAccessExpr(self, ctx: PParser.SeqAccessExprContext):
        pass

    # Enter a parse tree produced by PParser#NamedTupleAccessExpr.
    def enterNamedTupleAccessExpr(self, ctx: PParser.NamedTupleAccessExprContext):
        pass

    # Exit a parse tree produced by PParser#NamedTupleAccessExpr.
    def exitNamedTupleAccessExpr(self, ctx: PParser.NamedTupleAccessExprContext):
        pass

    # Enter a parse tree produced by PParser#PrimitiveExpr.
    def enterPrimitiveExpr(self, ctx: PParser.PrimitiveExprContext):
        pass

    # Exit a parse tree produced by PParser#PrimitiveExpr.
    def exitPrimitiveExpr(self, ctx: PParser.PrimitiveExprContext):
        pass

    # Enter a parse tree produced by PParser#BinExpr.
    def enterBinExpr(self, ctx: PParser.BinExprContext):
        pass

    # Exit a parse tree produced by PParser#BinExpr.
    def exitBinExpr(self, ctx: PParser.BinExprContext):
        pass

    # Enter a parse tree produced by PParser#UnaryExpr.
    def enterUnaryExpr(self, ctx: PParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by PParser#UnaryExpr.
    def exitUnaryExpr(self, ctx: PParser.UnaryExprContext):
        pass

    # Enter a parse tree produced by PParser#TupleAccessExpr.
    def enterTupleAccessExpr(self, ctx: PParser.TupleAccessExprContext):
        pass

    # Exit a parse tree produced by PParser#TupleAccessExpr.
    def exitTupleAccessExpr(self, ctx: PParser.TupleAccessExprContext):
        pass

    # Enter a parse tree produced by PParser#UnnamedTupleExpr.
    def enterUnnamedTupleExpr(self, ctx: PParser.UnnamedTupleExprContext):
        pass

    # Exit a parse tree produced by PParser#UnnamedTupleExpr.
    def exitUnnamedTupleExpr(self, ctx: PParser.UnnamedTupleExprContext):
        pass

    # Enter a parse tree produced by PParser#FunCallExpr.
    def enterFunCallExpr(self, ctx: PParser.FunCallExprContext):
        pass

    # Exit a parse tree produced by PParser#FunCallExpr.
    def exitFunCallExpr(self, ctx: PParser.FunCallExprContext):
        pass

    # Enter a parse tree produced by PParser#CastExpr.
    def enterCastExpr(self, ctx: PParser.CastExprContext):
        pass

    # Exit a parse tree produced by PParser#CastExpr.
    def exitCastExpr(self, ctx: PParser.CastExprContext):
        pass

    # Enter a parse tree produced by PParser#CtorExpr.
    def enterCtorExpr(self, ctx: PParser.CtorExprContext):
        pass

    # Exit a parse tree produced by PParser#CtorExpr.
    def exitCtorExpr(self, ctx: PParser.CtorExprContext):
        pass

    # Enter a parse tree produced by PParser#ParenExpr.
    def enterParenExpr(self, ctx: PParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PParser#ParenExpr.
    def exitParenExpr(self, ctx: PParser.ParenExprContext):
        pass

    # Enter a parse tree produced by PParser#NamedTupleExpr.
    def enterNamedTupleExpr(self, ctx: PParser.NamedTupleExprContext):
        pass

    # Exit a parse tree produced by PParser#NamedTupleExpr.
    def exitNamedTupleExpr(self, ctx: PParser.NamedTupleExprContext):
        pass

    # Enter a parse tree produced by PParser#formatedString.
    def enterFormatedString(self, ctx: PParser.FormatedStringContext):
        pass

    # Exit a parse tree produced by PParser#formatedString.
    def exitFormatedString(self, ctx: PParser.FormatedStringContext):
        pass

    # Enter a parse tree produced by PParser#primitive.
    def enterPrimitive(self, ctx: PParser.PrimitiveContext):
        pass

    # Exit a parse tree produced by PParser#primitive.
    def exitPrimitive(self, ctx: PParser.PrimitiveContext):
        pass

    # Enter a parse tree produced by PParser#DecimalFloat.
    def enterDecimalFloat(self, ctx: PParser.DecimalFloatContext):
        pass

    # Exit a parse tree produced by PParser#DecimalFloat.
    def exitDecimalFloat(self, ctx: PParser.DecimalFloatContext):
        pass

    # Enter a parse tree produced by PParser#ExpFloat.
    def enterExpFloat(self, ctx: PParser.ExpFloatContext):
        pass

    # Exit a parse tree produced by PParser#ExpFloat.
    def exitExpFloat(self, ctx: PParser.ExpFloatContext):
        pass

    # Enter a parse tree produced by PParser#unnamedTupleBody.
    def enterUnnamedTupleBody(self, ctx: PParser.UnnamedTupleBodyContext):
        pass

    # Exit a parse tree produced by PParser#unnamedTupleBody.
    def exitUnnamedTupleBody(self, ctx: PParser.UnnamedTupleBodyContext):
        pass

    # Enter a parse tree produced by PParser#namedTupleBody.
    def enterNamedTupleBody(self, ctx: PParser.NamedTupleBodyContext):
        pass

    # Exit a parse tree produced by PParser#namedTupleBody.
    def exitNamedTupleBody(self, ctx: PParser.NamedTupleBodyContext):
        pass

    # Enter a parse tree produced by PParser#rvalueList.
    def enterRvalueList(self, ctx: PParser.RvalueListContext):
        pass

    # Exit a parse tree produced by PParser#rvalueList.
    def exitRvalueList(self, ctx: PParser.RvalueListContext):
        pass

    # Enter a parse tree produced by PParser#rvalue.
    def enterRvalue(self, ctx: PParser.RvalueContext):
        pass

    # Exit a parse tree produced by PParser#rvalue.
    def exitRvalue(self, ctx: PParser.RvalueContext):
        pass

    # Enter a parse tree produced by PParser#ParenModuleExpr.
    def enterParenModuleExpr(self, ctx: PParser.ParenModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#ParenModuleExpr.
    def exitParenModuleExpr(self, ctx: PParser.ParenModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#PrimitiveModuleExpr.
    def enterPrimitiveModuleExpr(self, ctx: PParser.PrimitiveModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#PrimitiveModuleExpr.
    def exitPrimitiveModuleExpr(self, ctx: PParser.PrimitiveModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#NamedModule.
    def enterNamedModule(self, ctx: PParser.NamedModuleContext):
        pass

    # Exit a parse tree produced by PParser#NamedModule.
    def exitNamedModule(self, ctx: PParser.NamedModuleContext):
        pass

    # Enter a parse tree produced by PParser#ComposeModuleExpr.
    def enterComposeModuleExpr(self, ctx: PParser.ComposeModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#ComposeModuleExpr.
    def exitComposeModuleExpr(self, ctx: PParser.ComposeModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#UnionModuleExpr.
    def enterUnionModuleExpr(self, ctx: PParser.UnionModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#UnionModuleExpr.
    def exitUnionModuleExpr(self, ctx: PParser.UnionModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#HideEventsModuleExpr.
    def enterHideEventsModuleExpr(self, ctx: PParser.HideEventsModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#HideEventsModuleExpr.
    def exitHideEventsModuleExpr(self, ctx: PParser.HideEventsModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#HideInterfacesModuleExpr.
    def enterHideInterfacesModuleExpr(self, ctx: PParser.HideInterfacesModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#HideInterfacesModuleExpr.
    def exitHideInterfacesModuleExpr(self, ctx: PParser.HideInterfacesModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#AssertModuleExpr.
    def enterAssertModuleExpr(self, ctx: PParser.AssertModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#AssertModuleExpr.
    def exitAssertModuleExpr(self, ctx: PParser.AssertModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#RenameModuleExpr.
    def enterRenameModuleExpr(self, ctx: PParser.RenameModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#RenameModuleExpr.
    def exitRenameModuleExpr(self, ctx: PParser.RenameModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#MainMachineModuleExpr.
    def enterMainMachineModuleExpr(self, ctx: PParser.MainMachineModuleExprContext):
        pass

    # Exit a parse tree produced by PParser#MainMachineModuleExpr.
    def exitMainMachineModuleExpr(self, ctx: PParser.MainMachineModuleExprContext):
        pass

    # Enter a parse tree produced by PParser#bindExpr.
    def enterBindExpr(self, ctx: PParser.BindExprContext):
        pass

    # Exit a parse tree produced by PParser#bindExpr.
    def exitBindExpr(self, ctx: PParser.BindExprContext):
        pass

    # Enter a parse tree produced by PParser#namedModuleDecl.
    def enterNamedModuleDecl(self, ctx: PParser.NamedModuleDeclContext):
        pass

    # Exit a parse tree produced by PParser#namedModuleDecl.
    def exitNamedModuleDecl(self, ctx: PParser.NamedModuleDeclContext):
        pass

    # Enter a parse tree produced by PParser#SafetyTestDecl.
    def enterSafetyTestDecl(self, ctx: PParser.SafetyTestDeclContext):
        pass

    # Exit a parse tree produced by PParser#SafetyTestDecl.
    def exitSafetyTestDecl(self, ctx: PParser.SafetyTestDeclContext):
        pass

    # Enter a parse tree produced by PParser#RefinementTestDecl.
    def enterRefinementTestDecl(self, ctx: PParser.RefinementTestDeclContext):
        pass

    # Exit a parse tree produced by PParser#RefinementTestDecl.
    def exitRefinementTestDecl(self, ctx: PParser.RefinementTestDeclContext):
        pass

    # Enter a parse tree produced by PParser#implementationDecl.
    def enterImplementationDecl(self, ctx: PParser.ImplementationDeclContext):
        pass

    # Exit a parse tree produced by PParser#implementationDecl.
    def exitImplementationDecl(self, ctx: PParser.ImplementationDeclContext):
        pass
