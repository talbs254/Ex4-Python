from tkFileDialog import askopenfilename

from tkinter import *
from tkinter import messagebox
import plotly.plotly as py
from PIL import ImageTk, Image
import os.path


# packages:
# pip install image

class View():
    def __init__(self):
        self.root = Tk()
        self.root.title("K Mean Clustering by: Tal and Maor")
        self.data_path_entry = Entry(self.root)
        self.num_of_clusters_entry = Entry(self.root)
        self.num_of_runs_entry = Entry(self.root)
        self.data_path_entry['width'] = 100
        data_path_lbl = Label(self.root, text="Data Path: ", bg="blue", fg="white")
        data_path_browse_btn = Button(self.root, text="browse", command=self.browse_data)
        data_path_lbl.grid(row=0, column=0, sticky=W)
        self.data_path_entry.grid(row=0, column=1, sticky=W)
        data_path_browse_btn.grid(row=0, column=2, sticky=W)
        num_of_clusters_lbl = Label(self.root, text="Num of clusters k: ", bg="blue", fg="white")
        num_of_clusters_lbl.grid(row=1, column=0, sticky=W)
        self.num_of_clusters_entry.grid(row=1, column=1, sticky=W)
        num_of_runs_lbl = Label(self.root, text="Num of runs: ", bg="blue", fg="white")
        num_of_runs_lbl.grid(row=2, column=0, sticky=W)
        self.num_of_runs_entry.grid(row=2, column=1, sticky=W)
        preprocess_btn = Button(self.root, text="Pre-process", command=self.preprocess_data)
        preprocess_btn.grid(row=3, column=1, sticky=W)
        cluster_btn = Button(self.root, text="Cluster", command=self.cluster_data)
        cluster_btn.grid(row=4, column=1, sticky=W)
        self.choromap_img_lbl = Label(self.root)
        self.choromap_img_lbl.grid(row=5, column=1)
        self.scatter_img_lbl = Label(self.root)
        self.scatter_img_lbl.grid(row=5, column=2)

    def start(self):
        '''
        start the user interface
        '''
        self.root.mainloop()

    def preprocess_data(self):
        data_path = self.data_path_entry.get()
        if not os.path.isfile(data_path):
            self.pop_alert("data file was not found")
        else:
            self.pop_alert("preprocess now")
        pass

    def cluster_data(self):
        clusters_entry_get = self.num_of_clusters_entry.get()
        runs_entry_get = self.num_of_runs_entry.get()
        if not clusters_entry_get.isdigit() or int(clusters_entry_get) <= 0:
            self.pop_alert("'Num of clusters k' field must be an Positive Integer")

        elif not runs_entry_get.isdigit() or int(runs_entry_get) <= 0:
            self.pop_alert("'Num of runs' field must be an Positive Integer")
        else:
            num_of_clusters = int(clusters_entry_get)
            self.pop_alert("cluster now")
            self.choromap_img = ImageTk.PhotoImage(Image.open("newplot.png"))
            self.choromap_img_lbl['image'] = self.choromap_img
            self.scatter_img = ImageTk.PhotoImage(Image.open("life-expectancy-vs-gdp-per-capita.png"))
            self.scatter_img_lbl['image'] = self.scatter_img

    def pop_alert(self, msg):
        '''
        display alert for upload file
        '''
        messagebox.showinfo(title="K Mean Clustering", message=msg)

    def browse_data(self):
        '''
        ask the query file directory
        '''
        dir_path = askopenfilename(filetypes=[("Xlsx files", "*.xlsx"), ("Csv files", "*.csv")])
        self.data_path_entry.delete(0, len(self.data_path_entry.get()))
        self.data_path_entry.insert(0, dir_path)


v = View()
v.start()
