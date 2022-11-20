from ReservationStation import ReservationStation


class FunctionalUnit:
    ADD_TYPE = "add"
    MUL_TYPE = "mul"

    SIZE_ADD = 5
    SIZE_MUL = 10

    add_id = 0
    mul_id = 0

    def __init__(self, type: str) -> None:
        self.type = type

        if type == ReservationStation.ADD_TYPE:
            self.name = f'RS({type}_{str(FunctionalUnit.add_id)})'
            ReservationStation.add_id += 1
        if type == ReservationStation.MUL_TYPE:
            self.name = f'RS({type}_{str(FunctionalUnit.mul_id)})'
            ReservationStation.mul_id += 1

        self.clear()

    def __str__(self) -> str:
        return f'{self.name}'

    def clear(self):
        self.busy = False

        self.executionSize = None
        self.instruction = None
        self.Vj = None
        self.Vk = None
        self.result = None

    def appendInstruction(self, rs: ReservationStation):
        if rs.Vj is None or rs.Vk is None:
            return

        self.busy = True
        self.instruction = rs.instruction
        self.executionSize = self.getExecSize()

        self.Vj = rs.Vj
        self.Vk = rs.Vk

    def getExecSize(self):
        if self.type == FunctionalUnit.ADD_TYPE:
            return FunctionalUnit.SIZE_ADD
        elif self.type == FunctionalUnit.MUL_TYPE:
            return FunctionalUnit.SIZE_MUL
