import sys

padež = {1:'<nom>', 2:'<gen>',3:'<dat>',4:'<loc>',5:'<abl>',6:'<ins>',8:'<ter>'}

num = '<ND>'
cas = '<CD>'
pos = '<PD>'
cat = '<XD>'
lem = ''
for line in sys.stdin.readlines():
	if line.count('Пӗрреллӗ хисеп / Singular') > 0 or line.count('Singular') > 0:
		num = '';
		continue
	elif line.count('Нумайлӑ хисеп / Plural') > 0 or line.count('Plural') > 0:
		num = '<pl>';
		continue

	if line.count('1c.1х./1sg.') > 0 or line.count('1 sg') > 0: 
		pos = '<px1sg>';
	if line.count('2c.2х./2sg.') > 0 or line.count('2 sg') > 0: 
		pos = '<px2sg>';
	if line.count('3<') > 0 or line.count('3 ') > 0: 
		pos = '<px3sp>';
	if line.count('1c.нум.х./1pl.') > 0 or line.count('1 pl') > 0: 
		pos = '<px1pl>';
	if line.count('2c.нум.х./2pl.') > 0 or line.count('1 pl') > 0: 
		pos = '<px2pl>';
	if line.count('| - ||') > 0:
		pos = ''

	if line.count('||') > 0: 
		# | - || автан·сем || автан·се·н || автан·сен·е || автан·сен·че || автан·сен·чен || автан·сем·пе || автан·сем·сӗр || автан·сем·шӗн
		row = line.split('||')
		for i in range(1,len(row)):
			form = row[i].strip().replace('·','').replace('.','').replace('<br>','<br />').replace('<br/>','<br />')
			if num == '' and pos == '' and i in padež and padež[i] == '<nom>':
				lem = form
				if lem[0].upper() == form[0]:
					cat = '<np>';
				else:
					cat = '<n>';
			if i in padež:
				forms = [form]	
				if form.count('<br />') > 0:
					forms = form.split('<br />')
				for j in forms: 
					print(lem + cat + num + pos + padež[i] + ':' + j.strip())

