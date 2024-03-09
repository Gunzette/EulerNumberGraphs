from manim import *
import math


config.background_color = ManimColor("#E0E0D8")
xColor = PURPLE
aColor = PURPLE
tanColor = PURPLE

class Hmethod(Scene):
    def construct(self):
        t = ValueTracker(0)

        ax = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 5, 1],
            axis_config={"include_numbers": False, "stroke_color": BLACK, "fill_color": BLACK},
        )
        labels = ax.get_axis_labels(x_label=MathTex('x'), y_label=MathTex('y')).set_color(BLACK)

        f = (lambda x: 0.25*(math.e**x))

        fplot = ax.plot(f, x_range=[0, 4], stroke_color=RED)

        aDot = Dot(ax.coords_to_point(2.5, (0.25*(math.e**2.5))), color=aColor)

        xDot = Dot(ax.coords_to_point(0.5, (0.25*(math.e**0.5))), color=xColor)


        xDot.add_updater(
            lambda x: x.become(Dot(ax.coords_to_point(0.5+t.get_value(), (0.25*(math.e**(0.5+t.get_value())))), color=xColor))
        )

        aLine = DashedLine(aDot.get_center(), (aDot.get_x(), ax.get_origin()[1], 1), color=aColor)

        aLabel = MathTex("a", color=aColor).move_to([aDot.get_x(), ax.get_origin()[1], 1] - UP*0.5)

        xLine = DashedLine(xDot.get_center(), (xDot.get_x(), ax.get_origin()[1], 1), color=xColor)

        xLabel = MathTex("x", color=xColor).move_to([xDot.get_x(), ax.get_origin()[1], 1] - UP*0.5)

        xLine.add_updater(
            lambda x: x.become(DashedLine(xDot.get_center(), (xDot.get_x(), ax.get_origin()[1], 1), color=xColor))
        )

        xLabel.add_updater(
            lambda x: x.move_to([xDot.get_x(), ax.get_origin()[1], 1] - UP*0.5)
        )

        ta = always_redraw(lambda: Line(aDot.get_center(), xDot.get_center(), color=tanColor).set_length(100).set_z_index(-1))



        self.add(ax, fplot, aDot, xDot, aLine, aLabel, xLine, xLabel, ta, labels)

        self.wait()

        lim1tex = MathTex(r"\lim_{x \to a}").set_color(aColor).move_to(ax.c2p(1, 4)).scale(2)

        lim2tex = MathTex(r"\lim_{h \to 0}").set_color(aColor).move_to(lim1tex.get_center()).scale(2)

        self.play(FadeIn(lim1tex))

        self.play(t.animate.increment_value(1.59), run_time=4, rate_func=rate_functions.linear)

        self.play(t.animate.increment_value(0.40), FadeOut(xLabel, aLabel), run_time=1, rate_func=rate_functions.linear)


        self.wait()
        

        hbrace = BraceBetweenPoints([xDot.get_x(), ax.get_origin()[1], 1], [aDot.get_x(), ax.get_origin()[1], 1], color=aColor).add_updater(
            lambda x: x.become(BraceBetweenPoints([xDot.get_x(), ax.get_origin()[1], 1], [aDot.get_x(), ax.get_origin()[1], 1], color=aColor))
        )
        hlabel = MathTex(r"h", color=aColor).move_to(hbrace.get_center()-UP*0.4).add_updater(
            lambda x: x.move_to(hbrace.get_center()-UP*0.4)
        )

        self.play(t.animate.set_value(0), FadeTransform(lim1tex, lim2tex), FadeIn(hbrace, hlabel, aLabel, xLabel))

        self.wait()

        self.play(t.animate.increment_value(1.59), run_time=4, rate_func=rate_functions.linear)

        self.play(t.animate.increment_value(0.40), FadeOut(xLabel, aLabel), run_time=1, rate_func=rate_functions.linear)
