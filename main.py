from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
from Tomasulo import Tomasulo

regs = [Register(_) for _ in range(5)]
rs_add1 = ReservationStation(ReservationStation.ADD_TYPE)
rs_add2 = ReservationStation(ReservationStation.ADD_TYPE)
rs_mul1 = ReservationStation(ReservationStation.MUL_TYPE)
mul1 = Instruction(Instruction.OP_MUL, regs[0], regs[1], regs[2])
add1 = Instruction(Instruction.OP_ADD, regs[1], regs[1], regs[2])
add2 = Instruction(Instruction.OP_ADD, regs[4], regs[2], regs[3])

solver = Tomasulo()
solver.printIssuing = True
solver.printCompletion = True
solver.registers = regs
solver.instructions = [mul1, add1, add2]
solver.reservationStations = [rs_mul1, rs_add1, rs_add2]

# print(list(map(lambda x: x.busy, solver.reservationStations)))
print(regs)
solver.simulate()
print(regs)
# for rs in solve