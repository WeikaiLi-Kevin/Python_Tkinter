"""
Description: set up the GUI in Tkinter and load data from readCSVFile

---------------------
@author: Weikai Li
Last modify date: 31 Jan, 2018
"""
from tkinter import *
from tkinter.ttk import *
import readCSVFile as readCSVFile


class App(Frame):

    def __init__(self, parent):
        """
        Constructor
        :param parent: call parent constructor
        """
        Frame.__init__(self, parent)

        self.create_UI()
        self.load_data()
        self.insert_button()
        self.delete_button()
        self.grid(column=2, row=0,sticky=(N, S, W, E))
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        self.text_ref_date = Text()
        self.text_geo = Text()
        self.text_commod = Text()
        self.text_vector = Text()
        self.text_coordinate = Text()
        self.text_value = Text()
        self.text_id = Text()

    def create_UI(self):
        """
        This function creates a table format including heading on the GUI
        """
        self.winfo_toplevel().title("Weikai Li")
        tv = Treeview(self)
        # create scrollbar
        vsb = Scrollbar(orient="vertical", command=tv.yview)
        tv.configure(yscrollcommand=vsb.set)
        vsb.grid(column=1, row=0, sticky=(N, S, W, E))
        # create treeview columns with column names
        tv['columns'] = ('Ref_Date', 'GEO', 'COMMOD', 'Vector', 'Coordinate', 'Value')
        tv.heading("#0", text='id', anchor='center')
        tv.column("#0", anchor="center", width=100)
        tv.heading('Ref_Date', text='Ref_Date')
        tv.column('Ref_Date', anchor='center', width=100)
        tv.heading('GEO', text='GEO')
        tv.column('GEO', anchor='center', width=100)
        tv.heading('COMMOD', text='COMMOD')
        tv.column('COMMOD', anchor='center', width=100)
        tv.heading('Vector', text='Vector')
        tv.column('Vector', anchor='center', width=100)
        tv.heading('Coordinate', text='Coordinate')
        tv.column('Coordinate', anchor='center', width=100)
        tv.heading('Value', text='Value')
        tv.column('Value', anchor='center', width=100)
        tv.grid(column=0, row=0,sticky=(N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def insert_button(self):
        """
        This function is used to create a button to pop up a new window to insert data into GUI
        """
        button = Button(self, text="create data", command=self.create_insert_window)
        button.grid(row=0, column=3,sticky=(N, S, W, E))

    def delete_button(self):
        """
        This function is used to create a button to pop up a new window to delete data into GUI
        """
        button = Button(self, text="delete selected data", command=self.delete_data)
        button.grid(row=0, column=4,sticky=(N, S, W, E))

    def load_data(self):
        """
        This function is used to load the data in the CSV file to the table on the GUI
        """
        csv_file = readCSVFile.ReadFile()
        ref_date = csv_file.get_ref_date()
        geo = csv_file.get_geo()
        commond = csv_file.get_commond()
        coordinate = csv_file.get_coordinate()
        value = csv_file.get_value()
        vector = csv_file.get_vector()
        for i in range(len(ref_date)):
            self.text = i
            self.treeview.insert('', 'end', text=self.text, values=(ref_date[i], geo[i], commond[i], vector[i], coordinate[i], value[i]))

    def create_insert_window(self):
        """
        This function is used to add labels and textboxes to the new window for user to insert data
        """
        window = Toplevel(self)
        label_ref_date = Label(window, text="Ref_Date: ")
        label_ref_date.grid(row=0, column=0, sticky=(N, S, W, E))
        self.text_ref_date = Text(window,height = 1, width = 30)
        self.text_ref_date.grid(row=0, column=1, sticky=(N, S, W, E))
        label_geo = Label(window, text="GEO: ")
        label_geo.grid(row=1, column=0, sticky=(N, S, W, E))
        self.text_geo = Text(window,height = 1, width = 30)
        self.text_geo.grid(row=1, column=1, sticky=(N, S, W, E))
        label_commod = Label(window, text="COMMOD: ")
        label_commod.grid(row=2, column=0, sticky=(N, S, W, E))
        self.text_commod = Text(window,height = 1, width = 30)
        self.text_commod.grid(row=2, column=1, sticky=(N, S, W, E))
        label_vector = Label(window, text="Vector: ")
        label_vector.grid(row=3, column=0, sticky=(N, S, W, E))
        self.text_vector = Text(window,height = 1, width = 30)
        self.text_vector.grid(row=3, column=1, sticky=(N, S, W, E))
        label_coordinate = Label(window, text="Coordinate: ")
        label_coordinate.grid(row=4, column=0, sticky=(N, S, W, E))
        self.text_coordinate = Text(window,height = 1, width = 30)
        self.text_coordinate.grid(row=4, column=1, sticky=(N, S, W, E))
        label_value = Label(window, text="Value: ")
        label_value.grid(row=5, column=0, sticky=(N, S, W, E))
        self.text_value = Text(window,height = 1, width = 30)
        self.text_value.grid(row=5, column=1, sticky=(N, S, W, E))
        insert_button = Button(window, text='insert', command=self.insert_data)
        insert_button.grid(row=5, column=2, sticky=(N, S, W, E))

    def create_insert_window(self):
        """
        This function is used to add labels and textboxes to the new window for user to insert data
        """
        window = Toplevel(self)
        label_ref_date = Label(window, text="Ref_Date: ")
        label_ref_date.grid(row=0, column=0, sticky=(N, S, W, E))
        self.text_ref_date = Text(window,height = 1, width = 30)
        self.text_ref_date.grid(row=0, column=1, sticky=(N, S, W, E))
        label_geo = Label(window, text="GEO: ")
        label_geo.grid(row=1, column=0, sticky=(N, S, W, E))
        self.text_geo = Text(window,height = 1, width = 30)
        self.text_geo.grid(row=1, column=1, sticky=(N, S, W, E))
        label_commod = Label(window, text="COMMOD: ")
        label_commod.grid(row=2, column=0, sticky=(N, S, W, E))
        self.text_commod = Text(window,height = 1, width = 30)
        self.text_commod.grid(row=2, column=1, sticky=(N, S, W, E))
        label_vector = Label(window, text="Vector: ")
        label_vector.grid(row=3, column=0, sticky=(N, S, W, E))
        self.text_vector = Text(window,height = 1, width = 30)
        self.text_vector.grid(row=3, column=1, sticky=(N, S, W, E))
        label_coordinate = Label(window, text="Coordinate: ")
        label_coordinate.grid(row=4, column=0, sticky=(N, S, W, E))
        self.text_coordinate = Text(window,height = 1, width = 30)
        self.text_coordinate.grid(row=4, column=1, sticky=(N, S, W, E))
        label_value = Label(window, text="Value: ")
        label_value.grid(row=5, column=0, sticky=(N, S, W, E))
        self.text_value = Text(window,height = 1, width = 30)
        self.text_value.grid(row=5, column=1, sticky=(N, S, W, E))
        insert_button = Button(window, text='insert', command=self.insert_data)
        insert_button.grid(row=5, column=2, sticky=(N, S, W, E))

    def insert_data(self):
        """
        This function to trigger the action to insert data into GUI by clicking on the "insert" button
        """
        input_ref_date = self.text_ref_date.get("1.0", END)
        input_geo = self.text_geo.get("1.0", END)
        input_commod = self.text_commod.get("1.0", END)
        input_vector = self.text_vector.get("1.0", END)
        input_coordinate = self.text_coordinate.get("1.0", END)
        input_value = self.text_value.get("1.0", END)
        self.text = self.text + 1
        self.treeview.insert('', 'end', text=self.text,
                             values=(input_ref_date, input_geo, input_commod, input_vector, input_coordinate, input_value))

    def delete_data(self):
        """
        This function to trigger the action to delete data from GUI by clicking on the "delete selected data" button
        """
        selected_item = self.treeview.selection()[0]  # get selected item
        self.treeview.delete(selected_item)


# author is Weikai Li
if __name__ == '__main__':
    root = Tk()
    App(root)
    root.mainloop()
