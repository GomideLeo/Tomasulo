from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
from Tomasulo import Tomasulo
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-pI", "--printIssuing", action='store_true', help = "Sets Print Issuing to true")
parser.add_argument("-pC", "--printCompletion", action='store_true', help = "Sets Print Completion to true")
parser.add_argument("-pE", "--printExec", action='store_true', help = "Sets Print Exec to true")

parser.add_argument("-a", "--addRs", default=1, type=int, help = "Sets the number of ADD reservation stations available")
parser.add_argument("-m", "--mulRs", default=1, type=int, help = "Sets the number of MUL reservation stations available")
parser.add_argument("-r", "--registers", default=10, type=int, help = "Sets the number of registers available")

args = parser.parse_args()

addRs = [ReservationStation(ReservationStation.ADD_TYPE) for _ in range(args.addRs)]
mulRs = [ReservationStation(ReservationStation.MUL_TYPE) for _ in range(args.mulRs)]
rs = addRs + mulRs

# mul1 = Instruction(Instruction.OP_MUL, regs[0], regs[1], regs[2])
# add1 = Instruction(Instruction.OP_ADD, regs[0], regs[1], regs[2])
# add2 = Instruction(Instruction.OP_ADD, regs[0], regs[1], regs[2])

solver = Tomasulo()
solver.printIssuing = args.printIssuing
solver.printCompletion = args.printCompletion
solver.printExec = args.printExec
solver.registers = args.registers
solver.reservationStations = rs

# solver.instructions = [mul1, add1, add2]

# print(regs)
# solver.simulate()
# print(regs)