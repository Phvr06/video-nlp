%%manim -qh ModelosModernos

class ModelosModernos(Scene):
    def construct(self):
        text = Text('Mas como os modelos atuais').shift(UP * 0.5)
        text2 = Text('resolvem isso?').next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)))
        self.wait(1)

        self.play(FadeOut(VGroup(text, text2)))
        self.wait(1)

        text3 = Text('Eles utilizam a').shift(UP * 0.5)
        text4 = Text('ATENÇÃO', color='RED', weight='BOLD', font_size='58').next_to(text3, DOWN)
        self.play(Write(text3))
        self.play(GrowFromCenter(text4))

        self.wait(1)
        self.play(FadeOut(VGroup(text3, text4)))
        self.wait(1)

        subtext = Text('Um mecanismo que permite ao modelo', font_size=40).shift(UP * 1)
        subtext2 = Text('ponderar a relevância de cada palavra', font_size=40).next_to(subtext, DOWN)
        subtext3 = Text('em relação às outras', font_size=40).next_to(subtext2, DOWN)
        self.play(Write(VGroup(subtext, subtext2, subtext3)))
        self.wait(4)

        self.play(FadeOut(VGroup(subtext, subtext2, subtext3)))
        self.wait(1)

        subtext = Text('Vamos entender como!', font_size=58).shift(UP * 0.4)
        self.play(Write(VGroup(subtext)))
        self.wait(2)

        self.play(FadeOut(VGroup(subtext)))
        self.wait(1)