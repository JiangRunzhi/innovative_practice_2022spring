import psycopg2
import json

database = ""
user = ""
password = ""
host = ""
port = ""


class Database:
    def __init__(self):
        file = open("sql/jsons/db.json")
        config = json.load(file)
        file.close()
        database = config["pgsql"]["database"]
        user = config["pgsql"]["user"]
        password = config["pgsql"]["password"]
        host = config["pgsql"]["host"]
        port = config["pgsql"]["port"]
        self.connect = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        self.cursor = self.connect.cursor()
        self.__init_province()
        self.__init_tools()
        self.__init_source()

    def __init_province(self):
        file = open("sql/jsons/province.json", encoding="utf-8")
        self.province = json.load(file)
        file.close()

    def __init_tools(self):
        file = open("sql/jsons/tools.json", encoding="utf-8")
        self.tools = json.load(file)
        file.close()

    def __init_source(self):
        file = open("sql/jsons/source.json", encoding="utf-8")
        self.source = json.load(file)
        file.close()

    def single_execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            return self.cursor.fetchall()
        except Exception as e:
            self.connect.rollback()
            print(e)


    def mutiple_execute_sql(self, sql, values):
        try:
            self.cursor.executemany(sql, values)
            self.connect.commit()
            return self.cursor.fetchall()
        except Exception as e:
            self.connect.rollback()
            print(e)


    def insert_text(self, content: str, topoc_id, ip, source_id, time : str):
        if (content) == None or len(content) == 0:
            raise Exception("content cann't be NULL")
        sql = "insert into text(content,topic_id, ip, source_id, time) \
                values (%s, %s, %s, %s, %s)"
        self.single_execute_sql(sql)

    def insert_texts(self, list_values : list):
        sql = "insert into text(content,topic_id, ip, source_id, time) \
                values (%s, %s, %s, %s, %s)"
        self.mutiple_execute_sql(sql, list_values)

    def insert_result_for_topic(self, list_values : list):
        sql = "insert into result_for_topic(result, province_id, topic_id, analysis_id, source_id) \
                values (%s, %s, %s, %s, %s)"
        self.mutiple_execute_sql(sql, list_values)