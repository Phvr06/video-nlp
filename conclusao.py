%%manim -ql Conclusao

class Conclusao(Scene):
    def construct(self):
        # ========== PARTE 1: TÍTULO DE ENCERRAMENTO ==========
        title = Text("Conclusão", font_size=56, weight=BOLD, color=GOLD)
        subtitle = Text("Multi-Head Attention", font_size=42, color=YELLOW)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(subtitle))
        self.wait(2)
        
        self.play(
            title.animate.scale(0.7).to_edge(UP),
            FadeOut(subtitle)
        )
        self.wait(0.5)

        # ========== PARTE 2: PONTOS-CHAVE ==========
        # Criar ícones/bullets
        bullet1 = Text("●", font_size=40, color=BLUE).shift(LEFT*5.5)
        bullet2 = Text("●", font_size=40, color=GREEN).shift(LEFT*5.5)
        bullet3 = Text("●", font_size=40, color=ORANGE).shift(LEFT*5.5)
        
        # Ponto 1: Múltiplos especialistas
        point1 = Text(
            "MHA = Múltiplos especialistas em paralelo",
            font_size=36,
            t2c={"MHA": BLUE, "Múltiplos": BLUE, "paralelo": BLUE}
        )
        point1.next_to(bullet1, RIGHT, buff=0.3)
        
        # Alinhar bullet1 e point1 verticalmente no centro
        group1 = VGroup(bullet1, point1).move_to(UP*1.5)
        
        self.play(
            FadeIn(bullet1, scale=1.5),
            Write(point1),
            run_time=1.5
        )
        self.wait(2.5)
        
        # Ponto 2: Captura relações diversas
        point2 = Text(
            "Captura relações diversas sem 'diluir' o contexto",
            font_size=36,
            t2c={"relações diversas": GREEN, "sem 'diluir'": GREEN}
        )
        point2.next_to(bullet2, RIGHT, buff=0.3)
        
        group2 = VGroup(bullet2, point2).next_to(group1, DOWN, buff=0.8, aligned_edge=LEFT)
        
        self.play(
            FadeIn(bullet2, scale=1.5),
            Write(point2),
            run_time=1.5
        )
        self.wait(2.5)
        
        # Ponto 3: Custo computacional
        point3 = Text(
            "Custo computacional similar ao Single-Head",
            font_size=36,
            t2c={"Custo computacional": ORANGE, "similar": ORANGE}
        )
        point3.next_to(bullet3, RIGHT, buff=0.3)
        
        group3 = VGroup(bullet3, point3).next_to(group2, DOWN, buff=0.8, aligned_edge=LEFT)
        
        self.play(
            FadeIn(bullet3, scale=1.5),
            Write(point3),
            run_time=1.5
        )
        self.wait(3)

        # ========== PARTE 3: DESTAQUE VISUAL DOS PONTOS ==========
        # Criar retângulos ao redor de cada ponto
        box1 = SurroundingRectangle(group1, color=BLUE, buff=0.2, stroke_width=3, corner_radius=0.1)
        box2 = SurroundingRectangle(group2, color=GREEN, buff=0.2, stroke_width=3, corner_radius=0.1)
        box3 = SurroundingRectangle(group3, color=ORANGE, buff=0.2, stroke_width=3, corner_radius=0.1)
        
        self.play(Create(box1))
        self.wait(0.5)
        self.play(FadeOut(box1))
        
        self.play(Create(box2))
        self.wait(0.5)
        self.play(FadeOut(box2))
        
        self.play(Create(box3))
        self.wait(0.5)
        self.play(FadeOut(box3))
        
        self.wait(1)

        # ========== PARTE 4: REFERÊNCIA BIBLIOGRÁFICA ==========
        # Linha separadora
        separator = Line(LEFT*6, RIGHT*6, color=GRAY, stroke_width=2)
        separator.next_to(group3, DOWN, buff=1)
        
        self.play(Create(separator))
        self.wait(0.5)
        
        # Título da referência
        ref_title = Text("Referência:", font_size=32, color=GRAY, weight=BOLD)
        ref_title.next_to(separator, DOWN, buff=0.5).to_edge(LEFT).shift(RIGHT*0.5)
        
        self.play(Write(ref_title))
        self.wait(0.5)
        
        # Paper principal
        paper = Text(
            "'Attention Is All You Need'",
            font_size=34,
            color=WHITE,
            slant=ITALIC
        )
        
        authors = Text(
            "(Vaswani et al., 2017)",
            font_size=32,
            color=GRAY
        )
        
        reference = VGroup(paper, authors).arrange(RIGHT, buff=0.4)
        reference.next_to(ref_title, DOWN, buff=0.3).shift(RIGHT*0.5)
        
        self.play(Write(paper))
        self.wait(0.5)
        self.play(Write(authors))
        self.wait(2)
        
        # Adicionar link visual (ícone de paper)
        paper_icon = Text("📄", font_size=40)
        paper_icon.next_to(reference, LEFT, buff=0.3)
        
        self.play(FadeIn(paper_icon, scale=1.5))
        self.wait(1.5)

        # ========== PARTE 5: ANIMAÇÃO DE DESTAQUE FINAL ==========
        # Destacar todos os elementos juntos
        all_content = VGroup(
            title, group1, group2, group3,
            separator, ref_title, reference, paper_icon
        )
        
        self.play(
            all_content.animate.shift(UP*0.2),
            run_time=0.5
        )
        self.play(
            all_content.animate.shift(DOWN*0.2),
            run_time=0.5
        )
        self.wait(2)

        # ========== PARTE 6: MENSAGEM FINAL ==========
        final_message = Text(
            "Obrigado!",
            font_size=48,
            color=YELLOW,
            weight=BOLD
        )
        final_message.to_edge(DOWN).shift(UP*0.5)
        
        self.play(Write(final_message))
        self.wait(2)
        
        # ========== PARTE 7: FADE OUT GRADUAL ==========
        # Fade out em ondas
        self.play(
            FadeOut(final_message),
            run_time=0.8
        )
        
        self.play(
            FadeOut(VGroup(title, group1)),
            run_time=0.8
        )
        
        self.play(
            FadeOut(VGroup(group2, group3)),
            run_time=0.8
        )
        
        self.play(
            FadeOut(VGroup(separator, ref_title, reference, paper_icon)),
            run_time=1
        )
        
        self.wait(1)