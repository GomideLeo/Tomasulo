from Instruction import Instruction

class ReservationStation:
    ADD_TYPE = "add"
    MUL_TYPE = "mul"

    id = 0

    def __init__(self, type: str) -> None:
        ReservationStation.id += 1
        self.type = type
        self.name = f'RS({type}_{str(ReservationStation.id)})'
        self.busy = False
        
        self.instruction = None
        self.Vj = None
        self.Vk = None
        self.Qj = None
        self.Qk = None

        self.A = None
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def appendInstruction(self, ins: Instruction):
        self.busy = True
        self.instruction = ins

        self.Qj = ins.regS.writingUnit
        self.Qk = ins.regT.writingUnit

        if self.Qj is None:
            self.Vj = ins.regS.value

        if self.Qk is None:
            self.Vk = ins.regT.value
        
        ins.regDest.writingUnit = self.name