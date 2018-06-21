import random

import plotly.plotly as py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class PlotGenerator():
    def __init__(self, working_dir_path):
        '''
        Activating plotly account and set working dir
        '''
        py.sign_in("maor309", "FSzzbXNMhAZwI4B6ApPt")
        self.working_dir_path = working_dir_path

    def generate_choromap_image(self, df):
        '''
        Generate choromap image (the world map) as "map_plot.png"
        :param df: DataFrame containing countries names and their clusters results for graph
        :return:
        '''
        data = [dict(
            type='choropleth',
            locations=[x[0:3].upper() for x in df['country']],
            z=df['Cluster'],
            text=df['country'],
            colorscale=[[0, "rgb(5, 10, 172)"], [0.35, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], \
                        [0.6, "rgb(90, 120, 245)"], [0.7, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
            autocolorscale=False,
            reversescale=True,
            marker=dict(
                line=dict(
                    color='rgb(180,180,180)',
                    width=0.5
                )),
            colorbar=dict(
                autotick=False,
                tickprefix='',
                title='Clusters'),
        )]

        layout = dict(
            title='stupid assignments',
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection=dict(
                    type='Mercator'
                )
            )
        )

        fig = dict(data=data, layout=layout)
        # py.iplot( fig, validate=False, filename='d3-world-map' )
        py.image.save_as(fig, filename=self.working_dir_path + "/map_plot.png")

    def generate_scatter_plot_image(self, df):
        '''
        Generate scatter plot graph image as "scatter_plot.png"
        :param df: DataFrame containing ('Generosity', 'Social support','Cluster') for graph
        '''
        x = df['Generosity']
        y = df['Social support']
        colors = df['Cluster']
        plt.scatter(x, y, c=colors, s=60, alpha=0.5)
        plt.savefig(self.working_dir_path + '/scatter_plot.png')
