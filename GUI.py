import tkinter

class Gui(object):
    def __init__(self):
        self.root = tkinter.Tk()
        
        # set the title
        self.root.title("ICS Search Engine")
        
        # create a search/input bar
        self.ip_input = tkinter.Entry(self.root, width = 70)

        # create a display list
        self.display_info = tkinter.Listbox(self.root, width = 100, height = 50)

        # create a search button
        self.result_button = tkinter.Button(self.root, command = self.get_result, text = "Search")

    # 完成布局
    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    def get_result(self)->None:
        # get input
        self.ip_addr = self.ip_input.get()
        
        # clear the display list
        self.display_info.delete(0,'end')

        # print the result
        for i in range(int(self.ip_addr)):
            self.display_info.insert(i,str(int(self.ip_addr) - i))


def main():
    # initialize
    FL = Gui()
    # make arrangment
    FL.gui_arrang()
    # run main process
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
