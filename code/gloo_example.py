def _process_arg(s):
    return str(s).replace('\n', '\\n')

def _show_glir(canvas):
    commands = canvas.context.glir._commands
    print('\n'.join(' '.join(map(_process_arg, command))
          for command in commands))



from vispy import app, gloo
import numpy as np

vertex = """
attribute vec2 position;
void main() {
    gl_Position = vec4(position, 0.0, 1.0);
    gl_PointSize = 20.0;
}
"""

fragment = """
void main() {
    vec2 t = 2.0 * gl_PointCoord.xy - 1.0;
    float a = 1.0 - pow(t.x, 2.0) - pow(t.y, 2.0);
    gl_FragColor = vec4(0.1, 0.3, 0.6, a);
}
"""

canvas = app.Canvas()

program = gloo.Program(vertex, fragment)
data = 0.3 * np.random.randn(10000, 2)
program['position'] = data.astype(np.float32)

@canvas.connect
def on_resize(event):
    width, height = event.size
    gloo.set_viewport(0, 0, width, height)

@canvas.connect
def on_draw(event):
    gloo.set_state(clear_color=(0, 0, 0, 1), blend=True,
                   blend_func=('src_alpha', 'one'))
    gloo.clear()
    program.draw('points')
    _show_glir(canvas)

canvas.show()
app.run()














# canvas = app.Canvas(keys='interactive')

# program = gloo.Program(vertex, fragment)
# data = 0.3 * np.random.randn(10000, 2)
# program['position'] = data.astype(np.float32)

# @canvas.connect
# def on_resize(event):
#     width, height = event.size
#     gloo.set_viewport(0, 0, width, height)

# @canvas.connect
# def on_draw(event):
#     gloo.set_state(clear_color=(0, 0, 0, 1), blend=True,
#                    blend_func=('src_alpha', 'one'))
#     gloo.clear()
#     program.draw('points')

# if __name__ == '__main__':
#     canvas.show()
#     app.run()
