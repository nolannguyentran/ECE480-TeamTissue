import wx
import frames.back_end as back_end
#import gui_be          #REMEMBER TO UN-COMMENT INITIALIZATION AT THE BOTTOM OF THIS FILE!!!



app = wx.App(False)
back_end.start_program()
app.MainLoop()
