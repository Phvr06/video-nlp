%%manim -qh Antigamente

class Antigamente(Scene):
    def construct(self):
        text = Text("Só que antes de explicar o MHA,", font_size=38).shift(UP * 0.5)
        text2 = Text("preciamos lembrar que", font_size=38).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)))
        self.wait(4)
        self.play(FadeOut(VGroup(text, text2)))
        self.wait(0.2)
        
        text = Text("Uma das primeiras formas de", font_size=38).shift(UP * 1)
        text2 = Text("classificação textual, foi a técnica de", font_size=38).next_to(text, DOWN)
        text3 = Text("Bag of Words", font_size=38).next_to(text2, DOWN)
        self.play(Write(VGroup(text, text2, text3)))
        self.wait(5)
        self.play(FadeOut(VGroup(text, text2, text3)))
        self.wait(1)