from Actions.find_and_click_image_action import FindAndClickImageAction
from Actions.soft_find_and_click_image_action import SoftFindAndClickImageAction
from Actions.press_key_action import PressKeyAction
from Actions.find_image_action import FindImageAction
from Actions.manual_click_action import ManualClickAction
from Actions.manual_scroll_action import ManualScrollAction
from Actions.conditional_action import ConditionalAction
from Actions.manual_sleep_action import ManualSleepAction
from Actions.email_action import SendEmailAction
from Actions.quit_action import QuitAction
from Actions.extract_text_action import ExtractTextAction
from Actions.screenshot_action import ScreenshotAction
from Actions.chatgpt_action import ChatGPTAction
from Actions.wait_for_keypress_action import WaitForKeyPressAction
from manual_click import ManualClick
from email_handler import EmailHandler
from state_machine import StateMachine
from helpers import Helpers
import random

class ActionSets:
    def __init__(self, game_automator):
        self.manual_click = ManualClick()
        self.game_automator = game_automator

    def choose_icon(self):
        return random.choice(["logicon", "cornicon", "stoneicon"])
    
    def create_machine(self):
        return StateMachine()
    
    def scout_explore(self):
        machine = self.create_machine()
        machine.add_state("explorenight", FindAndClickImageAction('Media/explorenight.png', offset_y=25), "openmsgs", "exploreday")
        machine.add_state("exploreday", FindAndClickImageAction('Media/explore.png', delay=1, offset_y=25), "openmsgs", "explorenight")

        machine.add_state("openmsgs", PressKeyAction('z'), "reportactive")
        machine.add_state("reportactive", ManualClickAction(27,8,delay=.2), "explorationreport")
        machine.add_state("explorationreport", FindAndClickImageAction('Media/explorationreport.png',delay=.2), "villagereport", "explorationreportactive")
        machine.add_state("explorationreportactive", FindAndClickImageAction('Media/explorationreportactive.png',delay=.2), "villagereport", "explorationreport")

        machine.add_state("villagereport", FindAndClickImageAction('Media/villagereport.png', offset_x=370,delay=0), "checkexploredvillage", "barbreport")
        machine.add_state("checkexploredvillage", FindAndClickImageAction('Media/reportbanner.png', delay=0), "barbreport", "clickmonument")

        machine.add_state("barbreport", FindAndClickImageAction('Media/barbreport.png', offset_x=370,delay=0), "checkexploredbarb", "barbreport2")
        machine.add_state("checkexploredbarb", FindAndClickImageAction('Media/reportbanner.png', delay=0), "barbreport2", "clickmonument")

        machine.add_state("barbreport2", FindAndClickImageAction('Media/barbreport2.png', offset_x=370,delay=0), "checkexploredbarb2", "passreport")
        machine.add_state("checkexploredbarb2", FindAndClickImageAction('Media/reportbanner.png', delay=0), "passreport", "clickmonument")
        
        machine.add_state("passreport", FindAndClickImageAction('Media/passreport.png', offset_x=370,delay=0), "checkexploredpass", "holyreport")
        machine.add_state("checkexploredpass", FindAndClickImageAction('Media/reportbanner.png', delay=0), "holyreport", "clickmonument")

        machine.add_state("holyreport", FindAndClickImageAction('Media/holyreport.png', offset_x=370,delay=0), "checkexploredholy", "cavereport")
        machine.add_state("checkexploredholy", FindAndClickImageAction('Media/reportbanner.png', delay=0), "cavereport", "clickmonument")

        machine.add_state("cavereport", FindAndClickImageAction('Media/cavereport.png', offset_x=300, offset_y=20,delay=.1), "checkexploredcave", "emptyreport")
        machine.add_state("checkexploredcave", FindAndClickImageAction('Media/reportbanner.png', delay=.1), "emptyreport", "clickcave")
        machine.add_state("clickcave", ManualClickAction(50,54,delay=2), "investigateaction")
        machine.add_state("investigateaction", FindAndClickImageAction('Media/investigateaction.png',delay=.2), "sendactioncave","investigateaction")
        machine.add_state("sendactioncave", FindAndClickImageAction('Media/sendaction.png',delay=.2), "backtocity","sendactioncave")



        machine.add_state("checkexplored", FindAndClickImageAction('Media/reportbanner.png', delay=.1), "scouticon", "clickmonument")
        machine.add_state("scouticon", FindAndClickImageAction('Media/scoutticon.png', offset_x=30,delay=.1), "barbreport", "failexplorenight")
        machine.add_state("clickmonument", ManualClickAction(50,54,delay=2), "backtocitylong", "clickmonument")
        machine.add_state("backtocitylong", PressKeyAction('space',delay=4), "explorenight")
        # same but press esc

        machine.add_state("emptyreport", PressKeyAction('escape'), "failexplorenight")
        machine.add_state("failexplorenight", FindAndClickImageAction('Media/explorenight.png', offset_y=25), "exploreicon", "failexploreday")
        machine.add_state("failexploreday", FindAndClickImageAction('Media/explore.png', offset_y=25), "exploreicon", "failexplorenight")

        machine.add_state("exploreicon", FindAndClickImageAction('Media/exploreicon.png',delay=.4), "exploreaction", "failexplorenight")
        machine.add_state("exploreaction", FindAndClickImageAction('Media/exploreaction.png',delay=1), "exploreactionfog", "exploreaction")

        machine.add_state("exploreactionfog", FindAndClickImageAction('Media/exploreaction.png',delay=2), "exploreactionfogcheck", "exploreactionfogcheck")
        machine.add_state("exploreactionfogcheck", FindAndClickImageAction('Media/exploreaction.png',delay=.1), "exploreactionfog", "sendaction")

        machine.add_state("sendaction", FindAndClickImageAction('Media/sendaction.png',delay=1.2, retard=1), "sendactioncheck", "sendactioncheck")
        machine.add_state("sendactioncheck", FindAndClickImageAction('Media/sendaction.png',delay=1.2, retard=1), "sendaction", "backtocity")

        machine.add_state("backtocity", PressKeyAction('space'),"explorenight")
        machine.set_initial_state("explorenight")
        return machine
    

    def farm_barb (self):
        machine = self.create_machine()
        machine.add_state("restart", PressKeyAction('escape'), "cityview")
        machine.add_state("cityview", PressKeyAction('space'), "birdview","cityview")
        machine.add_state("birdview", PressKeyAction('f'), "barbland","cityview")
        machine.add_state("barbland", FindAndClickImageAction('Media/barbland.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","restart")
        machine.add_state("arrow", FindAndClickImageAction('Media/arrow.png',delay=2, offset_y=80), "attackaction","restart")
        machine.add_state("attackaction", FindAndClickImageAction('Media/attackaction.png'), "lohar","restart")
        #machine.add_state("lohar", ManualClickAction(96,80), "smallmarchaction","newtroopaction")
        machine.add_state("lohar", FindAndClickImageAction('Media/lohar.png'), "smallmarchaction","restart")
        #machine.add_state("lohar", FindAndClickImageAction('Media/lohar.png'), "smallmarchaction","newtroopaction")
        #machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png'), "marchaction","newtroopaction")
        #machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "victory","marchaction")
        machine.add_state("smallmarchaction", FindAndClickImageAction('Media/smallmarchaction.png',delay=.5), "victory","restart")
        machine.add_state("victory", FindImageAction('Media/victory.png', delay=2), "birdview","victory")
        machine.set_initial_state("cityview")
        return machine
    
    def farm_rss (self):
        machine = self.create_machine()
        machine.add_state("restart", PressKeyAction('escape'), "cityview")
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview", PressKeyAction('f', retard=1), Helpers.getRandomRss())

        machine.add_state("logicon", FindAndClickImageAction('Media/logicon.png'), "searchaction","restart")
        machine.add_state("cornicon", FindAndClickImageAction('Media/cornicon.png'), "searchaction","restart")
        machine.add_state("goldicon", FindAndClickImageAction('Media/goldicon.png'), "searchaction","restart")
        machine.add_state("stoneicon", FindAndClickImageAction('Media/stoneicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","logicon")
        machine.add_state("arrow", FindAndClickImageAction('Media/arrow.png',delay=2, offset_y=70), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindAndClickImageAction('Media/smallmarchaction.png', offset_x=300), "escape2","restart")
        machine.add_state("escape2", PressKeyAction('escape'), "openmsgs","restart")

        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "birdview","restart")

        machine.add_state("openmsgs", PressKeyAction('z', delay=60), "mailicon")
        machine.add_state("mailicon", FindImageAction('Media/mailicon.png', delay=.5), "reportactive","openmsgs")
        machine.add_state("reportactive", ManualClickAction(27,8,delay=.2), "gatheropen")
        machine.add_state("gatheropen", FindImageAction('Media/gatheropen.png'), "newicon","gatheringicon")
        machine.add_state("gatheringicon", FindAndClickImageAction('Media/gatheringicon.png', delay=0.5), "newicon","clickleftcollumn")
        machine.add_state("clickleftcollumn", ManualClickAction(27,20,delay=.2, remember_position=False), "scroll")
        machine.add_state("scroll", ManualScrollAction(y_scroll=10), "gatheringicon")
        machine.add_state("newicon", FindAndClickImageAction('Media/newicon.png'), "escape","escaperetry")
        machine.add_state("escaperetry", PressKeyAction('escape'), "openmsgs")
        machine.add_state("escape", PressKeyAction('escape'), "birdview")

        machine.set_initial_state("cityview")
        return machine

    def emailtest (self):
        machine = self.create_machine()
        machine.add_state("findcaptcha",  FindAndClickImageAction('Media/captchachest.png',delay=59), "notify","findcaptcha")
        machine.add_state("notify",  SendEmailAction(), "quit")
        machine.add_state("quit",  QuitAction(game_automator=self.game_automator), "findcaptcha")
        machine.set_initial_state("findcaptcha")
        return machine


    def lyceum (self):
        machine = self.create_machine()
        machine.add_state("sstittle",  ScreenshotAction(33.7,77,33.5,43), "ettitle")
        machine.add_state("ettitle", ExtractTextAction(description= "Give me the answer after thinking step by step:\n "), "ssq1")
        machine.add_state("ssq1", ScreenshotAction(33,52,45,51,), "eq1")
        machine.add_state("eq1",ExtractTextAction(description= "\n\n which of these is the most similar to your answer?: \nA: ", aggregate=True), "ssq2")
        machine.add_state("ssq2", ScreenshotAction(57,76,45,51), "eq2")
        machine.add_state("eq2", ExtractTextAction(description= "B: ", aggregate=True), "ssq3")
        machine.add_state("ssq3",  ScreenshotAction(33,52,54,60), "eq3")
        machine.add_state("eq3", ExtractTextAction(description= "C: ", aggregate=True), "ssq4")
        machine.add_state("ssq4", ScreenshotAction(57,74,54,60), "eq4")
        machine.add_state("eq4", ExtractTextAction(description= "D: ", aggregate=True), "cgpt")
        machine.add_state("cgpt", ChatGPTAction(),"sstittle")
        machine.set_initial_state("sstittle")
        return machine
    
    def lyceumMid (self):
        machine = self.create_machine()
        machine.add_state("keypress", WaitForKeyPressAction('k'), "sstittle","keypress")
        machine.add_state("sstittle",  ScreenshotAction(33.7,80,39.5,49), "ettitle")
        machine.add_state("ettitle", ExtractTextAction(description= "Give me the answer after thinking step by step:\n "), "ssq1")
        machine.add_state("ssq1", ScreenshotAction(33,52,49.5,57), "eq1")
        machine.add_state("eq1",ExtractTextAction(description= "\n\n which of these is the most similar to your answer?: \nA: ", aggregate=True), "ssq2")
        machine.add_state("ssq2", ScreenshotAction(57,74,49.5,57), "eq2")
        machine.add_state("eq2", ExtractTextAction(description= " B: ", aggregate=True), "ssq3")
        machine.add_state("ssq3",  ScreenshotAction(33,52,58,66), "eq3")
        machine.add_state("eq3", ExtractTextAction(description= " C: ", aggregate=True), "ssq4")
        machine.add_state("ssq4", ScreenshotAction(57,74,58,66), "eq4")
        machine.add_state("eq4", ExtractTextAction(description= " D: ", aggregate=True), "cgpt")
        machine.add_state("cgpt", ChatGPTAction(midterm=True),"keypress")
        machine.set_initial_state("keypress")
        return machine