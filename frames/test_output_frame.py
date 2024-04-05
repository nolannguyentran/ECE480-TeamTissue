import wx
import frames.back_end as back_end

from datetime import datetime
length = 800
width = 480

#--------------------------------------------------------------------------TEST OUTPUT SCREEN---------------------------------------------
# This is where the user can see the progress of the test being ran on the capsule, user will also be able to export the load cell 
# data into a .CSV file with a click of a button

class TestOutput(wx.Frame):
    def __init__(self, motor_name, test_type, strain_type):
        wx.Frame.__init__(self, None, size=(length, width))

        self.motor_name = motor_name        #Capsule name
        self.test_type = test_type          #Test Type
        self.strain_type = strain_type      #Strain type
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")
        logo_img = wx.Image("./pictures/logo.PNG", wx.BITMAP_TYPE_ANY)
        logo_img = logo_img.Scale(90, 30, wx.IMAGE_QUALITY_HIGH)

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For housing two test output buttons
        panel_4 = wx.Panel(self, -1,)       #For housing instruction
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((28, 28, 59))         
        panel_3.SetBackgroundColour((28, 28, 59))
        panel_4.SetBackgroundColour((28, 28, 59))  
        panel_5.SetBackgroundColour((53, 62, 108))  

        logo = wx.StaticBitmap(panel_1, wx.ID_ANY, wx.Bitmap(logo_img))           

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_2 = wx.StaticText(panel_2, label = self.motor_name+ " - "+ self.test_type+": "+self.strain_type) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        t_3 = wx.StaticText(panel_4, label = "Please select option")
        t_3.SetFont(font_2)
        t_3.SetForegroundColour((255, 255, 255))
        
        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(logo)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        text_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning instructions in center
        text_sizer_3.Add((0,0), 1, wx.EXPAND)
        text_sizer_3.Add(t_3,0,wx.ALIGN_CENTER)
        text_sizer_3.Add((0,0), 1, wx.EXPAND)

        button_clear_test = wx.Button(panel_3, wx.ID_ANY, 'Clear Test Results')
        button_export_test = wx.Button(panel_3, wx.ID_ANY, 'Export Test Results to .CSV')

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: back_end.on_home_click(event, self.__class__.__name__))
        button_jobs.Bind(wx.EVT_BUTTON, lambda event: back_end.on_jobs_click(event, self.__class__.__name__))
        button_settings.Bind(wx.EVT_BUTTON, lambda event: back_end.on_settings_click(event, self.__class__.__name__))
        
        button_clear_test.SetBackgroundColour((89, 99, 182))
        button_clear_test.SetForegroundColour((255, 255, 255))
        button_export_test.SetBackgroundColour((89, 99, 182))
        button_export_test.SetForegroundColour((255, 255, 255))

        button_clear_test.Bind(wx.EVT_BUTTON, lambda event: back_end.clear_test_results(event, self.motor_name, self.__class__.__name__))
        #button_export_test.Bind(wx.EVT_BUTTON, lambda event: back_end.export_test_results(event, self.motor_name, self.test_type, self.strain_type, self.__class__.__name__))

        button_home.SetBackgroundColour((28, 28, 59))
        button_jobs.SetBackgroundColour((28, 28, 59))
        button_settings.SetBackgroundColour((28, 28, 59))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.GridSizer(1, 2, 20, 20)         #For housing middle panel

        middle_sizer.Add(button_clear_test, 0, wx.EXPAND)
        middle_sizer.Add(button_export_test, 0, wx.EXPAND)
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons
        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
        panel_2.SetSizer(text_sizer_2)
        panel_3.SetSizer(middle_sizer)
        panel_4.SetSizer(text_sizer_3)
        panel_5.SetSizer(navigation_grid_sizer)
    
        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(panel_2, 2, wx.EXPAND)
        window_sizer.Add(panel_3, 6, wx.EXPAND)
        window_sizer.Add(panel_4, 2, wx.EXPAND)
        window_sizer.Add(panel_5, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()