import numpy as np
from numpy.random import RandomState
prng = RandomState(20150101)
import timeit
from vispy import app
from vispy.gloo import gl

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
        self.program = gl.glCreateProgram()
        vertex = gl.glCreateShader(gl.GL_VERTEX_SHADER)
        fragment = gl.glCreateShader(gl.GL_FRAGMENT_SHADER)
        gl.glShaderSource(vertex, vertex_code)
        gl.glShaderSource(fragment, fragment_code)
        gl.glCompileShader(vertex)
        gl.glCompileShader(fragment)
        gl.glAttachShader(self.program, vertex)
        gl.glAttachShader(self.program, fragment)
        gl.glLinkProgram(self.program)
        gl.glDetachShader(self.program, vertex)
        gl.glDetachShader(self.program, fragment)
        gl.glUseProgram(self.program)

        n = 10000000
        self.data = np.zeros((n, 4), dtype=np.float32)
        self.data[:, :2] = .15 * prng.randn(n, 2)
        self.data[:, 3] = 1.
        vbuffer = gl.glCreateBuffer()
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbuffer)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, self.data, gl.GL_DYNAMIC_DRAW)

        stride = self.data.strides[0]
        offset = 0
        loc = gl.glGetAttribLocation(self.program, "a_position")
        gl.glEnableVertexAttribArray(loc)
        gl.glVertexAttribPointer(loc, 4, gl.GL_FLOAT, False, stride, offset)

        gl.glClearColor(0, 0, 0, 1)
        gl.glEnable(34370)
        gl.glEnable(34913)

        # Auto-close after 10 seconds
        self.timer = app.Timer(10, self.on_timer, start=True)

    def on_draw(self, event):
        t = timeit.default_timer()
        self.times.append(t)
        if len(self.times) >= 2:
            print(1./(t-self.times[-2]))
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glDrawArrays(gl.GL_POINTS, 0, len(self.data))
        self.update()

    def on_timer(self, event):
        self.close()

    def on_resize(self, event):
        gl.glViewport(0, 0, *event.size)

def compute_fps(times):
    times = np.array(times)
    fps1 = len(times) / (times[-1] - times[0])
    fps2 = 1 / np.median(np.diff(times))
    return (fps1, fps2)

if __name__ == '__main__':
    c = Canvas()
    c.show()
    app.run()
    print(compute_fps(c.times))
