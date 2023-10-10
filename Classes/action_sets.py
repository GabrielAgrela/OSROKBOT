from Actions.find_and_click_image_action import FindAndClickImageAction
from Actions.press_key_action import PressKeyAction
from Actions.find_image_action import FindImageAction
from Actions.manual_click_action import ManualClickAction
from Actions.manual_scroll_action import ManualScrollAction
from Actions.conditional_action import ConditionalAction
from Actions.manual_sleep_action import ManualSleepAction
from Actions.email_action import SendEmailAction
from Actions.quit_action import QuitAction
from Actions.pause_action import PauseAction
from Actions.lyceum_action import LyceumAction
from Actions.extract_text_action import ExtractTextAction
from Actions.find_marauder_action import FindMarauderAction
from Actions.screenshot_action import ScreenshotAction
from Actions.chatgpt_action import ChatGPTAction
from Actions.check_color_action import CheckColorAction
from Actions.wait_for_keypress_action import WaitForKeyPressAction
from manual_click import ManualClick
from state_machine import StateMachine
from Actions.find_gems_action import FindGemAction
from helpers import Helpers
import random

class ActionSets:
    def __init__(self, game_automator):
        self.manual_click = ManualClick()
        self.game_automator = game_automator
    
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
        machine.add_state("cityview", PressKeyAction('space',delay=.3), "birdview","cityview")
        machine.add_state("birdview", PressKeyAction('f',delay=.3), "barbland","cityview")
        machine.add_state("barbland", FindAndClickImageAction('Media/barbland.png',delay=.3), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","restart")
        machine.add_state("arrow", FindAndClickImageAction('Media/arrow.png',delay=1.5, offset_y=105), "attackaction","restart")
        machine.add_state("attackaction", FindAndClickImageAction('Media/attackaction.png',delay=.3), "lohar","restart")
        machine.add_state("lohar", FindAndClickImageAction('Media/lohar.png',delay=.3), "smallmarchaction","newtroopaction")
        
        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png',delay=.3), "marchaction","restart")
        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "victory","restart")

        #machine.add_state("lohar", ManualClickAction(96,80), "smallmarchaction","newtroopaction")
        
        #machine.add_state("lohar", FindAndClickImageAction('Media/lohar.png'), "smallmarchaction","newtroopaction")
        #machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png'), "marchaction","newtroopaction")
        #machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "victory","marchaction")
        machine.add_state("smallmarchaction", FindAndClickImageAction('Media/smallmarchaction.png',delay=.5), "victory","restart")
        machine.add_state("victory", FindImageAction('Media/victory.png', delay=2), "birdview","victory")
        machine.set_initial_state("cityview")
        return machine
    
    def farm_barb_all (self):
        machine = self.create_machine()
        machine.add_state("restart", PressKeyAction('escape'), "cityview")
        machine.add_state("cityview", PressKeyAction('space',delay=.3), "birdview","cityview")
        machine.add_state("birdview", PressKeyAction('f',delay=.3), "barbland","cityview")
        machine.add_state("barbland", FindAndClickImageAction('Media/barbland.png',delay=.3), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","restart")
        machine.add_state("arrow", FindAndClickImageAction('Media/arrow.png',delay=1.5, offset_y=105), "attackaction","restart")
        machine.add_state("attackaction", FindAndClickImageAction('Media/attackaction.png',delay=.3), "lohar","restart")
        machine.add_state("lohar", ManualClickAction(96,80), "smallmarchaction","newtroopaction")
        
        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png',delay=.3), "marchaction","restart")
        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "victory","restart")

        #machine.add_state("lohar", ManualClickAction(96,80), "smallmarchaction","newtroopaction")
        
        #machine.add_state("lohar", FindAndClickImageAction('Media/lohar.png'), "smallmarchaction","newtroopaction")
        #machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png'), "marchaction","newtroopaction")
        #machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "victory","marchaction")
        machine.add_state("smallmarchaction", FindAndClickImageAction('Media/smallmarchaction.png',delay=.5), "victory","restart")
        machine.add_state("victory", FindImageAction('Media/victory.png', delay=2), "birdview","victory")
        machine.set_initial_state("cityview")
        return machine
    
    def train_troops (self):
        machine = self.create_machine()
        machine.add_state("restart", PressKeyAction('escape'), "stable")
        machine.add_state("stable", FindAndClickImageAction('Media/stable.png', offset_x=10), "speedupicon","restart")
        machine.add_state("speedupicon", FindAndClickImageAction('Media/speedupicon.png'), "use","trainhorse")
        machine.add_state("use", ManualClickAction(65,40), "mult","stable")
        machine.add_state("mult", FindAndClickImageAction('Media/mult.png'), "use2","stable")
        machine.add_state("use2", ManualClickAction(65,40), "leavemult","stable")
        machine.add_state("leavemult", PressKeyAction('escape'), "stable","stable")

        machine.add_state("trainhorse", FindAndClickImageAction('Media/trainhorse.png'), "t1cav","stable")
        machine.add_state("t1cav", FindAndClickImageAction('Media/t1cav.png'), "upgrade","stable")
        machine.add_state("upgrade", FindAndClickImageAction('Media/upgrade.png'), "upgradeaction","stable")
        machine.add_state("upgradeaction", FindAndClickImageAction('Media/upgradeaction.png'), "trainbutton","stable")
        machine.add_state("trainbutton", FindAndClickImageAction('Media/trainbutton.png'), "stable","stable")
        machine.set_initial_state("stable")
        return machine
    
    def farm_rss (self):
        machine = self.create_machine()
        
        machine.add_state("pause", PressKeyAction('escape', retard=65), "restart")
        machine.add_state("restart", PressKeyAction('escape'), "checkesc")
        machine.add_state("checkesc", FindAndClickImageAction('Media/escx.png'), "cityview","cityview",)
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview",FindAndClickImageAction('Media/ficon.png'), Helpers.getRandomRss(),"restart")

        machine.add_state("logicon", FindAndClickImageAction('Media/logicon.png'), "searchaction","restart")
        machine.add_state("cornicon", FindAndClickImageAction('Media/cornicon.png'), "searchaction","restart")
        machine.add_state("goldicon", FindAndClickImageAction('Media/goldicon.png'), "searchaction","restart")
        machine.add_state("stoneicon", FindAndClickImageAction('Media/stoneicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","logicon")
        machine.add_state("arrow", ManualClickAction(x=50, y=50, delay=1.5), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindImageAction('Media/smallmarchaction.png'), "pause","restart")


        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "birdview","restart")

        machine.set_initial_state("cityview")
        return machine
    
    def farm_rss_new (self):
        machine = self.create_machine()
        machine.add_state("pause1",  ManualSleepAction(delay=10), "test")
        machine.add_state("test",  ScreenshotAction(96,98,18.6,20.4), "test2")
        machine.add_state("test2", ExtractTextAction(description= "marchcount"), "restart","pause1")
        machine.add_state("pause", PressKeyAction('escape', retard=.5), "pause1")
        machine.add_state("restart", PressKeyAction('escape'), "checkesc")
        machine.add_state("checkesc", FindAndClickImageAction('Media/escx.png'), "cityview","cityview",)
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview",FindAndClickImageAction('Media/ficon.png'), Helpers.getRandomRss(),"restart")

        machine.add_state("logicon", FindAndClickImageAction('Media/logicon.png'), "searchaction","restart")
        machine.add_state("cornicon", FindAndClickImageAction('Media/cornicon.png'), "searchaction","restart")
        machine.add_state("goldicon", FindAndClickImageAction('Media/goldicon.png'), "searchaction","restart")
        machine.add_state("stoneicon", FindAndClickImageAction('Media/stoneicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","logicon")
        machine.add_state("arrow", ManualClickAction(x=50, y=50, delay=1.5), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindImageAction('Media/smallmarchaction.png'), "pause","restart")


        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "test","restart")

        machine.set_initial_state("test")
        return machine
    
    def farm_gems (self):
        machine = self.create_machine()
        #machine.add_state("0", PressKeyAction('space',retard=4), "1")
        #machine.add_state("1", PressKeyAction('space'), "2")
        machine.add_state("2",FindGemAction(),"3")

        machine.set_initial_state("2")
        return machine
    
    def loharjr (self):
        machine = self.create_machine()
        machine.add_state("0", PressKeyAction('space',retard=4), "1")
        machine.add_state("1", PressKeyAction('space'), "2")
        machine.add_state("2",FindMarauderAction(),"3")
        machine.add_state("3", FindAndClickImageAction('Media/attackaction.png',delay=.3), "4","0")
        machine.add_state("4", FindAndClickImageAction('Media/newtroopaction.png',delay=.3), "5","5f")
        machine.add_state("5f", ManualClickAction(96,80), "6f")
        machine.add_state("6f", FindAndClickImageAction('Media/smallmarchaction.png'), "7","0")
        machine.add_state("5", ManualClickAction(75,78), "6")
        machine.add_state("6", FindAndClickImageAction('Media/marchaction.png'), "7","0")

        machine.add_state("7", PressKeyAction('escape'), "8")
        machine.add_state("8", FindAndClickImageAction('Media/applus.png'), "9","0")
        machine.add_state("9", FindAndClickImageAction('Media/apuse.png'), "10","0")
        machine.add_state("10", ManualClickAction(60,40), "11","11")
        machine.add_state("11", PressKeyAction('escape'), "12")
        machine.add_state("12", PressKeyAction('escape'), "13")
        machine.add_state("13", FindImageAction('Media/victory.png', delay=2), "14","13")
        machine.add_state("14", FindImageAction('Media/defeat.png', delay=0), "15","2")
        machine.add_state("15", FindImageAction('Media/armyc.png', delay=5), "15","0")
        #machine.add_state("14", ExtractTextAction(description= "marchcount"), "0","2")
        #machine.add_state("13", FindImageAction('Media/armyc.png', delay=5), "13","2")
        #
        #machine.add_state("other", PressKeyAction('left'), "marchaction")
       # machine.add_state("other", FindAndClickImageAction('Media/marauder.png', delay=1), "marchaction","inventory")



        machine.set_initial_state("1")
        return machine

    def loharjrt (self):
        machine = self.create_machine()
        
        machine.add_state("inventory", PressKeyAction('i'), "other")
        machine.add_state("other", ManualClickAction(x=80, y=20), "loharjr","inventory")
        machine.add_state("loharjr", FindAndClickImageAction('Media/loharjr.png'), "useaction","inventory")
        machine.add_state("useaction", FindAndClickImageAction('Media/useaction.png'), "arrow","inventory")
        machine.add_state("arrow", FindAndClickImageAction('Media/arrow.png',delay=1.5, offset_y=105), "rallyaction","inventory")
        machine.add_state("rallyaction", FindAndClickImageAction('Media/rallyaction.png',delay=.3), "rallysmallaction","inventory")
        machine.add_state("rallysmallaction", FindAndClickImageAction('Media/rallysmallaction.png',delay=.5), "marchaction","inventory")
        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png',delay=.5), "end","inventory")
        machine.add_state("end", QuitAction(game_automator=self.game_automator), "inventory","inventory")


        machine.set_initial_state("inventory")
        return machine
    
    def farm_wood (self):
        machine = self.create_machine()
        machine.add_state("pause1",  ManualSleepAction(delay=10), "test")
        machine.add_state("test",  ScreenshotAction(96,98,18.6,20.4), "test2")
        machine.add_state("test2", ExtractTextAction(description= "marchcount"), "restart","pause1")
        machine.add_state("pause", PressKeyAction('escape', retard=.5), "pause1")
        machine.add_state("restart", PressKeyAction('escape'), "checkesc")
        machine.add_state("checkesc", FindAndClickImageAction('Media/escx.png'), "cityview","cityview",)
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview",FindAndClickImageAction('Media/ficon.png'), "logicon","restart")

        machine.add_state("logicon", FindAndClickImageAction('Media/logicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","logicon")
        machine.add_state("arrow", ManualClickAction(x=50, y=50, delay=1.5), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindImageAction('Media/smallmarchaction.png'), "pause","restart")


        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "test","restart")

        machine.set_initial_state("test")
        return machine
    
    def farm_food (self):
        machine = self.create_machine()
        machine.add_state("pause1",  ManualSleepAction(delay=10), "test")
        machine.add_state("test",  ScreenshotAction(96,98,18.6,20.4), "test2")
        machine.add_state("test2", ExtractTextAction(description= "marchcount"), "restart","pause1")
        machine.add_state("pause", PressKeyAction('escape', retard=.5), "pause1")
        machine.add_state("restart", PressKeyAction('escape'), "checkesc")
        machine.add_state("checkesc", FindAndClickImageAction('Media/escx.png'), "cityview","cityview",)
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview",FindAndClickImageAction('Media/ficon.png'), "cornicon","restart")

        machine.add_state("cornicon", FindAndClickImageAction('Media/cornicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","cornicon")
        machine.add_state("arrow", ManualClickAction(x=50, y=50, delay=1.5), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindImageAction('Media/smallmarchaction.png'), "pause","restart")


        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "test","restart")

        machine.set_initial_state("test")
        return machine
    
    def farm_stone (self):
        machine = self.create_machine()
        machine.add_state("pause1",  ManualSleepAction(delay=10), "test")
        machine.add_state("test",  ScreenshotAction(96,98,18.6,20.4), "test2")
        machine.add_state("test2", ExtractTextAction(description= "marchcount"), "restart","pause1")
        machine.add_state("pause", PressKeyAction('escape', retard=.5), "pause1")
        machine.add_state("restart", PressKeyAction('escape'), "checkesc")
        machine.add_state("checkesc", FindAndClickImageAction('Media/escx.png'), "cityview","cityview",)
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview",FindAndClickImageAction('Media/ficon.png'), "stoneicon","restart")

        machine.add_state("stoneicon", FindAndClickImageAction('Media/stoneicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","stoneicon")
        machine.add_state("arrow", ManualClickAction(x=50, y=50, delay=1.5), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindImageAction('Media/smallmarchaction.png'), "pause","restart")


        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "test","restart")

        machine.set_initial_state("test")
        return machine
    
    def farm_gold (self):
        machine = self.create_machine()
        machine.add_state("pause1",  ManualSleepAction(delay=10), "armyc")
        machine.add_state("armyc", FindImageAction('Media/armyc.png'), "test","pause1")
        machine.add_state("test",  ScreenshotAction(96,98,18.6,20.5), "test2")
        machine.add_state("test2", ExtractTextAction(description= "marchcount"), "restart","pause1")
        machine.add_state("pause", PressKeyAction('escape', retard=.5), "pause1")
        machine.add_state("restart", PressKeyAction('escape'), "checkesc")
        machine.add_state("checkesc", FindAndClickImageAction('Media/escx.png'), "cityview","cityview",)
        machine.add_state("cityview", PressKeyAction('space'), "birdview")
        machine.add_state("birdview",FindAndClickImageAction('Media/ficon.png'), "goldicon","restart")

        machine.add_state("goldicon", FindAndClickImageAction('Media/goldicon.png'), "searchaction","restart")
        machine.add_state("searchaction", FindAndClickImageAction('Media/searchaction.png'), "arrow","goldicon")
        machine.add_state("arrow", ManualClickAction(x=50, y=50, delay=1.5), "gatheraction","restart")
        machine.add_state("gatheraction", FindAndClickImageAction('Media/gatheraction.png'), "newtroopaction","restart")

        machine.add_state("newtroopaction", FindAndClickImageAction('Media/newtroopaction.png', delay=1), "marchaction","smallmarchaction")
        machine.add_state("smallmarchaction", FindImageAction('Media/smallmarchaction.png'), "pause","restart")


        machine.add_state("marchaction", FindAndClickImageAction('Media/marchaction.png'), "armyc","restart")

        machine.set_initial_state("armyc")
        return machine

    def emailtest (self):
        machine = self.create_machine()
        machine.add_state("findcaptcha",  FindAndClickImageAction('Media/captchachest.png',delay=11), "notify","findcaptcha")
        machine.add_state("notify",  SendEmailAction(), "pause")
        machine.add_state("pause",  PauseAction(game_automator=self.game_automator), "findcaptcha")
        machine.set_initial_state("findcaptcha")
        return machine
    

    def lyceum (self):
        machine = self.create_machine()
        machine.add_state("sstittle",  ScreenshotAction(33.7,77,33.5,43), "ettitle")
        machine.add_state("ettitle", ExtractTextAction(description= "Q"), "ssq1")
        machine.add_state("ssq1", ScreenshotAction(33,52,45,51), "eq1")
        machine.add_state("eq1",ExtractTextAction(description= "A"), "ssq2")
        machine.add_state("ssq2", ScreenshotAction(57,76,45,51), "eq2")
        machine.add_state("eq2", ExtractTextAction(description= "B"), "ssq3")
        machine.add_state("ssq3",  ScreenshotAction(33,54,54,60), "eq3")
        machine.add_state("eq3", ExtractTextAction(description= "C"), "ssq4")
        machine.add_state("ssq4", ScreenshotAction(57,76,54,60), "eq4")
        machine.add_state("eq4", ExtractTextAction(description= "D"), "lyceumManual")
        machine.add_state("lyceumManual", LyceumAction(retard=1.5),"sstittle","lyceumGPT")
        machine.add_state("lyceumGPT", ChatGPTAction(retard=1.5),"sstittle")
        machine.set_initial_state("sstittle")
        return machine
    
    def lyceumMid (self):
        machine = self.create_machine()
        machine.add_state("keypress", WaitForKeyPressAction('k', "for the next question"), "sstittle","keypress")
        machine.add_state("sstittle",  ScreenshotAction(33.7,80,39.5,49), "ettitle")
        machine.add_state("ettitle", ExtractTextAction(description= "Q"), "ssq1")
        machine.add_state("ssq1", ScreenshotAction(33,52,49.5,57), "eq1")
        machine.add_state("eq1",ExtractTextAction(description= "A"), "ssq2")
        machine.add_state("ssq2", ScreenshotAction(57,74,49.5,57), "eq2")
        machine.add_state("eq2", ExtractTextAction(description= "B"), "ssq3")
        machine.add_state("ssq3",  ScreenshotAction(33,54,58,66), "eq3")
        machine.add_state("eq3", ExtractTextAction(description= "C"), "ssq4")
        machine.add_state("ssq4", ScreenshotAction(57,76,58,66), "eq4")
        machine.add_state("eq4", ExtractTextAction(description= "D"), "lyceumManual")
        machine.add_state("lyceumManual", LyceumAction(midterm=True,retard=1.5),"keypress","lyceumGPT")
        machine.add_state("lyceumGPT", ChatGPTAction(midterm=True,retard=1.5),"keypress")
        
        machine.set_initial_state("keypress")
        return machine