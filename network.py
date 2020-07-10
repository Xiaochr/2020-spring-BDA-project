import pandas as pd 
import numpy as np 
import networkx as nx
from networkx.algorithms.centrality import closeness_centrality, betweenness_centrality
from networkx.algorithms.distance_measures import center


class DataTransformer(object):
    def __init__(self, file_path="./data/I.xlsx"):
        self.raw_data = pd.read_excel(file_path, encoding="UTF-8")
        self.data = self.raw_data.drop_duplicates(subset=["TIN", "TIM"])
        self.data.index = range(0, self.data.shape[0])
        self.city_list = list(self.data["TSC"].drop_duplicates())
        
    def transform(self):
        self.adj_mat = pd.DataFrame(np.zeros((10, 10)), columns=self.city_list, index=self.city_list)
        for i in range(0, self.data.shape[0]-1):
            if self.data.loc[i, "TIN"] == self.data.loc[i+1, "TIN"] and self.data.loc[i, "TSC"] != self.data.loc[i+1, "TSC"]:
                self.adj_mat.loc[self.data.loc[i, "TSC"], self.data.loc[i+1, "TSC"]] += 1
        self.adj_mat.to_csv("./results/network_mat_I.csv")

    def transform_delayed(self):
        adj_mat = pd.DataFrame(np.zeros((10, 10)), columns=self.city_list, index=self.city_list)
        for i in range(0, self.data.shape[0]-1):
            if self.data.loc[i, "TIN"] == self.data.loc[i+1, "TIN"] and self.data.loc[i, "TSC"] != self.data.loc[i+1, "TSC"]:
                adj_mat.loc[self.data.loc[i, "TSC"], self.data.loc[i+1, "TSC"]] += (self.data.loc[i, "TAc"]+self.data.loc[i+1, "TAc"])
        #print(self.adj_mat)
        adj_mat.to_csv("./results/network_mat_I_delayed.csv")

    def transform_by_time(self, time=9):
        adj_mat = pd.DataFrame(np.zeros((10, 10)), columns=self.city_list, index=self.city_list)
        data = self.data.loc[self.data["TP"] >= time]
        data = data.loc[data["TP"] <= time+3]
        data.index = range(0, data.shape[0])
        for i in range(0, data.shape[0]-1):
            if data.loc[i, "TIN"] == data.loc[i+1, "TIN"] and data.loc[i, "TSC"] != data.loc[i+1, "TSC"]:
                adj_mat.loc[data.loc[i, "TSC"], data.loc[i+1, "TSC"]] += 1
        return adj_mat
        
    def save_data_by_time(self):
        for t in range(9, 21):
            adj_mat = self.transform_by_time(time=t)
            adj_mat.to_csv("./results/time_mat/mat_%d-%d.csv"%(t, t+3))
            print("data saved. ")



class NetworkGraph(object):
    def __init__(self, file_path="./results/network_mat_I.csv"):
        self.mat = pd.read_csv(file_path, index_col=0)
        self.G = nx.from_pandas_adjacency(self.mat, create_using=nx.DiGraph)

    def get_centralities(self):
        c_d = self.G.degree(weight="weight")
        print(c_d)
        #print(self.G.in_degree(weight="weight"))
        #print(self.G.out_degree(weight="weight"))
        c_b = betweenness_centrality(self.G, weight="weight")
        print(c_b)
        c_c = closeness_centrality(self.G)
        print(c_c)


def run_network():
    data = DataTransformer()
    data.transform()
    data.transform_delayed()
    data.save_data_by_time()
    nw = NetworkGraph()
    nw.get_centralities()
    nw1 = NetworkGraph(file_path="./results/network_mat_I_delayed.csv")
    nw1.get_centralities()


if __name__ == "__main__":
    run_network()

