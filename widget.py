from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QFrame
from PySide6.QtGui import QFont
from HomeWindow import Ui_HomeWindow
from NewWindow import Ui_NewWindow
from ExistingWindow import Ui_ExistingWindow
from ProfileWindow import Ui_ProfileWindow
from TestWindow import Ui_TestWindow
from TransitionWindow import Ui_Trans
import os
from theme import *
import time


class Widget(QWidget, Ui_HomeWindow, Ui_NewWindow, Ui_ExistingWindow, Ui_ProfileWindow, Ui_TestWindow, Ui_Trans):
    
    def __init__(self):
        ''' To mmake the starting screen'''
        super().__init__()
        
        # Home UI
        self.mainlayout = QVBoxLayout()
        
        self.frameHome = QFrame()
        self.mainlayout.addWidget(self.frameHome)
        self.home = self.setupHomeUi(self.frameHome)
        self.setWindowTitle('Home Window')
        self.buttonContinueHome.setFocus()

        self.buttonNewHome.clicked.connect(self.__new)
        self.buttonContinueHome.clicked.connect(self.__continue)
        self.buttonContinueHome.setDefault(True)
        self.buttonExisitingHome.clicked.connect(self.__existing)
        self.buttonSettingsHome.clicked.connect(self.__setting)
        self.buttonThemHome.clicked.connect(self.theme_)
        self.buttonEcitHome.clicked.connect(exit)
        self.setLayout(self.mainlayout)


    def theme_(self):
        ''' Theme control'''
        theme_toggle(self)


    def __new(self):
        ''' Changing the screen to the new profile'''
        
        self.frameHome.setVisible(False)
        self.frameNewProfile = QFrame()
        self.mainlayout.addWidget(self.frameNewProfile)
        self.setWindowTitle('New Profile')
        self.new = self.setupNewUi(self.frameNewProfile)
        self.lineEditNew.textChanged.connect(self.name__)
        self.buttonContinueNew.setVisible(False)
        self.buttonContinueNew.clicked.connect(self.profile_view_n)
        self.buttonHomeNew.pressed.connect(self.Home_n)
        self.lineEditNew.setFocus()
        self.buttonExitNew.clicked.connect(exit)


    def name__(self):
        '''Check the name enetred by the user for the veracity and show Continue button in accordance to it'''
        name = self.lineEditNew.displayText()
        lenName = len(name)
        flag = 0


        try:
            with open('profiles/profile_list', 'r') as f:
                # Comment: profile/profile/list       
                profile_list = f.readlines()
                # end for
            # end readline file

            for i in range(len(profile_list)):
                profile_name = profile_list[i].strip('\n')
                if profile_name == name:
                    flag = 3

        except FileNotFoundError:
            with open('profiles/profile_list', 'x') as f:
                # Comment: profile/profile/list
                f.write('')
                # end for
            # end readline file

        for i in range (lenName):
            if name[i].isspace() and name[i-1].isspace():
                flag = 1
                break

            elif name[i-1].isalnum() == False and name[i-1].isspace() == False:
                flag = 2
                break

        if lenName < 5:
            self.lineEditNew.setStyleSheet("""
            color: 'red'
            """)
            self.labelWarnNew.setText('UserName must be atleast 6 characters long')

        elif lenName > 30:
            self.lineEditNew.setStyleSheet("""
            color: 'red'
            """)
            self.labelWarnNew.setText('UserName must be atmost 30 characters long')
            self.buttonContinueNew.setVisible(False)

        elif flag == 1:
            self.lineEditNew.setStyleSheet("""
            color: 'red'
            """)
            self.labelWarnNew.setText('UserName must not contain consequtive spaces')
            self.buttonContinueNew.setVisible(False)

        elif flag == 2:
            self.lineEditNew.setStyleSheet("""
            color: 'red'
            """)
            self.labelWarnNew.setText('UserName must not symbols or unidentifyable characters')
            self.buttonContinueNew.setVisible(False)

        elif flag == 3:
            self.lineEditNew.setStyleSheet("""
            color: 'red'
            """)
            self.labelWarnNew.setText('UserName already exists')
            self.buttonContinueNew.setVisible(False)

        else:
            self.lineEditNew.setStyleSheet("""
            color: 'green'
            """)
            self.labelWarnNew.setText('')
            self.buttonContinueNew.setVisible(True)
            

    def __continue(self):
        '''PassThrough to the Profile Frame'''
        self.frameHome.setVisible(False)
        self.frameContinue = QFrame()
        self.profile_view_h()


    def __existing(self):
        ''' Show the existing frame'''
        self.frameHome.setVisible(False)
        self.frameExProfile = QFrame()
        self.mainlayout.addWidget(self.frameExProfile)
        self.setWindowTitle('New Profile')
        self.new = self.setupExUi(self.frameExProfile)
        list_profile = self.getProfileList()
        if list_profile == []:
            self.buttonContinueEx.setDisabled(True)
        self.comboBoxEx.addItems(list_profile)
        self.comboBoxEx.setFocus()
        self.buttonContinueEx.pressed.connect(self.profile_view_e)
        self.buttonHomeEx.pressed.connect(self.Home_e)
        self.buttonExitEx.clicked.connect(exit)

    
    def getProfileList(self):
        '''Get the list of the names of the users from file for the existing frame'''

        with open('profiles/profile_list', 'r') as f:
            # Comment: 
            profile_list = f.readlines()
        # end readline file

        for i in range (len(profile_list)):
            if profile_list[i] == '':
                profile_list.pop(i)
            profile_list[i] = profile_list[i].strip('\n')

        return profile_list


    def getUser(self):
        '''Return the previous user name'''
        with open('profiles/last_profile', 'r') as f:
            # Comment: 
            name = f.readline()
        # end readline file

        return name


    def __setting(self):
        ''' Settings for the app'''
        pass


    def writeNread(self):
        '''Save the name of the profile or create one if not available'''
        with open('profiles/profile_list', 'a') as f:
            # Comment: 
            f.write(f'\n{self.name_}')
        # end append file
            
        with open('profiles/last_profile', 'w') as f:
            # Comment: 
            f.write(self.name_)
        # end overwrite file
            
        with open(f'profiles/P_{self.name_}', 'w') as f:
            # Comment: 
            f.write('1 0')
        # end overwrite file
            
        with open(f'profiles/D_{self.name_}', 'w') as f:
            # Comment: 
            f.write(' ')
    

    def profile_view_n(self):
        '''Passthrough to Profile from New Window'''
        self.name_ = self.lineEditNew.text()
        self.writeNread()
        self.__profile(self.frameNewProfile, self.name_)


    def profile_view_h(self):
        '''Passthrough to Profile from Home Window'''
        with open('profiles/last_profile', 'r') as f:
            # Comment: 
            if f.readline() == '':
                self.name_ = 'Guest'
                self.writeNread()
        self.name_ = self.getUser()
        self.__profile(self.frameHome, self.name_)


    def profile_view_e(self):
        '''Passthrough to Profile from Exisitng Window'''
        self.name_ = self.comboBoxEx.currentText()
        with open('profiles/last_profile', 'w') as f:
            # Comment: 
            f.write(self.name_)
        # end overwrite file
        self.__profile(self.frameExProfile, self.name_)


    def __profile(self, frame, name):
        ''' To display profile Window'''
        frame.setVisible(False)
        self.frameProfile = QFrame()
        self.mainlayout.addWidget(self.frameProfile)

        self.setWindowTitle(f'Profile Display')
        self.profile = self.setupProfileUi(self.frameProfile)
        self.labelWelcomeProfile.setText(f'Welcome {name}')
        self.buttonContinueProfile.setFocus()

        with open(f'profiles/D_{self.name_}') as f:
            list_D = f.readlines()
        self.label.setFont(QFont('OldEnglish'))

        if list_D != []:
            last_D = list_D[0]
            last_D = list(last_D.split(' '))

            self.label.setText(f"\
1 CPM :                 {float(last_D[0]):.2f}\n\
2 WPM :                 {float(last_D[1]):.2f}\n\
3 Time Taken :          {float(last_D[2]):.2f}\n\
4 Characters Typed :    {last_D[3]}\n\
5 Correct Characters :  {last_D[6]}\n\
6 Wrong Chars :         {last_D[8]}\n\
7 Words Typed :         {last_D[5]}\n\
8 Correct Words :       {last_D[7]}\n")
            
      
        self.buttonExitProfile.clicked.connect(exit)
        
        self.buttonContinueProfile.pressed.connect(self.__test)
        self.buttonInfoProfile.pressed.connect(self.__info)
        self.buttonExitProfile.clicked.connect(exit)


    def __test(self):
        '''Passthrough to testwindow'''
        self.testText = self.getText(self.name_)
        self.__testWindow()


    def getText(self,name):
        ''' To get the text for the test using the exercise and chapter'''
        _details = ['']
        try:
            with open(f'profiles/P_{name}', 'r') as f:
                # Comment: 
                _details = f.readlines()
            # end readline file

        except FileNotFoundError:
            _details[0] = '1 0'
            try:
                os.mkdir('profiles')
                with open(f'profiles/P_{name}', 'w') as f:
                    # Comment: 
                    f.write('1 0')
                # end overwrite file
                
            except FileExistsError:
                with open(f'profiles/P_{name}', 'w') as f:
                    # Comment: 
                    f.write('1 0')
                # end overwrite file
            
        list2 = list(_details[0].split(' '))
        for i in range (len(list2)):
            list2[i] = int(list2[i])
        
        self.exBack = list2

        with open(f'courses/course{list2[0]}', 'r') as f:
            # Comment: 
            textList = f.readlines()
        # end readline file

        return textList[list2[1]]


    def __info(self):        
        
        pass


    def __testWindow(self):
        
        self.frameProfile.setVisible(False)
        self.frameTest = QFrame()
        self.mainlayout.addWidget(self.frameTest)
        self.new = self.setupTestUi(self.frameTest)
        
        self.countChar = 0
        self.CPM = 0
        self.WPM = 0
        self.chars = 0
        self.words = 0
        self.correctChars = 0
        self.correctWords = 0
        self.wrongChars = 0
        self.wrongWords = 0
        self.word = ''
        self.typedWord = ''

        self.setWindowTitle('Test Baby')
        self.labelUserNameTest.setText(self.name_)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.timer_)
        self.start = time.time()
        
        self.lineEditTest.textEdited.connect(self.runTest)


    def timer_(self):
        self.time = time.time()-self.start
        self.labelTimeTest.setText(f'{self.time:.2f}')
        self.CPM = (self.chars*60)/self.time
        self.WPM = (self.words*60)/self.time
        self.labelCPMTest.setText(f'CPM : {self.CPM:.2f}')
        self.labelWPMTest.setText(f'WPM : {self.WPM:.2f}')
        self.timer.start()


    def runTest(self):

        self.timer.start()
      
        if self.countChar <= 8:
            self.str = self.testText[0:self.countChar+10]

            self.labelChar_19.setText(self.str[-1])
            self.labelChar_18.setText(self.str[-2])
            self.labelChar_17.setText(self.str[-3])
            self.labelChar_16.setText(self.str[-4])
            self.labelChar_15.setText(self.str[-5])
            self.labelChar_14.setText(self.str[-6])
            self.labelChar_13.setText(self.str[-7])
            self.labelChar_12.setText(self.str[-8])
            self.labelChar_11.setText(self.str[-9])
            self.labelChar_Main.setText(self.str[-10])
            try:
                self.labelChar_9.setText(self.str[-11])
            except IndexError:
                self.labelChar_9.setText(' ')
            try:
                self.labelChar_8.setText(self.str[-12])
            except IndexError:
                self.labelChar_8.setText(' ')
            try:
                self.labelChar_7.setText(self.str[-13])
            except IndexError:
                self.labelChar_7.setText(' ')
            try:
                self.labelChar_6.setText(self.str[-14])
            except IndexError:
                self.labelChar_6.setText(' ')
            try:
                self.labelChar_5.setText(self.str[-15])
            except IndexError:
                self.labelChar_5.setText(' ')
            try:
                self.labelChar_4.setText(self.str[-16])
            except IndexError:
                self.labelChar_4.setText(' ')
            try:
                self.labelChar_3.setText(self.str[-17])
            except IndexError:
                self.labelChar_3.setText(' ')
            try:
                self.labelChar_2.setText(self.str[-18])
            except IndexError:
                self.labelChar_2.setText(' ')
            try:
                self.labelChar_1.setText(self.str[-19])
            except IndexError:
                self.labelChar_1.setText(' ')

        elif len(self.testText) - self.countChar <= 9:
            self.str = self.testText[self.countChar-9:-1]

            self.labelChar_1.setText(self.str[0])
            self.labelChar_2.setText(self.str[1])
            self.labelChar_3.setText(self.str[2])
            self.labelChar_4.setText(self.str[3])
            self.labelChar_5.setText(self.str[4])
            self.labelChar_6.setText(self.str[5])
            self.labelChar_7.setText(self.str[6])
            self.labelChar_8.setText(self.str[7])
            self.labelChar_9.setText(self.str[8])
            try:
                self.labelChar_Main.setText(self.str[9])
            except IndexError:
                self.labelChar_Main.setText('Finished ')
                self.setFocus()
                self.testFinished()

            try:
                self.labelChar_11.setText(self.str[10])
            except IndexError:
                self.labelChar_11.setText(' ')
            try:
                self.labelChar_12.setText(self.str[11])
            except IndexError:
                self.labelChar_12.setText(' ')
            try:
                self.labelChar_13.setText(self.str[12])
            except IndexError:
                self.labelChar_13.setText(' ')
            try:
                self.labelChar_14.setText(self.str[13])
            except IndexError:
                self.labelChar_14.setText(' ')
            try:
                self.labelChar_15.setText(self.str[14])
            except IndexError:
                self.labelChar_15.setText(' ')
            try:
                self.labelChar_16.setText(self.str[15])
            except IndexError:
                self.labelChar_16.setText(' ')
            try:
                self.labelChar_17.setText(self.str[16])
            except IndexError:
                self.labelChar_17.setText(' ')
            try:
                self.labelChar_18.setText(self.str[17])
            except IndexError:
                self.labelChar_18.setText(' ')
            try:
                self.labelChar_19.setText(self.str[18])
            except IndexError:
                self.labelChar_19.setText(' ')

        elif self.countChar == len(self.testText):
            self.testFinished()

        else:
            self.str = self.testText[self.countChar-9:self.countChar+10]

            self.labelChar_1.setText(self.str[0])
            self.labelChar_2.setText(self.str[1])
            self.labelChar_3.setText(self.str[2])
            self.labelChar_4.setText(self.str[3])
            self.labelChar_5.setText(self.str[4])
            self.labelChar_6.setText(self.str[5])
            self.labelChar_7.setText(self.str[6])
            self.labelChar_8.setText(self.str[7])
            self.labelChar_9.setText(self.str[8])
            self.labelChar_Main.setText(self.str[9])
            self.labelChar_11.setText(self.str[10])
            self.labelChar_12.setText(self.str[11])
            self.labelChar_13.setText(self.str[12])
            self.labelChar_14.setText(self.str[13])
            self.labelChar_15.setText(self.str[14])
            self.labelChar_16.setText(self.str[15])
            self.labelChar_17.setText(self.str[16])
            self.labelChar_18.setText(self.str[17])
            self.labelChar_19.setText(self.str[18])
        
        self.updateData()

        self.countChar += 1


    def updateData(self):
        typedChar = self.lineEditTest.text()[-1]
        char = self.testText[self.countChar]

        self.chars += 1
        if char == ' ':
            if self.typedWord == self.word:
                self.correctWords += 1
            else:
                self.wrongWords += 1
            self.word = ''
            self.typedWord = '' 
            self.words += 1
        else:
            self.word += char
            self.typedWord += typedChar
        
        if typedChar == char:
            self.correctChars += 1
        else:
            self.wrongChars += 1

        self.labelCharTest.setText(f'Chars : {self.chars}')
        self.labelWordTest.setText(f'Words : {self.words}')
        self.labelWrongCharTest.setText(f'Wrong Chars : {self.wrongChars}')
        self.labelWrongWordTest.setText(f'Wrong Words : {self.wrongWords}')


    def testFinished(self):
        self.timer.stop()
        self.stop = time.time()
        self.final_time = self.stop - self.start
        self.checkData()
        
        list_S = [self.CPM, self.WPM, self.time, self.countChar, self.chars, self.words, self.correctChars, self.correctWords, self.wrongChars]
        str = ''
        for x in list_S:
            str += f'{x} '
        
        str += '\n'

        with open(f'profiles/D_{self.name_}', 'r') as f:
            # Comment: 
            list_D = f.readlines()
        # end readline file
            
        if len(list_D)>100:
            list_D.pop(-1)
            list_D.insert(0, str)
            with open(f'profiles/D_{self.name_}', 'w') as f:
                # Comment: 
                f.writelines(list_D)
        # end append file
        else:
            list_D.insert(0, str)
            with open(f'profiles/D_{self.name_}', 'w') as f:
                # Comment: 
                f.writelines(list_D)

        self.__trans()


    def checkData(self):
        self.flag = 0
        correct_per = self.correctChars*100/self.chars
        if self.CPM >= 40 and correct_per > 90:
            self.flag = 1
            self.incrementChap()
         
        else:
            self.flag = 0

            
    def incrementChap(self):
        '''to make 2d matrix which stores the chapters and the exercises and increment the no ofn the exercise'''

        listChap = [[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7],[0,1,2,3,4],4,5,6]

        _details = ['']
    
        with open(f'profiles/P_{self.name_}', 'r') as f:
            # Comment: 
            _details = f.readlines()
        # end readline file
                
        list2 = list(_details[0].split(' '))
        for i in range (len(list2)):
            list2[i] = int(list2[i])

        if list2[1]<len(listChap[list2[0]]):
            list2[1] += 1
        else:
            list2[0] += 1
            list2[1] = 0

        
        with open(f'profiles/P_{self.name_}', 'w') as f:
            # Comment: 
            f.write(f'{list2[0]} {list2[1]}')
        # end overwrite file


    def __trans(self):
        self.frameTest.setVisible(False)
        self.frameTrans = QFrame()
        self.mainlayout.addWidget(self.frameTrans)
        self.new = self.setupTransUi(self.frameTrans)
        if self.flag == 1:
            self.labeHeaderTrans.setText('Passed')
            self.buttonContinueTrans.setFocus()
        else:
            self.labeHeaderTrans.setText('Failed')
            self.buttonRestartTrans.setFocus()

        self.labelDetailsTrans.setText(f'\
CPM : {self.CPM:.2f}\n\
WPM : {self.WPM:.2f}\n\
Time : {self.time:.2f}\n\
Total Words : {self.words}\n\
Total Chars : {self.countChar}')
        self.label_2.setText(f'\
Wrong Words : {self.wrongWords}\n\
Wrong Chars : {self.wrongChars}\n\
Correct Word Percent : {self.correctWords*100/self.words:.2f}\n\
Correct Char Percent : {self.correctChars*100/self.countChar:.2f}\n\
Weakest Chars : \n\
Strongest Chars : ')
        self.buttonContinueTrans.pressed.connect(self.__test_p)
        self.buttonRestartTrans.pressed.connect(self.__test_restart)
        self.buttonHomeTrans.pressed.connect(self.Home_tr)
        

    def __test_restart(self):
        with open(f'profiles/P_{self.name_}', 'w') as f:
            # Comment: 
            f.write(f'{self.exBack[0]} {self.exBack[1]}')
        self.frameTrans.setVisible(False)
        self.__test()


    def __test_p(self):
        self.frameTrans.setVisible(False)
        self.__test()


    def Home_p(self):
        frame = self.frameProfile
        self.__home(frame)


    def Home_e(self):
        frame = self.frameExProfile
        self.__home(frame)


    def Home_tr(self):
        frame = self.frameTrans
        self.__home(frame)


    def Home_n(self):
        frame = self.frameNewProfile
        self.__home(frame)


    def __home(self, frame):
        frame.setVisible(False)
        self.frameHome = QFrame()
        self.mainlayout.addWidget(self.frameHome)

        self.home = self.setupHomeUi(self.frameHome)
        self.setWindowTitle('Home Window')

        self.buttonNewHome.clicked.connect(self.__new)
        self.buttonContinueHome.clicked.connect(self.__continue)
        self.buttonExisitingHome.clicked.connect(self.__existing)
        self.buttonSettingsHome.clicked.connect(self.__setting)
        self.buttonThemHome.clicked.connect(self.theme_)
        self.buttonEcitHome.clicked.connect(exit)
        self.setFocus()

