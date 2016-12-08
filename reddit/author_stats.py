__author__ = 'Matt'
import os
import time
import yaml
import praw

client_secret = 'CKrztgMbwq8nSCjhuXVM6XTPFZo'
username = 'diracdeltafunct_v2'
password = 'Soccer03!'
client_id = 'FPiBPsxOOkwLNA'
user_agent = 'python:authorstats:0.0 (by /u/diracdeltafunct_v2)'


#auths = ["R-W-D-S","themessias1001","SurakofVulcan","CedTruz","tommy_chicago","maggi2929","fake_views","adeldk","Isaac51290","tuckfenpin","moonlightsugar","chepabit","BrownBabyBeater","NoISaidCutOffHisHeth","theseattlewall","Cjkavyy","Dronez","spump_tram","thrustingpanther","DatLaffyTaffy","StarDestinyGuy","47thSage","cezecu","Dankbarber","average_user_421","Forkfoot","TossMeAwayToTheMount","insaincain02","SuperSmith_","catdecal","ThisIsntGoldWorthy","joker68","BlueBear45","Allen_R24","neyymarr","BiglyMAGA","moelottosoprano","ShillingforKek","skinnywhiteblonde","PlantaholicPerson","ModestBanana","CoC4Hire","Lee956","hilariasm","EricKingCantona","u_spezWifesBoyfriend","DeadHead-","Hurricane_Trump","Mariotas_Love_Child","Dodge1992","Teflon_Don420","LoyalEider","IAmWithStoopid","MNJGA","TrappedInsideTheMSM","Trump_The_Triumphant","Earth_Runs_Red","SeriousBlak","Tegucigalpan","liseux","Roryedd","HarshMammal","ou812ou812","lord-helmet","Orlyborly","Pokemon_Jesus","HIGH_ENERGY_MEMES","Sparkyis007","Nfgiven","ButInTheStoneAge","ntmera","spudlikkr","hinduyankee","bruinboy86","Frank-durst","pinkocommiegreen","semlaw","Ayrane","Oh_hamburgers_","Wu-Tang_Swarm","ToTheRescues","DrJarns","altillythebum","UnicornMoonPie","NoFreeStuff4Liberal","conantheking","10gauge","gmax325","phillycowboy","Serres","TrUmPoCaLyPsEnOw","effingdb","Darth_Venath","InstaTwit","WalkingInMemphis1","llIllIIlllIIlIIlllII","IowaBarnOwl","GrandDaddyBlockchain","Getmeamfcoat","RhodesiaRob","Deus_G","Stupidlizardface","loudspoiledcat","castol","SPC1995","YirosBoy","MakeMyDickHardAgain","mikeroolz","themistake3","Dasigesi","KoviCZ","V00D00Doll","thunderbert80","alfiealfiealfie","plotagon","PleadingtheYiff","golden430","10_Feet_Higher","thatguy292","UnStumpableDonald","13301","gillymead","cynicsrising","flavorraven","N4tticus","SteveJohnson47","SneezeSpasm","FEAR_THE_TRUMP","stfuusjw","TrumpWonHaha","trumppostin","CensorshipOfReddit","fuckedchildhood","th3An0nyMoose","DEYoungRepublicans","Vonski27","Exile127","Quinn43","BlakeRidley","majorbacon98","Hairyballzak","NamasteCuntface","TheTrumpRecord","kochi1","Blameocrats","loudbounce","MAGAvember_8th","ghostwr1ter","bk112","SoldiersofGod","racemark","J_Dub_TX","Lhtfoot","redditvibe","Ramblin_OnMyMind","gx79","Urbaninja","insickness","rzjoey","dinker","mrshinvari1","stopdropnrofl","JxhnBinder","__wlaurs__","malioswa","rumbletubble","niceboy03","ricolah","UsernameTomorrow","TruthForHarambe"]
with open(os.path.join(os.path.expanduser('~'), 'Desktop', 'data.yaml'), 'r') as f:
    data = yaml.load(f)
auths = [x['author'] for _, x in data.items()]
class Author:
    subreddit = 'the_donald'

    def __init__(self, new=False):
        self.reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                          user_agent=user_agent,
                         )

    def get_author(self, author):
        red = self.reddit.redditor(author)
        #print(red.comment_karma)
        #print(red.link_karma)
        #print(red.submissions)
        #print(red.__dict__)
        created = time.gmtime(red.created)
        #print(created.tm_year)
        if str(created.tm_year) == '2016':

            return author, created
        #print(len([comment for comment in red.comments.top(limit=10000)]))


x = Author()
print(auths)
i = 0
for auth in auths:

    z = x.get_author(auth)
    if z:
        print(z)
        i += 1

print(len(auths), i)

