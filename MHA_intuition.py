%%manim -ql MHAIntuitionScene

from random import uniform

class MHAIntuitionScene(Scene):
    def construct(self):
        sentence1 = Text("A galinha não atravessou a").shift(UP*1.5)
        sentence2 = Text("rua porque ela estava cansada.").next_to(sentence1, DOWN)
        self.play(Write(VGroup(sentence1, sentence2)))

        # Palavras importantes
        word_galinha = sentence1[1:8]
        word_ela = sentence2[9:12]
        word_cansada = sentence2[-8:-1]

        centro_galinha = word_galinha.get_center()
        centro_cansada = word_cansada.get_center()

        galinha = Text("galinha").move_to(centro_galinha)
        cansada = Text("cansada").move_to(centro_cansada)

        galinha2 = Text("galinha", color=BLUE).next_to(sentence2, DOWN).shift(LEFT*2.5, DOWN*1)
        cansada2 = Text("cansada", color=GREEN).next_to(sentence2, DOWN).shift(RIGHT*2.5, DOWN*1)
        
        # Destacar "ela"
        self.add(galinha, cansada)
        self.play(Indicate(word_ela, color=YELLOW))
        self.wait(0.8)
        self.play(Transform(galinha, galinha2), Transform(cansada, cansada2))
        self.wait(1)

        # Cabeça 1: Co-referência (azul)
        arrow1 = Arrow(word_ela.get_bottom(), galinha2.get_top(), buff=0.2, color=BLUE)
        label1 = MathTex("H_1: 90\\%").scale(0.7).next_to(arrow1, LEFT)
        self.play(GrowArrow(arrow1), FadeIn(label1))

        # Cabeça 2: Estado (verde)
        arrow2 = Arrow(word_ela.get_bottom(), cansada2.get_top(), buff=0.2, color=GREEN)
        label2 = MathTex("H_2: 85\\%").scale(0.7).next_to(arrow2, RIGHT)
        self.play(GrowArrow(arrow2), FadeIn(label2))

        self.wait(1.5)

        z1_tex = MathTex(r"\vec{z}_1=\begin{bmatrix}0.12 & -0.34\end{bmatrix}", color=BLUE)
        z2_tex = MathTex(r"\vec{z}_2=\begin{bmatrix}0.56 & 0.78\end{bmatrix}", color=GREEN)

        z1_tex.next_to(galinha2, DOWN)
        z2_tex.next_to(cansada2, DOWN*1.5)

        self.play(FadeIn(z1_tex), FadeIn(z2_tex))
        self.wait(0.5)

        concat_label = Text("Concatenação", font_size=24).next_to(VGroup(z1_tex, z2_tex), DOWN)
        self.play(Write(concat_label))
        self.wait(0.6)

        Z_tex = MathTex(r"Z = \begin{bmatrix}0.12 & -0.34 & 0.56 & 0.78\end{bmatrix}")
        Z_tex.next_to(concat_label, UP)

        small_group = VGroup(z1_tex, z2_tex)
        self.play(Transform(small_group, Z_tex))
        self.play(FadeOut(concat_label), FadeOut(label1), FadeOut(label2))
        self.wait(0.6)
        self.wait(3)