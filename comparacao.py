%%manim -qh ComparacaoHeads

class ComparacaoHeads(Scene):
    def construct(self):
        # ========== PARTE 1: INTRODUÇÃO ==========
        title = Text("Comparação: 1 Cabeça vs 8 Cabeças", font_size=42, weight=BOLD)
        subtitle = Text("Resultados em Dataset do IMDB", font_size=32)
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.wait(0.5)
        self.play(Write(subtitle))
        self.wait(2)
        
        self.play(FadeOut(VGroup(title, subtitle)))
        self.wait(0.5)

        # ========== PARTE 2: CRIAR OS EIXOS ==========
        # Eixo da Acurácia (esquerda)
        axes_acc = Axes(
            x_range=[0, 7, 1],
            y_range=[0.55, 0.85, 0.05],
            x_length=5.5,
            y_length=4,
            axis_config={"color": WHITE, "include_numbers": True},
            x_axis_config={
                "numbers_to_include": [1, 2, 3, 4, 5, 6],
                "font_size": 22,
            },
            y_axis_config={
                "numbers_to_include": [0.60, 0.65, 0.70, 0.75, 0.80],
                "font_size": 22,
                "decimal_number_config": {"num_decimal_places": 2},
            },
            tips=False,
        ).shift(LEFT*3, DOWN*0.3).scale(0.9)
        
        # Labels do eixo de Acurácia
        acc_x_label = Text("Época", font_size=20).next_to(axes_acc, DOWN, buff=0.3)
        acc_y_label = Text("Acurácia", font_size=20).next_to(axes_acc, LEFT, buff=0.05).rotate(PI/2)
        acc_title = Text("Acurácia por Época", font_size=22, weight=BOLD)
        acc_title.next_to(axes_acc, UP, buff=0.3)
        
        # Eixo da Loss (direita)
        axes_loss = Axes(
            x_range=[0, 7, 1],
            y_range=[0.40, 0.75, 0.05],
            x_length=5.5,
            y_length=4,
            axis_config={"color": WHITE, "include_numbers": True},
            x_axis_config={
                "numbers_to_include": [1, 2, 3, 4, 5, 6],
                "font_size": 22,
            },
            y_axis_config={
                "numbers_to_include": [0.45, 0.50, 0.55, 0.60, 0.65, 0.70],
                "font_size": 24,
                "decimal_number_config": {"num_decimal_places": 2},
            },
            tips=False,
        ).shift(RIGHT*4, DOWN*0.3).scale(0.9)
        
        # Labels do eixo de Loss
        loss_x_label = Text("Época", font_size=20).next_to(axes_loss, DOWN, buff=0.3)
        loss_y_label = Text("Loss", font_size=20).next_to(axes_loss, LEFT, buff=0.1).rotate(PI/2)
        loss_title = Text("Loss por Época", font_size=22, weight=BOLD)
        loss_title.next_to(axes_loss, UP, buff=0.3)
        
        # Mostrar eixos
        self.play(
            Create(axes_acc), Write(acc_x_label), Write(acc_y_label), Write(acc_title),
            Create(axes_loss), Write(loss_x_label), Write(loss_y_label), Write(loss_title),
            run_time=2
        )
        self.wait(1)

        # ========== PARTE 3: DADOS ==========
        # Dados de Acurácia
        epochs = [1, 2, 3, 4, 5, 6]
        acc_h1 = [0.605, 0.580, 0.575, 0.573, 0.588, 0.575]  # 1 cabeça
        acc_h8 = [0.708, 0.738, 0.725, 0.785, 0.795, 0.808]  # 8 cabeças
        
        # Dados de Loss
        loss_h1 = [0.695, 0.695, 0.695, 0.695, 0.690, 0.690]  # 1 cabeça (quase flat)
        loss_h8 = [0.570, 0.530, 0.532, 0.462, 0.451, 0.430]  # 8 cabeças
        
        # Criar pontos para acurácia
        points_acc_h1 = [axes_acc.coords_to_point(e, a) for e, a in zip(epochs, acc_h1)]
        points_acc_h8 = [axes_acc.coords_to_point(e, a) for e, a in zip(epochs, acc_h8)]
        
        # Criar pontos para loss
        points_loss_h1 = [axes_loss.coords_to_point(e, l) for e, l in zip(epochs, loss_h1)]
        points_loss_h8 = [axes_loss.coords_to_point(e, l) for e, l in zip(epochs, loss_h8)]

        # ========== PARTE 4: ANIMAR 1 CABEÇA (AZUL) ==========
        explanation_h1 = Text("Modelo com 1 Cabeça de Atenção", font_size=30, color=BLUE)
        explanation_h1.to_edge(UP)
        
        self.play(Write(explanation_h1))
        self.wait(1)
        
        # Linha de acurácia h1
        line_acc_h1 = VMobject(color=BLUE, stroke_width=4)
        line_acc_h1.set_points_as_corners(points_acc_h1)
        
        # Dots de acurácia h1
        dots_acc_h1 = VGroup(*[
            Dot(point, color=BLUE, radius=0.08) for point in points_acc_h1
        ])
        
        # Linha de loss h1
        line_loss_h1 = VMobject(color=BLUE, stroke_width=4)
        line_loss_h1.set_points_as_corners(points_loss_h1)
        
        # Dots de loss h1
        dots_loss_h1 = VGroup(*[
            Dot(point, color=BLUE, radius=0.08) for point in points_loss_h1
        ])
        
        # Animar desenho das linhas h1
        self.play(
            Create(line_acc_h1),
            Create(line_loss_h1),
            run_time=2.5
        )
        self.wait(2)

        # ========== PARTE 5: ANIMAR 8 CABEÇAS (LARANJA) ==========
        explanation_h8 = Text("Modelo com 8 Cabeças de Atenção", font_size=30, color=ORANGE)
        explanation_h8.to_edge(UP)
        
        self.play(Transform(explanation_h1, explanation_h8))
        self.wait(1)
        
        # Linha de acurácia h8
        line_acc_h8 = VMobject(color=ORANGE, stroke_width=4)
        line_acc_h8.set_points_as_corners(points_acc_h8)
        
        # Dots de acurácia h8
        dots_acc_h8 = VGroup(*[
            Dot(point, color=ORANGE, radius=0.08) for point in points_acc_h8
        ])
        
        # Linha de loss h8
        line_loss_h8 = VMobject(color=ORANGE, stroke_width=4)
        line_loss_h8.set_points_as_corners(points_loss_h8)
        
        # Dots de loss h8
        dots_loss_h8 = VGroup(*[
            Dot(point, color=ORANGE, radius=0.08) for point in points_loss_h8
        ])
        
        # Animar desenho das linhas h8
        self.play(
            Create(line_acc_h8),
            Create(line_loss_h8),
            run_time=2.5
        )
        self.wait(2)

        # ========== PARTE 7: ANÁLISE E CONCLUSÃO ==========
        self.play(FadeOut(explanation_h1))
        self.wait(0.3)
        
        # Destacar diferença na acurácia final
        final_acc_h1_val = Text(f"{acc_h1[-1]:.1%}", font_size=24, color=BLUE)
        final_acc_h1_val.next_to(dots_acc_h1[-1], UP, buff=0.2)
        
        final_acc_h8_val = Text(f"{acc_h8[-1]:.1%}", font_size=24, color=ORANGE)
        final_acc_h8_val.next_to(dots_acc_h8[-1], UP, buff=0.2)
        
        self.play(
            Write(final_acc_h1_val),
            Write(final_acc_h8_val),
            Indicate(dots_acc_h1[-1], scale_factor=1.5, color=BLUE),
            Indicate(dots_acc_h8[-1], scale_factor=1.5, color=ORANGE)
        )
        self.wait(2)

        # Fade out final
        self.play(FadeOut(VGroup(
            axes_acc, acc_x_label, acc_y_label, acc_title,
            axes_loss, loss_x_label, loss_y_label, loss_title,
            line_acc_h1, line_acc_h8, dots_acc_h1[-1],
            line_loss_h1, line_loss_h8, dots_acc_h8[-1],
            final_acc_h1_val, final_acc_h8_val
        )))
        self.wait(2)

        
        conclusion = Text(
            "Múltiplas cabeças de atenção melhoram",
            font_size=34
        ).shift(UP*0.5)
        
        conclusion2 = Text(
            "significativamente o desempenho do modelo!",
            font_size=34
        ).next_to(conclusion, DOWN)
        
        self.play(Write(VGroup(conclusion, conclusion2)))
        self.wait(3)
        
        self.play(FadeOut(VGroup(conclusion, conclusion2)))
        self.wait(2)