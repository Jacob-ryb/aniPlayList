import urllib

from django.db import models
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class PlayList(models.Model):
    mal_or_kitsu_link = models.TextField(max_length=50, blank=False) #Text becuase user can enter just the username
    youtube_link = models.TextField(blank=True)  # change to URLField later, for now I just want to return all the shows
    #user_slug = models.SlugField(max_length=25) # This may eventually be the primary key
    # choices
    # could use an array to switch between mal and kitsu in the method
    MAL =  'My Anime List'
    KITSU = 'Kitsu'
    DONE = '&status=completed'  # hardcoded to kitsu's for now, will change later
    WATCHING = '&status=current'
    PTW = '&status=planned'
    HOLD = '&status=completed'
    DROPPED = '&status=dropped'  # add order first to the link sent to BS
    TOP = 'library?sort=-rating'
    LOW = 'library?sort=rating'
    OLD = 'library?sort=watched'
    FULL = "Full size"
    TV = "TV size"

    KITSU_MAL_CHOICES = (
        (KITSU, 'Kitsu'),
        (MAL, 'My Anime List'),
    )
    MODE_CHOICES = (
        (DONE, 'Completed'),
        (WATCHING, 'Currently watching'),
        (PTW, 'Plan to watch'),
        (HOLD, 'On hold'),
        (DROPPED, 'droped'),  # why would some want to willingly listen to trash?
    )

    ORDER_CHOICES = ( # may want to include a random option later
        (TOP, "Highest rated first"),
        (LOW, "Lowest rated first"),
        (OLD, "Oldest first"),
    )
    SIZE_CHOICES = (
        (FULL, "Full size"),
        (TV, "TV size"),
    )
    size = models.CharField(
        max_length=25,
        choices=SIZE_CHOICES,
        default=FULL,
    )


    kitsu_or_mal = models.CharField(
        max_length=25,
        choices=KITSU_MAL_CHOICES,
        default=KITSU,
    )
    mode = models.CharField(
        max_length=25,
        choices=MODE_CHOICES,
        default=DONE
    )

    order = models.CharField(
        max_length=25,
        choices=ORDER_CHOICES,
        default=TOP
    )

    def start_data_scarping(self): # needs better name
        if self.kitsu_or_mal == 'kitsu':
            self.prepare_link_kitsu(self)
        else:
            self.prepare_link_mal(self)

    # A method that sets that gets the username from link, will later be used as part of the URL
    # or if a username was supplied it attempts to create a link or returns an error
    def prepare_link_kitsu(self):
        if '/' not in self.mal_or_kitsu_link: # the user has only given us a username
            self.kitsu_or_mal= 'https://kitsu.io/users/' + self.kitsu_or_mal + '/'
        self.kitsu_or_mal = self.kitsu_or_mal + self.order + self.mode # assuming url is valid we complete it
        self.set_youtube_kitsu()

    def prepare_link_mal(self):
        if '/' in self.mal_or_kitsu_link: # The user given us a link but we need to format at as mal is stupid
            self.mal_or_kitsu_link =  self.mal_or_kitsu_link[self.mal_or_kitsu_link.find('profile/')+8:self.mal_or_kitsu_link.find('?')] # maybe get rid of the hard coded +8
            # maybe do a second if in case the user gives us their list already instead of profile

        self.mal_or_kitsu_link =  'https://myanimelist.net/animelist/' + self.mal_or_kitsu_link + "?"
        self.set_youtube_mal(self)

    def set_youtube_kitsu(self):
        try:
            Uclient = urllib.request.Request(self.kitsu_or_mal, headers={'User-Agent': 'Mozilla/5.0'}) # dont forget to close this later
            page_html = Uclient.read()
            page_soup = soup(page_html, "html.parser")
        except:
            self.mal_or_kitsu_link = 'There appeared to be some sort of error, please try agian and make sure to enter'

    # I'm repaeating myself so maybe we need another function here
    # form error checking needs to be returned in a bitter way
    def set_youtube_mal(self):
        try:
            Uclient = uReq(self.kitsu_or_mal) # dont forget to close this later
            page_html = Uclient.read()
            page_soup = soup(page_html, "html.parser")
        except:
            self.mal_or_kitsu_link = 'There appeared to be some sort of error, please try agian and make sure to enter'
