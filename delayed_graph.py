from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

geo = (
    Geo()
    .add_schema(maptype="德国")
    .add_coordinate_json(json_file="./data/city_coor.json")
    .add(
        "",
        [("Berlin", 121), ("Frankfurt", 213), ("Muechen", 106), 
        ("Hamburg", 88), ("Bremen", 6), ("Dresden", 11), 
        ("Hannover", 136), ("Koeln", 110), ("Mainz", 34), ("Stuttgart", 68)],
        type_=ChartType.EFFECT_SCATTER,
        symbol_size = 10,
        color="blue",
    )
    .add(
        "ICE tracks",
        [("Berlin", "Hamburg"), ("Berlin", "Frankfurt"), ("Hannover", "Berlin"), 
        ("Hannover", "Bremen"), ("Hannover", "Dresden"), ("Stuttgart", "Frankfurt"), 
        ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Bremen", "Mainz"), 
        ("Bremen", "Frankfurt"), ("Bremen", "Koeln"), ("Hamburg", "Berlin"), 
        ("Hamburg", "Hannover"), ("Hamburg", "Koeln"), ("Mainz", "Stuttgart"), 
        ("Mainz", "Koeln"), ("Muechen", "Berlin"), ("Muechen", "Stuttgart"), 
        ("Frankfurt", "Koeln"), ("Frankfurt", "Berlin"), ("Frankfurt", "Stuttgart"), 
        ("Frankfurt", "Hannover"), ("Frankfurt", "Dresden"), ("Frankfurt", "Mainz"), 
        ("Koeln", "Stuttgart"), ("Koeln", "Hamburg"), ("Koeln", "Mainz"), 
        ("Koeln", "Frankfurt")],
        type_=ChartType.LINES,
        symbol_size = 6,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="blue"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="Delayed ICE Daily Graph"))
    .render("./results/delayed_track_graph.html")
)



