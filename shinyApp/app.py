# import matplotlib.pyplot as plt
# import numpy as np
from pathlib import Path

# import pandas

from shiny import reactive
import pandas as pd
from shiny.express import ui, input, render
from shinyswatch import theme
# songs = pd.read_csv("../data/3_spotify_5000_songs.csv")
# songs.columns = songs.columns.str.strip()
# songs = songs.set_index(["name", "artist"])
# songs_df = songs.drop(columns=["id", "html",  "type", "Unnamed: 0"])
@reactive.calc
def dat():
    infile = Path(__file__).parent / "2_spotify_10_songs.csv"
    return pd.read_csv(infile)

ui.page_opts(title="Create custom playlists using machine learning", theme=theme.journal)

with ui.navset_pill_list(id="tab"):  
    with ui.nav_panel("Get started"):
        "Panel A content"    
        @render.data_frame
        def frame():
            # Give dat() to render.DataGrid to customize the grid
            return dat()      

    with ui.nav_panel("Scaling"):
        #"Slect your scaling method"
        ui.input_radio_buttons(  
            "radio_scaling",  
            "Select your scaling or transformation method:",  
            {"no_scaling": "No Scaling",
            "minmax": "Min Max Scaling", 
            "standard": "Standard Scaling",
            "robust": "Robust Scaling",
            "power": "Power Transformation",
            "quantile": "Quantile Transformation"},  
        )  
        @render.ui
        def value_scaling():
            return input.radio_scaling()
        # plot impact of scaling here
        #@render.plot(alt="Scaling")

    with ui.nav_panel("PCA"):
        "Panel C content"
        ui.HTML("<iframe src='https://open.spotify.com/embed/playlist/5L2TYdgPxgGBTRCNqSlx1Q?utm_source=generator' width='100%' height='352' frameBorder='0' allow='autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture' loading='lazy'></iframe>")
                
    with ui.nav_panel("Clustering"):
            "Page D content"
            ui.input_slider("slider_cluster", 
                            "Select the number of clusters:", 2, 200, 100)  

            @render.text
            def num_clusters():
                return f"{input.slider_cluster()}"


    with ui.nav_panel("Generated Playlists"):
         "Page D content"



    


# @render.plot(alt="A histogram")
# def histogram():
#     np.random.seed(19680801)
#     x = 100 + 15 * np.random.randn(437)
#     plt.hist(x, input.n(), density=True)

# @reactive.calc
# def dat():
#     infile = Path(__file__).parent / "2_spotify_10_songs.csv"
#     return pandas.read_csv(infile)


# with ui.navset_card_underline():

#     with ui.nav_panel("Data frame"):
#         @render.data_frame
#         def frame():
#             # Give dat() to render.DataGrid to customize the grid
#             return dat()

#     with ui.nav_panel("Table"):
#         @render.table
#         def table():
#             return dat()