from flask import Flask, render_template, make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
import numpy as np


app = Flask(__name__)

fig = plt.figure(figsize=[16,4])
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)


x = np.arange(0,10,0.1)
y1 = x**2
y2=  np.sin(x)

@app.route('/')
def index():
  plt.cla()
  
  fig.suptitle('figure title', fontsize=24)

  ax1.set_title('Graph1')
  ax1.grid()
  ax1.set_xlabel('x',fontsize=16)
  ax1.set_ylabel('y1',fontsize=16)
  ax1.plot(x, y1)

  ax2.set_title('Graph2')
  ax2.grid()
  ax2.set_xlabel('x',fontsize=16)
  ax2.set_ylabel('y2',fontsize=16)
  ax2.plot(x, y2)

  canvas = FigureCanvasAgg(fig)
  png_output = BytesIO()
  canvas.print_png(png_output)
  data = png_output.getvalue()

  response = make_response(data)
  response.headers['Content-Type'] = 'image/png'
 

  return response


if __name__ == "__main__":
  app.run()