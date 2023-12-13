import read_file
import re

input = read_file.read_whole_file('four.input')

def a():
    counter = 0
    passports = input.split('\n\n')
    for p in passports:
        d = dict(e.split(':') for e in p.split())
        if 'byr' in d and 'iyr' in d and 'eyr' in d and 'hgt' in d and \
            'hcl' in d and 'ecl' in d and 'pid' in d:
            counter += 1
    return counter

print(str(a()))

def b():
    counter = 0
    passports = input.split('\n\n')
    for p in passports:
        d = dict(e.split(':') for e in p.split())
        if 'byr' in d and 'iyr' in d and 'eyr' in d and 'hgt' in d and \
            'hcl' in d and 'ecl' in d and 'pid' in d:
            if len(d['byr']) != 4 or int(d['byr']) < 1920 or int(d['byr']) > 2002:
                continue
            if len(d['iyr']) != 4 or int(d['iyr']) < 2010 or int(d['iyr']) > 2020:
                continue
            if len(d['eyr']) != 4 or int(d['eyr']) < 2020 or int(d['eyr']) > 2030:
                continue
            h_unit = d['hgt'][-2:]
            try:
                h_val = int(d['hgt'][:-2])
            except:
                continue
            if h_unit != 'cm' and h_unit != 'in':
                continue
            if h_unit == 'cm' and (h_val < 150 or h_val > 193):
                continue
            if h_unit == 'in' and (h_val < 59 or h_val > 76):
                continue
            if not re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$',d['hcl']):
                continue
            if not d['ecl'] in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                continue
            if not re.search(r'^[0-9]{9}$', d['pid']):
                continue
            counter += 1
    return counter

print(str(b()))
