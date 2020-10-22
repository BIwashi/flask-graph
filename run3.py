from flask import Flask, render_template, make_response
from io import BytesIO
import urllib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import random
import numpy as np


app = Flask(__name__)

fig, axes = plt.subplots(3,3,figsize=(32, 15))


x = np.arange(0,10,0.1)
y1 = x**2
y2=  np.sin(x)

@app.route('/')
def index():
  plt.cla()
  
  fig.suptitle('figure title', fontsize=24)

  axes[0,1].set_title('Graph1')
  axes[0,1].grid()
  axes[0,1].set_xlabel('x',fontsize=16)
  axes[0,1].set_ylabel('y1',fontsize=16)
  axes[0,1].plot(x, y1)

  axes[1,2].set_title('Graph2')
  axes[1,2].grid()
  axes[1,2].set_xlabel('x',fontsize=16)
  axes[1,2].set_ylabel('y2',fontsize=16)
  axes[1,2].plot(x, y2)

  canvas = FigureCanvasAgg(fig)
  png_output = BytesIO()
  canvas.print_png(png_output)
  data = png_output.getvalue()

  response = make_response(data)
  response.headers['Content-Type'] = 'image/png'
 

  return response


if __name__ == "__main__":
  app.run()