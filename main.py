from manim import *
from math import floor

config.background_color = ManimColor("#EEEFED")

class Interest(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1.1, 0.1],
            y_range=[0, 3, 1],
            axis_config={"include_numbers": True, "stroke_color": BLACK, "fill_color": BLACK},
        )
        x = ax.get_x_axis()
        x.numbers.set_color(BLACK)
        y = ax.get_y_axis()
        y.numbers.set_color(BLACK)
        labels = ax.get_axis_labels(x_label=MathTex('Zeit (Jahre)'), y_label=MathTex('Geld (Euro)')).set_color(BLACK)

        def f1(x):
            if x < 1:
                return 1
            else:
                return 2

        def f2(x):
            if x < 0.5:
                return 1
            elif x < 1:
                return (1+(1/2))**1
            else:
                return (1+(1/2))**2
            
        def f3(x):
            return (1+(1/4))**(floor(4*x))
        
        def f4(x):
            return (1+(1/5000))**(floor(x*5000))
        


        #graph = ax.plot(f1, x_range=[0, 1.1], stroke_color=RED, use_smoothing=False)
        #graph = ax.plot(f2, x_range=[0, 1.1], stroke_color=RED, use_smoothing=False)
        #graph = ax.plot(f3, x_range=[0, 1.1], stroke_color=RED, use_smoothing=False)
        graph = ax.plot(f4, x_range=[0, 1.0], stroke_color=RED, use_smoothing=True)

        endpoint = Dot(graph.get_end(), color=RED)

        #xLine = DashedLine([endpoint.get_x(), ax.get_origin()[1], 0], [endpoint.get_x(), endpoint.get_y(), 0], color=RED)
        #yLine = DashedLine([ax.get_origin()[0], endpoint.get_y(), 0], [endpoint.get_x(), endpoint.get_y(), 0], color=RED)

        #yDot = Dot([ax.get_origin()[0], endpoint.get_y(), 0], color=RED)
        #yQM = Text("?", color=RED, font="Cambria", weight=LIGHT).move_to(yDot).shift(LEFT*0.5)

        self.add(ax, graph, endpoint, labels) 
        #self.add(ax, graph, endpoint, xLine, yLine, yDot, yQM, labels)

        #TODO GESTRICHELTE LINIE ZUM ENDWERT, ENDWERT HINSCHREIBEN

