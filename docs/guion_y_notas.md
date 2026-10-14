0:40
Persona 1 — Presentación y contexto
Manim: título, pregunta central y contexto de transferencia de datos.
“Nuestro tema es la acumulación a partir de una tasa variable. Imaginemos que un servidor transfiere datos a una tasa que cambia con el tiempo. Queremos determinar cuántos megabytes se transfieren durante cuatro segundos, aunque la tasa no sea constante.”



0:40
1:30
Persona 1 — Tasa, intervalo y unidades
Manim: ejes, curva y etiquetas con unidades.
“Usaremos la función \(r(t)=t+2\), donde \(t\) se mide en segundos y \(r(t)\) en megabytes por segundo. La tasa aumenta de 2 a 6 MB/s. Como representa una velocidad de transferencia, debemos multiplicarla por tiempo para obtener una cantidad de datos.”



1:30
2:30
Persona 1 — Primera suma de Riemann
Manim: partición en cuatro intervalos y aparición de cada rectángulo.
“Dividimos los cuatro segundos en cuatro intervalos de un segundo. Usando los extremos derechos, evaluamos la tasa en 1, 2, 3 y 4 segundos. Obtenemos 5, 6, 7 y 8 MB, respectivamente, como aportes de cada intervalo. Al sumarlos, la aproximación es de 26 MB.”
Corrección matemática: para \(r(t)=t+2\), las tasas en los extremos derechos son 3, 4, 5 y 6 MB/s, por lo que los aportes correctos son 3, 4, 5 y 6 MB y \(S_4=18\) MB.



2:30
3:35
Persona 2 — Refinamiento de la partición
Manim: transición de 4 a 8, 16 y 32 rectángulos; contador de \(S_n\).
“Cuando aumentamos el número de intervalos, cada rectángulo tiene una base más pequeña. De esta forma representamos mejor las variaciones de la tasa. En nuestro caso, como la tasa aumenta, los rectángulos derechos sobreestiman la cantidad transferida, pero esa sobreestimación disminuye al refinar la partición.”



3:35
4:30
Persona 2 — Integral definida y cálculo exacto
Manim: área bajo la curva, integral y evaluación de la antiderivada.
“Al llevar el ancho de los intervalos hacia cero, la suma de Riemann converge a la integral definida. Calculamos la integral de \(t+2\) entre cero y cuatro, obteniendo 16 MB. Ese es el valor exacto de la cantidad transferida.”



4:30
5:00
Persona 2 — Respuesta y créditos
Manim: ecuación final, respuesta central y créditos bibliográficos.
“Una tasa variable produce una cantidad acumulada porque cada pequeño intervalo aporta una cantidad proporcional a la tasa y al tiempo transcurrido. La integral definida suma todos esos aportes en el límite. Así conectamos una tasa instantánea con una cantidad total.”