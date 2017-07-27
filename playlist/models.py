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
    TOP = '?sort=-rating'
    LOW = '?sort=rating'
    OLD = '?sort=watched'
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

    ORDER_CHOICES = ( # may want to come up with a few more options
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
    #def __str__(self):
        #return self.mal_or_kitsu_link + self.tv_size + self.youtube_link
        # return self.mal_or_kitsu_link + self.youtube_link + self.mode + self.order + self.tv_size
    def set_yotube_link(self):
        # for now I want this just to return all the shows the user has watched
        if self.kitsu_or_mal == 'kitsu'
            prepare_link_kitsu(self)
            set_youtube_kitsu(self)
        else:
            prepare_link_mal(self)
            set_youtube_mal(self)

    # A method that sets that gets the username from link, will later be used as part of the URL
    # or if a username was supplied it attempts to create a link or returns an error
    def prepare_link_kitsu(self):
        return  0

    def prepare_link_mal(self):
        return 0

    # Do the datascarping neeeded youtube_link from a users already fully prepared kitsu link
    def set_youtube_kitsu(self):
        #do'nt forget to add 'libary to the link'
        return 0

    # Do the datascarping from a users already fully prepared MAL link
    def set_youtube_mal(self):
        return 0
