def read_rex_pf(rex: int) -> None:
	# print('{:08b}'.format(rex))
	print('|w|r|x|b|')
	print('|{}|{}|{}|{}|'.format(*'{:04b}'.format(rex - 64)))
	rex_str = '{:04b}'.format(rex - 64)
	if rex_str[3] == '1':
		print('REX.b', end=' ')
	if rex_str[2] == '1':
		print('REX.x', end=' ')
	if rex_str[1] == '1':
		print('REX.r', end=' ')
	if rex_str[0] == '1':
		print('REX.w', end=' ')
	print()

def REG(reg: int) -> str:
	match reg:
		case 0:
			return '*ax|r8|al'
		case 1:
			return '*cx|r9|cl'
		case 2:
			return '*dx|r10|dl'
		case 3:
			return '*bx|r11|bl'
		case 4:
			return '*sp|r12|ah'
		case 5:
			return '*bp|r13|ch'
		case 6:
			return '*si|r14|dh'
		case 7:
			return '*di|r51|bh'
		
def read_mod_rm(mod_rm: int) -> None:
	# print('{:08b}'.format(mod_rm))
	mod_rm_str = '{:08b}'.format(mod_rm)
	mod = mod_rm_str[:2]
	reg = mod_rm_str[2:5]
	rm = mod_rm_str[5:]
	print('|mod|reg| rm|')
	print('|{:>3}|{:>3}|{:>3}|'.format(mod, reg, rm))
	print(f'mod: {mod}')
	print('reg: {}({})'.format(reg, REG(int(reg, base=2))))
	print(f'rm: {rm}')

def read_sib(sib: int) -> None:
	# print('{:08b}'.format(sib))
	sib_str = '{:08b}'.format(sib)
	scale = sib_str[:2]
	index = sib_str[2:5]
	base = sib_str[5:]
	print('|scale|index|base|')
	print('|{:>5}|{:>5}|{:>4}|'.format(scale, index, base))
	print(f'scale: {scale}')
	print('index: {}({})'.format(index, REG(int(index, base=2))))
	print('base: {}({})'.format(base, REG(int(base, base=2))))
	

if __name__ == '__main__':
	while True:
		cmd = input('>> ').split()
		match cmd[0]:
			case 'rex':
				read_rex_pf(int(cmd[1], base=16))
			case 'mod':
				read_mod_rm(int(cmd[1], base=16))
			case 'sib':
				read_sib(int(cmd[1], base=16))
			case _:
				print('invalid input')

