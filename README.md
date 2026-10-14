# Proyecto EID Manim 2026

## Datos del proyecto

- Curso: MAT1188 - Calculo Intermedio
- Grupo: G05
- Integrantes: Gustavo Valenzuela y Ricardo Aravena
- Tema: Acumulación a partir de una tasa variable.
- Pregunta central: ¿Cómo una tasa que cambia con el tiempo produce una cantidad acumulada?

## Requisitos

- Python: 3.13.7
- Manim Community:  v0.22.0

## Instalacion

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Ejecucion

```bash
manim -pqh src/escenas.py NombreDeLaEscena
```

Reemplazar los nombres por los archivos y escenas reales.

## Estructura

├── src/
│   ├── config_comun.py       # Colores, la función r(t) y ejes base para que el video se vea uniforme
│   ├── escena_1_2.py         # Persona A: Presentación, contexto de tasa y partición inicial (n=4)
│   └── escena_3_4.py         # Persona B: Refinamiento (n=8, 16, 32), límite, integral y cierre
├── docs/
│   ├── guion_y_notas.md      # Guion cronometrado (4 a 6 min) + desarrollo matemático del ejemplo
│   └── ficha_EID.pdf         # El documento final para subir a Blackboard
├── assets/                   # Audios de sus voces (.mp3/.wav) o imágenes de apoyo
├── requirements.txt
└── README.md

## Fuentes

Agregar al menos dos fuentes matematicas complementarias y la documentacion oficial de Manim.

## Declaracion de IA

[Indicar si se utilizo IA, para que se utilizo y como se verificaron sus aportes. Si no se utilizo, declararlo explicitamente.]

## Version entregada

- Commit final (SHA): [completar al finalizar]
