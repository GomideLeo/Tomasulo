from Register import Register

class Instruction:
    OP_ADD = 1
    OP_SUB = 2
    OP_MUL = 3
    OP_DIV = 4
    
    def __init__(self, operation, reg1 : Register, reg2 : Register, reg3 : Register) -> None:
        self.issueCycle = 0
        self.executedCycle = 0
        self.executionSize = 0

        self.op = operation
        self.reg1 = reg1
        self.reg2 = reg2
        self.reg3 = reg3
    
    def solve(self) -> None:
        if self.op == Instruction.OP_ADD:
            self.reg1.value = self.reg2.value + self.reg3.value
        elif self.op == Instruction.OP_SUB:
            self.reg1.value = self.reg2.value - self.reg3.value
        elif self.op == Instruction.OP_MUL:
            self.reg1.value = self.reg2.value * self.reg3.value
        elif self.op == Instruction.OP_DIV:
            self.reg1.value = self.reg2.value / self.reg3.value