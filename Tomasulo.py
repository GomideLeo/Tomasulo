from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
import functools
import time

class Tomasulo:
    def __init__(self) -> None:
        self.printIssuing = False
        self.printCompletion = False
        self.printExec = False

        self.currentCycle = 0

        self.reservationStations: list[ReservationStation] = None
        self.registers: list[Register] = None
        self.instructions: list[Instruction] = None
    
    def issue(self):
        rs = None
        if len(self.instructions) == 0:
            return 

        toIssue = self.instructions[0]

        if toIssue.op == Instruction.OP_ADD or toIssue.op == Instruction.OP_SUB:
            rs = functools.reduce(lambda a, b: b if b.type == ReservationStation.ADD_TYPE and b.busy == False else a, self.reservationStations, None)
        elif toIssue.op == Instruction.OP_MUL or toIssue.op == Instruction.OP_DIV:
            rs = functools.reduce(lambda a, b: b if b.type == ReservationStation.MUL_TYPE and b.busy == False else a, self.reservationStations, None)
        
        if rs is None: # No Reservation Station was found, stall for a cycle
            return
        
        self.instructions = self.instructions[1:]

        toIssue.issueCycle = self.currentCycle
        toIssue.executionSize = Instruction.SIZE_ADD if toIssue.op == Instruction.OP_ADD or toIssue.op == Instruction.OP_SUB else Instruction.SIZE_MUL

        if self.printIssuing:
            print(toIssue, 'is being issued to', rs)
        rs.appendInstruction(toIssue)
    
    def execute(self):
        for rs in self.reservationStations:
            if rs.busy is False:
                continue
                
            if rs.Qj is not None or rs.Qk is not None:
                continue

            if rs.instruction.executionComplete != -1:
                continue

            if rs.instruction.executionStart == -1: # Hasnt started
                if rs.instruction.issueCycle == self.currentCycle: # Just got issued
                    continue

                rs.instruction.executionStart = self.currentCycle
                rs.instruction.executionSize -= 1

                if rs.instruction.executionSize == 0:
                    rs.instruction.executionComplete = self.currentCycle
                    continue

            if rs.instruction.executionSize != 0:
                if self.printExec:
                    print(f'Instruction {rs.instruction} has completed extra at {rs}')
                rs.instruction.executionSize -= 1
            
            if rs.instruction.executionSize == 0:
                if self.printCompletion:
                    print(f'Instruction {rs.instruction} has finished at {rs}')
                rs.instruction.executionComplete = self.currentCycle

    def writeBack(self):
        for rs in self.reservationStations:
            if rs.busy is False:
                continue

            if rs.instruction.executionSize != 0: # Instruction hasnt finished
                continue

            if rs.instruction.executionComplete == self.currentCycle: # Just finished
                continue

            rs.instruction.writeBackCycle = self.currentCycle

            val = Instruction.solve(rs.Vj, rs.Vk, rs.instruction.op)
            self.broadCast(rs.name, val)

            if rs.instruction.regDest.writingUnit == rs.name:
                rs.instruction.regDest.writingUnit = None
                rs.instruction.regDest.value = val
            
            rs.busy = False
            rs.instruction = None
            rs.Qj = None
            rs.Qk = None
            rs.Vj = None
            rs.Vk = None

    def broadCast(self, rsName, value):
        for rs in self.reservationStations:
            if rs.Qj == rsName:
                rs.Qj = None
                rs.Vj = value
            
            if rs.Qk     == rsName:
                rs.Qk    = None
                rs.Vk    = value
    
    def simulate(self):
        self.currentCycle = 0
        

        while len(self.instructions) != 0 or any(list(map(lambda x: x.busy, self.reservationStations))):
            self.currentCycle += 1
            self.issue()
            self.execute()
            self.writeBack()
            # time.sleep(.5)
