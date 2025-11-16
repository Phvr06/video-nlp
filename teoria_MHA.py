%%manim -ql MHA

from manim import config

class MHA(Scene):
    def construct(self):
        title = Text("Multi-Head Attention").to_edge(UP)
        self.add(title)

        frase = Text("O gato viu ela correr", font_size=40).shift(UP * 0.5)
        g = Text("ela")
        v0 = Matrix([[1.3, -2.1, 0.6, -1.7]]).set_color(RED).scale(0.8).set_stroke(width=2)
        
        b1 = Rectangle(height=1, width=2.5, fill_opacity=1, fill_color=GREEN, stroke_color=GREEN)
        at1 = Text("attention", color=WHITE, weight=SEMIBOLD, font_size=26)
        r1 = VGroup(b1, at1)
        b2 = Rectangle(height=1, width=2.5, fill_opacity=1, fill_color=BLUE_E, stroke_color=BLUE_E)
        at2 = Text("attention", color=WHITE, weight=SEMIBOLD, font_size=26)
        r2 = VGroup(b2, at2)
        gr = VGroup(r1, r2).arrange(DOWN, buff=2)
        content_group = VGroup(g, v0, gr)
        top_limit_y = title.get_bottom()[1]           # y do limite superior disponível
        bottom_frame_y = -config.frame_height / 2.0   # y da borda inferior da tela
        target_center_y = (top_limit_y + bottom_frame_y) / 2.0
        current_center = content_group.get_center()
        dy = target_center_y - current_center[1]
        content_group.shift(UP * dy)

         # Mostrar a frase completa
        self.play(Write(frase), runtime=1)
        self.wait(1)

        self.play(FadeOut(frase), FadeIn(g, scale=1.2))
        self.wait(0.5)
        self.wait(1)
        self.play(Transform(g, v0))
        self.wait(0.2)
        v0 = g
        
        self.play(v0.animate.to_edge(LEFT).scale(0.7), runtime=1)
        self.wait(1)
        a1 = Arrow(start=v0, end=r1.get_left()).set_color(GREEN)
        a2 = Arrow(start=v0, end=r2.get_left()).set_color(BLUE_E)
        self.play(FadeIn(gr), GrowArrow(a1), GrowArrow(a2))
        self.wait(1.5)
        
        q1 = Tex(r"$\mathbf{Q_{1}}$", color=GREEN).scale(0.5)
        k1 = Tex(r"$\mathbf{K_{1}}$", color=GREEN).scale(0.5)
        v1 = Tex(r"$\mathbf{V_{1}}$", color=GREEN).scale(0.5)
        rq1 = SurroundingRectangle(q1, buff=0.12, stroke_color=GREEN, stroke_width=3)
        rk1 = SurroundingRectangle(k1, buff=0.12, stroke_color=GREEN, stroke_width=3)
        rv1 = SurroundingRectangle(v1, buff=0.12, stroke_color=GREEN, stroke_width=3)
        gq1 = VGroup(rq1, q1)
        gk1 = VGroup(rk1, k1)
        gv1 = VGroup(rv1, v1)
        gqkv1 = VGroup(gq1, gk1, gv1).arrange(RIGHT, buff=0.15)

        q2 = Tex(r"$\mathbf{Q_{2}}$", color=BLUE_E).scale(0.5)
        k2 = Tex(r"$\mathbf{K_{2}}$", color=BLUE_E).scale(0.5)
        v2 = Tex(r"$\mathbf{V_{2}}$", color=BLUE_E).scale(0.5)
        rq2 = SurroundingRectangle(q2, buff=0.12, stroke_color=BLUE_E, stroke_width=3)
        rk2 = SurroundingRectangle(k2, buff=0.12, stroke_color=BLUE_E, stroke_width=3)
        rv2 = SurroundingRectangle(v2, buff=0.12, stroke_color=BLUE_E, stroke_width=3)
        gq2 = VGroup(rq2, q2)
        gk2 = VGroup(rk2, k2)
        gv2 = VGroup(rv2, v2)
        gqkv2 = VGroup(gq2, gk2, gv2).arrange(RIGHT, buff=0.15)

        gqkv1.next_to(r1, UP)
        gqkv2.next_to(r2, UP)
        
        self.play(Create(rq1), Write(q1),
                  Create(rk1), Write(k1),
                  Create(rv1), Write(v1),
                  Create(rq2), Write(q2),
                  Create(rk2), Write(k2),
                  Create(rv2), Write(v2))
        self.wait(1)

        # Extrair os 2 primeiros elementos [1.3, -2.1]
        v1_elements = Matrix([[1.3, -2.1]]).set_color(GREEN).scale(0.6).set_stroke(width=2)
        v1_elements.next_to(r1.get_left(), LEFT, buff=1)
        
        # Extrair os 2 últimos elementos [0.6, -1.7]
        v2_elements = Matrix([[0.6, -1.7]]).set_color(BLUE_E).scale(0.6).set_stroke(width=2)
        v2_elements.next_to(r2.get_left(), LEFT, buff=1)
        
        # Animar extração dos elementos para Attention 1
        self.play(Create(v1_elements))
        self.wait(0.5)
        
        # Elementos transformados após passar por Attention 1
        v1_transformed = Matrix([[0.8, -1.5]]).set_color(GREEN).scale(0.6).set_stroke(width=2)
        v1_transformed.next_to(r1, RIGHT, buff=0.3)
        
        # Animar transformação dentro do Attention 1
        self.play(v1_elements.animate.move_to(r1.get_center()+DOWN), runtime=0.8)
        self.wait(1)

        self.play(Indicate(b1, scale_factor=1.1, color=GREEN), Indicate(at1, scale_factor=1.1, color=WHITE), 
                  Indicate(gqkv1, scale_factor=1.1, color=GREEN))
        self.wait(2.5)
        
        self.play(FadeOut(v1_elements), Create(v1_transformed), runtime=0.8)
        self.wait(0.5)
        
        # Extrair e processar Attention 2
        self.play(Create(v2_elements))
        self.wait(0.5)
        
        # Elementos transformados após passar por Attention 2
        v2_transformed = Matrix([[0.4, -1.2]]).set_color(BLUE_E).scale(0.6).set_stroke(width=2)
        v2_transformed.next_to(r2, RIGHT, buff=0.3)
        
        # Animar transformação dentro do Attention 2
        self.play(v2_elements.animate.move_to(r2.get_center()+DOWN), runtime=0.8)
        self.wait(1)

        self.play(Indicate(b2, scale_factor=1.1, color=BLUE_E), Indicate(at2, scale_factor=1.1, color=WHITE), 
                  Indicate(gqkv2, scale_factor=1.1, color=BLUE_E))
        self.wait(2.5)
        
        self.play(FadeOut(v2_elements), Create(v2_transformed), runtime=0.8)
        self.wait(0.5)
        
        # Concatenação dos resultados
        concat_box = Rectangle(height=1, width=3.2, fill_opacity=0.1, stroke_color=YELLOW, stroke_width=2)
        concat_box.to_edge(RIGHT)
        concat_box.shift(UP * dy)
        
        # Setas para concatenação
        arrow_to_concat_1 = Arrow(start=v1_transformed.get_right(), end=concat_box.get_top(), color=GREEN)
        arrow_to_concat_2 = Arrow(start=v2_transformed.get_right(), end=concat_box.get_bottom(), color=BLUE_E)
        
        self.play(Create(concat_box), runtime=0.5)
        self.wait(0.3)
        self.play(Create(arrow_to_concat_1), Create(arrow_to_concat_2))
        self.wait(0.5)
        
        # Resultado final concatenado
        final_result = Matrix([[0.8, -1.5, 0.4, -1.2]]).set_color(YELLOW).scale(0.6).set_stroke(width=2)
        final_result.move_to(concat_box.get_center())
        final_result2 = Matrix([[0.8, -1.5, 0.4, -1.2]]).set_stroke(width=2).shift(UP * 0.8)

        subtext = Text('O vetor de "ela" agora carrega o significado', font_size=36).next_to(final_result2, DOWN*3)
        subtext2 = Text('"correto" de todas as palavras da frase!', font_size=36).next_to(subtext, DOWN)
        
        self.play(FadeOut(concat_box), Create(final_result))
        self.wait(3)

        tudo = VGroup(a1, a2, gr, v0, v1, gqkv2, gqkv1, concat_box, arrow_to_concat_1, arrow_to_concat_2, v2_transformed, v1_transformed)

        self.play(FadeOut(tudo), Transform(final_result, final_result2))
        self.wait(0.5)
        self.play(Write(VGroup(subtext, subtext2)))

        self.wait(3)