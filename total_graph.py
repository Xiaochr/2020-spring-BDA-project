from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType

geo = (
    Geo()
    .add_schema(maptype="德国")
    .add_coordinate_json(json_file="./data/city_coor.json")
    .add(
        "",
        [("Berlin", 57), ("Frankfurt", 61), ("Muechen", 16), 
        ("Hamburg", 35), ("Bremen", 29), ("Dresden", 10), 
        ("Hannover", 58), ("Koeln", 26), ("Mainz", 15), ("Stuttgart", 19)],
        type_=ChartType.EFFECT_SCATTER,
        symbol_size = 10,
        color="blue",
    )
    .add(
        "ICE tracks",
        [("Frankfurt", "Koeln"), ("Frankfurt", "Berlin"), ("Frankfurt", "Stuttgart"), 
        ("Frankfurt", "Hannover"), ("Frankfurt", "Hamburg"), ("Frankfurt", "Dresden"), 
        ("Frankfurt", "Mainz"), ("Koeln", "Frankfurt"), ("Koeln", "Stuttgart"), 
        ("Koeln", "Hamburg"), ("Koeln", "Mainz"), 
        ("Muechen", "Berlin"), ("Muechen", "Stuttgart"), ("Muechen", "Hamburg"), 
        ("Berlin", "Frankfurt"), ("Berlin", "Hamburg"), ("Berlin", "Hannover"), 
        ("Berlin", "Bremen"), ("Hannover", "Berlin"), ("Hannover", "Bremen"), 
        ("Hannover", "Dresden"), ("Stuttgart", "Muechen"), ("Stuttgart", "Frankfurt"), 
        ("Hamburg", "Berlin"), ("Hamburg", "Hannover"), ("Hamburg", "Koeln"), 
        ("Bremen", "Stuttgart"), ("Dresden", "Berlin"), 
        ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Bremen", "Mainz"), 
        ("Bremen", "Frankfurt"), ("Bremen", "Koeln"), 
        ("Mainz", "Frankfurt"), ("Mainz", "Stuttgart"), ("Mainz", "Koeln")],
        type_=ChartType.LINES,
        symbol_size = 6,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="blue"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="ICE Daily Graph"))
    .render("./results/total_track_graph.html")
)



