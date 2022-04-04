import plotly.express as px
import os
import hvplot.pandas



map_box_api = os.getenv("mapbox")
px.set_mapbox_access_token(map_box_api)

def create_scatter_plot(data, size="size", lat="lat", lon="lon", color="color", hover_data=[], hover_name="", zoom=3, mapbox_style="open-street-map"):
    fig = px.scatter_mapbox(
        data,
        size=size,
        lat=lat,
        lon=lon,
        color=color,
        hover_data=hover_data,
        hover_name=hover_name,
        zoom=zoom
    )
    fig.update_layout(mapbox_style=mapbox_style)
    return fig

def create_bar_chart(data,x="x",y="y",xlabel="xlabel",ylabel="ylabel",rot=90):
    return  data.hvplot(kind="bar",x=x, y=y, xlabel=xlabel, ylabel=ylabel, rot=rot)
