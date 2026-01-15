class CPU:
    register = {i: 0 for i in range(32)}
    pc = 0
    
    def __init__(self) -> None:
        pass

    def spec_display(self):
        print("rv32i - sim")
        print("="*50)
        self.display_general_registers()
        
    def display_general_registers(self):
        print('register:', self.register)
        print('pc:', self.pc)

    def pc_increment(self):
        self.pc += 4

cpu = CPU()
cpu.spec_display()