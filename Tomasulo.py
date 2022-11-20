from FunctionalUnit import FunctionalUnit
from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
import functools
import time


class Tomasulo:
    def __init__(self) -> None:
        self.printIssuing = True
        self.printCompletion = True
        self.printStart = False
        self.printExec = False

        self.currentCycle = 0

        self.reservationStations: list[ReservationStation] = []
        self.functionalUnits: list[FunctionalUnit] = []
        self.registers: list[Register] = []
        self.instructions: list[Instruction] = []

    def issue(self):
        if len(self.instructions) == 0:
            return

        toIssue = self.instructions[0]
        rs = self.getReservationStation(toIssue.op)

        if rs is None:  # No Reservation Station was found, stall for a cycle
            return

        self.instructions = self.instructions[1:]

        toIssue.issueCycle = self.currentCycle

        if self.printIssuing:
            print(
                f'Cicle {self.currentCycle} - {toIssue} is being issued to {rs}')
        rs.appendInstruction(toIssue)

    def execute(self):
        for fu in self.functionalUnits:
            if not fu.busy:
                continue

            if fu.instruction.executionStart == -1:
                fu.instruction.executionStart = self.currentCycle

            fu.executionSize -= 1
            if fu.executionSize > 0:
                if self.printExec:
                    print(
                        f'Cicle {self.currentCycle} - Instruction {fu.instruction} has completed extra at {fu} - Cicles remaining: {fu.executionSize}')
            else:
                fu.instruction.executionComplete = self.currentCycle
                fu.result = Instruction.solve(fu.Vj, fu.Vk, fu.instruction.op)
                if self.printCompletion:
                    print(
                        f'Cicle {self.currentCycle} - Instruction {fu.instruction} has finished at {fu} - {fu.instruction.regDest.name} = {fu.result}')

        for rs in self.reservationStations:
            if rs.busy is False:
                continue

            if rs.Qj is not None or rs.Qk is not None:
                continue

            fu = self.getFunctionalUnit(rs.type)

            if fu is None:  # No FuncionalUnit was found, stall for a cycle
                continue

            if self.printStart:
                print(
                    f'Cicle {self.currentCycle} - Instruction {rs.instruction} has started at {fu}')
            fu.appendInstruction(rs)

            rs.clear()

    def writeBack(self):
        for fu in self.functionalUnits:
            if fu.busy is False:
                continue

            if fu.executionSize != 0:  # Instruction hasnt finished
                continue

            fu.instruction.writeBackCycle = self.currentCycle

            val = fu.result
            self.broadCast(fu.instruction, val)

            if fu.instruction.regDest.writingInstruction == fu.instruction:
                fu.instruction.regDest.writingInstruction = None
                fu.instruction.regDest.value = val

            fu.clear()

    def broadCast(self, instruction, value):
        for rs in self.reservationStations:
            if rs.Qj == instruction:
                rs.Qj = None
                rs.Vj = value

            if rs.Qk == instruction:
                rs.Qk = None
                rs.Vk = value

    def simulate(self):
        self.currentCycle = 0

        while len(self.instructions) != 0 or any(list(map(lambda x: x.busy, self.reservationStations))) or any(list(map(lambda x: x.busy, self.functionalUnits))):
            self.currentCycle += 1
            self.issue()
            self.execute()
            self.writeBack()
            # time.sleep(.5)

    def getReservationStation(self, op):
        rs = None

        if op == Instruction.OP_ADD or op == Instruction.OP_SUB or op == Instruction.OP_ADDI:
            rs = functools.reduce(
                lambda a, b: b if b.type == ReservationStation.ADD_TYPE else a, filter(lambda a: not a.busy, self.reservationStations), None)
        elif op == Instruction.OP_MUL or op == Instruction.OP_DIV:
            rs = functools.reduce(
                lambda a, b: b if b.type == ReservationStation.MUL_TYPE else a, filter(lambda a: not a.busy, self.reservationStations), None)

        return rs

    def getFunctionalUnit(self, op):
        fu = None

        fu = functools.reduce(
            lambda a, b: b if b.type == op else a, filter(
                lambda a: not a.busy, self.functionalUnits), None)

        return fu
