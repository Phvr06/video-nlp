%%manim -ql QuestionamentoMHA

class QuestionamentoMHA(Scene):
    def construct(self):
        text = Text('E se uma palavra precisar').shift(UP * 0.5)
        text2 = Text('de múltiplos contextos diferentes?', t2c={'diferentes?':RED}, t2s={'diferentes?':ITALIC}).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)), run_time=1.5)
        self.wait(1)

        self.remove(text, text2)

        text = Text('É aí que introduzímos o').shift(UP * 0.5)
        text2 = Text('Multi-Head Attention', weight=BOLD).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)), run_time=1.5)
        self.wait(2)

        self.remove(text)

        title = Text('Multi-Head Attention', weight=BOLD).to_edge(UP)

        self.play(Transform(text2, title))
        
        text = Text('Veja esta frase:').shift(UP * 1.5)
        text2 = Text('"A galinha não atravessou a').next_to(text, DOWN * 3)
        text3 = Text('rua porque ela estava cansada"').next_to(text2, DOWN)

        self.play(Write(VGroup(text, text2, text3)), run_time=1.5)
        self.wait(2)

        text4 = Text('rua porque ela estava cansada"', t2c={'ela':BLUE}).next_to(text2, DOWN)
        self.play(Transform(text3, text4))
        self.wait()

        self.play(Indicate(text2[2:9], scale_factor=1.1))
        self.wait(0.5)
        self.play(Indicate(text3[18:25], scale_factor=1.1))
        self.wait(1)

        self.play(FadeOut(VGroup(text, text2, text3)))
        
        self.wait(2)
