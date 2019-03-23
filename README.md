



# Informe de Simulación 

## Eventos discretos

## Problema 6: Poblado en Evolución

**Sándor Martín Leyva C412**




## Problema

Se dese conocer la evolución de la población de una determinada región. Se conoce que la probabilidad de fallecer de una persona distribuye uniforme y se corresponde, según su edad y sexo, con la siguiente tabla:

|  Edad  | Hombre | Mujer |
| :----: | :----: | :---: |
|  0-12  |  0.25  | 0.25  |
| 12-45  |  0.1   | 0.15  |
| 45-76  |  0.3   | 0.35  |
| 76-125 |  0.7   | 0.65  |

Del mismo modo, se conoce que la probabilidad de una mujer se embarace es uniforme y está relacionada con la edad:

|  Edad  | Probabilidad Embarazarce |
| :----: | :----------------------: |
| 12-15  |           0.2            |
| 15-21  |           0.45           |
| 21-35  |           0.8            |
| 35-45  |           0.4            |
| 45-60  |           0.2            |
| 60-125 |           0.05           |

Para que una mujer quede embarazada debe tener pareja y no haber tenido el número máximo de hijos que deseaba tener ella o su pareja en ese momento. El número de hijos que cada persona desea tener distribuye uniforme según la tabla siguiente:

| Número | Probabilidad |
| :----: | :----------: |
|   1    |     0.6      |
|   2    |     0.75     |
|   3    |     0.35     |
|   4    |     0.2      |
|   5    |     0.1      |
|  + 5   |     0.05     |

Para que dos personas sean pareja deben estar solas en ese instante y deben desear tener pareja. El desear tener pareja está relacionado con la edad:

|  Edad  | Probabilidad de querer pareja |
| :----: | :---------------------------: |
| 12-15  |              0.6              |
| 15-21  |             0.65              |
| 21-35  |              0.8              |
| 35-45  |              0.6              |
| 45-60  |              0.5              |
| 60-125 |              0.2              |

Si dos personas de diferente sexo están solas y ambas desean querer tener parejas entonces la probabilidad de volverse pareja está relacionada con la diferencia de edad: 

| Diferencia de Edad | Probabilidad Establecer Pareja |
| :----------------: | :----------------------------: |
|        0-5         |              0.45              |
|        5-10        |              0.4               |
|       10-15        |              0.35              |
|       15-20        |              0.25              |
|        +20         |              0.15              |

Cuando dos personas están en pareja la probabilidad de que ocurra una ruptura distribuye uniforme y es de 0.2. Cuando una persona se separa, o enviuda, necesita estar sola por un período de tiempo que distribuye exponencial con un parámetro que está relacionado con la edad:

|  Edad  |  lambda  |
| :----: | :------: |
| 12-15  | 3 meses  |
| 15-21  | 6 meses  |
| 21-35  | 6 meses  |
| 35-45  | 12 meses |
| 45-60  | 24 meses |
| 60-125 | 48 meses |

Cuando están dadas todas las condiciones y una mujer queda embarazada puede tener o no un embarazo múltiple y esto distribuye uniforme acorde a las probabilidades siguientes:

| Número de Bebés | Probabilidad |
| :-------------: | :----------: |
|        1        |     0.7      |
|        2        |     0.16     |
|        3        |     0.08     |
|        4        |     0.04     |
|        5        |     0.02     |



La probabilidad del sexo de cada bebé nacido es uniforme 0,5. Asumiendo que se tiene una población inicial de M mujeres y H hombres y que cada poblador, en el instante incial, tiene una edad que distribuye uniforme (U(0,100). Realice un proceso de simulación para determinar como evoluciona la población en un per´ıodo de 100 años.



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

Algunos aspectos a tener en cuenta sobre la implementación del modelo son:

- La edad máxima de una persona
  - Esta es 126 años, pero se tiene en cuenta que pueda vivir unos años mas, ya que cuando se comprueba si el individuo va a morir y tiene 126 años, este no muere automáticamente, sino que el individuo pasa a tener probabilidad 0.88 de morir, lo cual se aproxima bastante a la realidad

Después de un gran número de simulaciones, se ha observado que los resultados finales siguen un orden. Un ejemplo de esto es que se hicieron varias pruebas para ver como se comportaba el número total de personas que habían vivido en el poblado, para **200 mujeres** y **200 hombres**  durante **10 años** después de **71 simulaciones** los resultados tenían una desviación estandar de 13.932 aproximadamente y luego de **191** simulaciones su desviación estandar era de 12.815 aproximadamente, lo que significa que la dispersión de los resultados con respecto a la media no es están grande. 

Si comprobamos con el resto de los resultados, podremos apreciar que la desviación estandar va a seguir siendo bastante baja.

Este es solo un ejemplo, con el software vamos a poder verificar estos resultados e incluso cambiar los parámetros para ver los distintos comportamientos de la población.



## Ejecución del Software

Para poder correr el software es necesario tener instalado la librería **numpy**

Si lo corremos **sin parámetros** vamos a simular una población de **500 mujeres y 500 hombres durante 100 años**

```bash
python3 main.py
```

Los parametros van en el mismo orden <mujers> <hombres> <tiempo maximo de simulacion>

```
python3 main.py 500 500 100
```

Para levantar el servidor web para tener un resumen mas detallados de los datos de la simulación debe pasar el parametro **graph** al final de la linea, debe tener instalado **flask**.

```
python3 main.py graph


# si desea pasarle los parametros de la población 

python3 main.py 500 500 graph
```
