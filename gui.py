import os.path
from tkFileDialog import askopenfilename
from Tkinter import *
import tkMessageBox as messagebox
from clustering_model import ClusteringModel
from plot_generator import PlotGenerator
from PIL import ImageTk, Image
# python -m pip install --upgrade pillow (for images need latest verision)

class View():
    def __init__(self):
        self.model = None
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
        """
        Active preprocess logic
        """
        data_path = self.data_path_entry.get()
        try:
            if not os.path.isfile(data_path):
                self.pop_alert("data file was not found")
            else:
                self.pop_alert("preprocess now")
                self.model = ClusteringModel(data_path)
                self.model.preprocess()
                self.pop_alert("preprocess done!!!")
        except Exception as e:
            self.pop_alert("Data file is not correct or corrupted done!!!")

    def cluster_data(self):
        """
        Active k-mean clustering logic and represent graphs on gui using PlotGenerator class.
        """
        try:
            clusters_entry_get = self.num_of_clusters_entry.get()
            runs_entry_get = self.num_of_runs_entry.get()
            if not clusters_entry_get.isdigit() or int(clusters_entry_get) <= 0:
                self.pop_alert("'Num of clusters k' field must be an Positive Integer")

            elif not runs_entry_get.isdigit() or int(runs_entry_get) <= 0:
                self.pop_alert("'Num of runs' field must be an Positive Integer")

            elif self.model is None:
                self.pop_alert("you need to preprocess the data")
            else:
                num_of_clusters = int(clusters_entry_get)
                n_runs = int(runs_entry_get)
                self.pop_alert("cluster now")

                cluster_result = self.model.k_means(num_of_clusters, n_runs)
                plot_generator = PlotGenerator()
                plot_generator.generate_scatter_plot_image(cluster_result)
                plot_generator.generate_choromap_image(cluster_result)
                self.choromap_img = ImageTk.PhotoImage(Image.open("map_plot.png"))
                self.choromap_img_lbl['image'] = self.choromap_img
                self.scatter_img = ImageTk.PhotoImage(Image.open("scatter_plot.png"))
                self.scatter_img_lbl['image'] = self.scatter_img
                self.pop_alert("cluster done!!!")
        except Exception as e:
            self.pop_alert("Data file missing one of the following ( 'Country','Social support', 'Generosity')!!!")

    def pop_alert(self, msg):
        '''
        display 'msg' alert
        '''
        messagebox.showinfo(title="K Mean Clustering", message=msg)

    def browse_data(self):
        '''
        ask the query excel file
        '''
        dir_path = askopenfilename(filetypes=[("Xlsx files", "*.xlsx"), ("Csv files", "*.csv")])
        self.data_path_entry.delete(0, len(self.data_path_entry.get()))
        self.data_path_entry.insert(0, dir_path)


# Run the application
v = View()
v.start()
