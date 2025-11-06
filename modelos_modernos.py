%%manim -qh ModelosModernos

class ModelosModernos(Scene):
    def construct(self):
        text = Text('Mas como os modelos atuais').shift(UP * 0.5)
        text2 = Text('resolvem isso?').next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)))
        self.wait(1)

        self.remove(text, text2)

        text3 = Text('É simples! Eles utilizam a').shift(UP * 0.5)
        text4 = Text('ATENÇÃO', color='RED', weight='BOLD', font_size='58').next_to(text3, DOWN)
        self.play(Write(text3))
        self.play(GrowFromCenter(text4))

        self.wait(2)
