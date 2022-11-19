from FunctionalUnit import FunctionalUnit
from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
from Tomasulo import Tomasulo

regs = [Register(_) for _ in range(5)]
rs = []
rs.append(ReservationStation(ReservationStation.ADD_TYPE))
rs.append(ReservationStation(ReservationStation.ADD_TYPE))
fu = []
fu.append(FunctionalUnit(FunctionalUnit.ADD_TYPE))
fu.append(FunctionalUnit(FunctionalUnit.ADD_TYPE))
ops = []
ops.append(Instruction(Instruction.OP_ADD, regs[0], regs[0], regs[1]))
ops.append(Instruction(Instruction.OP_ADD, regs[1], regs[0], regs[1]))
ops.append(Instruction(Instruction.OP_ADD, regs[2], regs[2], regs[4]))
ops.append(Instruction(Instruction.OP_ADD, regs[2], regs[2], regs[4]))

solver = Tomasulo()
solver.registers = regs
solver.instructions = ops
solver.reservationStations = rs
solver.functionalUnits = fu

solver.simulate()

# for rs in solve
