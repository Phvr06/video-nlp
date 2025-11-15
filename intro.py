%%manim -qh Intro

class Intro(Scene):
    def construct(self):
        text = Text("Nesse trabalho iremos destrinchar", font_size=42).shift(UP * 0.5)
        text2 = Text("o funcionamento do Multi-Head Attention", font_size=42).next_to(text, DOWN)
        self.play(Write(VGroup(text, text2)))
        self.wait(5)
        self.play(FadeOut(VGroup(text, text2)))
        self.wait(1)