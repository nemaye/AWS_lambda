#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import os


class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        self.set_icon_from_file("web.png")
        self.set_title("Downloader")

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox.set_homogeneous(False)


        URL = Gtk.Label(label="URL")
        vbox.pack_start(URL, True, True, 0)


        self.entry_URL = Gtk.Entry()
        vbox.pack_start(self.entry_URL, True, True, 0)

        Name = Gtk.Label(label="Name")
        vbox.pack_start(Name, True, True, 0)

        self.entry_Name = Gtk.Entry()
        vbox.pack_start(self.entry_Name, True, True, 0)


        hbox = Gtk.Box(spacing=30)
        vbox.pack_start(hbox, True, True, 0)


        self.OK_Btn = Gtk.Button(label="Download")
        self.OK_Btn.connect("clicked", self.on_Dwnld_clicked)
        hbox.pack_start(self.OK_Btn, True, True, 0)

        self.Quit_Btn = Gtk.Button(label="Quit")
        self.Quit_Btn.connect("clicked", self.on_Quit_clicked)
        hbox.pack_start(self.Quit_Btn, True, True, 0)


        self.set_border_width(40)
        self.add(vbox)

        self.connect("destroy", Gtk.main_quit)


    def on_Quit_clicked(self, widget):
        Gtk.main_quit()
        
    def on_Dwnld_clicked(self,widget):
        text = self.entry_URL.get_text()
        name = self.entry_Name.get_text()

        command = "ytdl " + text + " > " + name + ".mp4"
        print(command)
        os.system(command)
        Gtk.main_quit()


win = MyWindow()
win.show_all()
Gtk.main()