from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy import platform
from kivy.lang import Builder



if platform == "android":
    from android.permissions import request_permissions, Permission

    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])



class Menu(Screen):
    pass

class EndGame(Screen):
    pass



def clearquestions(self):
    self.manager.ids.question1.ids.Clear.text = ""
    self.manager.ids.question2.ids.Clear2.text = ""
    self.manager.ids.question3.ids.Clear3.text = ""
    self.manager.ids.question4.ids.Clear4.text = ""
    self.manager.ids.question5.ids.Clear5.text = ""
    self.manager.ids.question6.ids.Clear6.text = ""
    self.manager.ids.question7.ids.Clear7.text = ""
    self.manager.ids.question8.ids.Clear8.text = ""
    self.manager.ids.question9.ids.Clear9.text = ""
    self.manager.ids.question10.ids.Clear10.text = ""
    self.manager.ids.question11.ids.Clear11.text = ""
    self.manager.ids.question12.ids.Clear12.text = ""
    self.manager.ids.question13.ids.Clear13.text = ""
    self.manager.ids.question14.ids.Clear14.text = ""


def showpopup60():
    show = BoxLayout(orientation="vertical")
    img = Image(source="GameOver.png", size_hint=(1,.5))
    btn = Button(text="Start New Game", size_hint=(1, .2))
    lab = Label(text="Your game is over and we hope you \nenjoyed your experience seeing "
                    "some of  \n your favorite celebrities of yesterday ""today."" \nThank you  "
                    "for playing and come visit us at\nhttp://www.fomodin.com",
                size_hint=(1, .3))
    show.add_widget(img)
    show.add_widget(lab)
    show.add_widget(btn)
    popupwindow = Popup(title="You are out of guesses", content=show, size_hint=(1, 1))
    popupwindow.open()
    btn.bind(on_press=popupwindow.dismiss)


class Question1(Screen, Widget):
    answer1 = StringProperty("LL COOL J")
    answer2 = StringProperty("LLCOOLJ")
    answer3 = StringProperty("LLCOOL J")
    answer4 = StringProperty("LL COOLJ")
    KivyLimitkv = StringProperty("4")
    HintLimit = 3

    def on_enter(self, *args):
        self.KivyLimitkv = "4"
        self.HintLimit = 3

        clearquestions(self)

    def questionpass(self):

        if self.manager.ids.question1.ids.Clear.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question2"
        elif self.manager.ids.question1.ids.Clear.text == self.answer2:
            print("Correct")
            self.manager.current = "question2"
        elif self.manager.ids.question1.ids.Clear.text == self.answer3:
            print("Correct")
            self.manager.current = "question2"
        elif self.manager.ids.question1.ids.Clear.text == self.answer4:
            print("Correct")
            self.manager.current = "question2"


        else:
            print("WRONG")


    def letterpress2(self, Button):
        prior = self.ids.Clear.text
        self.ids.Clear.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear.text = ""

    def space(self, button):
        prior = self.ids.Clear.text
        self.ids.Clear.text = f"{prior}{button}"


    def hint1(self):

        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "llhint.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimitkv = str(self.HintLimit)
        self.HintLimit -= 1

        if self.HintLimit <= -1:
            print("try again")

            showpopup60()
            self.manager.ids.question1.ids.Clear.text = ""
            self.manager.current = "question1"
            self.KivyLimitkv = "4"
            self.HintLimit = 3

        else:
            print("game not over")






class Question2(Screen):
    answer1 = StringProperty("TONY DANZA")
    answer2 = StringProperty("TONYDANZA")
    KivyLimit2 = NumericProperty()

    def on_enter(self, *args):
        self.KivyLimit2 = int(self.manager.ids.question1.ids.KivyLimit.text)

    def questionpass(self):

        if self.manager.ids.question2.ids.Clear2.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question3"
        elif self.manager.ids.question2.ids.Clear2.text == self.answer2:
            print("Correct")
            self.manager.current = "question3"



        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear2.text
        self.ids.Clear2.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear2.text = ""

    def space(self, button):
        prior = self.ids.Clear2.text

        self.ids.Clear2.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "boss.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit2 = str(self.KivyLimit2)
        self.KivyLimit2 -= 1

        if self.KivyLimit2 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)
            self.manager.current = "question1"
            self.KivyLimitkv = "4"
            self.HintLimit = 3


        else:
            print("game not over")




class Question3(Screen):
    KivyLimit3 = NumericProperty()

    answer1 = StringProperty("BALKY")


    def on_enter(self, *args):
        self.KivyLimit3 = int(self.manager.ids.question2.ids.KivyLimit2.text)

    def questionpass(self):

        if self.manager.ids.question3.ids.Clear3.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question4"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear3.text
        self.ids.Clear3.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear3.text = ""

    def space(self, button):
        prior = self.ids.Clear3.text

        self.ids.Clear3.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "balkylarry.jpeg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit3 = str(self.KivyLimit3)
        self.KivyLimit3 -= 1

        if self.KivyLimit3 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)


            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3




class Question4(Screen):
    KivyLimit4 = NumericProperty()

    answer1 = StringProperty("RICKI LAKE")
    answer2 = StringProperty("RICKILAKE")


    def on_enter(self, *args):
        self.KivyLimit4 = int(self.manager.ids.question3.ids.KivyLimit3.text)

    def questionpass(self):

        if self.manager.ids.question4.ids.Clear4.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question5"
        elif self.manager.ids.question4.ids.Clear4.text == self.answer2:
            print("Correct")
            self.manager.current = "question5"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear4.text
        self.ids.Clear4.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear4.text = ""

    def space(self, button):
        prior = self.ids.Clear4.text

        self.ids.Clear4.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "lake.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit4 = str(self.KivyLimit4)
        self.KivyLimit4 -= 1

        if self.KivyLimit4 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)


            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3

class Question5(Screen):
    KivyLimit5 = NumericProperty()

    answer1 = StringProperty("TORISPELLING")
    answer2 = StringProperty("TORI SPELLING")


    def on_enter(self, *args):
        self.KivyLimit5 = int(self.manager.ids.question4.ids.KivyLimit4.text)

    def questionpass(self):

        if self.manager.ids.question5.ids.Clear5.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question6"
        elif self.manager.ids.question5.ids.Clear5.text == self.answer2:
            print("Correct")
            self.manager.current = "question6"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear5.text
        self.ids.Clear5.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear5.text = ""

    def space(self, button):
        prior = self.ids.Clear5.text

        self.ids.Clear5.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "90210.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit5 = str(self.KivyLimit5)
        self.KivyLimit5 -= 1

        if self.KivyLimit5 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3


class Question6(Screen):
    KivyLimit6 = NumericProperty()

    answer1 = StringProperty("KIETHCOOGAN")
    answer2 = StringProperty("KIETH COOGAN")


    def on_enter(self, *args):
        self.KivyLimit6 = int(self.manager.ids.question5.ids.KivyLimit5.text)

    def questionpass(self):

        if self.manager.ids.question6.ids.Clear6.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question7"
        elif self.manager.ids.question6.ids.Clear6.text == self.answer2:
            print("Correct")
            self.manager.current = "question7"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear6.text
        self.ids.Clear6.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear6.text = ""

    def space(self, button):
        prior = self.ids.Clear6.text

        self.ids.Clear6.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "adventures1.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit6 = str(self.KivyLimit6)
        self.KivyLimit6 -= 1

        if self.KivyLimit6 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3





class Question7(Screen):
    KivyLimit7 = NumericProperty()

    answer1 = StringProperty("NANCY")


    def on_enter(self, *args):
        self.KivyLimit7 = int(self.manager.ids.question6.ids.KivyLimit6.text)

    def questionpass(self):

        if self.manager.ids.question7.ids.Clear7.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question8"
        elif self.manager.ids.question7.ids.Clear7.text == self.answer2:
            print("Correct")
            self.manager.current = "question8"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear7.text
        self.ids.Clear7.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear7.text = ""

    def space(self, button):
        prior = self.ids.Clear7.text

        self.ids.Clear7.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "nightmare.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit7 = str(self.KivyLimit7)
        self.KivyLimit7 -= 1

        if self.KivyLimit7 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3


class Question8(Screen):
    KivyLimit8 = NumericProperty()

    answer1 = StringProperty("SHARON STONE")
    answer2 = StringProperty("SHARONSTONE")



    def on_enter(self, *args):
        self.KivyLimit8 = int(self.manager.ids.question7.ids.KivyLimit7.text)

    def questionpass(self):

        if self.manager.ids.question8.ids.Clear8.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question9"
        elif self.manager.ids.question8.ids.Clear8.text == self.answer2:
            print("Correct")
            self.manager.current = "question9"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear8.text
        self.ids.Clear8.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear8.text = ""

    def space(self, button):
        prior = self.ids.Clear8.text

        self.ids.Clear8.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "sharon.jpeg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit8 = str(self.KivyLimit8)
        self.KivyLimit8 -= 1

        if self.KivyLimit8 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3

class Question9(Screen):
    KivyLimit9 = NumericProperty()

    answer1 = StringProperty("AXEL ROSE")
    answer2 = StringProperty("AXLE ROSE")
    answer3 = StringProperty("AXLEROSE")
    answer4 = StringProperty("AXELROSE")




    def on_enter(self, *args):
        self.KivyLimit9 = int(self.manager.ids.question8.ids.KivyLimit8.text)

    def questionpass(self):

        if self.manager.ids.question9.ids.Clear9.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question10"
        elif self.manager.ids.question9.ids.Clear9.text == self.answer2:
            print("Correct")
            self.manager.current = "question10"
        elif self.manager.ids.question9.ids.Clear9.text == self.answer3:
            print("Correct")
            self.manager.current = "question10"
        elif self.manager.ids.question9.ids.Clear9.text == self.answer4:
            print("Correct")
            self.manager.current = "question10"





        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear9.text
        self.ids.Clear9.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear9.text = ""

    def space(self, button):
        prior = self.ids.Clear9.text

        self.ids.Clear9.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "guns.jpeg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit9 = str(self.KivyLimit9)
        self.KivyLimit9 -= 1

        if self.KivyLimit9 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3


class Question10(Screen):
    KivyLimit10 = NumericProperty()

    answer1 = StringProperty("CHEVY CHASE")
    answer2 = StringProperty("CHEVYCHASE")



    def on_enter(self, *args):
        self.KivyLimit10 = int(self.manager.ids.question9.ids.KivyLimit9.text)

    def questionpass(self):

        if self.manager.ids.question10.ids.Clear10.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question11"
        elif self.manager.ids.question10.ids.Clear10.text == self.answer2:
            print("Correct")
            self.manager.current = "question11"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear10.text
        self.ids.Clear10.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear10.text = ""

    def space(self, button):
        prior = self.ids.Clear10.text

        self.ids.Clear10.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "christmas.jpeg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit10 = str(self.KivyLimit10)
        self.KivyLimit10 -= 1

        if self.KivyLimit10 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3

class Question11(Screen):
    KivyLimit11 = NumericProperty()

    answer1 = StringProperty("BRANDON FRAISER")
    answer2 = StringProperty("BRANDONFRAISER")



    def on_enter(self, *args):
        self.KivyLimit11 = int(self.manager.ids.question10.ids.KivyLimit10.text)

    def questionpass(self):

        if self.manager.ids.question11.ids.Clear11.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question12"
        elif self.manager.ids.question11.ids.Clear11.text == self.answer2:
            print("Correct")
            self.manager.current = "question12"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear11.text
        self.ids.Clear11.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear11.text = ""

    def space(self, button):
        prior = self.ids.Clear11.text

        self.ids.Clear11.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "mummy.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit11 = str(self.KivyLimit11)
        self.KivyLimit11 -= 1

        if self.KivyLimit11 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3

class Question12(Screen):
    KivyLimit12 = NumericProperty()

    answer1 = StringProperty("GEENA DAVIS")
    answer2 = StringProperty("GEENADAVIS")



    def on_enter(self, *args):
        self.KivyLimit12 = int(self.manager.ids.question11.ids.KivyLimit11.text)

    def questionpass(self):

        if self.manager.ids.question12.ids.Clear12.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question13"
        elif self.manager.ids.question12.ids.Clear12.text == self.answer2:
            print("Correct")
            self.manager.current = "question13"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear12.text
        self.ids.Clear12.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear12.text = ""

    def space(self, button):
        prior = self.ids.Clear12.text

        self.ids.Clear12.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "thelma.jpeg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit12 = str(self.KivyLimit12)
        self.KivyLimit12 -= 1

        if self.KivyLimit12 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3

class Question13(Screen):
    KivyLimit13 = NumericProperty()

    answer1 = StringProperty("DAVIDLETTERMAN")
    answer2 = StringProperty("DAVID LETTERMAN")



    def on_enter(self, *args):
        self.KivyLimit13 = int(self.manager.ids.question12.ids.KivyLimit12.text)

    def questionpass(self):

        if self.manager.ids.question13.ids.Clear13.text == self.answer1:
            print("CORRECT")
            self.manager.current = "question14"
        elif self.manager.ids.question13.ids.Clear13.text == self.answer2:
            print("Correct")
            self.manager.current = "question14"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear13.text
        self.ids.Clear13.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear13.text = ""

    def space(self, button):
        prior = self.ids.Clear13.text

        self.ids.Clear13.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "latenight.jpg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit13 = str(self.KivyLimit13)
        self.KivyLimit13 -= 1

        if self.KivyLimit13 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3

class Question14(Screen):
    KivyLimit14 = NumericProperty()

    answer1 = StringProperty("EDFURLONG")
    answer2 = StringProperty("ED FURLONG")



    def on_enter(self, *args):
        self.KivyLimit14 = int(self.manager.ids.question13.ids.KivyLimit13.text)

    def questionpass(self):

        if self.manager.ids.question14.ids.Clear14.text == self.answer1:
            print("CORRECT")
            self.manager.current = "EndGame"
        elif self.manager.ids.question14.ids.Clear14.text == self.answer2:
            print("Correct")
            self.manager.current = "EndGame"




        else:
            print("WRONG")


    def letterpress3(self, Button):
        prior = self.ids.Clear14.text
        self.ids.Clear14.text = f"{prior}{Button}"


    def clear(self):
        self.ids.Clear14.text = ""

    def space(self, button):
        prior = self.ids.Clear14.text

        self.ids.Clear14.text = f"{prior}{button}"


    def hint1(self):
        show = BoxLayout(orientation = "vertical")
        llhint = Image(source = "BIKE.jpeg",size_hint= (1, .5))
        show.add_widget(llhint)
        popupwindow = Popup(title="", separator_height=0, content=show, size_hint=(1, .5))
        popupwindow.open()

    def hint_counter(self):
        self.KivyLimit14 = str(self.KivyLimit14)
        self.KivyLimit14 -= 1

        if self.KivyLimit13 <= 0:
            print("try again")

            showpopup60()
            clearquestions(self)

            self.manager.current = "question1"

            self.KivyLimitkv = "4"

            self.HintLimit = 3




class WindowManager(ScreenManager):
    pass

Celebstoday1 = Builder.load_file("Celebstoday1.kv")


class Celebstoday(App):
    def build(self):
        self.icon = "washedupicon.png"

        return WindowManager()


if __name__ == '__main__':
    Celebstoday().run()

