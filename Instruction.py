from Register import Register

class Instruction:
    OP_ADD = 'ADD'
    OP_SUB = 'SUV'
    OP_MUL = 'MUL'
    OP_DIV = 'DIV'

    SIZE_ADD = 5
    SIZE_MUL = 10
    
    def __init__(self, operation, regDest : Register, regS : Register, regT : Register) -> None:
        self.issueCycle         = -1
        self.executionStart     = -1
        self.executionComplete  = -1
        self.writeBackCycle     = -1

        self.executionSize      = -1

        self.op         = operation
        self.regDest    = regDest
        self.regS       = regS
        self.regT       = regT

    def __str__(self) -> None:
       return f'{self.op}({self.regDest.name}, {self.regS.name} {self.regT.name})'
    
    def solve(a, b, opType) -> None:
        if opType == Instruction.OP_ADD:
           return a + b
        elif opType == Instruction.OP_SUB:
           return a - b
        elif opType == Instruction.OP_MUL:
           return a * b
        elif opType == Instruction.OP_DIV:
           return a / b