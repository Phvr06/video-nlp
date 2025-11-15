%%manim -qh BagOfWords

class BagOfWords(Scene):
    def construct(self):
        title = Text("Bag of Words", font_size=48).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        text = Text("o cachorro mordeu o homem", font_size=38).shift(UP * 1.5)
        imagem = ImageMobject("cachorro.png").scale(1.2).shift(DOWN * 1)
        self.play(Write(text), FadeIn(imagem), run_time=0.8)
        self.wait(1)

        vec = Text("[1, 1, 1, 1]", font_size=38).shift(UP * 1.5)
        self.play(Transform(text, vec))
        self.wait(6)
        
        self.play(FadeOut(text, imagem), run_time=1)
        self.wait(1)

        text_target1 = Text("o homem mordeu o cachorro", font_size=38).shift(UP * 1.5)
        imagem2 = ImageMobject("homem.png").scale(1.2).shift(DOWN * 1)
        self.play(Write(text_target1), FadeIn(imagem2), run_time=0.8)
        self.wait(1)

        self.play(Transform(text_target1, vec))
        self.wait(2)
        self.play(FadeOut(text_target1, imagem2), run_time=1)
        self.wait(1)

        text_inte = Text("E qual é o problema disso?", weight='BOLD')
        self.play(Write(VGroup(text_inte)), run_time=1)
        self.wait(2)
        self.play(FadeOut(text_inte))
        self.wait(1)
        
        text = Text("Para o modelo de Bag of Words", font_size=36).shift(UP * 1.4)
        text2 = Text("ambas as frases são iguais!", font_size=36).next_to(text, DOWN * 0.8)
        self.play(Write(VGroup(text, text2)), run_time=1)
        self.wait(0.5)

        wrong = Text("E, por causa disso, perdemos", font_size=48).next_to(text2, DOWN * 1.4)
        wrong2 = Text("todo o contexto!", font_size=48, t2c={'contexto!': RED}).next_to(wrong, DOWN * 0.8)
        self.play(Write(VGroup(wrong, wrong2)), run_time=1)
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, text, text2, wrong, wrong2)))
        self.wait(1)