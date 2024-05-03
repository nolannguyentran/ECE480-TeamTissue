import wx
import gui_be as gui_be

length = 800
width = 480

#--------------------------------------------------------------------------LOAD CELL CALLIBRATION SCREEN---------------------------------------------
# This is where the program calibrates the load cells against a given, known weight entered in by the user

class Calibration(wx.Frame):
       def __init__(self, name):
        wx.Frame.__init__(self, None, size=(length, width))

        self.name = name        #settings selection name
       
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")
        logo_img = wx.Image("./pictures/logo.PNG", wx.BITMAP_TYPE_ANY)
        logo_img = logo_img.Scale(90, 30, wx.IMAGE_QUALITY_HIGH)

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For user input strain and percentage
        panel_4 = wx.Panel(self, -1,)       #For 'START' button
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((28, 28, 59))         
        panel_3.SetBackgroundColour((28, 28, 59))
        panel_4.SetBackgroundColour((28, 28, 59))               
        panel_5.SetBackgroundColour((53, 62, 108))

        logo = wx.StaticBitmap(panel_1, wx.ID_ANY, wx.Bitmap(logo_img))

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_2 = wx.StaticText(panel_2, label = "Callibrating "+self.name) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        
        known_weight_text = wx.StaticText(panel_3, label = "Enter known weight in grams:")
        known_weight_text.SetForegroundColour((255, 255, 255))                  
        known_weight_input = wx.TextCtrl(panel_3)        #---might need to rename to strain_input_constant

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(logo)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        button_enter = wx.Button(panel_4, wx.ID_ANY, 'ENTER')
        button_enter.SetBackgroundColour((190, 37, 66))
        button_enter.SetForegroundColour((255,255,255))
 
        button_enter.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_enter_known_weight_click(event, self.__class__.__name__, self.name, known_weight_input.GetValue()))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_home_click(event, self.__class__.__name__))
        button_settings.Bind(wx.EVT_BUTTON, lambda event: gui_be.on_settings_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((28, 28, 59))
        button_jobs.SetBackgroundColour((28, 28, 59))
        button_settings.SetBackgroundColour((28, 28, 59))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        test_button_sizer = wx.GridSizer(3,1,10,10) #--------------------------------------------------------------->
        user_field_sizer = wx.BoxSizer(wx.VERTICAL)
        
        
        user_field_sizer.Add((0,0), 1, wx.EXPAND)
        user_field_sizer.Add(known_weight_text, 0, wx.EXPAND)
        user_field_sizer.Add(known_weight_input, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)

        middle_sizer.Add(panel_3, 1, wx.EXPAND)
        middle_sizer.Add(panel_4, 1, wx.EXPAND)

        test_button_sizer.Add((0,0), 0, wx.EXPAND)
        test_button_sizer.Add(button_enter, 0, wx.EXPAND)
        test_button_sizer.Add((0,0), 0, wx.EXPAND)
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons
        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
        panel_2.SetSizer(text_sizer_2)
        panel_3.SetSizer(user_field_sizer)
        panel_4.SetSizer(test_button_sizer)
        panel_5.SetSizer(navigation_grid_sizer)

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(panel_2, 2, wx.EXPAND)
        window_sizer.Add(middle_sizer, 8, wx.EXPAND)
        window_sizer.Add(panel_5, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()