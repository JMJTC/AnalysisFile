import tkinter as tk
from tkinter import filedialog, ttk, messagebox, simpledialog
import pandas as pd
from matplotlib import pyplot as plt
from db_handler import DatabaseHandler


class FileAnalysisWindow:
    def __init__(self, master, username, userid):
        self.master = master
        self.master.title(f"{username}.{userid} 的文件数据分析")
        self.db_handler = DatabaseHandler()

        self.create_widgets()

    def create_widgets(self):
        tk.Button(self.master, text="选择文件", command=self.load_file).pack()
        self.tree = ttk.Treeview(self.master, columns=("A", "B", "C", "D"), show='headings')
        self.tree.heading("A", text="字段A")
        self.tree.heading("B", text="字段B")
        self.tree.heading("C", text="字段C")
        self.tree.heading("D", text="字段D")
        self.tree.pack()

        tk.Button(self.master, text="保存到数据库", command=self.save_to_db).pack()
        tk.Button(self.master, text="筛选数据", command=self.filter_data).pack()
        tk.Button(self.master, text="数据统计", command=self.show_statistics).pack()

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xls *.xlsx")])
        if file_path:
            self.data = pd.read_excel(file_path)
            self.display_data(self.data)

    def display_data(self, data):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for _, row in data.iterrows():
            self.tree.insert("", "end", values=list(row))

    def save_to_db(self):
        self.db_handler.save_data(self.data)
        messagebox.showinfo("保存成功", "数据已保存到数据库")

    def filter_data(self):
        field1 = simpledialog.askstring("筛选条件", "请输入字段1的筛选条件 (例如: value1):")
        field2 = simpledialog.askstring("筛选条件", "请输入字段2的筛选条件 (例如: value2):")

        conditions = []
        if field1:
            conditions.append(f"field1='{field1}'")
        if field2:
            conditions.append(f"field2='{field2}'")

        if conditions:
            filtered_data = self.db_handler.filter_data(conditions)
            self.display_data(pd.DataFrame(filtered_data, columns=["id", "field1", "field2", "field3", "field4"]))
        else:
            messagebox.showinfo("无条件", "没有输入任何筛选条件")

    def show_statistics(self):
        index = ['1_2024ACP世界大赛中国赛区省级赛入围名单', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3',
                 'Unnamed: 4', 'Unnamed: 5']
        print(self.data.columns)
        plt.figure(figsize=(6, 4))
        for i, column in enumerate(self.data.columns):
            plt.subplot(2, 3, i+1)
            self.data[column].value_counts().plot(kind='bar')
            plt.title(index[i])

        plt.tight_layout()
        plt.show()

        # self.data['Unnamed: 1'].value_counts().plot(kind='bar')
        # plt.show()

    def on_closing(self):
        self.db_handler.close()
        self.master.destroy()
