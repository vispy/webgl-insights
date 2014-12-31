import numpy as np
from numpy.random import RandomState
prng = RandomState(20150101)
import timeit
from vispy import app, gloo
app.use_app('glfw')

vertex_code = """
attribute vec4 a_position;
void main () {
    gl_Position = a_position;
    gl_PointSize = 1.;
}
"""

fragment_code = """
void main()
{
    gl_FragColor = vec4(1,1,1,1);
}
"""

class Canvas(app.Canvas):
    def __init__(self):
        app.Canvas.__init__(self, size=(800, 800), keys='interactive')
        self.times = []

    def on_initialize(self, event):
        self.program = gloo.Program(vertex_code, fragment_code)

        n = 10000000
        self.data = np.zeros((n, 4), dtype=np.float32)
        self.data[:, :2] = .15 * prng.randn(n, 2)
        self.data[:, 3] = 1.
        self.program['a_position'] = self.data

        gloo.clear((0, 0, 0, 1))

        # Auto-close after 10 seconds
        self.timer = app.Timer(10, self.on_timer, start=True)

    def on_draw(self, event):
        t = timeit.default_timer()
        self.times.append(t)
        if len(self.times) >= 2:
            print(1./(t-self.times[-2]))
        gloo.clear()
        self.program.draw('points')
        self.update()

    def on_timer(self, event):
        self.close()

    def on_resize(self, event):
        gloo.set_viewport(0, 0, *event.size)

def compute_fps(times):
    times = np.array(times)
    times -= times[0]
    dtimes = np.diff(times)
    fps = len(times) / (times[-1])
    std = np.mean(np.abs(dtimes - np.median(dtimes))) * fps
    return (fps, std)

if __name__ == '__main__':
    c = Canvas()
    c.show()
    app.run()
    print(compute_fps(c.times))
