from FunctionalUnit import FunctionalUnit
from Instruction import Instruction
from Register import Register
from ReservationStation import ReservationStation
from Tomasulo import Tomasulo
import argparse


def parseFile(file, registers):
    instructions = []

    with open(file, 'r') as f:
        for line in f:
            [opType, regD, regS, regT] = line.split()

            if int(regD) >= len(registers) or int(regS) >= len(registers) or int(regT) >= len(registers):
                raise "Registrador Invalido"

            instructions.append(Instruction(opType, registers[int(
                regD)], registers[int(regS)], registers[int(regT)]))

    return instructions


parser = argparse.ArgumentParser()

parser.add_argument("-pI", "--printIssuing",
                    action='store_true', help="Sets Print Issuing to true")
parser.add_argument("-pC", "--printCompletion",
                    action='store_true', help="Sets Print Completion to true")
parser.add_argument("-pE", "--printExec", action='store_true',
                    help="Sets Print Exec to true")
parser.add_argument("-pS", "--printStart", action='store_true',
                    help="Sets Print on execution Start to true")

parser.add_argument("-a", "--addRs", default=1, type=int,
                    help="Sets the number of ADD reservation stations available")
parser.add_argument("-m", "--mulRs", default=1, type=int,
                    help="Sets the number of MUL reservation stations available")
parser.add_argument("-a", "--addFu", default=1, type=int,
                    help="Sets the number of ADD functional units available")
parser.add_argument("-m", "--mulFu", default=1, type=int,
                    help="Sets the number of MUL functional units available")
parser.add_argument("-r", "--registers", default=8, type=int,
                    help="Sets the number of registers available")
parser.add_argument("-f", "--file", default='./cmds.txt',
                    type=str, help="File path to comands file")

args = parser.parse_args()

registers = [Register(_) for _ in range(args.registers)]
instructions = parseFile(args.file, registers)

addRs = [ReservationStation(ReservationStation.ADD_TYPE)
         for _ in range(args.addRs)]
mulRs = [ReservationStation(ReservationStation.MUL_TYPE)
         for _ in range(args.mulRs)]
rs = addRs + mulRs

addFu = [ReservationStation(ReservationStation.ADD_TYPE)
         for _ in range(args.addFu)]
mulFu = [ReservationStation(ReservationStation.MUL_TYPE)
         for _ in range(args.mulFu)]
fu = addFu + mulFu

solver = Tomasulo()

solver.printIssuing = args.printIssuing
solver.printCompletion = args.printCompletion
solver.printExec = args.printExec
solver.printStart = args.printStart

solver.registers = registers
solver.reservationStations = rs
solver.functionalUnits = fu

solver.instructions = instructions

print("Registers:", *registers, sep="\n\t")
solver.simulate()
print("Registers:", *registers, sep="\n\t")
