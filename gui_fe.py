import wx
import gui_be as gui_be

#--------------------------------------------------------------------------FRONT-END---------------------------------------------
# This is where the user will run the file

app = wx.App(False)
gui_be.start_program()
app.MainLoop()
