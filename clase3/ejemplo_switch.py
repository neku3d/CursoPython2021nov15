# Ejemplo simulando el constructor switch
def semana(i):
	dias={
		0:'Domingo',
		1:'Lunes',
		2:'Martes',
		3:'Miércoles',
		4:'Jueves',
		5:'Viernes',
		6:'Sábado'
	}
	return dias.get(i,"No corresponde a un día de la semana")

print(semana(0))
print('***')
print(semana(10))