import pandas as pd 
import numpy as np 
import os


class Preprocessor(object):
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, encoding="UTF-8")
        self.data = self.data.drop(["TIL"], axis=1)
        self.data = self.data.loc[self.data["TAc"] >= 0]
        self.data = self.data.drop_duplicates()
        self.delayed_data = self.data.dropna()

    def get_num(self):
        total_num = self.data.shape[0]
        self.arr_data = self.data.loc[self.data["TIM"] == "arr"]
        self.dep_data = self.data.loc[self.data["TIM"] == "dep"]
        arr_num = self.arr_data.shape[0]
        dep_num = self.dep_data.shape[0]
        return total_num, arr_num, dep_num

    def get_delay_num(self):
        delay_total_num = self.delayed_data.shape[0]
        self.delayed_arr = self.delayed_data.loc[self.delayed_data["TIM"] == "arr"]
        self.delayed_dep = self.delayed_data.loc[self.delayed_data["TIM"] == "dep"]
        delay_arr_num = self.delayed_arr.shape[0]
        delay_dep_num = self.delayed_dep.shape[0]
        return delay_total_num, delay_arr_num, delay_dep_num

    def get_delay_type_num(self):
        delay_type = self.delayed_data["TIN"].drop_duplicates()
        self.delayed_type_data = self.delayed_data.loc[delay_type.index]
        self.delayed_arr_type = self.delayed_type_data.loc[self.delayed_data["TIM"] == "arr"]
        self.delayed_dep_type = self.delayed_type_data.loc[self.delayed_data["TIM"] == "dep"]
        delay_type_num = self.delayed_type_data.shape[0]
        delay_arr_type_num = self.delayed_arr_type.shape[0]
        delay_dep_type_num = self.delayed_dep_type.shape[0]
        return delay_type_num, delay_arr_type_num, delay_dep_type_num

    def get_delay_time(self):
        total_delayed_time = sum(self.delayed_data["TAc"])
        return total_delayed_time, total_delayed_time/self.delayed_data.shape[0]

    def groupby_time(self, data):
        df = data
        df["TP"] = df["TIT"].apply(lambda x: x[0:2])
        df_grouped = df.groupby("TP")
        return df_grouped.count().iloc[:, 1:3]

    def groupby_type(self):
        df1 = self.data
        df1["Type"] = df1["TIN"].apply(lambda x: x[0])
        df1_grouped = df1.groupby("Type")
        I_num = list(df1_grouped.count().loc["I"][0:2])
        S_num = list(df1_grouped.count().loc["S"][0:2])
        R_num = list(df1_grouped.count().loc["R"][0:2])
        temp_list = I_num
        temp_list.extend(S_num)
        temp_list.extend(R_num)
        return temp_list
    
    def get_I_data(self):
        df1 = self.data
        df1["Type"] = df1["TIN"].apply(lambda x: x[0])
        df1 = df1.loc[df1["Type"] == "I"]
        return df1

    def get_error_info(self):
        error_info = self.delayed_data["TAA"]
        error_info = error_info.loc[error_info != " "]
        #temp = error_info.groupby(error_info)
        #print(temp.count())
        return error_info


def save_delayed_data(file_path="./DB_data"):
    num_data = pd.DataFrame([])
    for file_name in os.listdir(file_path):
        if file_name.endswith(".csv"):
            city = Preprocessor(os.path.join(file_path, file_name))
            temp = list(city.get_num())
            temp.extend(list(city.get_delay_num()))
            temp.extend(list(city.get_delay_type_num()))
            temp.extend(list(city.get_delay_time()))
            temp = pd.DataFrame(temp)
            temp = temp.rename({0:file_name[17:]}, axis="columns")
            num_data = pd.concat([num_data, temp], axis=1)
    #print(num_data)
    num_data = num_data.T
    num_data.to_csv("./results/num_data.csv")
    print("data saved. ")


def save_time_data(file_path="./DB_data"):
    time_data = pd.DataFrame([])
    for file_name in os.listdir(file_path):
        if file_name.endswith(".csv"):
            city = Preprocessor(os.path.join(file_path, file_name))
            temp = city.groupby_time(data=city.data)
            temp = temp.rename({"TA":file_name[17:]+"_TA", "TIN":file_name[17:]+"_TIN"}, axis="columns")
            time_data = pd.concat([time_data, temp], axis=1)
    #print(time_data)
    time_data.to_csv("./results/time_data.csv")
    print("data saved. ")


def save_type_data(file_path="./DB_data"):
    type_data = pd.DataFrame([])
    for file_name in os.listdir(file_path):
        if file_name.endswith(".csv"):
            city = Preprocessor(os.path.join(file_path, file_name))
            temp = city.groupby_type()
            temp = pd.DataFrame(temp)
            temp = temp.rename({0:file_name[17:]}, axis="columns")
            type_data = pd.concat([type_data, temp], axis=1)
    #print(type_data)
    type_data = type_data.T
    type_data.to_csv("./results/type_data.csv")
    print("data saved. ")


def save_error_info(file_path="./DB_data"):
    error_data = pd.DataFrame([])
    for file_name in os.listdir(file_path):
        if file_name.endswith(".csv"):
            city = Preprocessor(os.path.join(file_path, file_name))
            temp = city.get_error_info()
            error_data = pd.concat([error_data, temp], axis=0)
    error_data = error_data.rename({0:"TAA"}, axis="columns")
    error_count = error_data["TAA"].groupby(error_data["TAA"]).count()
    #print(error_count)
    error_count.to_csv("./results/error_data.csv")
    print("data saved. ")


def save_I_time_data(file_path="./DB_data"):
    time_data = pd.DataFrame([])
    full_data = pd.DataFrame([])
    for file_name in os.listdir(file_path):
        if file_name.endswith(".csv"):
            city = Preprocessor(os.path.join(file_path, file_name))
            full_I_data = city.get_I_data()
            full_I_data["TP"] = full_I_data["TIT"].apply(lambda x: x[0:2])
            full_I_data.to_csv("./results/I_data/I_"+file_name[17:])
            print("saved")
            full_data = pd.concat([full_data, full_I_data], axis=0)
            full_I_data = full_I_data.drop_duplicates(subset=["TIN", "TIM"])
            temp = city.groupby_time(data=full_I_data)
            temp = temp.rename({"TA":file_name[17:]+"_TA", "TIN":file_name[17:]+"_TIN"}, axis="columns")
            time_data = pd.concat([time_data, temp], axis=1)
    #print(time_data)
    full_data.to_csv("./results/full_I_data.csv")
    time_data.to_csv("./results/I_time_data.csv")
    print("data saved. ")

def run_preprocessing():
    temp = Preprocessor("./DB_data/19.06.20_travels_Frankfurt.csv")
    save_delayed_data()
    save_time_data()
    save_type_data()
    save_error_info()
    save_I_time_data()

if __name__ == "__main__":
    run_preprocessing()

