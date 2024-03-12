import wx
#import gui_be          #REMEMBER TO UN-COMMENT INITIALIZATION AT THE BOTTOM OF THIS FILE!!!


from datetime import datetime
length = 800
width = 480
current_date_time = datetime.now()
now = current_date_time.strftime("%A, %B %d, %Y %I:%M %p")

def get_current_frame(frame_name):                       #determines which frame user is currently in, assign to existing global frame name class
    global current_frame
    match frame_name:
        case 'TestSelectionFrame':
            current_frame = test_selection_frame
        case 'StrainInputTypeFrame':
            current_frame = strain_input_type_frame
        case 'ConstantStrainTestInput':
            current_frame = constant_strain_test_frame
        case 'RandomizedStrainTestInput':
            current_frame = randomized_strain_test_frame
        case 'WaveStrainTestInput':
            current_frame = square_wave_strain_test_frame
        #case 'TestOutput':
        #    current_frame = live_test_frame


#TODO: Add functions for grabing max,min,and rate from each of the different strain type input tests


def on_constant_start_test(event):                           #function for start button to start test; call function run_motor (used for constant strain test only) 
        #print("hello world")
        print(constant_strain_input.GetValue()) 

def on_motor_click(event):
    identity = event.GetEventObject().GetLabel()    #Returns which capsule selected
    global test_selection_frame
    test_selection_frame = TestSelectionFrame(identity)
    test_selection_frame.Show()

def on_compression_test_click(event, motor_name):
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()
    #global strain_rate_frame
    #strain_rate_frame = TestInput(motor_name, identity)
    #strain_rate_frame.Show()

def on_tensile_test_click(event, motor_name):
    identity = event.GetEventObject().GetLabel()    #Returns which test selected
    test_selection_frame.Destroy()
    global strain_input_type_frame
    strain_input_type_frame = StrainInputTypeFrame(motor_name, identity)
    strain_input_type_frame.Show()
    #global strain_rate_frame
    #strain_rate_frame = TestInput(motor_name, identity)
    #strain_rate_frame.Show()

def on_constant_test_click(event, motor_name, test_type):       #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global constant_strain_test_frame
    constant_strain_test_frame = ConstantStrainTestInput(motor_name, test_type, strain_type)
    constant_strain_test_frame.Show()

def on_random_test_click(event, motor_name, test_type):         #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global randomized_strain_test_frame
    randomized_strain_test_frame = RandomizedStrainTestInput(motor_name, test_type, strain_type)
    randomized_strain_test_frame.Show()

def on_square_wave_test_click(event, motor_name, test_type):    #[strain input test selection page]
    strain_type = event.GetEventObject().GetLabel()    #Returns which strain input type selected (constant rate)
    strain_input_type_frame.Destroy()
    global square_wave_strain_test_frame
    square_wave_strain_test_frame = WaveStrainTestInput(motor_name, test_type, strain_type)
    square_wave_strain_test_frame.Show()


#def on_start_test_click(event, motor_name, test_name):          
#    identity = event.GetEventObject().GetLabel()
#    constant_strain_test_frame.Destroy()
#    global live_test_frame
#    live_test_frame = TestOutput(motor_name, test_name)
#    live_test_frame.Show()

def on_home_click(event, frame_name):
    get_current_frame(frame_name)
    current_frame.Destroy()
    #HomeFrame.test()

#def test(event):
#    gui_be.randomized_strain(10,100)


class HomeFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, size=(length, width))

        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For housing live-view display
        panel_3 = wx.Panel(self, -1,)       #For housing buttons
        panel_4 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))         
        panel_4.SetBackgroundColour((53, 62, 108))       

        global button_a
        button_a = wx.Button(panel_3, wx.ID_ANY, 'Capsule: A')
        button_b = wx.Button(panel_3, wx.ID_ANY, 'Capsule: B')
        button_c = wx.Button(panel_3, wx.ID_ANY, 'Capsule: C')
        button_d = wx.Button(panel_3, wx.ID_ANY, 'Capsule: D')

        button_home = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = settings_img)

        button_home.Disable()
        #button_settings.Bind(wx.EVT_BUTTON, test)

        button_a.SetBackgroundColour((89, 99, 182))
        button_a.SetForegroundColour((255,255,255))
        button_b.SetBackgroundColour((89, 99, 182))
        button_b.SetForegroundColour((255,255,255))
        button_c.SetBackgroundColour((89, 99, 182))
        button_c.SetForegroundColour((255,255,255))
        button_d.SetBackgroundColour((89, 99, 182))
        button_d.SetForegroundColour((255,255,255))
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        button_a.Bind(wx.EVT_BUTTON, on_motor_click)
        button_b.Bind(wx.EVT_BUTTON, on_motor_click)
        button_c.Bind(wx.EVT_BUTTON, on_motor_click)
        button_d.Bind(wx.EVT_BUTTON, on_motor_click)

        t_0 = wx.StaticText(panel_1, label = "BioReact")    #tmp placeholder for future photoshopped trademark
        t_0.SetForegroundColour((255, 255, 255))
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)
   
        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        motor_grid_sizer = wx.GridSizer(2, 2, 10, 10)     #For housing the four motor buttons
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

        middle_sizer.Add(panel_2, 1, wx.EXPAND)
        middle_sizer.Add(panel_3, 1, wx.EXPAND)

        motor_grid_sizer.Add(button_a, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_b, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_c, 0, wx.EXPAND)
        motor_grid_sizer.Add(button_d, 0, wx.EXPAND)

        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
        panel_3.SetSizer(motor_grid_sizer)
        panel_4.SetSizer(navigation_grid_sizer)

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
        window_sizer.Add(panel_4, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()
    #def test():                            -------------------maybe disable button of motors or change color to reflect status
        #print("hello worlds")
        #button_a.SetBackgroundColour((255,255,255))

class TestSelectionFrame(wx.Frame):
       def __init__(self, name):
        wx.Frame.__init__(self, None, size=(length, width))

        self.name = name                    #Capsule Name
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For housing two test selection buttons
        panel_4 = wx.Panel(self, -1,)       #For housing instructions
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))
        panel_4.SetBackgroundColour((33, 37, 41))               
        panel_5.SetBackgroundColour((53, 62, 108))

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_0 = wx.StaticText(panel_1, label = "BioReact")    #tmp placeholder for future photoshopped trademark
        t_0.SetForegroundColour((255, 255, 255))
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.name) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        t_3 = wx.StaticText(panel_4, label = "Please select which type of test to conduct with "+self.name)
        t_3.SetFont(font_2)
        t_3.SetForegroundColour((255, 255, 255))
      
        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        text_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning instructions in center
        text_sizer_3.Add((0,0), 1, wx.EXPAND)
        text_sizer_3.Add(t_3,0,wx.ALIGN_CENTER)
        text_sizer_3.Add((0,0), 1, wx.EXPAND)

        button_compression = wx.Button(panel_3, wx.ID_ANY, 'Compression Test')
        button_tensile = wx.Button(panel_3, wx.ID_ANY, 'Tensile Test')

        button_compression.SetBackgroundColour((89, 99, 182))
        button_compression.SetForegroundColour((255,255,255))
        button_tensile.SetBackgroundColour((89, 99, 182))
        button_tensile.SetForegroundColour((255,255,255))

        button_compression.Bind(wx.EVT_BUTTON, lambda event: on_compression_test_click(event, self.name))
        button_tensile.Bind(wx.EVT_BUTTON, lambda event: on_tensile_test_click(event, self.name))


        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: on_home_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.GridSizer(1, 2, 20, 20)         #For housing middle panel
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

        middle_sizer.Add(button_compression, 0, wx.EXPAND)
        middle_sizer.Add(button_tensile, 0, wx.EXPAND)
        
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

class StrainInputTypeFrame(wx.Frame):
       def __init__(self, motor_name, test_type):
        wx.Frame.__init__(self, None, size=(length, width))

        self.name = motor_name                    #Capsule Name
        self.test_type = test_type
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For capsule name
        panel_3 = wx.Panel(self, -1,)       #For housing two test selection buttons
        panel_4 = wx.Panel(self, -1,)       #For housing instructions
        panel_5 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))
        panel_4.SetBackgroundColour((33, 37, 41))               
        panel_5.SetBackgroundColour((53, 62, 108))

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_0 = wx.StaticText(panel_1, label = "BioReact")    #tmp placeholder for future photoshopped trademark
        t_0.SetForegroundColour((255, 255, 255))
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.name) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        t_3 = wx.StaticText(panel_4, label = "Please select test input type to conduct with "+self.name+ " - "+ self.test_type)
        t_3.SetFont(font_2)
        t_3.SetForegroundColour((255, 255, 255))
      
        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        text_sizer_3 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning instructions in center
        text_sizer_3.Add((0,0), 1, wx.EXPAND)
        text_sizer_3.Add(t_3,0,wx.ALIGN_CENTER)
        text_sizer_3.Add((0,0), 1, wx.EXPAND)

        button_constant = wx.Button(panel_3, wx.ID_ANY, 'Constant Strain')
        button_random = wx.Button(panel_3, wx.ID_ANY, 'Random Strain')
        button_wave = wx.Button(panel_3, wx.ID_ANY, 'Square Wave')

        button_constant.SetBackgroundColour((89, 99, 182))
        button_constant.SetForegroundColour((255,255,255))
        button_random.SetBackgroundColour((89, 99, 182))
        button_random.SetForegroundColour((255,255,255))
        button_wave.SetBackgroundColour((89, 99, 182))
        button_wave.SetForegroundColour((255,255,255))

        button_constant.Bind(wx.EVT_BUTTON, lambda event: on_constant_test_click(event, self.name, self.test_type))
        button_random.Bind(wx.EVT_BUTTON, lambda event: on_random_test_click(event, self.name, self.test_type))
        button_wave.Bind(wx.EVT_BUTTON, lambda event: on_square_wave_test_click(event, self.name, self.test_type))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: on_home_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.GridSizer(1, 3, 20, 20)         #For housing middle panel
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons

        middle_sizer.Add(button_constant, 0, wx.EXPAND)
        middle_sizer.Add(button_random, 0, wx.EXPAND)
        middle_sizer.Add(button_wave, 0, wx.EXPAND)
        
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
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.motor_name+ " - "+ self.test_type+": "+self.strain_type) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        
        constant_strain_text = wx.StaticText(panel_3, label = "Strain:")
        constant_strain_text.SetForegroundColour((255, 255, 255))
        global constant_strain_input                        #---------------------------------------------------------> might refactor in the future
        constant_strain_input = wx.TextCtrl(panel_3)
        #strain_input.Bind(wx.EVT_TEXT, on_key_typed)
        rate_text = wx.StaticText(panel_3, label = "Rate:")
        rate_text.SetForegroundColour((255, 255, 255))
        global rate_input_constant                          #-----------------------------------------------------------> maybe better name for "constant" starin input test
        rate_input_constant = wx.TextCtrl(panel_3)

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        button_start = wx.Button(panel_4, wx.ID_ANY, 'START')
        button_start.SetBackgroundColour((190, 37, 66))
        button_start.SetForegroundColour((255,255,255))
        button_start.Bind(wx.EVT_BUTTON, on_constant_start_test)
 

        #button_start.Bind(wx.EVT_BUTTON, lambda event: on_start_test_click(event, self.motor_name, self.test_type))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: on_home_click(event, self.__class__.__name__))
        
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

class RandomizedStrainTestInput(wx.Frame):
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
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.motor_name+ " - "+ self.test_type+": "+self.strain_type) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        
        minimum_strain_text = wx.StaticText(panel_3, label = "Minimum Strain:")
        minimum_strain_text.SetForegroundColour((255, 255, 255))
        global randomized_strain_min
        randomized_strain_min = wx.TextCtrl(panel_3)
        maximum_strain_text = wx.StaticText(panel_3, label = "Maximum Strain:")
        maximum_strain_text.SetForegroundColour((255, 255, 255))
        global randomized_strain_max
        randomized_strain_max = wx.TextCtrl(panel_3)
        rate_text = wx.StaticText(panel_3, label = "Rate:")
        rate_text.SetForegroundColour((255, 255, 255))
        global rate_input_randomized
        rate_input_randomized = wx.TextCtrl(panel_3)

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        button_start = wx.Button(panel_4, wx.ID_ANY, 'START')
        button_start.SetBackgroundColour((190, 37, 66))
        button_start.SetForegroundColour((255,255,255))
        button_start.Bind(wx.EVT_BUTTON, on_constant_start_test)
 

        #button_start.Bind(wx.EVT_BUTTON, lambda event: on_start_test_click(event, self.motor_name, self.test_type))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: on_home_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        test_button_sizer = wx.GridSizer(3,1,10,10) #--------------------------------------------------------------->
        user_field_sizer = wx.BoxSizer(wx.VERTICAL)
        
        user_field_sizer.Add(minimum_strain_text, 1, wx.EXPAND)
        user_field_sizer.Add(randomized_strain_min, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)
        user_field_sizer.Add(maximum_strain_text, 1, wx.EXPAND)
        user_field_sizer.Add(randomized_strain_max, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)
        user_field_sizer.Add(rate_text, 1, wx.EXPAND)
        user_field_sizer.Add(rate_input_randomized, 0, wx.EXPAND)
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

class WaveStrainTestInput(wx.Frame):
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
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.motor_name+ " - "+ self.test_type+": "+self.strain_type) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        
        minimum_strain_text = wx.StaticText(panel_3, label = "wavyMinimum Strain:")
        minimum_strain_text.SetForegroundColour((255, 255, 255))
        global wave_strain_min
        wave_strain_min = wx.TextCtrl(panel_3)
        maximum_strain_text = wx.StaticText(panel_3, label = "Maximum Strain:")
        maximum_strain_text.SetForegroundColour((255, 255, 255))
        global wave_strain_max
        wave_strain_max = wx.TextCtrl(panel_3)
        rate_text = wx.StaticText(panel_3, label = "Rate:")
        rate_text.SetForegroundColour((255, 255, 255))
        global rate_input_wave
        rate_input_wave = wx.TextCtrl(panel_3)

        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        button_start = wx.Button(panel_4, wx.ID_ANY, 'START')
        button_start.SetBackgroundColour((190, 37, 66))
        button_start.SetForegroundColour((255,255,255))
        button_start.Bind(wx.EVT_BUTTON, on_constant_start_test)
 

        #button_start.Bind(wx.EVT_BUTTON, lambda event: on_start_test_click(event, self.motor_name, self.test_type))

        button_home = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_5, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: on_home_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel
        test_button_sizer = wx.GridSizer(3,1,10,10) #--------------------------------------------------------------->
        user_field_sizer = wx.BoxSizer(wx.VERTICAL)
        
        user_field_sizer.Add(minimum_strain_text, 1, wx.EXPAND)
        user_field_sizer.Add(wave_strain_min, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)
        user_field_sizer.Add(maximum_strain_text, 1, wx.EXPAND)
        user_field_sizer.Add(wave_strain_max, 0, wx.EXPAND)
        user_field_sizer.Add((0,0), 1, wx.EXPAND)
        user_field_sizer.Add(rate_text, 1, wx.EXPAND)
        user_field_sizer.Add(rate_input_wave, 0, wx.EXPAND)
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

class TestOutput(wx.Frame):
    def __init__(self, motor_name, test_type):
        wx.Frame.__init__(self, None, size=(length, width))

        self.motor_name = motor_name        #Test type
        self.test_type = test_type                    #Capsule name
        dashboard_img = wx.Bitmap("./pictures/dashboard.png")
        jobs_img = wx.Bitmap("./pictures/jobs.png")
        settings_img = wx.Bitmap("./pictures/settings.png")

        panel_1 = wx.Panel(self, -1,)       #For housing name, date, and time
        panel_2 = wx.Panel(self, -1,)       #For housing graph
        panel_3 = wx.Panel(self, -1,)       #For housing capsule name, test, and export button
        panel_4 = wx.Panel(self, -1,)       #For housing navigation buttons
    
        panel_1.SetBackgroundColour((53, 62, 108))        
        panel_2.SetBackgroundColour((33, 37, 41))         
        panel_3.SetBackgroundColour((33, 37, 41))
        panel_4.SetBackgroundColour((53, 62, 108))               

        font_1 = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        font_2 = wx.Font(14, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        
        t_0 = wx.StaticText(panel_1, label = "BioReact")    #tmp placeholder for future photoshopped trademark
        t_0.SetForegroundColour((255, 255, 255))
        t_1 = wx.StaticText(panel_1, label = now)
        t_1.SetForegroundColour((255, 255, 255))
        t_2 = wx.StaticText(panel_2, label = self.motor_name+ " - "+ self.test_type) 
        t_2.SetFont(font_1)
        t_2.SetForegroundColour((255, 255, 255))
        
        text_sizer_1 = wx.BoxSizer(wx.HORIZONTAL)     #Aligning date and time right
        text_sizer_1.Add(t_0, 1, wx.EXPAND)
        text_sizer_1.Add((0,0), 2, wx.ALIGN_CENTER)
        text_sizer_1.Add(t_1, 0, wx.EXPAND)

        text_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)   #Aligning Capsule Name and type of test in center
        text_sizer_2.Add((0,0), 1, wx.EXPAND)
        text_sizer_2.Add(t_2, 0, wx.ALIGN_CENTER)
        text_sizer_2.Add((0,0), 1, wx.EXPAND)

        #button_start = wx.Button(panel_4, wx.ID_ANY, 'START')
        #button_start.SetBackgroundColour((190, 37, 66))

        button_home = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = dashboard_img)
        button_jobs = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = jobs_img)
        button_settings = wx.BitmapButton(panel_4, wx.ID_ANY, bitmap = settings_img)

        button_home.Bind(wx.EVT_BUTTON, lambda event: on_home_click(event, self.__class__.__name__))
        
        button_home.SetBackgroundColour((0, 0, 0))
        button_jobs.SetBackgroundColour((0, 0, 0))
        button_settings.SetBackgroundColour((0, 0, 0))

        window_sizer = wx.BoxSizer(wx.VERTICAL)           #For housing entire application window 
        middle_sizer = wx.BoxSizer(wx.HORIZONTAL)         #For housing middle panel

        middle_sizer.Add(panel_2, 1, wx.EXPAND)
        middle_sizer.Add(panel_3, 1, wx.EXPAND)
       
        navigation_grid_sizer = wx.GridSizer(1, 3, 0, 0)  #For housig the three navigation buttons
        navigation_grid_sizer.Add(button_home, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_jobs, 0, wx.EXPAND)
        navigation_grid_sizer.Add(button_settings, 0, wx.EXPAND)
        
        panel_1.SetSizer(text_sizer_1)
        panel_2.SetSizer(text_sizer_2)
        #panel_3.SetSizer(user_field_sizer)
        panel_4.SetSizer(navigation_grid_sizer)
    

        window_sizer.Add(panel_1, 1, wx.EXPAND)
        #window_sizer.Add(panel_2, 2, wx.EXPAND)
        window_sizer.Add(middle_sizer, 10, wx.EXPAND)
        window_sizer.Add(panel_4, 2, wx.EXPAND)
   
        self.SetAutoLayout(True)
        self.SetSizer(window_sizer)
        self.Layout()

   
app = wx.App(False)
global home_frame
home_frame = HomeFrame(None, -1, "BioReactor")
#gui_be.initialization() #initialize motors and load cells
home_frame.Show()
app.MainLoop()
