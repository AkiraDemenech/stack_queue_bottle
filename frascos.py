import random

altura = 4
cores = 5
vazio = '~'
densidade = False

def voltar (a, f, h):
	return
	
def igual (frasco, i, incr, val = vazio):
	try:
		while(frasco[i] == val):
			i += incr
	except IndexError:		
		pass
	return i	
	
def mover (a,f,h,o):	
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
	
	try:
		t = f[a[0]][v]
		while(u < -1):		
			f[a[0]].pop(v)# = vazio			
			v += o
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
	a.insert(0,o)		
	print(*a)
	
pilha = lambda args,frascos,hist: mover(args, frascos, hist, -1)	
fila = lambda args, frascos, hist: mover(args, frascos, hist, 0)
reiniciar = lambda args, frascos, hist: {'s':frascos.clear}[input('S para confirmar reiníncio: ')[0].lower()]()
escolhas = {'v': voltar, 'f': fila, 'p': pilha, 'r': reiniciar}	

def fases (f = None, x = cores, y = altura):
	if(type(f) == str):
		try:
			f = eval(f)
		except: 
			f = None
	if(f == None):
		f = random.randint(0,x**(x*y) - 1)
	g = f	
#	p = list(range(x)) * y	
	p = [[] for c in range(x)]
	q = {}
	for m in range(y):
		for n in range(x):		
			o = (f%x)%len(p)
			f //= x
			p[o].append(n)
			if(len(p[o]) == y):
				q[str(len(q))] = p.pop(o)
	return q, g			
	
def mostrar (f, s = -1):	
	print('0x' + ('%x' %s).upper())
	t = False
	for c in f:
		s = igual(f[c], 0, 1, f[c][0]) == len(f[c])
		t += s		
		print(c,s*'!','\t','-',*f[c],'+')				 
	return t == len(f)	
		
		
def fazer (a, f, h):		
	try:				
		escolhas[a[0]](a[1:],f,h)
	except KeyError:	
		return 
	
	
d = None	
while __name__ == '__main__':
	if type(d) != tuple:		
		d = fases(input('Semente='))
		antes = []
	if mostrar(*d):
		print('Venceu!')
		d = None
		continue
	fazer(input().lower().split(),d[0],antes)