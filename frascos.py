import random
# 3700493179219720
# 0xD25943570EF08

altura = 4
cores = 5
vazio = '~'
densidade = False

def identidade (x = cores, y = altura):
	'''Retorna uma semente que cria vitória instantânea sem permutação.'''
	k = 0
	for j in range(y):		
		for i in range(x):
			k = (k * x) + i
		k *= x	
	return k		

def voltar (a, f, h):
	'''Desfaz a última ação'''
#	[Opção, Origem, Destino, Quantidade, Valor]
	if(len(h) <= 0):
		return
	h = h.pop(-1)	
	i = igual(f[h[2]],-1,-1)
	for j in range(h[3]):				
		f[h[1]].insert(h[0],f[h[2]][i]) 
		f[h[1]].pop(-1)
		f[h[2]][i] = vazio		
		i -= 1
	print(h)	

	 	


	
def igual (frasco, i = 0, incr = 1, val = vazio):
	'''Retorna o primeiro índice cujo elemento é diferente do valor dado.'''
	try:
		while(frasco[i] == val):
			i += incr
	except IndexError:		
		pass
	return i	
	
def mover (a,f,h,o):	
	'''Move uma fase de um frasco para outro, de acordo com a opção pilha/fila dada, e registra a alteração no histórico'''
	if(len(a) < 2):
		return
	inc = (2*o) + 1
#	u = v = o
	c = False
	v = igual(f[a[0]], o, inc)
	try:
		u = igual(f[a[1]],-1,-1)
	except KeyError:	
		f[a[1]] = [vazio] * len(f[a[0]])
		u = igual(f[a[1]], -1, -1)
	#	u = o + (inc*len(f[a[1]]))
	
	t = vazio
	try:
		t = f[a[0]][v]				
		while(u < -1):		
			f[a[0]].pop(v)# = vazio						
			u += 1
			c += 1
			f[a[1]][u] = t			
			if(f[a[0]][v] != t):				
				break
	except IndexError:	
		pass
	while(len(f[a[0]]) < len(f[a[1]])):
		f[a[0]].append(vazio)
		
	h.append(a)
	a.append(c)	
	a.append(t)
	a.insert(0,o)		
	print(*a)
	
pilha = lambda args,frascos,hist: mover(args, frascos, hist, -1)	
fila = lambda args, frascos, hist: mover(args, frascos, hist, 0)
reiniciar = lambda args, frascos, hist: {'s':frascos.clear}[input('S para confirmar reiníncio: ')[0].lower()]()
escolhas = {'v': voltar, 'f': fila, 'p': pilha, 'r': reiniciar}	

def fases (f = None, x = cores, y = altura):
	'''Distribui as fases em x frascos de y unidades de altura'''
	if(type(f) == str):
		try:
			f = eval(f)
		except: 
			f = None
	if(type(f) != int):
		f = random.randint(0,x**((x+1)*y) - 1)
	g = f	
#	p = list(range(x)) * y	
	p = [[] for c in range(x)]
	q = {}
	for m in range(y):
		m = f%x
		f //= x
		for n in range(x):		
			n = (m+n)%x
			o = (f%x)%len(p)
			f //= x
			p[o].append(n)
			if(len(p[o]) == y):
				q[str(len(q))] = p.pop(o)
	for f in p:			
		q['%x'%len(q)] = f
	p.clear()	
	q['g'] = p
	for f in q:
		while len(q[f]) < y:
			q[f].append(vazio)
	return q, g			
	
def mostrar (f, s = -1):	
	'''Exibe os frascos e retorna se já estão todos iguais'''
	print('0x' + ('%x' %s).upper())
	t = False
	for c in f:
		s = igual(f[c], 0, 1, f[c][0]) == len(f[c])
		t += s		
		print(c,s*'!','\t','-',*f[c],'+')				 
	return t == len(f)	
		
		
def fazer (a, f, h, p):		
	'''Escolhe a ação solicitada e segura eventuais erros. Caso a ação não seja informada, faz a ação padrão passada.'''
	try:				
		o = a[0]
		if len(a) == 2:
			o = p
		escolhas[o](a[ - 2:],f,h)
	except:	
		pass 	
	return o	
		
		
	
	
d = None	
ult = 'p' # pilha por padrão
print(identidade())
while __name__ == '__main__':
	if type(d) != tuple:		
		d = fases(input('Semente='))
		antes = []
	if mostrar(*d):
		print('Venceu!')
		d = None
		continue
	ult = fazer(input().lower().split(),d[0],antes,ult)
	