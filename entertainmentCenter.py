import media
import fresh_tomatoes

the_god_father = media.Movie("The God Father","""The aging patriarch of an organized crime dynasty transfers control of his clandestine 
empire to his reluctant son.""","http://celebmix.com/wp-content/uploads/2017/03/celebrating-45-years-of-the-godfather-01.jpg","https://www.youtube.com/watch?v=sY1S34973zA")

the_shawshank_redemption = media.Movie("The Shawshank Redemption","""Two imprisoned men bond over a number of years,
 finding solace and eventual redemption through acts of common decency.""","http://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm", "https://www.youtube.com/watch?v=6hB3S9bIaco")

schindlers_list = media.Movie("Schindler's List", """In German-occupied Poland during World War II,
 Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.""","https://i.ytimg.com/vi/2tcJLZt6Cnc/maxresdefault.jpg", "https://www.youtube.com/watch?v=M5FpB6qDGAE")

raging_bull= media.Movie("Raging Bull" , """An emotionally self-destructive boxer's journey through life,
 as the violence and temper that leads him to the top in the ring destroys his life outside it.""", "https://thesouloftheplot.files.wordpress.com/2013/03/poster_ragingbull.jpg","https://www.youtube.com/watch?v=YiVOwxsa4OM")

casablanca  = media.Movie("Casablanca" , """In Casablanca in December 1941, a cynical American expatriate
 encounters a former lover, with unforeseen complications. """, "http://www.doctormacro.com/Images/Posters/C/Poster%20-%20Casablanca_13.jpg","https://www.youtube.com/watch?v=BkL9l7qovsE")

citizen_kane = media.Movie("Citizen Kane", """Following the death of a publishing tycoon,
 news reporters scramble to discover the meaning of his final utterance. ""","https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2Mjc1MDQwMl5BMl5BanBnXkFtZTcwNzUyOTUyMg@@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=zyv19bg0scg")

movies =[the_god_father,the_shawshank_redemption,schindlers_list,raging_bull,casablanca,citizen_kane,the_god_father]

fresh_tomatoes.open_movies_page(movies)
