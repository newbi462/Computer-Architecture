"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        #pass

        #Registers
        #self.registers = [0] * 8 # Registers | 8 general-purpose 8-bit numeric registers R0-R7.
        self.reg = [0] * 8# exisisting code NOT IN SPEC DOC uses self.reg???
        #R5 is reserved as the interrupt mask (IM)
        #R6 is reserved as the interrupt status (IS)
        #R7 is reserved as the stack pointer (SP)

        #Internal Registers
        self.pc = 0 #PC: Program Counter, address of the currently executing instruction
        #IR: Instruction Register, contains a copy of the currently executing instruction
        ##FROM STEP 2: You don't need to add the MAR or MDR to your CPU class #MAR: Memory Address Register, holds the memory address we're reading or writing
        ##FROM STEP 2: You don't need to add the MAR or MDR to your CPU class #MDR: Memory Data Register, holds the value to write or the value just read
        #FL: Flags, see below

        #Memory
        #self.memory = [0] * 256 #Memory | The LS-8 has 8-bit addressing, so can address 256 bytes of RAM total.
        self.ram = [0] * 256 #per line 49 ERROR name already defined but not given in spec
        #Stack

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def LDI(self):
        register = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)
        self.reg[register] = value
        self.pc += 3

    def PRN(self):
        register = self.ram_read(self.pc+1)
        print(self.reg[register])
        self.pc += 2

    def HLT(self):
        sys.exit(0)

    def run(self):
        """Run the CPU."""
        #pass
        self.pc = 0
        halted = False

        while not halted:
            #print(self.ram_read(self.pc))
            if 0b10000010 == self.ram_read(self.pc):
                self.LDI()
            elif 0b01000111 == self.ram_read(self.pc):
                self.PRN()
            elif 0b00000001 == self.ram_read(self.pc):
                self.HLT()
            else:
                print("you break it you buy it")
                sys.exit(1)




    #should accept the address to read and return the value stored there
    def ram_read(self, address_to_read):
        #pass
        return self.ram[address_to_read]

    # should accept a value to write, and the address to write it to.
    def ram_write(self, value_to_write, address_to_write_it_to):
        #pass
        self.ram[address_to_write_it_to] = value_to_write
