#!/usr/bin/python
# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

# list of movie objects to follow

# God father : Movie title,storyline, poster url, trailer youtube url
the_god_father = media.Movie(
    'The God Father',
    "The aging patriarch of an organized crime "
    "dynasty transfers control of his clandestine"
    " empire to his reluctant son.",
    'https://resizing.flixster.com/YniHouvJXo_Hz6sgwbGDOSHou3A=/206x305/v1.bTsxMTE3MTYxMjtqOzE3NDk5OzEyMDA7ODAwOzEyMDA',  # NOQA475
    'https://www.youtube.com/watch?v=sY1S34973zA'
)

# The Shawshank Redemption : Movie title,storyline, poster url, trailer
# youtube url
the_shawshank_redemption = media.Movie(
    'The Shawshank Redemption',
    'Two imprisoned men bond over a number of years,finding solace and '
    'eventual redemptionthrough acts of common decency.',
    'https://images-na.ssl-images-amazon.com/images/I/519NBNHX5BL.jpg',
    'https://www.youtube.com/watch?v=6hB3S9bIaco'
)

# Schindler's List : Movie title,storyline, poster url, trailer youtube url
schindlers_list = media.Movie(
    "Schindler's List",
    "In German-occupied Polandduring World War II, Oskar Schindler "
    "gradually becomes concerned for hisJewish workforce after "
    "witnessing their persecution by the Nazi Germans.",
    'https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UY1200_CR85,0,630,1200_AL_.jpg',  # NOQA697
    'https://www.youtube.com/watch?v=JdRGC-w9syA'
)
# Raging Bull : Movie title,storyline, poster url, trailer youtube url
raging_bull = media.Movie(
    'Raging Bull',
    "An emotionally self-destructiveboxer's journey "
    "through life, as the violence and temper that leads"
    " him tothe top in the ring destroys his life outside it.",
    'https://upload.wikimedia.org/wikipedia/en/5/5f/Raging_Bull_poster.jpg',  # NOQA697
    'https://www.youtube.com/watch?v=YiVOwxsa4OM')

# Casablanca : Movie title,storyline, poster url, trailer youtube url
casablanca = media.Movie('Casablanca',
                         "In Casablanca in December 1941, acynical American expatriate"
                         " encounters a former lover, with unforeseencomplications. ",
                         'http://www.doctormacro.com/Images/Posters/C/Poster%20-%20Casablanca_13.jpg',  # NOQA697
                         'https://www.youtube.com/watch?v=BkL9l7qovsE'
                         )
# Citizen Kane : Movie title,storyline, poster url, trailer youtube url
citizen_kane = media.Movie(
    'Citizen Kane',
    'Following the death of a publishingtycoon, news reporters scramble to'
    'discover the meaning of his finalutterance.',
    'https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2Mjc1MDQwMl5BMl5BanBnXkFtZTcwNzUyOTUyMg@@._V1_UY1200_CR90,0,630,1200_AL_.jpg',  # NOQA697
    'https://www.youtube.com/watch?v=zyv19bg0scg'
)

# WALL-E : Movie title,storyline, poster url, trailer youtube url
wall_e = media.Movie(
    'WALL-E ',
    'In the distant future, a smallwaste-collecting robot inadvertently'
    ' embarks on a space journey that willultimately decide the fate of'
    ' mankind.',
    'http://www.gstatic.com/tv/thumb/movieposters/174374/p174374_p_v8_ab.jpg',
    'https://www.youtube.com/watch?v=alIq_wG9FNk'
)

# Ratatouille : Movie title,storyline, poster url, trailer youtube url
ratatouille = media.Movie(
    'Ratatouille',
    'A rat who can cook makes an unusual alliance with a young kitchen'
    ' worker at a famous restaurant.',
    'http://www.gstatic.com/tv/thumb/dvdboxart/165058/p165058_d_v8_aa.jpg',
    'https://www.youtube.com/watch?v=c3sBBRxDAqk'
)

# Finding Nemo : Movie title,storyline, poster url, trailer youtube url
finding_nemo = media.Movie(
    'Finding Nemo ',
    'After his son is captured in theGreat Barrier Reef and taken to Sydney,'
    ' a timid clownfish sets out on ajourney to bring him home. ',
    'http://t1.gstatic.com/images?q=tbn:ANd9GcSoStMb2jeN136xQhf2g3ROpTB9Dker9IlfGbMbwYB3ruC9VcOj',  # NOQA
    'https://www.youtube.com/watch?v=wZdpNglLbt8'
)


# The Jungle Book : Movie title,storyline, poster url, trailer youtube url
the_jungle_book = media.Movie(
    'The Jungle Book',
    'Bagheera the Panther andBaloo the Bear have a difficult time trying'
    ' to convince a boy to leave thejungle for human civilization. ',
    'http://t1.gstatic.com/images?q=tbn:ANd9GcQgNaB5wtt0G7_mTFVygkFtmjWut_Z0QSz2GzDsHeiZDHno4fjh',  # NOQA697
    'https://www.youtube.com/watch?v=C4qgAaxB_pc'
)

# UP : Movie title,storyline, poster url, trailer youtube url
up = media.Movie(
    'Up',
    'Seventy-eight year old Carl Fredricksen travels to Paradise Falls in his'
    ' home equipped with balloons, inadvertently taking ayoung stowaway. ',
    'https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-12561-17yo1p6_142a7bbd.jpeg',  # NOQA697
    'https://www.youtube.com/watch?v=pkqzFUhGPJg')

# creating an list of movie to pass to fresh_tomatoes

movies = [
    the_god_father,
    the_shawshank_redemption,
    schindlers_list,
    raging_bull,
    casablanca,
    citizen_kane,
    wall_e,
    ratatouille,
    finding_nemo,
    the_jungle_book,
    up,
]

# using a pre define program that creates a webpage Takes a list of movie
# objects and creates a web page

fresh_tomatoes.open_movies_page(movies)
