from Instruction import Instruction


class ReservationStation:
    ADD_TYPE = "add"
    MUL_TYPE = "mul"

    id = 0

    def __init__(self, type: str) -> None:
        ReservationStation.id += 1
        self.type = type
        self.name = f'RS({type}_{str(ReservationStation.id)})'
        self.clear()

    def __str__(self) -> str:
        return f'{self.name}'

    def clear(self):
        self.busy = False

        self.op = None
        self.Vj = None
        self.Vk = None
        self.Qj = None
        self.Qk = None
        self.A = None

    def appendInstruction(self, ins: Instruction):
        self.busy = True
        self.op = ins

        if ins.reg2.busy:
            self.Qj = ins.reg2.reservationStation
        else:
            self.Vj = ins.reg2.value

        if ins.reg3.busy:
            self.Qk = ins.reg3.reservationStation
        else:
            self.Vk = ins.reg3.value

        ins.reg1.busy = True
        ins.reg1.reservationStation = self

    def canExecute(self):
        if not self.busy:
            return False

        return self.Qj is None and self.Qk is None
