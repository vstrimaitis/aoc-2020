import sys
from typing import List

class Printer:

    def __init__(self):
        self.buffer: List[str] = []

    def print(self, s):
        s = str(s)
        if "\n" in s:
            for line in s.split("\n"):
                self.println(line)
            return
        sys.stdout.write(s)
        self.buffer.append(s)

    def println(self, s, commit=False):
        s = str(s)
        s += "\n"
        sys.stdout.write(s)
        self.buffer.append(s)
        if commit:
            self.commit()

    def clear(self):
        while self.buffer:
            self._delete_last_line()

    def commit(self):
        self.buffer = []

    def _delete_last_line(self):
        if not self.buffer:
            return
        while self.buffer[-1] and self.buffer[-1][-1] == "\n":
            self._move_cursor_up()
            self.buffer[-1] = self.buffer[-1][:-1]
        self._clear_line()
        self.buffer = self.buffer[:-1]

    def _move_cursor_up(self):
        sys.stdout.write("\033[F")

    def _clear_line(self):
        sys.stdout.write("\033[K")