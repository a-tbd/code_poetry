import random

verbs = ['bury','hide','see','grin','scream','scratch','hear','reach','cry','die','go','sigh','break']
adjs = ['alone','slow','quick','quiet','late','wide','soon','loud','small','long']

def poem_maker():
	poem = []
	prev_index = 0
	for i in range(5):
		for j in range(2):
			verb = verbs[random.randint(0,len(verbs)-1)]
			adj = adj = adjs[random.randint(0,len(adjs)-1)]
			if prev_index > 0 :
				while verb in poem[prev_index]:
					verb = verbs[random.randint(0,len(verbs)-1)]
				while adj in poem[prev_index]:
					adj = adjs[random.randint(0,len(adjs)-1)]
			temp = 'We '+ verb + ' ' + adj + '\n'
			poem.append(temp)
		poem.append('\n')
		prev_index += 2
	return ''.join(poem)

print poem_maker()










