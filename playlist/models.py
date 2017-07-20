from django.db import models
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class PlayList(models.Model):
    mal_or_kitsu_link = models.URLField(max_length=200, blank=False)
    tv_size = models.BooleanField()
    youtube_link = models.TextField(blank=True)  # change to URLField later, for now I just want to return all the shows
    # is_kitsu = models.BooleanField() # if the link is mal or kitsu
    #user_slug = models.SlugField(max_length=25) # This may eventually be the primary key
    # choices
    # could use an array to switch between mal and kitsu in the method
    DONE = '&status=completed'  # hardcoded to kitsu's for now, will change later
    WATCHING = '&status=current'
    PTW = '&status=planned'
    HOLD = '&status=completed'
    DROPPED = '&status=dropped'  # add order first to the link sent to BS
    TOP = '?sort=-rating'
    LOW = '?sort=rating'
    OLD = '?sort=watched'

    MODE_CHOICES = (
        (DONE, 'Completed'),
        (WATCHING, 'Currently watching'),
        (PTW, 'Plan to watch'),
        (HOLD, 'On hold'),
        (DROPPED, 'droped'),  # Why would some want to willingly listen to trash?
    )

    ORDER_CHOICES = (
        (TOP, "Highest first"),
        (LOW, "Lowest first"),
        (OLD, "Oldest"),
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


    def __str__(self):
        return self.mal_or_kitsu_link + self.tv_size + self.youtube_link
        # return self.mal_or_kitsu_link + self.youtube_link + self.mode + self.order + self.tv_size

    #def set_yotube_link(self):
        # for now I want this just to return all the shows the user has watched
        # do'nt forget to add 'libary to the link'
        #return self.youtube_link

    #def set_yotube_mal_kitsu(self):  # deals with changing  the mode and order settings if link is mal or kitsu
        #return
