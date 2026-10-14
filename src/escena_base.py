from manim import *

class AcumulacionTasa(Scene):
    def construct(self):
        # 1. Definir ejes: t (segundos) en X, r(t) (MB/s) en Y
        ejes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 16, 2],
            x_length=7,
            y_length=4.5,
            axis_config={"include_numbers": True}
        ).to_edge(DOWN)
        
        etiquetas = ejes.get_axis_labels(
            x_label=Tex("Tiempo $t$ (s)"), 
            y_label=Tex("Tasa $r(t)$ (MB/s)")
        )

        # 2. Definir función de tasa propia: ej. r(t) = 3t + 2
        def tasa(t):
            return 3 * t + 2

        curva = ejes.plot(tasa, x_range=[0, 4], color=BLUE)
        label_curva = MathTex("r(t) = 3t + 2").next_to(curva, UP)

        # Animación inicial
        self.play(Create(ejes), Write(etiquetas))
        self.play(Create(curva), Write(label_curva))
        self.wait(1)

        # 3. Rectángulos de Riemann (Aportes r(t_i*) * \Delta t)
        rectangulos_n4 = ejes.get_riemann_rectangles(
            curva, x_range=[0, 4], dx=1.0, input_sample_type="right", fill_opacity=0.5
        )
        formula_aporte = MathTex(r"\text{Aporte}_i = r(t_i^*) \cdot \Delta t \text{ [MB]}").to_edge(UP)

        self.play(Write(formula_aporte), Create(rectangulos_n4))
        self.wait(2)

        # 4. Refinamiento (Aumentar n -> disminuir dx)
        for dx_val in [0.5, 0.25, 0.125]:
            nuevos_rect = ejes.get_riemann_rectangles(
                curva, x_range=[0, 4], dx=dx_val, input_sample_type="right", fill_opacity=0.6
            )
            self.play(Transform(rectangulos_n4, nuevos_rect), run_time=1.5)
            self.wait(0.5)

        # 5. Integral definida (Área exacta acumulada)
        area_exacta = ejes.get_area(curva, x_range=[0, 4], color=GREEN, opacity=0.6)
        integral_tex = MathTex(r"Q = \int_0^4 (3t+2)\,dt = 32\text{ MB}").to_edge(UP)

        self.play(
            ReplacementTransform(rectangulos_n4, area_exacta),
            ReplacementTransform(formula_aporte, integral_tex)
        )
        self.wait(2)