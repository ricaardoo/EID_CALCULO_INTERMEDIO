# Proyecto EID Manim 2026

## Datos del proyecto

- Curso: MAT1188 - Cálculo Intermedio
- Grupo: G05
- Integrantes y cuentas de GitHub:
  - Gustavo Valenzuela (@GustavoVlnz)
  - Ricardo Aravena (@ricaardoo)
- Tema: Acumulación a partir de una tasa variable.
- Pregunta central: ¿Cómo una tasa que cambia con el tiempo produce una cantidad acumulada?

## Resumen del ejemplo

Se estudia una transferencia de datos cuya tasa aumenta con el tiempo:

- Función: `r(t) = 2 + t` (Mb/s), con `t` en segundos.
- Intervalo: `[0, 4]`.
- Partición: `n = 4` subintervalos, con `Δt = (4 - 0)/4 = 1 s`.
- Puntos muestra: puntos medios `0,5; 1,5; 2,5; 3,5`.
- Suma de Riemann: `2,5 + 3,5 + 4,5 + 5,5 = 16 Mb`.
- Integral: `∫₀⁴ (2 + t) dt = [2t + t²/2]₀⁴ = 16 Mb`.

Ambos valores coinciden porque la tasa es lineal y el punto medio compensa el error de cada rectángulo.

## Requisitos

- Python: 3.13.7
- Manim Community: v0.22.0
- MiKTeX (distribución de LaTeX): necesario para escribir los símbolos matemáticos con `MathTex` y `Tex`. En MiKTeX Console, en *Settings > General*, conviene elegir "Install missing packages on-the-fly: Always".
- Dependencias de Python: ver `requirements.txt`.

## Instalación

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecución

Video completo en alta calidad (1080p60):

```bash
manim -qh main.py VideoCompleto
```

El resultado queda en `media/videos/main/1080p60/VideoCompleto.mp4`.

Escenas por separado (opcional, en baja calidad para revisar rápido):

```bash
manim -ql main.py IntroduccionTasa
manim -ql main.py SumaRiemannTasa
manim -ql main.py AcumulacionTotal
manim -ql main.py Creditos
```

## Estructura

```text
EID_CALCULO_INTERMEDIO/
├── main.py                 # Escenas de Manim (código del video)
├── requirements.txt        # Dependencias de Python
├── README.md
└── docs/
    ├── guion_y_notas.md    # Guion y desarrollo matemático del ejemplo
    └── ficha_EID.pdf       # Ficha para Blackboard
```

## Fuentes

Fuentes matemáticas:

1. Stewart, J. (2012). *Cálculo de una variable*. Cengage Learning. Caps. 5 a 7. 
2. Thomas, G., Weir, M. y Hass, J. (2010). *Cálculo: una variable*. Pearson. Cap. 5. 
3. Apunte base: *Introducción a la integral*. MAT1188, 2026. Material del curso, publicado en Educa.

Documentación de Manim:

4. Manim Community. *Manim Community Documentation*. https://docs.manim.community/

## Declaración de IA

**Herramienta:** Claude y ChatGPT, usados como asistentes de estudio y de apoyo técnico.

**Finalidades y partes apoyadas:**

- Plan de estudio del contenido matemático (sumas de Riemann, integral definida, antiderivada).
- Explicación de dependencias, comandos y funciones de Manim.
- Guía de instalación de MiKTeX para escribir símbolos matemáticos.
- Propuesta de estructura del proyecto.
- Apoyo en el código de `main.py`: uso de `MathTex`, escena `VideoCompleto` y correcciones menores (unidades, nombres, tildes).
- Revisión de la corrección matemática y de la redacción del guion de la narración.

**Cómo se verificó:**

- Los resultados del ejemplo (suma de Riemann y integral, ambos 16 Mb) se calcularon a mano y se compararon con las fuentes citadas.
- Las explicaciones de conceptos se contrastaron con Stewart, Thomas y el apunte del curso.
- El código se ejecutó y el video generado se revisó completo, comprobando que gráficas, valores y fórmulas coinciden con el cálculo.
- Los comandos de Manim se contrastaron con la documentación oficial.

La narración del video fue escrita y grabada por los integrantes con sus propias voces.

## Versión entregada

- Commit final (SHA): []