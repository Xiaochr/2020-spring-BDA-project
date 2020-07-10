from pyecharts import options as opts
from pyecharts.charts import Timeline
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


track_list = [[("Hannover", "Bremen"), ("Bremen", "Hannover"), ("Hamburg", "Hannover"), 
                ("Mainz", "Frankfurt"), ("Frankfurt", "Koeln"), ("Koeln", "Frankfurt")], 
            [("Hannover", "Berlin"), ("Hannover", "Bremen"), ("Bremen", "Hannover"), 
                ("Bremen", "Hamburg"), ("Hamburg", "Hannover"), ("Mainz", "Frankfurt"), 
                ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), ("Koeln", "Frankfurt")], 
            [("Berlin", "Hannover"), ("Hannover", "Berlin"), ("Hannover", "Bremen"), 
                ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Bremen", "Koeln"), 
                ("Hamburg", "Hannover"), ("Mainz", "Frankfurt"), ("Frankfurt", "Berlin"), 
                ("Frankfurt", "Hannover"), ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), 
                ("Frankfurt", "Koeln"), ("Koeln", "Stuttgart")], 
            [("Berlin", "Hannover"), ("Hannover", "Berlin"), ("Hannover", "Bremen"), 
                ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Bremen", "Koeln"), 
                ("Hamburg", "Hannover"), ("Mainz", "Koeln"), ("Muechen", "Stuttgart"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln")], 
            [("Berlin", "Hannover"), ("Hannover", "Berlin"), ("Hannover", "Bremen"), 
                ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Hamburg", "Hannover"), 
                ("Mainz", "Koeln"), ("Frankfurt", "Berlin"), ("Frankfurt", "Hannover"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Koeln", "Frankfurt"), ("Koeln", "Stuttgart")], 
            [("Berlin", "Hannover"), ("Berlin", "Hamburg"), ("Hannover", "Berlin"), 
                ("Hannover", "Bremen"), ("Stuttgart", "Frankfurt"), ("Bremen", "Hannover"), 
                ("Bremen", "Hamburg"), ("Hamburg", "Hannover"), ("Frankfurt", "Hannover"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Koeln", "Frankfurt")], 
            [("Berlin", "Hannover"), ("Berlin", "Hamburg"), ("Hannover", "Berlin"), 
                ("Hannover", "Bremen"), ("Stuttgart", "Frankfurt"), ("Bremen", "Hannover"), 
                ("Bremen", "Hamburg"), ("Hamburg", "Berlin"), ("Hamburg", "Hannover"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Frankfurt", "Berlin"), ("Koeln", "Stuttgart"), ("Koeln", "Mainz")], 
            [("Berlin", "Hannover"), ("Berlin", "Hamburg"), ("Hannover", "Berlin"), 
                ("Hannover", "Bremen"), ("Stuttgart", "Muechen"), ("Stuttgart", "Frankfurt"), 
                ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Hamburg", "Berlin"), 
                ("Hamburg", "Hannover"), ("Hamburg", "Koeln"), ("Frankfurt", "Hannover"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Koeln", "Hamburg"), ("Koeln", "Mainz"), ("Koeln", "Frankfurt")], 
            [("Berlin", "Hannover"), ("Berlin", "Hamburg"), ("Hannover", "Berlin"), 
                ("Hannover", "Bremen"), ("Bremen", "Hannover"), ("Bremen", "Hamburg"), 
                ("Hamburg", "Berlin"), ("Hamburg", "Hannover"), ("Muechen", "Stuttgart"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Frankfurt", "Berlin"), ("Koeln", "Frankfurt")], 
            [("Berlin", "Hannover"), ("Berlin", "Hamburg"), ("Hannover", "Berlin"), 
                ("Stuttgart", "Frankfurt"), ("Bremen", "Hannover"), ("Bremen", "Hamburg"), 
                ("Hamburg", "Hannover"), ("Muechen", "Stuttgart"), ("Frankfurt", "Hannover"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Koeln", "Mainz"), ("Koeln", "Frankfurt"), ("Dresden", "Berlin")], 
            [("Berlin", "Hamburg"), ("Hannover", "Berlin"), ("Stuttgart", "Frankfurt"), 
                ("Bremen", "Hannover"), ("Bremen", "Hamburg"), ("Hamburg", "Berlin"), 
                ("Hamburg", "Hannover"), ("Muechen", "Stuttgart"), ("Frankfurt", "Hannover"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), 
                ("Frankfurt", "Berlin"), ("Koeln", "Mainz"), ("Koeln", "Stuttgart")], 
            [("Berlin", "Hamburg"), ("Hannover", "Berlin"), ("Stuttgart", "Frankfurt"), 
                ("Bremen", "Hannover"), ("Hamburg", "Berlin"), ("Hamburg", "Hannover"), 
                ("Mainz", "Stuttgart"), ("Muechen", "Stuttgart"), 
                ("Frankfurt", "Stuttgart"), ("Frankfurt", "Mainz"), ("Frankfurt", "Koeln"), ]]



tl = Timeline()
for i in range(9, 21):
    geo0 = (
        Geo()
        .add_schema(maptype="德国")
        .add_coordinate_json(json_file="./data/city_coor.json")
        .add(
            "",
            [("Berlin", 1), ("Frankfurt", 1), ("Muechen", 1), 
            ("Hamburg", 1), ("Bremen", 1), ("Dresden", 1), 
            ("Hannover", 1), ("Koeln", 1), ("Mainz", 1), ("Stuttgart", 1)],
            type_=ChartType.EFFECT_SCATTER,
            color="blue",
        )
        .add(
            "ICE tracks",
            track_list[i-9],
            type_=ChartType.LINES,
            symbol_size = 6,
            effect_opts=opts.EffectOpts(
                symbol=SymbolType.ARROW, symbol_size=6, color="blue"
            ),
            linestyle_opts=opts.LineStyleOpts(curve=0.2),
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(title_opts=opts.TitleOpts(title="ICE Tracks during %d-%d Time Period"%(i, i+3)))
    )
    
    tl.add(geo0, "%d-%d"%(i, i+3))
tl.render("./results/timeline_map.html")
