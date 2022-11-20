from FunctionalUnit import FunctionalUnit
from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
from Tomasulo import Tomasulo

regs = [Register(_) for _ in range(5)]

fu = []
fu.append(FunctionalUnit(FunctionalUnit.ADD_TYPE))
fu.append(FunctionalUnit(FunctionalUnit.ADD_TYPE))
rs = []
rs.append(ReservationStation(ReservationStation.ADD_TYPE))
rs.append(ReservationStation(ReservationStation.ADD_TYPE))
rs.append(ReservationStation(ReservationStation.ADD_TYPE))
rs.append(ReservationStation(ReservationStation.ADD_TYPE))
rs.append(ReservationStation(ReservationStation.MUL_TYPE))
ops = []
ops.append(Instruction(Instruction.OP_ADD, regs[0], regs[0], regs[1]))
ops.append(Instruction(Instruction.OP_ADD, regs[2], regs[2], regs[1]))
ops.append(Instruction(Instruction.OP_ADD, regs[3], regs[3], regs[3]))
ops.append(Instruction(Instruction.OP_ADD, regs[2], regs[1], regs[3]))
ops.append(Instruction(Instruction.OP_ADD, regs[3], regs[2], regs[1]))

solver = Tomasulo()
solver.printIssuing = True
solver.printCompletion = True
solver.printStart = True
solver.printExec = True
solver.registers = regs
solver.instructions = ops
solver.reservationStations = rs
solver.functionalUnits = fu

# print(list(map(lambda x: x.busy, solver.reservationStations)))
print("Registers:", *regs, sep="\n\t")
solver.simulate()
print("Registers:", *regs, sep="\n\t")
# for rs in solve
