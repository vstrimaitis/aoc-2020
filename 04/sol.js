const fs = require("fs");

const data = fs.readFileSync(0).toString();

const pwds = data
    .trim()
    .split("\n\n")
    .map(p => p.split(/[ \n]/))
    .map(p => new Map(p.map(x => x.split(":"))));

const isValid1 = p => ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].every(x => p.has(x));

const ans1 = pwds
    .filter(isValid1)
    .length;

console.log("Part 1:", ans1);

const isValid2 = p => {
    if (!isValid1(p)) return false;
    const byr = p.get("byr");
    if (!(/^\d{4}$/.test(byr) && 1920 <= parseInt(byr) && parseInt(byr) <= 2002)) return false;

    const iyr = p.get("iyr");
    if (!(/^\d{4}$/.test(iyr) && 2010 <= parseInt(iyr) && parseInt(iyr) <= 2020)) return false;

    const eyr = p.get("eyr");
    if (!(/^\d{4}$/.test(eyr) && 2020 <= parseInt(eyr) && parseInt(eyr) <= 2030)) return false;

    const hgt = p.get("hgt");
    const groups = /^(\d+)(in|cm)$/.exec(hgt);
    if (!groups) return false;
    if (groups[2] == "in" && !(59 <= parseInt(groups[1]) && parseInt(groups[1]) <= 76)) return false;
    if (groups[2] == "cm" && !(150 <= parseInt(groups[1]) && parseInt(groups[1]) <= 193)) return false;

    const hcl = p.get("hcl");
    if (!(/^#[0-9a-f]{6}$/.test(hcl))) return false;

    const ecl = p.get("ecl");
    if (!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].includes(ecl)) return false;

    const pid = p.get("pid");
    if (!(/^\d{9}$/.test(pid))) return false;
    
    return true;
}

const ans2 = pwds
    .filter(isValid2)
    .length;

console.log("Part 2:", ans2);
