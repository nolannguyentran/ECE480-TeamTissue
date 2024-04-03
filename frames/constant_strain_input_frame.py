import wx
import frames.back_end as back_end

from datetime import datetime
length = 800
width = 480

#--------------------------------------------------------------------------CONSTANT STRAIN TYPE SCREEN---------------------------------------------
# This is where the user has selected the 'constant strain type' test where the user will enter a constant strain value alongside with time duration
# that will be used for the test

def on_constant_start_test(event):                           #function for start button to start test; call function run_motor (used for constant strain test only) 
        #print("hello world")
        print(constant_strain_input.GetValue()) 

class ConstantStrainTestInput(wx.Frame):
    def __init__(self, motor_name, test_type, strain_type):
        wx.Frame.__init__(self, None, size=(length, width))

        self.motor_name = motor_name        #Capsule name
        self.test_type = test_type          #Test type name
        self.strain_type = strain_type
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For user input strain and percentage
        panel_4 = wx.Panel(self, -1,)       #For 'START' button
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))
        panel_4.SetBackgroundColour((33, 37, 41))               
        panel_5.SetBackgroundColour((53, 62, 108))

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_0 = wx.StaticText(panel_1, label = "BioReact")    #tmp placeholder for future photoshopped trademark]
        t_0.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.motor_name+ " - "+ self.test_type+": "+self.strain_type) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        
        constant_strain_text = wx.StaticText(panel_3, label = "Strain:")
        constant_strain_text.SetForegroundColour((255, 255, 255))
        global constant_strain_input                        #---------------------------------------------------------> might refactor in the future
        constant_strain_input = wx.TextCtrl(panel_3)        #---might need to rename to strain_input_constant
        #strain_input.Bind(wx.EVT_TEXT, on_key_typed)
        rate_text = wx.StaticText(panel_3, label = "Rate:")
        rate_text.SetForegroundColour((255, 255, 255))
        global rate_input_constant                          #-----------------------------------------------------------> maybe better name for "constant" starin input test
        rate_input_constant = wx.TextCtrl(panel_3)

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        button_start = wx.Button(panel_4, wx.ID_ANY, 'START')
        button_start.SetBackgroundColour((190, 37, 66))
        button_start.SetForegroundColour((255,255,255))
        button_start.Bind(wx.EVT_BUTTON, on_constant_start_test)
 

        button_start.Bind(wx.EVT_BUTTON, lambda event: back_end.on_start_test_click(event, self.motor_name, self.test_type, self.strain_type))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: back_end.on_home_click(event, self.__class__.__name__))
        button_settings.Bind(wx.EVT_BUTTON, lambda event: back_end.on_settings_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        test_button_sizer = wx.GridSizer(3,1,10,10) #--------------------------------------------------------------->
        user_field_sizer = wx.BoxSizer(wx.VERTICAL)
        
        user_field_sizer.Add(constant_strain_text, 1, wx.EXPAND)
        user_field_sizer.Add(constant_strain_input, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)
        user_field_sizer.Add(rate_text, 1, wx.EXPAND)
        user_field_sizer.Add(rate_input_constant, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)

        middle_sizer.Add(panel_3, 1, wx.EXPAND)
        middle_sizer.Add(panel_4, 1, wx.EXPAND)

        test_button_sizer.Add((0,0), 0, wx.EXPAND)
        test_button_sizer.Add(button_start, 0, wx.EXPAND)
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