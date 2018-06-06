import plotly.plotly as py
import pandas as pd

class ChoroMapGenerator():
    def __init__(self):
        py.sign_in("maor309", "FSzzbXNMhAZwI4B6ApPt")

    def generate_choromap_image(self, df, output_image_name):
        data = [ dict(
                type = 'choropleth',
                locations = [x[0:3].upper() for x in df['country']],
                z = df['Life Ladder'],
                text = df['country'],
                colorscale = [[0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
                    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"]],
                autocolorscale = False,
                reversescale = True,
                marker = dict(
                    line = dict (
                        color = 'rgb(180,180,180)',
                        width = 0.5
                    ) ),
                colorbar = dict(
                    autotick = False,
                    tickprefix = '$',
                    title = 'GDP<br>Billions US$'),
              ) ]

        layout = dict(
            title = 'stupid assignments',
            geo = dict(
                showframe = False,
                showcoastlines = False,
                projection = dict(
                    type = 'Mercator'
                )
            )
        )

        fig = dict( data=data, layout=layout )
        # py.iplot( fig, validate=False, filename='d3-world-map' )
        py.image.save_as(fig, filename="{0}.png".format(output_image_name))

df = pd.read_excel('data.xlsx')
ChoroMapGenerator().generate_choromap_image(df, "img1")