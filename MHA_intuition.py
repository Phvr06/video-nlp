%%manim -qh MHAIntuitionSceneExtended

class MHAIntuitionSceneExtended(Scene):
    def construct(self):
        sentence1 = Text("A galinha não atravessou a").shift(UP*1.5)
        sentence2 = Text("rua porque ela estava cansada.").next_to(sentence1, DOWN)
        self.play(Write(VGroup(sentence1, sentence2)))

        # ======== Primeira interação: "ela" ==========
        word_galinha = sentence1[1:8]
        word_ela = sentence2[9:12]
        word_cansada = sentence2[-8:-1]

        galinha = Text("galinha").move_to(word_galinha.get_center())
        cansada = Text("cansada").move_to(word_cansada.get_center())

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
        label1 = MathTex("H_1: 85\\%").scale(0.7).next_to(arrow1, LEFT)
        self.play(GrowArrow(arrow1), FadeIn(label1))

        # Cabeça 2: Estado (verde)
        arrow2 = Arrow(word_ela.get_bottom(), cansada2.get_top(), buff=0.2, color=GREEN)
        label2 = MathTex("H_2: 90\\%").scale(0.7).next_to(arrow2, RIGHT)
        self.play(GrowArrow(arrow2), FadeIn(label2))

        self.wait(1.5)

        z1_tex = MathTex(r"\begin{bmatrix}0.12 & -0.34\end{bmatrix}", color=BLUE)
        z2_tex = MathTex(r"\begin{bmatrix}0.56 & 0.78\end{bmatrix}", color=GREEN)

        z1_tex.next_to(galinha2, DOWN)
        z2_tex.next_to(cansada2, DOWN*1.5)

        self.play(FadeIn(z1_tex), FadeIn(z2_tex))
        self.wait(0.5)

        concat_label = Text("Concatenação", font_size=24).next_to(VGroup(z1_tex, z2_tex), DOWN)
        self.play(Write(concat_label))
        self.wait(0.6)

        Z_tex = MathTex(r"\begin{bmatrix}0.12 & -0.34 & 0.56 & 0.78\end{bmatrix}")
        Z_tex.next_to(concat_label, UP)

        small_group = VGroup(z1_tex, z2_tex)
        self.play(Transform(small_group, Z_tex))
        self.play(FadeOut(concat_label), FadeOut(label1), FadeOut(label2))
        self.wait(1)

        # ======== Limpa a tela antes da nova ==========
        self.play(
            FadeOut(arrow1), FadeOut(arrow2),
            FadeOut(galinha), FadeOut(cansada),
            FadeOut(small_group), FadeOut(Z_tex)
        )
        self.wait(0.5)

        # ======== Segunda interação: "galinha" ==========
        word_nao = sentence1[8:11]
        word_atravessou = sentence1[11:21]

        nao = Text("não").move_to(word_nao.get_center())
        atravessou = Text("atravessou").move_to(word_atravessou.get_center())

        nao2 = Text("não", color=PURPLE).next_to(sentence2, DOWN).shift(LEFT*2.5, DOWN*1)
        atravessou2 = Text("atravessou", color=ORANGE).next_to(sentence2, DOWN).shift(RIGHT*2.5, DOWN*1)

        self.add(nao, atravessou)
        self.play(Indicate(word_galinha, color=BLUE))
        self.wait(0.8)
        self.play(Transform(nao, nao2), Transform(atravessou, atravessou2))
        self.wait(1)

        arrow3 = Arrow(word_galinha.get_bottom(), nao2.get_top(), buff=0.2, color=PURPLE)
        label3 = MathTex("H_1: 80\\%").scale(0.7).next_to(arrow3, LEFT)
        self.play(GrowArrow(arrow3), FadeIn(label3))

        arrow4 = Arrow(word_galinha.get_bottom(), atravessou2.get_top(), buff=0.2, color=ORANGE)
        label4 = MathTex("H_2: 85\\%").scale(0.7).next_to(arrow4, RIGHT)
        self.play(GrowArrow(arrow4), FadeIn(label4))

        self.wait(1.5)

        z3_tex = MathTex(r"\begin{bmatrix}-0.22 & 0.44\end{bmatrix}", color=PURPLE)
        z4_tex = MathTex(r"\begin{bmatrix}0.18 & 0.63\end{bmatrix}", color=ORANGE)

        z3_tex.next_to(nao2, DOWN)
        z4_tex.next_to(atravessou2, DOWN*1.5)

        self.play(FadeIn(z3_tex), FadeIn(z4_tex))
        concat_label2 = Text("Concatenação", font_size=24).next_to(VGroup(z3_tex, z4_tex), DOWN)
        self.play(Write(concat_label2))
        self.wait(0.6)

        Z2_tex = MathTex(r"\begin{bmatrix}-0.22 & 0.44 & 0.18 & 0.63\end{bmatrix}")
        Z2_tex.next_to(concat_label2, UP)

        small_group2 = VGroup(z3_tex, z4_tex)
        self.play(Transform(small_group2, Z2_tex))
        self.play(FadeOut(concat_label2), FadeOut(label3), FadeOut(label4))
        self.wait(4)

        self.play(FadeOut(VGroup(small_group2, Z2_tex, nao, nao2, atravessou, atravessou2, sentence1, sentence2, arrow3, arrow4)))
        self.wait(1)