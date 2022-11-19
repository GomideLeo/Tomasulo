import time
from FunctionalUnit import FunctionalUnit
from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
import functools


class Tomasulo:
    def __init__(self) -> None:
        self.currentCycle = 0

        self.reservationStations: list[ReservationStation] = None
        self.functionalUnits: list[FunctionalUnit] = None
        self.registers: list[Register] = None
        self.instructions: list[Instruction] = None

    def getReservationStation(self, op):
        rs = None

        if op == Instruction.OP_ADD or op == Instruction.OP_SUB:
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

    def issue(self):
        if len(self.instructions) == 0:
            return

        toIssue = self.instructions[0]
        rs = self.getReservationStation(toIssue.op)

        if rs is None:  # No Reservation Station was found, stall for a cycle
            return

        self.instructions = self.instructions[1:]
        toIssue.issueCycle = self.currentCycle
        rs.appendInstruction(toIssue)

        # return rs

    def execute(self):
        for unit in filter(lambda a: a.busy, self.functionalUnits):
            unit.execute(self.currentCycle)

        for station in self.reservationStations:
            if station.canExecute():
                fu = self.getFunctionalUnit(station.type)

                if fu is None:  # No FuncionalUnit was found, stall for a cycle
                    continue

                fu.appendInstruction(station, self.currentCycle)

    def broadcast(self, value, station):
        for rs in self.reservationStations:
            if rs.Qj == station:
                rs.Qj = None
                rs.Vj = value

            if rs.Qk == station:
                rs.Qk = None
                rs.Vk = value

    def writeBack(self):
        for unit in self.functionalUnits:
            if unit.result is not None:
                self.broadcast(unit.result, unit.originStation)
                reg = unit.op.reg1
                if reg.reservationStation == unit.originStation:
                    reg.value = unit.result
                    reg.busy = False
                unit.originStation.clear()
                unit.clear()

    def simulate(self):
        self.currentCycle = 0

        while len(self.instructions) != 0 or any(list(map(lambda x: x.busy, self.reservationStations))) or any(list(map(lambda x: x.busy, self.functionalUnits))):
            self.currentCycle += 1
            self.issue()
            self.execute()
            self.writeBack()

            print(self.currentCycle)
            print(self.registers, end="\n\n")
            time.sleep(.5)
