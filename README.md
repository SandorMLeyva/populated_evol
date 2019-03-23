# Informe de Simulación 

## Eventos discretos

## Problema 6: Poblado en Evolución

**Sándor Martín Leyva C412**




## Problema

​					


## Ideas

Para este problema se va a desarrollar un modelo basado en eventos discreto, ya que con este se puede modelar el paso del tiempo y interacción entre sus entidades, dejando a un lado las variables de menor significación y solo usando las que en realidad van a traer cambios significativos a la simulación. 

Para el modelo correspondiente se van a usar 3 tipos de variables principales,  *las variables de tiempo, las variables contadoras y las variables de estado* al ocurrir un evento estas variables se van a actualizar y de esta forma se va a poder recuperar toda la información de la simulación en proceso.

#### Eventos

1. **birthday** Día en que una persona cumple años
2. **born** Día en que una persona nace
3. **end_timeout** Cuando se acaba el periodo de luto o el tiempo de espera despues de una ruptura de una relacion

En este modelo se toma el **mes** como unidad mas pequeña de tiempo, el paso del tiempo lo efectuan los eventos, si el evento mas proximo a ocurrir es en 5 meses entonces la variable tiempo va a aumentar en 5, por lo que no hubo que analizar tiempo en el que se conoce que no va a pasar nada relevante para la población.

El resto de acciones que van a dar comportamiento casi único a la simulación son:

1. **Morir**
2. **Número de hijos que cada persona desea tener**
3. **Desear tener pareja**
4. **Volverse pareja**
5. **Número de bebes en un parto**

Estas tienen probabilidades de ocurrir, las cuales se pueden variar para tener mas informacion sobre la población simulada.




## Modelo

- [ ] Variables de tiempo: **t**
- [ ] Variables contadoras: **woman_t, man_t**
- [ ] Variables de estado: **woman, man, person, partners, population**
- [ ] Variables de salida: **tp**
- [ ] Lista de eventos: **birthday, born, end_timeout **

```
Init:
	t = 0
	tp = 0
	partners = 0
	woman_t = woman
	man_t = man
	population = Generar hombres y mujeres de las variables woman y man
	Generar los eventos de cumpleaños de las personas en population	
```

```
Caso 1 birthday and not (born and end_timeout):
	person = Persona asociada al evento
	t = Momento en que ocurre el evento
	person.age += 1
	.
	.
	<Metodo1>
```

```
Caso 2 born and not (birthday and end_timeout):
	person = Persona asociada al evento
	t = Momento en que ocurre el evento
	for child in Childs(person):
		Si es mujer
			woman_t += 1		
			woman += 1
		Si es hombre
			man_t += 1			
			man += 1
		population.append(child)
		Generar evento de cumpleaños de child
	.
	.
	<Metodo1>
```

```
Caso 3 end_timeout and not (birthday and born):
	person = Persona asociada al evento
	t = Momento en que ocurre el evento
	person = Finaliza tiempo de luto
	.
	.
	<Metodo1>
```

```
Metodo1:
	Si person muere
    	es hombre
			man -= 1
		es mujer
			woman -= 1
		Si person tenia pareja
        	Generar evento end_timeout para la pareja
        population.remove(person)
    En otro caso
    	Si person tiene pareja
    		Si person rompe con su pareja
    			Generar evento end_timeout para la pareja y para person
    	Si person esta disponible
    		Si encuentra pareja
    			partners += 1
    	Si EsMujer(person) y TienePareja(person)
    		Si person se embaraza
    			Genera evento born para person
		
	
```



## Consideraciones

Después de un gran número de simulaciones, se ha observado que los resultados finales siguen un orden. Un ejemplo de esto es que se hicieron varias pruebas para ver como se comportaba el número total de personas que habían vivido en el poblado, para **200 mujeres** y **200 hombres**  durante **10 años** después de **71 simulaciones** los resultados tenían una desviación estandar de 13.932 aproximadamente y luego de **191** simulaciones su desviación estandar era de 12.815 aproximadamente, lo que significa que la dispersión de los resultados con respecto a la media no es están grande. 

Si comprobamos con el resto de los resultados, podremos apreciar que la desviación estandar va a seguir siendo bastante baja.

Este es solo un ejemplo, con el software vamos a poder verificar estos resultados e incluso cambiar los parámetros para ver los distintos comportamientos de la población.