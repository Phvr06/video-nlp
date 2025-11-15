%%manim -qh QuestionamentoMHA

class QuestionamentoMHA(Scene):
    def construct(self):
        text = Text('E se uma palavra precisar').shift(UP * 0.5)
        text2 = Text('de múltiplos contextos diferentes?', t2c={'diferentes?':RED}, t2s={'diferentes?':ITALIC}).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)), run_time=1.5)
        self.wait(3)

        self.play(FadeOut(VGroup(text, text2)))
        self.wait(1)
        
        text = Text('Veja esta frase:', font_size=32).to_edge(UP)
        text2 = Text('"A galinha não atravessou a').shift(UP * 0.5)
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

        self.play(FadeOut(VGroup(text2, text3)))
        self.wait(1)
        
        subtext = Text('Se considerarmos o modelo de atenção tradicional', font_size=40).shift(UP * 1)
        subtext2 = Text('a atenção do nosso modelo ficaria dividida', font_size=40).next_to(subtext, DOWN)
        subtext3 = Text('entre as palavras "cansada", "galinha"', font_size=40).next_to(subtext2, DOWN)
        subtext4 = Text('e todas as outras palavras presentes na frase', font_size=40).next_to(subtext3, DOWN)

        self.play(Write(VGroup(subtext, subtext2, subtext3, subtext4)), run_time=3)
        self.wait(5)

        self.play(FadeOut(VGroup(subtext, subtext2, subtext3, subtext4)))
        self.wait(2)

        subtext = Text('É como se, por exemplo, nosso modelo não', font_size=40).shift(UP * 1)
        subtext2 = Text('tivesse 100% de certeza de que "ela" realmente se', font_size=40).next_to(subtext, DOWN)
        subtext3 = Text('refere às palavras "galinha" e "cansada"', font_size=40).next_to(subtext2, DOWN)

        self.play(Write(VGroup(subtext, subtext2, subtext3)), run_time=3)
        self.wait(5)

        self.play(FadeOut(VGroup(subtext, subtext2, subtext3)))
        self.wait(2)

        text = Text('É aí que introduzímos o').shift(UP * 0.5)
        text2 = Text('Multi-Head Attention', weight=BOLD).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)), run_time=1.5)
        self.wait(2)

        title = Text('Multi-Head Attention').to_edge(UP)

        self.play(FadeOut(text))
        self.play(Transform(text2, title))
        self.wait(1)