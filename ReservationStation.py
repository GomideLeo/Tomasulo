from Instruction import Instruction
from Register import Register


class ReservationStation:
    ADD_TYPE = "add"
    MUL_TYPE = "mul"

    mul_id = 0
    add_id = 0

    def __init__(self, type: str) -> None:
        self.type = type
        if type == ReservationStation.ADD_TYPE:
            self.name = f'RS({type}_{str(ReservationStation.add_id)})'
            ReservationStation.add_id += 1
        if type == ReservationStation.MUL_TYPE:
            self.name = f'RS({type}_{str(ReservationStation.mul_id)})'
            ReservationStation.mul_id += 1
        self.clear()

    def __str__(self) -> str:
        return f'{self.name}'

    def clear(self):
        self.busy = False
        self.instruction = None

        self.Qj = None
        self.Qk = None
        self.Vj = None
        self.Vk = None
        self.A = None

    def __str__(self) -> str:
        return f'{self.name}'

    def __repr__(self) -> str:
        return f'{self.name}'

    def appendInstruction(self, ins: Instruction):
        self.busy = True
        self.instruction = ins

        if type(ins.regS) == Register:
            self.Qj = ins.regS.writingInstruction
            if self.Qj is None:
                self.Vj = ins.regS.value
        else:
            self.Vj = ins.regS

        if type(ins.regT) == Register:
            self.Qk = ins.regT.writingInstruction
            if self.Qk is None:
                self.Vk = ins.regT.value
        else:
            self.Vk = ins.regT

        ins.regDest.writingInstruction = ins
