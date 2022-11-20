from Register import Register


class Instruction:
    OP_ADD = 'ADD'
    OP_SUB = 'SUB'
    OP_MUL = 'MUL'
    OP_DIV = 'DIV'

    def __init__(self, operation, regDest: Register, regS: Register, regT: Register) -> None:
        self.issueCycle = -1
        self.executionStart = -1
        self.executionComplete = -1
        self.writeBackCycle = -1

        self.op = operation
        self.regDest = regDest
        self.regS = regS
        self.regT = regT

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f'{self.issueCycle} {self.op}({self.regDest.name}, {self.regS.name} {self.regT.name})'

    def solve(a, b, opType):
        return Instruction.getOp(opType)(a, b)

    def getOp(opType):
        if opType == Instruction.OP_ADD:
            return lambda a, b: a + b
        elif opType == Instruction.OP_SUB:
            return lambda a, b: a - b
        elif opType == Instruction.OP_MUL:
            return lambda a, b: a * b
        elif opType == Instruction.OP_DIV:
            return lambda a, b: a / b
