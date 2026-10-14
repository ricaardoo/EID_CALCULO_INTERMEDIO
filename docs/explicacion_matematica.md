# Ejemplo matemático: Acumulación de datos mediante una tasa de transferencia variable

## 1. Contexto del problema
En informática, cuando un dispositivo transfiere datos a un servidor, la velocidad de transferencia puede cambiar con el tiempo debido a las condiciones de la conexión, la carga del servidor o la estabilidad de la red.

Para estudiar este fenómeno, consideraremos una transferencia de datos cuya tasa aumenta progresivamente durante un intervalo de cuatro segundos.

La pregunta que buscamos responder es:
**¿Cuántos megabytes se transfieren durante los primeros cuatro segundos si la tasa de transferencia cambia continuamente con el tiempo?**

Para resolverlo, utilizaremos una función de tasa, sumas de Riemann y la integral definida. Este ejemplo permite comprender cómo una tasa variable genera una cantidad acumulada.

## 2. Definición de la función de tasa
Modelaremos la tasa de transferencia mediante la siguiente función:

> **r(t) = t + 2**

Donde:
- **t**: tiempo transcurrido, medido en segundos (s).
- **r(t)**: tasa instantánea de transferencia, medida en megabytes por segundo (MB/s).
- **Intervalo de estudio**: [0, 4] segundos.

La función es lineal y creciente. Esto significa que la tasa aumenta una unidad de MB/s por cada segundo transcurrido.
Por ejemplo:

| Tiempo t (s) | Tasa r(t) (MB/s) |
| :---: | :---: |
| 0 | 2 |
| 1 | 3 |
| 2 | 4 |
| 3 | 5 |
| 4 | 6 |

Al comenzar, la transferencia ocurre a una tasa de 2 MB/s. Al llegar al segundo 4, la tasa es de 6 MB/s.
Es importante distinguir entre tasa y cantidad acumulada. La tasa indica cuántos megabytes se transfieren por segundo en un instante, mientras que la cantidad acumulada representa el total de megabytes transferidos durante un intervalo de tiempo.

## 3. Aproximación mediante sumas de Riemann
Como la tasa cambia con el tiempo, no podemos multiplicar directamente una única tasa por los cuatro segundos para obtener la cantidad exacta.
En su lugar, dividiremos el intervalo de tiempo en subintervalos y estimaremos la cantidad transferida en cada uno.
La aproximación de cada aporte se calcula mediante:

> **Aporteᵢ = r(tᵢ*) · Δt**

Donde:
- **r(tᵢ*)** es la tasa evaluada en un punto de muestra del subintervalo.
- **Δt** es la duración de cada subintervalo.
- **r(tᵢ*) · Δt** representa la cantidad aproximada de datos transferidos en ese subintervalo.

La suma de todos los aportes constituye una suma de Riemann:

> **Sₙ = ∑ᵢ₌₁ⁿ r(tᵢ*) · Δt**

Para comenzar, utilizaremos cuatro subintervalos y los extremos derechos como puntos de muestra.

### 3.1. Cálculo para n = 4
El intervalo de estudio es [0, 4] y queremos dividirlo en cuatro partes iguales.
El ancho de cada subintervalo es:

> **Δt = (b - a) / n = (4 - 0) / 4 = 1 s**

Por lo tanto, cada subintervalo dura un segundo.
Como utilizaremos los extremos derechos, los puntos de muestra serán:

> **tᵢ* = 1, 2, 3, 4**

Evaluamos la función r(t) = t + 2 en cada uno de esos puntos.

| i | Intervalo | tᵢ* (s) | r(tᵢ*) (MB/s) | Aporte (MB) |
| :---: | :---: | :---: | :---: | :---: |
| 1 | [0, 1] | 1 | 3 | 3 · 1 = 3 |
| 2 | [1, 2] | 2 | 4 | 4 · 1 = 4 |
| 3 | [2, 3] | 3 | 5 | 5 · 1 = 5 |
| 4 | [3, 4] | 4 | 6 | 6 · 1 = 6 |

Sumamos los aportes de los cuatro subintervalos:

> S₄ = 3(1) + 4(1) + 5(1) + 6(1)
> S₄ = 3 + 4 + 5 + 6
> **S₄ = 18 MB**

La aproximación indica que se transfieren 18 MB durante los cuatro segundos.
Sin embargo, este resultado todavía no es exacto. Como la tasa aumenta durante el intervalo, utilizar los extremos derechos asigna a cada subintervalo la tasa que se alcanza al final de este. Por ello, los rectángulos quedan por encima de la gráfica y la suma sobreestima la cantidad acumulada.

## 4. Refinamiento de la partición
Para mejorar la aproximación, aumentaremos el número de subintervalos.
La duración de cada uno disminuye según:

> **Δt = 4 / n**

Cuanto mayor sea n, menor será el ancho de los rectángulos y mejor representarán la región bajo la curva.
Para esta función lineal y utilizando extremos derechos, las sumas se pueden calcular mediante:

> **Sₙ = ∑ᵢ₌₁ⁿ (4i/n + 2) · (4/n)**

Al simplificar la expresión, obtenemos:

> **Sₙ = 16 + 8/n**

Esta fórmula permite calcular las aproximaciones para diferentes cantidades de rectángulos.

| Número de rectángulos (n) | Ancho Δt (s) | Suma Sₙ (MB) |
| :---: | :---: | :---: |
| 4 | 1 | 18 |
| 8 | 0,5 | 17 |
| 16 | 0,25 | 16,5 |
| 32 | 0,125 | 16,25 |
| 64 | 0,0625 | 16,125 |

La tabla muestra que, al aumentar el número de rectángulos, la aproximación disminuye y se acerca progresivamente a 16 MB.
El resultado no cambia porque la tasa sea diferente, sino porque cada rectángulo representa un intervalo más pequeño y, por tanto, estima mejor la cantidad transferida en él.

## 5. Obtención del valor exacto mediante la integral definida
El proceso anterior nos permite aproximar la cantidad transferida utilizando sumas de Riemann.
Para obtener el valor exacto, hacemos que el número de subintervalos tienda a infinito y que su ancho tienda a cero:

> **Q = lím (n → ∞) Sₙ**

Como Sₙ = 16 + 8/n, se obtiene:

> **Q = lím (n → ∞) (16 + 8/n) = 16 MB**

Este límite corresponde a la integral definida de la tasa entre los segundos 0 y 4:

> **Q = ∫₀⁴ (t + 2) dt**

Calculamos la integral mediante una antiderivada:

> **F(t) = t²/2 + 2t**

Aplicando el teorema fundamental del cálculo:

> Q = F(4) - F(0)
> Q = (4²/2 + 2(4)) - (0²/2 + 2(0))
> Q = 8 + 8
> **Q = 16 MB**

Por lo tanto, la cantidad exacta de datos transferidos durante los primeros cuatro segundos es de 16 MB.

## 6. Interpretación física y análisis de unidades
La integral definida representa el área bajo la gráfica de la tasa de transferencia entre t = 0 y t = 4.
Las unidades permiten verificar el significado del resultado:

> **(MB / s) · s = MB**

La tasa se mide en megabytes por segundo y el tiempo en segundos. Al multiplicarlos, los segundos se cancelan y obtenemos megabytes, que corresponden a la cantidad de datos transferidos.
En este ejemplo, la integral no representa una tasa instantánea ni una velocidad final: representa la cantidad total acumulada durante el intervalo.

## 7. Respuesta a la pregunta central
**¿Cómo una tasa que cambia con el tiempo produce una cantidad acumulada?**
Una tasa variable produce una cantidad acumulada porque, durante cada pequeño intervalo de tiempo, se transfiere una cantidad de datos que puede aproximarse multiplicando la tasa por la duración de ese intervalo. Al sumar todos esos aportes obtenemos una aproximación de la transferencia total.
Cuando refinamos la partición, los rectángulos representan cada vez mejor el área bajo la curva. En el límite, la suma de Riemann se convierte en una integral definida, que permite calcular exactamente la cantidad acumulada.
Para nuestro ejemplo, la tasa r(t) = t + 2 MB/s transfiere exactamente 16 MB durante los primeros cuatro segundos.

## 8. Relación con la animación en Manim
La animación del proyecto debe representar cada etapa del razonamiento matemático:
1. Mostrar la función r(t) = t + 2 y los ejes con sus unidades.
2. Dividir el intervalo [0, 4] en cuatro subintervalos.
3. Construir los cuatro rectángulos usando extremos derechos y mostrar sus aportes.
4. Mostrar la suma S₄ = 18 MB y aclarar que es una sobreestimación.
5. Aumentar el número de rectángulos a 8, 16, 32 y 64, mostrando cómo disminuye la aproximación.
6. Transformar visualmente la suma de rectángulos en el área bajo la curva.
7. Presentar la integral definida y evaluar la antiderivada para obtener Q = 16 MB.
8. Destacar la cancelación de las unidades de tiempo y cerrar con la respuesta a la pregunta central.

La animación debe mantener coherencia con las tablas y los cálculos de este documento. Los valores mostrados en pantalla deben provenir del mismo modelo matemático y utilizar siempre el mismo criterio de muestreo.