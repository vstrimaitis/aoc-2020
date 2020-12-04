from typing import Callable, Dict, List, Optional
import re 

def _validate_byr(s: str) -> bool:
    return re.match("^\d{4}$", s) and 1920 <= int(s) <= 2002

def _validate_iyr(s: str) -> bool:
    return re.match("^\d{4}$", s) and 2010 <= int(s) <= 2020

def _validate_eyr(s: str) -> bool:
    return re.match("^\d{4}$", s) and 2020 <= int(s) <= 2030

def _validate_hgt(s: str) -> bool:
    x = re.search("^(\d+)(in|cm)$", s)
    if x is None:
        return False
    if x[2] == "cm":
        return 150 <= int(x[1]) <= 193
    return 59 <= int(x[1]) <= 76

def _validate_hcl(s: str) -> bool:
    return re.match("^#[0-9a-f]{6}$", s)

def _validate_ecl(s: str) -> bool:
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def _validate_pid(s: str) -> bool:
    return re.match("^\d{9}$", s)

def _validate_cid(s: str) -> bool:
    return True

_REQUIRED_VALIDATORS: Dict[str, Callable[["Passport"], bool]] = {
    "byr": _validate_byr,
    "iyr": _validate_iyr,
    "eyr": _validate_eyr,
    "hgt": _validate_hgt,
    "hcl": _validate_hcl,
    "ecl": _validate_ecl,
    "pid": _validate_pid,
}

_OPTIONAL_VALIDATORS: Dict[str, Callable[["Passport"], bool]] = {
    "cid": _validate_cid,
}


class Passport:

    _next_id = 0

    def __init__(self, fields: Dict[str, str], run_validators=True):
        self.id = Passport._next_id

        for k, v in fields.items():
            if hasattr(self, k):
                raise ValueError(f"Duplicate field '{k}' detected in passport #{self.id} ({fields})")
            setattr(self, k, v)

        Passport._next_id += 1
        self._validate_fields(run_validators)

    def _validate_fields(self, run_validators: bool):
        for name, validator in _REQUIRED_VALIDATORS.items():
            if not hasattr(self, name):
                raise ValueError(f"Missing field '{name}' in passport {self}")
            if run_validators and validator is not None and not validator(getattr(self, name)):
                raise ValueError(f"Invalid field '{name}' in passport {self}")
        
        for name, validator in _OPTIONAL_VALIDATORS.items():
            if not hasattr(self, name):
                continue
            if run_validators and validator is not None and not validator(getattr(self, name)):
                raise ValueError(f"Invalid field '{name}' in passport {self}")

    def __str__(self):
        return "(" + ", ".join(f"{k}: {getattr(self, k)}" for k in self.__dict__) + ")"


def from_string(s: str, run_validators=True) -> Optional[Passport]:
    parts = re.split(r"[ \n:]", s)
    fields = dict()
    for i in range(0, len(parts)-1, 2):
        fields[parts[i]] = parts[i+1]
    try:
        return Passport(fields, run_validators=run_validators)
    except ValueError as e:
        # print(e)
        return None

def from_input(s: str, run_validators=True) -> List[Passport]:
    passports = [from_string(x, run_validators=run_validators) for x in s.split("\n\n")]
    return [p for p in passports if p is not None]