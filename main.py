from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
from Tomasulo import Tomasulo

regs = [Register(_) for _ in range(5)]
rs_add1 = ReservationStation(ReservationStation.ADD_TYPE)
add1 = Instruction(Instruction.OP_ADD, regs[0], regs[1], regs[2])

solver = Tomasulo()
solver.registers = regs
solver.instructions = [add1]
solver.reservationStations = []#rs_add1]

print(solver.issue())

# for rs in solve