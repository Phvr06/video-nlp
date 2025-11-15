%%manim -qh Attention

class Attention(Scene):
    def construct(self):
        title = Text('Atenção').to_edge(UP)
        self.play(Write(title))
        self.wait(3)
        
        words = [Text("A"), Text("gata"), Text("laranja")]
        
        group = VGroup(*words).arrange(RIGHT, buff=0.3)
        self.play(Write(group))
        self.wait(1.5)

        vectors = [
            Matrix([[0.6, -0.2, 2.4]]).set_color(RED),
            Matrix([[-2.1, 1.3, 0.7]]).set_color(RED),
            Matrix([[3.2, 0.5, -1.3]]).set_color(RED)
        ]

        left_x = -3.5
        right_x = 3.5
        start_y = 1

        for i, word in enumerate(words):
            word.generate_target()
            word.target.move_to([left_x, start_y - i*1.5, 0])
            vectors[i].scale(0.8)
            vectors[i].move_to([right_x, start_y - i*1.5, 0])

        self.play(*[MoveToTarget(w) for w in words], run_time=2)

        # Mostra os vetores correspondentes
        self.play(*[FadeIn(v) for v in vectors], run_time=1)
        self.wait(3)

        q_list = []
        k_list = []
        v_list = []
        qkv_groups = []
        for i, txt in enumerate(['A', 'G', 'L']):
            q = Tex(rf"$Q_{{{txt}}}$", color=RED).scale(0.5)
            k = Tex(rf"$K_{{{txt}}}$", color=BLUE).scale(0.5)
            v = Tex(rf"$V_{{{txt}}}$", color=YELLOW).scale(0.5)
            g = VGroup(q, k, v).arrange(DOWN, buff=0.15)
            q_list.append(q)
            k_list.append(k)
            v_list.append(v)
            qkv_groups.append(g)

        # usa a posição vertical das palavras, mas alinha todos pelo x do último (laranja)
        target_x = left_x + 1.7
        for i, g in enumerate(qkv_groups):
            g.move_to([target_x, start_y - i*1.5, 0])

        self.play(*[FadeIn(g) for g in qkv_groups], run_time=1)
        self.wait(3)

        q_list[0].generate_target()
        q_list[0].target.next_to(k_list[1], RIGHT, buff=0.2)
        self.play(MoveToTarget(q_list[0]), run_time=1.2)
        self.wait(0.6)

        v_gata_copy = v_list[1].copy()
        v_gata_copy.move_to(v_list[1].get_center())
        self.add(v_gata_copy)
        self.play(v_gata_copy.animate.move_to(vectors[0].get_center() + UP * 0.5), run_time=1.0)
        self.wait(0.4)

        new_matrix_for_A = Matrix([[-1.6, 2.1, 1.7]]).set_color(RED)
        new_matrix_for_A.scale(0.8)
        new_matrix_for_A.move_to(vectors[0].get_center())
        self.play(ReplacementTransform(vectors[0], new_matrix_for_A), run_time=1.0)
        vectors[0] = new_matrix_for_A

        self.play(FadeOut(v_gata_copy), run_time=0.6)
        self.wait(0.6)

        q_list[0].generate_target()
        q_list[0].target.next_to(k_list[2], RIGHT, buff=0.2)
        self.play(MoveToTarget(q_list[0]), run_time=1.2)
        self.wait(0.6)

        v_laranja_copy = v_list[2].copy()
        v_laranja_copy.move_to(v_list[2].get_center())
        self.add(v_laranja_copy)
        self.play(v_laranja_copy.animate.move_to(vectors[0].get_center() + UP * 0.5), run_time=1.0)
        self.wait(0.4)

        new_matrix_for_A_2 = Matrix([[-1.5, 2.1, 1.8]]).set_color(RED)
        new_matrix_for_A_2.scale(0.8)
        new_matrix_for_A_2.move_to(vectors[0].get_center())
        self.play(ReplacementTransform(vectors[0], new_matrix_for_A_2), run_time=1.0)
        vectors[0] = new_matrix_for_A_2

        q_list[0].generate_target()
        q_list[0].target.next_to(k_list[0], UP, buff=0.15)
        self.play(FadeOut(v_laranja_copy), MoveToTarget(q_list[0]), run_time=0.6)
        self.wait(1.0)

        q_list[1].generate_target()
        q_list[1].target.next_to(k_list[0], RIGHT, buff=0.2)
        self.play(MoveToTarget(q_list[1]), run_time=0.6)
        self.wait(0.3)

        v_A_copy = v_list[0].copy()
        v_A_copy.move_to(v_list[0].get_center())
        self.add(v_A_copy)
        self.play(v_A_copy.animate.move_to(vectors[1].get_center() + UP * 0.5), run_time=0.5)
        self.wait(0.2)

        new_matrix_for_gata = Matrix([[ -0.7, 0.9, 1.5]]).set_color(RED)
        new_matrix_for_gata.scale(0.8)
        new_matrix_for_gata.move_to(vectors[1].get_center())
        self.play(ReplacementTransform(vectors[1], new_matrix_for_gata), run_time=0.5)
        vectors[1] = new_matrix_for_gata

        self.play(FadeOut(v_A_copy), run_time=0.3)
        self.wait(0.3)

        q_list[1].generate_target()
        q_list[1].target.next_to(k_list[2], RIGHT, buff=0.2)
        self.play(MoveToTarget(q_list[1]), run_time=0.6)
        self.wait(0.3)

        v_laranja_copy_2 = v_list[2].copy()
        v_laranja_copy_2.move_to(v_list[2].get_center())
        self.add(v_laranja_copy_2)
        self.play(v_laranja_copy_2.animate.move_to(vectors[1].get_center() + UP * 0.5), run_time=0.5)
        self.wait(0.2)

        new_matrix_for_gata_2 = Matrix([[0.4, -0.3, 2.0]]).set_color(RED)
        new_matrix_for_gata_2.scale(0.8)
        new_matrix_for_gata_2.move_to(vectors[1].get_center())
        self.play(ReplacementTransform(vectors[1], new_matrix_for_gata_2), run_time=0.5)
        vectors[1] = new_matrix_for_gata_2

        q_list[1].generate_target()
        q_list[1].target.next_to(k_list[1], UP, buff=0.15)
        self.play(FadeOut(v_laranja_copy_2), MoveToTarget(q_list[1]), run_time=0.3)
        self.wait(0.5)

        q_list[2].generate_target()
        q_list[2].target.next_to(k_list[0], RIGHT, buff=0.2)
        self.play(MoveToTarget(q_list[2]), run_time=0.6)
        self.wait(0.3)

        v_A_copy_2 = v_list[0].copy()
        v_A_copy_2.move_to(v_list[0].get_center())
        self.add(v_A_copy_2)
        self.play(v_A_copy_2.animate.move_to(vectors[2].get_center() + UP * 0.5), run_time=0.5)
        self.wait(0.2)

        new_matrix_for_laranja = Matrix([[3.0, 0.6, -1.3]]).set_color(RED)
        new_matrix_for_laranja.scale(0.8)
        new_matrix_for_laranja.move_to(vectors[2].get_center())
        self.play(ReplacementTransform(vectors[2], new_matrix_for_laranja), run_time=0.5)
        vectors[2] = new_matrix_for_laranja

        self.play(FadeOut(v_A_copy_2), run_time=0.3)
        self.wait(0.3)

        q_list[2].generate_target()
        q_list[2].target.next_to(k_list[1], RIGHT, buff=0.2)
        self.play(MoveToTarget(q_list[2]), run_time=0.6)
        self.wait(0.3)

        v_gata_copy_2 = v_list[1].copy()
        v_gata_copy_2.move_to(v_list[1].get_center())
        self.add(v_gata_copy_2)
        self.play(v_gata_copy_2.animate.move_to(vectors[2].get_center() + UP * 0.5), run_time=0.5)
        self.wait(0.2)

        new_matrix_for_laranja_2 = Matrix([[0.9, -0.3, -2.1]]).set_color(RED)
        new_matrix_for_laranja_2.scale(0.8)
        new_matrix_for_laranja_2.move_to(vectors[2].get_center())
        self.play(ReplacementTransform(vectors[2], new_matrix_for_laranja_2), run_time=0.5)
        vectors[2] = new_matrix_for_laranja_2

        q_list[2].generate_target()
        q_list[2].target.next_to(k_list[2], UP, buff=0.15)
        self.play(FadeOut(v_gata_copy_2), MoveToTarget(q_list[2]), run_time=0.3)
        self.wait(2)
