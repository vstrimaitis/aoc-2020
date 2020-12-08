from typing import Callable, List, Optional


class Command:

    def __init__(self, arg: int):
        self.arg = arg

    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def modifies_ip(self) -> bool:
        return False

    def execute(self, program: "Program") -> None:
        raise NotImplementedError

    def __repr__(self):
        arg = f"{self.arg}"
        if self.arg >= 0:
            arg = "+" + arg
        return f"{self.name} {arg}"

class Nop(Command):

    @property
    def name(self):
        return "nop"

    def execute(self, program: "Program") -> None:
        pass

class Acc(Command):

    @property
    def name(self):
        return "acc"

    def execute(self, program: "Program") -> None:
        program.accumulator += self.arg

class Jmp(Command):

    @property
    def name(self):
        return "jmp"

    @property
    def modifies_ip(self):
        return True

    def execute(self, program: "Program") -> None:
        program.ip += self.arg

class Program:

    def __init__(self, source_code):
        self.ip = 0
        self.accumulator = 0
        self.stuck_in_loop = False
        self._commands: List[Command] = []
        self._parse_source(source_code)

    def _parse_source(self, source_code):
        for line in source_code.split("\n"):
            if not line:
                continue
            self._commands.append(self._parse_command(line))

    def _parse_command(self, line) -> Command:
        opname, arg = line.split(" ")
        arg = int(arg)
        for cls in Command.__subclasses__():
            op = cls(arg)
            if op.name == opname:
                return cls(arg)
        return None

    def run(self, cb: Optional[Callable[["Program"], None]] = None):
        if cb is not None:
            cb(self)
        executed_lines = set()
        while not self.stuck_in_loop:
            if self.ip < 0 or self.ip >= len(self._commands):
                break
            if self.ip in executed_lines:
                self.stuck_in_loop = True
                continue
            executed_lines.add(self.ip)
            cmd = self._commands[self.ip]
            cmd.execute(self)
            if not cmd.modifies_ip:
                self.ip += 1
            if cb is not None:
                cb(self)

    def __repr__(self):
        lines = []
        lines.append(f"ip = {self.ip}")
        lines.append(f"accumulator = {self.accumulator}")
        lines.append(f"source:")
        for i in range(len(self._commands)):
            line_num = str(i).zfill(3)
            line = f"    {line_num} {self._commands[i]}"
            if i == self.ip:
                line += "   <--"
            lines.append(line)
        
        return "\n".join(lines)