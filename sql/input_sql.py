from sql.database import Database
import pandas as pd
import json
import os

class InputTool:
    def __init__(self):
        self.db = Database()
        self.result_list = []

    def log_result(self, result, province, topic, analysis, source):
        province_id = self.db.province[province]
        topic_id = topic
        analysis_id = self.db.tools[analysis]
        source_id = self.db.source[source]
        self.result_list.append((result, province_id, topic_id, analysis_id, source_id))


    def finish_log(self):
        self.db.insert_result_for_topic(self.result_list)
        self.result_list = []



if __name__ == '__main__':
    db = Database()
    file = open("sql/jsons/input.json")
    inputs = json.load(file)
    file_head = inputs["file_head"]
    data_files = inputs["data_files"]
    for file_name in data_files:
        df = pd.read_csv(file_head + os.path.sep +  file_name)
        print(df.info())
        df.dropna(axis=0, how='all', subset=df.columns[[1]], inplace=True)
        print(df.info())
        list_values = []
        for index, row in df.iterrows():
            list_values.append((str(row['text']), None, None, None, str(row['time'])))
        db.insert_texts(list_values)
        # print(dataframe)