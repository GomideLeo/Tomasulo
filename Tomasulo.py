from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
import functools

class Tomasulo:
    def __init__(self) -> None:
        self.currentCycle = 0

        self.reservationStations: list[ReservationStation] = None
        self.registers: list[Register] = None
        self.instructions: list[Instruction] = None
    
    def issue(self):
        rs = None
        toIssue = self.instructions[0]

        if toIssue.op == Instruction.OP_ADD or toIssue.op == Instruction.OP_SUB:
            rs = functools.reduce(lambda a, b: b if b.type == ReservationStation.ADD_TYPE else a, self.reservationStations, None)
        elif toIssue.op == Instruction.OP_MUL or toIssue.op == Instruction.OP_DIV:
            rs = functools.reduce(lambda a, b: b if b.type == ReservationStation.MUL_TYPE else a, self.reservationStations, None)
        
        if rs is None: # No Reservation Station was found, stall for a cycle
            return
        
        self.instructions = self.instructions[1:]
        toIssue.issueCycle = self.currentCycle
        rs.appendInstruction(toIssue)
        
        # return rs
    
    def execute():
        pass

    def writeBack():
        pass