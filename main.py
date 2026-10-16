from manim import (
    DOWN,
    GREEN,
    ORANGE,
    UP,
    UR,
    YELLOW,
    Axes,
    Create,
    FadeIn,
    Scene,
    Text,
    VGroup,
    Write,
)

def rate(t):
    return 2 + t

START = 0
END = 4
N = 4
DT = (END - START) / N

class IntroduccionTasa(Scene):
    def construct(self):
        title = Text("Una tasa variable produce acumulacion", font_size=34)
        question = Text(
            "Pregunta central: Como una tasa variable produce una cantidad acumulada?",
            font_size=21,
            color=YELLOW,
        )
        subtitle = Text("Ejemplo: transferencia de datos", font_size=25)
        team = Text("Ricardo Aravena y Gustavo Valenzuela", font_size=24)
        group = Text("Grupo 5", font_size=24, color=YELLOW)
        formula = Text("r(t) = 2 + t   MB/s", font_size=40)
        context = Text(
            "r(t) indica cuantos MB se transfieren por segundo en el instante t.",
            font_size=22,
        )
        units = Text("t en segundos      r(t) en MB/s", font_size=26)

        title.to_edge(UP)
        question.next_to(title, DOWN, buff=0.2)
        subtitle.next_to(question, DOWN, buff=0.25)
        team.next_to(subtitle, DOWN, buff=0.35)
        group.next_to(team, DOWN, buff=0.2)
        formula.next_to(group, DOWN, buff=0.45)
        context.next_to(formula, DOWN, buff=0.6)
        units.next_to(context, DOWN, buff=0.45)

        self.play(Write(title), FadeIn(question), FadeIn(subtitle), FadeIn(team), FadeIn(group))
        self.play(Write(formula))
        self.play(FadeIn(context), Write(units))
        # Pausa amplia para presentar el problema y definir las unidades.
        self.wait(54)

class SumaRiemannTasa(Scene):
    def construct(self):
        title = Text("Pequeños aportes y suma de Riemann", font_size=31).to_edge(UP)
        axes = Axes(
            x_range=[0, 4.5, 1],
            y_range=[0, 7, 1],
            x_length=7.2,
            y_length=4.5,
            axis_config={
                "include_numbers": True,
                "label_constructor": Text,
                "font_size": 24,
                "decimal_number_config": {"num_decimal_places": 0},
            },
            tips=False,
        ).shift(DOWN * 0.35)
        labels = axes.get_axis_labels(Text("t", font_size=24), Text("r(t)", font_size=24))
        graph = axes.plot(rate, x_range=[0, 4])
        graph_label = Text("r(t) = 2 + t", font_size=24).next_to(graph, UR, buff=0.1)
        rectangles = axes.get_riemann_rectangles(
            graph,
            x_range=[0, 4],
            dx=DT,
            input_sample_type="center",
            color=[YELLOW, ORANGE],
            fill_opacity=0.55,
            stroke_width=1,
        )
        explanation = Text(
            "Delta t = (4-0)/4 = 1 s     aporte = r(t_i*) Delta t",
            font_size=24,
        ).to_edge(DOWN)

        self.play(Write(title), Create(axes), Write(labels))
        self.play(Create(graph), Write(graph_label))
        self.play(FadeIn(rectangles))
        self.play(Write(explanation))
        # Tiempo para explicar el ancho, la altura y el area de cada rectangulo.
        self.wait(105)

class AcumulacionTotal(Scene):
    def construct(self):
        title = Text("De los aportes a la cantidad acumulada", font_size=31).to_edge(UP)
        terms = Text(
            "r(0.5) Delta t + r(1.5) Delta t + r(2.5) Delta t + r(3.5) Delta t",
            font_size=24,
        )
        calculation = Text("= 2.5 + 3.5 + 4.5 + 5.5 = 16 MB", font_size=34)
        integral = Text(
            "integral de 0 a 4 de (2+t) dt = [2t + t^2/2]_0^4 = 16 MB",
            font_size=26,
        )
        conclusion = Text(
            "La integral suma una tasa por pequeños intervalos de tiempo.",
            font_size=25,
            color=GREEN,
        )
        answer = Text(
            "Respuesta: la acumulacion total es la integral de la tasa.",
            font_size=24,
        )

        terms.next_to(title, DOWN, buff=0.9)
        calculation.next_to(terms, DOWN, buff=0.65)
        integral.next_to(calculation, DOWN, buff=0.8)
        conclusion.next_to(integral, DOWN, buff=0.8)
        answer.next_to(conclusion, DOWN, buff=0.4)

        self.play(Write(title))
        self.play(Write(terms))
        self.play(Write(calculation))
        self.play(Write(integral))
        self.play(FadeIn(conclusion), FadeIn(answer))
        # Pausa para explicar la integral y relacionarla con la suma anterior.
        self.wait(106)

class Creditos(Scene):
    def construct(self):
        lines = VGroup(
            Text("Fuentes", font_size=34),
            Text("Stewart, Calculo de una variable, 2012", font_size=24),
            Text("Thomas, Weir y Hass, Calculo: una variable, 2010", font_size=24),
            Text("Apunte base: Introduccion a la integral, MAT1188, 2026", font_size=24),
            Text("Manim Community Documentation, 0.19.x", font_size=24),
        )
        lines.arrange(DOWN, buff=0.35)
        self.play(FadeIn(lines))
        self.wait(21)