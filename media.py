import webbrowser


class Movie():
    """ Class to define a movie object """


    """ constructor method of movie class"""
    # movie_name:name of movie movie_storyline:description of movie
    # movie_poster:poster image url movie_trailer:youtube trailer url
    
    def __init__(self, movie_name, movie_storyline,
                 movie_poster, movie_trailer):
            self.title = movie_name
            self.storyline = movie_storyline
            self.poster_image_url = movie_poster
            self.trailer_youtube_url = movie_trailer
    ''' method to use for displaying the trailer'''
    
    def showtrailer(self):
        webbrowser.open(self.trailer_youtube)
