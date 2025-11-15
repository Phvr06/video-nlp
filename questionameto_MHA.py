%%manim -qh QuestionamentoMHA

class QuestionamentoMHA(Scene):
    def construct(self):
        text = Text('E se uma palavra precisar').shift(UP * 0.5)
        text2 = Text('de múltiplos contextos diferentes?', t2c={'diferentes?':RED}, t2s={'diferentes?':ITALIC}).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)), run_time=1.5)
        self.wait(3)

        self.play(FadeOut(VGroup(text, text2)))
        self.wait(1)

        text = Text('É aí que introduzímos o').shift(UP * 0.5)
        text2 = Text('Multi-Head Attention', weight=BOLD).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(text))

        title = Text('Multi-Head Attention').to_edge(UP)

        self.play(Transform(text2, title))
        self.wait(0.1)
        self.remove(text2)
        self.add(title)
        
        text = Text('Veja esta frase:', font_size=32).shift(UP * 1.5)
        text2 = Text('"A galinha não atravessou a').next_to(text, DOWN * 3)
        text3 = Text('rua porque ela estava cansada"').next_to(text2, DOWN)

        self.play(Write(text))
        self.play(Write(VGroup(text2, text3)), run_time=1.5)
        self.wait(2)

        text4 = Text('rua porque ela estava cansada"', t2c={'ela':BLUE}).next_to(text2, DOWN)
        self.play(Transform(text3, text4), FadeOut(text))
        self.wait(1.5)

        self.play(Indicate(text2[2:9], scale_factor=1.1))
        self.wait(2)
        self.play(Indicate(text3[18:25], scale_factor=1.1))
        self.wait(2)

        self.play(FadeOut(VGroup(title, text2, text3)))
        
        self.wait(2)