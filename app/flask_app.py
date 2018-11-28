from app import app
import pandas as pd
import numpy as np

import random
from io import BytesIO
# from StringIO import StringIO  # python 2.7x
import matplotlib.pyplot as plt
from flask import make_response, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import base64

plt.style.use('seaborn')



@app.route('/')
@app.route('/index')
def index():
    df = pd.read_csv('/home/vikibytes/mysite/app/dbtable.csv')
    htm = df.to_html()
    return htm
    
@app.route('/vikas')
def my_barplot():
    """
    This function creates barchart
    """
    df = pd.read_csv('/home/vikibytes/mysite/app/dbtable.csv')

    x_labels = df['CallDate'].values
    x_coordinates = np.arange(len(x_labels))

    bar_heights = df['count'].values
    plt.bar(x_coordinates, bar_heights, align='center', color=['lightblue'], edgecolor=['grey'])
    plt.xticks(x_coordinates, x_labels, rotation='vertical')

    plt.ylabel('Count')
    plt.title('simple bar chart')
    plt.tight_layout()
    plt.savefig('pic.png')

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = str(figdata_png)[2:-1]
    return render_template('output.html', result=result)
