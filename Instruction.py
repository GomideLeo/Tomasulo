from Register import Register


class Instruction:
    OP_ADD = 1
    OP_SUB = 2
    OP_MUL = 3
    OP_DIV = 4

    def getOpKey(self):
        if self.op == Instruction.OP_ADD:
            return "add"
        elif self.op == Instruction.OP_SUB:
            return "sub"
        elif self.op == Instruction.OP_MUL:
            return "mul"
        elif self.op == Instruction.OP_DIV:
            return "div"

    def __init__(self, operation, reg1: Register, reg2: Register, reg3: Register) -> None:
        self.issueCycle = 0
        self.executedCycle = 0
        self.executionSize = 0

        self.op = operation
        self.reg1 = reg1
        self.reg2 = reg2
        self.reg3 = reg3

    def __str__(self):
        return f'{self.getOpKey()} ${self.reg1.name} ${self.reg2.name} ${self.reg3.name}'

    def __repr__(self) -> str:
        return str(self)

    def solve(self):
        if self.op == Instruction.OP_ADD:
            self.reg1.value = self.reg2.value + self.reg3.value
        elif self.op == Instruction.OP_SUB:
            self.reg1.value = self.reg2.value - self.reg3.value
        elif self.op == Instruction.OP_MUL:
            self.reg1.value = self.reg2.value * self.reg3.value
        elif self.op == Instruction.OP_DIV:
            self.reg1.value = self.reg2.value / self.reg3.value

    def getOp(self):
        if self.op == Instruction.OP_ADD:
            return lambda a, b: a + b
        elif self.op == Instruction.OP_SUB:
            return lambda a, b: a - b
        elif self.op == Instruction.OP_MUL:
            return lambda a, b: a * b
        elif self.op == Instruction.OP_DIV:
            return lambda a, b: a / b
