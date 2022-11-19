from ReservationStation import ReservationStation


class FunctionalUnit:
    ADD_TYPE = "add"
    MUL_TYPE = "mul"

    mulDelay = 5
    addDelay = 2

    id = 0

    def __init__(self, type: str) -> None:
        FunctionalUnit.id += 1
        self.type = type
        self.name = f'FU({type}_{str(FunctionalUnit.id)})'
        self.clear()

    def __str__(self) -> str:
        return f'{self.name}'

    def clear(self):
        self.busy = False

        self.issueCycle = None
        self.op = None
        self.Vj = None
        self.Vk = None
        self.result = None
        self.originStation = None

    def appendInstruction(self, rs: ReservationStation, cicle):
        if rs.Vj is None or rs.Vk is None:
            return

        self.busy = True
        self.originStation = rs
        self.op = rs.op
        self.issueCycle = cicle

        self.Vj = rs.Vj
        self.Vk = rs.Vk

    def getDelay(self):
        if self.type == FunctionalUnit.ADD_TYPE:
            return FunctionalUnit.addDelay
        elif self.type == FunctionalUnit.MUL_TYPE:
            return FunctionalUnit.mulDelay

    def execute(self, currentCicle):
        if self.Vk is not None and self.Vj is not None and self.result is None:
            if currentCicle - self.issueCycle >= self.getDelay():
                self.result = self.op.getOp()(self.Vk, self.Vj)
