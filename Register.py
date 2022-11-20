# from ReservationStation import ReservationStation

class Register:
    id = 0

    def __init__(self, value=0) -> None:
        self.name = 'Reg_' + str(Register.id)
        Register.id += 1
        self.value = value
        self.busy = False
        self.writingInstruction = None

    def __str__(self) -> str:
        return f'{self.name}(value={self.value})'

    def __repr__(self) -> str:
        return f'{self.name}(value={self.value})'
