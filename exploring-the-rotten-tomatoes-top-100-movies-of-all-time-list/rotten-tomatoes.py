"""
Gather Rotten Tomatoes 100 Best Movies List In Python

"""

__author__ = "Mohamed Abdel-Gawad Ibrahim"
__contact__ = "muhammadabdelgawwad@gmail.com"
__phone__ =  "+201069052620"
__phone__ =  "+201147821232"
__date__ = "25th April, 2021"

import pandas as pd # open source data analysis and manipulation tool
import requests # We import the request library to request the htmls from the web server
import os # import the OS library, too, so we can store the downloaded files and create new folders
from bs4 import BeautifulSoup # library for pulling data out of HTML and XML files, bs4 stands for Beautiful Soup Version 4
# The glob module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell,
# although results are returned in arbitrary order.
import glob
import wptools # Wekipedia API library
# The image module inside pillow package contains some important inbuilt functions like, load images or create new images, etc.
from PIL import Image # best way to download image using Image Module from the Pillow package
from io import BytesIO # a recommended way for downloading non-text content is to download them in bytes.

def critic_reviews():

    """
    Source: Files on Hand
    Thd data set we import here is the critic reviews about the top 100 Rotten Tomatoes movie list,
    while the one we build later in the web scraping function, is the audience reviews.
    """
    df = pd.read_csv('bestofrt.tsv', sep = '\t') # read the flat file (the data set) which is a tab separated
    print('Source: Files on Hand:\n', df.head)


def movies_html():

    """
    Download the top 100 Rotten Tomatoes movie list webpages using the Requests library
    This is one method to work with html files. Another method, is to work with files without downloading them
    which I attached an example function for it after this function (but I made it as a comment since I don't need)
    Saving the HTML files to our computer (using the Requests library for example) library and
    later, read these files into a BeautifulSoup constructor
    """

    # List of the top 100 Rotten Tomatoes movie list
    # To get theses urls, I used chrome's plugin 'Link Klipper' to extract all the urls in the top 100 Rotten Tomatoes movie list
    # Then I extracted them in excel, and concatenated the double quotes at the begining of each url, and a double quote and a comma at the end of each url
    html_urls = ["https://www.rottentomatoes.com/m/it_happened_one_night",
            "https://www.rottentomatoes.com/m/modern_times",
            "https://www.rottentomatoes.com/m/the_wizard_of_oz_1939",
            "https://www.rottentomatoes.com/m/black_panther_2018",
            "https://www.rottentomatoes.com/m/citizen_kane",
            "https://www.rottentomatoes.com/m/parasite_2019",
            "https://www.rottentomatoes.com/m/avengers_endgame",
            "https://www.rottentomatoes.com/m/1003707-casablanca",
            "https://www.rottentomatoes.com/m/knives_out",
            "https://www.rottentomatoes.com/m/us_2019",
            "https://www.rottentomatoes.com/m/toy_story_4",
            "https://www.rottentomatoes.com/m/lady_bird",
            "https://www.rottentomatoes.com/m/mission_impossible_fallout",
            "https://www.rottentomatoes.com/m/blackkklansman",
            "https://www.rottentomatoes.com/m/get_out",
            "https://www.rottentomatoes.com/m/the_irishman",
            "https://www.rottentomatoes.com/m/godfather",
            "https://www.rottentomatoes.com/m/mad_max_fury_road",
            "https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse",
            "https://www.rottentomatoes.com/m/1000626-all_about_eve",
            "https://www.rottentomatoes.com/m/moonlight_2016",
            "https://www.rottentomatoes.com/m/1017293-rebecca",
            "https://www.rottentomatoes.com/m/a_star_is_born_2018",
            "https://www.rottentomatoes.com/m/wonder_woman_2017",
            "https://www.rottentomatoes.com/m/inside_out_2015",
            "https://www.rottentomatoes.com/m/a_quiet_place_2018",
            "https://www.rottentomatoes.com/m/the_cabinet_of_dr_caligari",
            "https://www.rottentomatoes.com/m/eighth_grade",
            "https://www.rottentomatoes.com/m/roma_2018",
            "https://www.rottentomatoes.com/m/booksmart",
            "https://www.rottentomatoes.com/m/dunkirk_2017",
            "https://www.rottentomatoes.com/m/coco_2017",
            "https://www.rottentomatoes.com/m/1015002-night_at_the_opera",
            "https://www.rottentomatoes.com/m/portrait_of_a_lady_on_fire",
            "https://www.rottentomatoes.com/m/the_farewell_2019",
            "https://www.rottentomatoes.com/m/the_shape_of_water_2017",
            "https://www.rottentomatoes.com/m/thor_ragnarok_2017",
            "https://www.rottentomatoes.com/m/selma",
            "https://www.rottentomatoes.com/m/spotlight_2015",
            "https://www.rottentomatoes.com/m/la_grande_illusion",
            "https://www.rottentomatoes.com/m/the_third_man",
            "https://www.rottentomatoes.com/m/seven_samurai_1956",
            "https://www.rottentomatoes.com/m/arrival_2016",
            "https://www.rottentomatoes.com/m/singin_in_the_rain",
            "https://www.rottentomatoes.com/m/the_favourite_2018",
            "https://www.rottentomatoes.com/m/american_in_paris",
            "https://www.rottentomatoes.com/m/logan_2017",
            "https://www.rottentomatoes.com/m/1000642-all_quiet_on_the_western_front",
            "https://www.rottentomatoes.com/m/double_indemnity",
            "https://www.rottentomatoes.com/m/on_the_waterfront",
            "https://www.rottentomatoes.com/m/marriage_story_2019",
            "https://www.rottentomatoes.com/m/et_the_extraterrestrial",
            "https://www.rottentomatoes.com/m/1048445-snow_white_and_the_seven_dwarfs",
            "https://www.rottentomatoes.com/m/the_big_sick",
            "https://www.rottentomatoes.com/m/star_wars_the_last_jedi",
            "https://www.rottentomatoes.com/m/star_wars_episode_vii_the_force_awakens",
            "https://www.rottentomatoes.com/m/1052609-kid",
            "https://www.rottentomatoes.com/m/paddington_2",
            "https://www.rottentomatoes.com/m/boyhood",
            "https://www.rottentomatoes.com/m/best_years_of_our_lives",
            "https://www.rottentomatoes.com/m/1000355-adventures_of_robin_hood",
            "https://www.rottentomatoes.com/m/1011615-king_kong",
            "https://www.rottentomatoes.com/m/once_upon_a_time_in_hollywood",
            "https://www.rottentomatoes.com/m/12_years_a_slave",
            "https://www.rottentomatoes.com/m/manchester_by_the_sea",
            "https://www.rottentomatoes.com/m/leave_no_trace",
            "https://www.rottentomatoes.com/m/argo_2012",
            "https://www.rottentomatoes.com/m/nosferatu",
            "https://www.rottentomatoes.com/m/la_la_land",
            "https://www.rottentomatoes.com/m/alien",
            "https://www.rottentomatoes.com/m/spider_man_far_from_home",
            "https://www.rottentomatoes.com/m/incredibles_2",
            "https://www.rottentomatoes.com/m/1012007-laura",
            "https://www.rottentomatoes.com/m/call_me_by_your_name",
            "https://www.rottentomatoes.com/m/psycho",
            "https://www.rottentomatoes.com/m/zootopia",
            "https://www.rottentomatoes.com/m/1018688-shadow_of_a_doubt",
            "https://www.rottentomatoes.com/m/war_for_the_planet_of_the_apes",
            "https://www.rottentomatoes.com/m/gravity_2013",
            "https://www.rottentomatoes.com/m/1917_2019",
            "https://www.rottentomatoes.com/m/1013139-maltese_falcon",
            "https://www.rottentomatoes.com/m/the_florida_project",
            "https://www.rottentomatoes.com/m/sunset_boulevard",
            "https://www.rottentomatoes.com/m/widows_2018",
            "https://www.rottentomatoes.com/m/beatles_a_hard_days_night",
            "https://www.rottentomatoes.com/m/godfather_part_ii",
            "https://www.rottentomatoes.com/m/the_invisible_man_2020",
            "https://www.rottentomatoes.com/m/the_battle_of_algiers",
            "https://www.rottentomatoes.com/m/baby_driver",
            "https://www.rottentomatoes.com/m/spider_man_homecoming",
            "https://www.rottentomatoes.com/m/top_hat",
            "https://www.rottentomatoes.com/m/pain_and_glory",
            "https://www.rottentomatoes.com/m/never_rarely_sometimes_always",
            "https://www.rottentomatoes.com/m/north-by-northwest",
            "https://www.rottentomatoes.com/m/schindlers_list",
            "https://www.rottentomatoes.com/m/philadelphia_story",
            "https://www.rottentomatoes.com/m/shoplifters",
            "https://www.rottentomatoes.com/m/1013775-metropolis",
            "https://www.rottentomatoes.com/m/1012928-m",
            "https://www.rottentomatoes.com/m/jaws"]

    movies_htmls_folder = 'movies_htmls' # Variable to store the htmls files inside it
    if not os.path.exists(movies_htmls_folder): # check if folder 'movies_htmls' is not created
        os.makedirs(movies_htmls_folder) # and create the folder 'movies_htmls' if it is not created

    print("\nWe have created a directory called 'movies_htmls' in the path of this script; to download the HTML files\n of the top 100 Rotten Tomatoes movie list inside it")

    print('\n\nPlease wait while we download the HTML files of the 100 movies..')
    rank = 1 # the rank variable store the rank number of the movie html. URLs are stored in the list with the order of their rank, from 1 to 100
    # So, we start with rank = 1 and assign it to the name of the first html, then incrment it by 1 before moving to the next html url
    for html_url in html_urls: # Iterate through all the urls in the html_urls list, and assign each url to the variable 'html_url'
        response = requests.get(html_url) # Request the url (html file) from the web server, and save the response inside the variable 'response'

        # Prepare the html file name in this format: (rank)-(end_of_url).html (we must specify the extension we want to save the file with)
        html_name = str(rank) + '-' + html_url.split('/')[-1] + '.html'

        # Create and open a new html file each loop, with the path of the new file, which consists of:
            # The folder name to create inside it the new file, which is stored inside the variable 'movies_htmls_folder'
            # The file's name which we created inside the variable 'html_name'
        # and open the file in web binary mode, since the content of the file is returned in bytes format
        # and finally use the keyword 'file' to express the new file with it.
        with open(os.path.join(movies_htmls_folder, html_name) , mode = 'wb') as file:
            file.write(response.content) # write the content of the 'response' variable inside the new created file
        rank += 1 # increase the rank by 1 before looping to the next movie url (Remember that urls are ordered by their rank and stored in the list with that order )

    print("\n\nDone! We've downloaded the HTML files of the top 100 Rotten Tomatoes movie list inside the directory 'movies_htmls'")


#def online_html():

#    """
#    Second Method: Using Requests library & BeautifulSoup constructor
#    Reading the HTML response content directly into a BeautifulSoup constructor
#    (again using the Requests library for example)
#    """
#    url = 'https://www.rottentomatoes.com/m/et_the_extraterrestrial'
#    response = requests.get(url)
#    # Work with HTML in memory
#    from bs4 import BeautifulSoup #library for pulling data out of HTML and XML files, bs4 stands for Beautiful Soup Version 4
#    soup = BeautifulSoup(response.content)

def audience_reviews():

    """
    Source: Web Scraping
    The data set we build here is the audience reviews for the 100 best movies in Rotten Tomatoes website.
    We will build this data set row by row with web scraping the pages of these movies, then extract the
    information we want from them.

    Web Scraping is a fancy way of saying extracting data from websites using code.

    We want to extract 3 items of each webpage:
        - The title of the movie
        - The audience score
        - The number of audience who rated the movie

    Steps are:
    1. Creates an empty list, df_list, to which dictionaries will be appended.
    This list of dictionaries will eventually be converted to a pandas DataFrame (this is the most efficient way of building a DataFrame row by row).
    2. Loops through each movie's Rotten Tomatoes HTML file in the rt_html folder.
    3. Opens each HTML file and passes it into a file handle called file, then extrac the info we need using BeautifulSoup.
    4. Creates a DataFrame called df by converting df_list using the pd.DataFrame constructor.
    """
    df_list = [] # An empty list, that will be a list of dictionaries to build file by file and later convert it to a DataFrame
    # Each dictionary entry will have title, audience_score, and number_of_audience_ratings for each movie

    folder_html = 'rt_html' # A string variable contains the folder name that holds the HTML files of the 100 rotten tomatoes movies inside the script's directory

    # A loop to capture the title, audience score, and number of audience ratings for each movie, then append them to the list of dictionaries
    print("\n\nPlease wait while we create the data set of the top 100 Rotten Tomatoes movie list")
    for movie_html in os.listdir(folder_html): # We itrate through all the files inside the HTML folder.
    # We take one file in each loop and assign its name (with extension) to movie_html variable

        with open(os.path.join(folder_html, movie_html)) as file: # First step in Web Scraping: Pass the file path into a 'file handle', and give it a shortname 'file'
        # Error so I used encoding: UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 214742: character maps to <undefined>
        # The file's path consists of the folder name which is saved in 'folder_html' variable, followed by the movie html file name with its extension,
        # which is saved in the movie_html variable. Both variables are joined through os.path.join() method, which combines one or more path names into a
        # single path. os.path.join() automatically adds any required forward slashes into a file path name

            soup = BeautifulSoup(file, 'lxml') # We make the soup! And make it use the most popular parser which is called 'lxml'
            # lxml is a Python library which allows for easy handling of XML and HTML files, and can also be used for web scraping
            # soup now returns the HTML structure of the webpage which its path inside the file handle: 'file'
            # The soup looks exactly like an HTML document, but in actuality, we can use methods in the beautiful Soup library to
            # easily find and extract data from this HTML
            # one of the most popular methods is the find() method, which scans the entire document looking for results

            # The title of the movie exists inside title tag, which happens to be the only title tag in the whole document
            title = soup.find('title').contents[0][0: - len(' - Rotten Tomatoes')] # This is actually the title of the webpage, not the title of the movie. It returns:
            # <title>E.T. The Extra-Terrestrial (1982) - Rotten Tomatoes</title> to get the movie title only, we have to do some simple string slicing to remove that
            # .contents returns a list of the tags children: ['E.T. The Extra-Terrestrial (1982) - Rotten Tomatoes']
            # The title has index [0] in the previous list, and it's the only item in the list. So, we select it using index [0]
            # which returns: E.T. The Extra-Terrestrial (1982) - Rotten Tomatoes
            # To remove the unwanted part in the title ' - Rotten Tomatoes'. We should select all characters in the strings from the start of the title,
            # to the start of that unwanted part. We access the start of unwanted part by getting the the length of that unwanted part, and negative indexing it.
            # Final output returns the title successfully: E.T. The Extra-Terrestrial (1982)

            # To find the audience score, we inspec it in the browser, to find out that its html structure is the following:
            # <span class="superPageFontColor" style="vertical-align:top">97%</span>
            # When we open the html code, We find that it exits in an outer html structure as following:
            # <div class="audience-score meter">
            #   <a href="#audience_reviews" class="unstyled articleLink">
            #       <div class="meter media">
            #           <div class="meter-tomato icon big medium-xs upright pull-left"></div>
            #           <div class="media-body" style="line-height:36px">
            #               <div class="meter-value">
            #                   <span class="superPageFontColor" style="vertical-align:top">97%</span>
            #               </div>
            #               <div class="smaller bold hidden-xs superPageFontColor" style="padding-left:5px;line-height:12px">liked it</div>
            #           </div>
            #       </div>
            #   </a>
            # </div>
            # The class of the outer div seems to exists only once, so we use it to filter on it.
            # The score exits in the first span element from the start, so we filter on it, and since there is no more tags inside it, we use the contents keyword
            # it returns a list contains the audience score: ['97%']. So, we choose it by its index [0]
            # Last step is to get rid of the percentage % mark, and we do it by string indexing and using negative indexing at the end of the selection.
            audience_score = soup.find('div', class_ = 'audience-score meter').find('span').contents[0][:-1] # Returns the audience score: 97

            # To find the number of audience ratings, we inspect it in the web page, then we can copy the number of audience ratings
            # and search it in the html code, to find its html structure as following:
            # <div class="audience-info hidden-xs superPageFontColor">
            #    <div>
            #        <span class="subtle superPageFontColor">Average Rating:</span>
            #        4.2/5
            #    </div>
            #    <div>
            #        <span class="subtle superPageFontColor">User Ratings:</span>
            #        103,672
            #    </div>
            # </div>
            # We find that there is a unique div with the class of 'audience-info hidden-xs superPageFontColor' so we filter using it.
            # The number of audience exits in the second div child, so we use find_all function to returns all the children div tags, so we can choose the second tag
            # that has the info we need. It returns a list of two items, the first one contains the first complete div structure, and the second one contains the
            # complete structue of the second div that we are interested in. So, we choose the second element by its index [1]
            # We find that the number of audience exists directly in the content of the div, and not nested in any more tags, so we use the contents keyword.
            # The contetns keyword returns the following list:
            # ['\n', <span class="subtle superPageFontColor">User Ratings:</span>, '\n        103,672']
            # the number of audience is the third elements, so we choose it by its index [2].
            # We see that it has a lot of space before it, so, we use the strip() method to delete all the unnecessary spaces
            # Finally, we find that the number we get has a comma inside it: 103,672 , which prevents us from using it as an integer, so, we need to remove that comma
            # We use the replace() method; to replace the comma with an empty character to remove the comma
            # Final output is: 103672
            num_audience_ratings = soup.find('div', class_ = 'audience-info hidden-xs superPageFontColor').find_all('div')[1].contents[2].strip().replace(',' , '')

            # Append the 3 variables that we scraped of the webpage, to a dictionary inside the list of dictionaries we created in the begining 'df_list'
            df_list.append({'title' : title ,
                            'audience_score' : audience_score ,
                            'number_of_audience_ratings' : num_audience_ratings })

    # After the loop finished iterating over the 100 webpages, and assigned them to 100 dictionaries, we now create a DataFrame of the list of the dictionaries
    df = pd.DataFrame(df_list, columns = ['title', 'audience_score', 'number_of_audience_ratings']) # We pass the list of dictionaries and the columns titles
    print(df.head(10)) # Print the first 10 rows of the DataFrame to check if we did a good job :)

def download_ebert_reviews():
    """
    Source: Downloading Files from the Internet
    data set: Ebert reviews for the top 100 Rotten Tomatoes movie list

    So now we can start the Roger Ebert review word cloud. So the first thing we need, the text from each of his reviews,
    for each of the movies on the Rotten Tomatoes Top 100 Movies of All Time list.
    They live on his website. All of this text is gathered in the form of 100.txt files on Udacity hosted web page
    and we're going to download them all programmatically.
    """
    folder_name = 'ebert_reviews' # save the folder name
    if not os.path.exists(folder_name): # Check if the folder is Not already created
        os.makedirs(folder_name) # then creates the folder ebert_reviews if it doesn't exist already

    # Here comes the actual bit of request code

    # The following URL is for the Roger Ebert reviews text file that is saved on new Udacity's servers.
    url = 'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9904_11-e.t.-the-extra-terrestrial/11-e.t.-the-extra-terrestrial.txt'
    response = requests.get(url) # We use requests.get() method on a URL, and that returns a response
    # We can't see it currently, but all the text in our text file is actually in
    # our computer's working memory right now within this response variable.
    # It's stored in the body of the response which we can access using .content,

    # The first step in writing to a file is create the file object by using the built-in Python command “open”. To create and write to a new file
    # use open with “wb” option, to write a content that is in bytes and not text.
    # A common way to work with files in Python is to create file handler with “open” statement and work with the file.
    # After finishing the work with the file, we need to close the file handler with close statement
    # Often, it is hard to remember to close the file once we are done with the file. Python offers an easy solution for this.
    # We can use with statement in Python such that we don’t have to close the file handler. The with statement creates a context manager
    # and it will automatically close the file handler for us when we are done with it
    with open(os.path.join( folder_name, url.split('/')[-1] ), mode = 'wb') as file: # Now 'file' keyword represents the new file that we created and opened
        file.write(response.content) # we use the .write() method to write the content of the new created and opended file

    # That's how we download one file programmatically. To download the rest of review files,
    # We first have to provid the URLs we need to download, then write a for loop, and download all of the Roger Ebert review files programmatically.

    # Here are the 88 urls of the 88 reviews that Ebert has done. There are 12 movies in the top 100 Rotten Tomatoes list didn't have reviews on Roger Ebert's site
    # I have commented the url in the below list, that we've just already downloaded above
    ebert_review_urls = ['https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9900_1-the-wizard-of-oz-1939-film/1-the-wizard-of-oz-1939-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9901_2-citizen-kane/2-citizen-kane.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9901_3-the-third-man/3-the-third-man.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9902_4-get-out-film/4-get-out-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9902_5-mad-max-fury-road/5-mad-max-fury-road.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9902_6-the-cabinet-of-dr.-caligari/6-the-cabinet-of-dr.-caligari.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9903_7-all-about-eve/7-all-about-eve.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9903_8-inside-out-2015-film/8-inside-out-2015-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9903_9-the-godfather/9-the-godfather.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9904_10-metropolis-1927-film/10-metropolis-1927-film.txt',
                     #'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9904_11-e.t.-the-extra-terrestrial/11-e.t.-the-extra-terrestrial.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9904_12-modern-times-film/12-modern-times-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9904_14-singin-in-the-rain/14-singin-in-the-rain.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9905_15-boyhood-film/15-boyhood-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9905_16-casablanca-film/16-casablanca-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9905_17-moonlight-2016-film/17-moonlight-2016-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9906_18-psycho-1960-film/18-psycho-1960-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9906_19-laura-1944-film/19-laura-1944-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9906_20-nosferatu/20-nosferatu.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9907_21-snow-white-and-the-seven-dwarfs-1937-film/21-snow-white-and-the-seven-dwarfs-1937-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9907_22-a-hard-day27s-night-film/22-a-hard-day27s-night-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9907_23-la-grande-illusion/23-la-grande-illusion.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9908_25-the-battle-of-algiers/25-the-battle-of-algiers.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9908_26-dunkirk-2017-film/26-dunkirk-2017-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9908_27-the-maltese-falcon-1941-film/27-the-maltese-falcon-1941-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9909_29-12-years-a-slave-film/29-12-years-a-slave-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9909_30-gravity-2013-film/30-gravity-2013-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9909_31-sunset-boulevard-film/31-sunset-boulevard-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990a_32-king-kong-1933-film/32-king-kong-1933-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990a_33-spotlight-film/33-spotlight-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990a_34-the-adventures-of-robin-hood/34-the-adventures-of-robin-hood.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990b_35-rashomon/35-rashomon.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990b_36-rear-window/36-rear-window.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990b_37-selma-film/37-selma-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990c_38-taxi-driver/38-taxi-driver.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990c_39-toy-story-3/39-toy-story-3.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990c_40-argo-2012-film/40-argo-2012-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990d_41-toy-story-2/41-toy-story-2.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990d_42-the-big-sick/42-the-big-sick.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990d_43-bride-of-frankenstein/43-bride-of-frankenstein.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990d_44-zootopia/44-zootopia.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990e_45-m-1931-film/45-m-1931-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990e_46-wonder-woman-2017-film/46-wonder-woman-2017-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990e_48-alien-film/48-alien-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990f_49-bicycle-thieves/49-bicycle-thieves.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990f_50-seven-samurai/50-seven-samurai.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad990f_51-the-treasure-of-the-sierra-madre-film/51-the-treasure-of-the-sierra-madre-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9910_52-up-2009-film/52-up-2009-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9910_53-12-angry-men-1957-film/53-12-angry-men-1957-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9910_54-the-400-blows/54-the-400-blows.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9911_55-logan-film/55-logan-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9911_57-army-of-shadows/57-army-of-shadows.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9912_58-arrival-film/58-arrival-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9912_59-baby-driver/59-baby-driver.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9913_60-a-streetcar-named-desire-1951-film/60-a-streetcar-named-desire-1951-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9913_61-the-night-of-the-hunter-film/61-the-night-of-the-hunter-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9913_62-star-wars-the-force-awakens/62-star-wars-the-force-awakens.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9913_63-manchester-by-the-sea-film/63-manchester-by-the-sea-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9914_64-dr.-strangelove/64-dr.-strangelove.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9914_66-vertigo-film/66-vertigo-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9914_67-the-dark-knight-film/67-the-dark-knight-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9915_68-touch-of-evil/68-touch-of-evil.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9915_69-the-babadook/69-the-babadook.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9915_72-rosemary27s-baby-film/72-rosemary27s-baby-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9916_73-finding-nemo/73-finding-nemo.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9916_74-brooklyn-film/74-brooklyn-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9917_75-the-wrestler-2008-film/75-the-wrestler-2008-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9917_77-l.a.-confidential-film/77-l.a.-confidential-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9918_78-gone-with-the-wind-film/78-gone-with-the-wind-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9918_79-the-good-the-bad-and-the-ugly/79-the-good-the-bad-and-the-ugly.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9918_80-skyfall/80-skyfall.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9919_82-tokyo-story/82-tokyo-story.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9919_83-hell-or-high-water-film/83-hell-or-high-water-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9919_84-pinocchio-1940-film/84-pinocchio-1940-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad9919_85-the-jungle-book-2016-film/85-the-jungle-book-2016-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991a_86-la-la-land-film/86-la-la-land-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991b_87-star-trek-film/87-star-trek-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991b_89-apocalypse-now/89-apocalypse-now.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991c_90-on-the-waterfront/90-on-the-waterfront.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991c_91-the-wages-of-fear/91-the-wages-of-fear.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991c_92-the-last-picture-show/92-the-last-picture-show.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991d_93-harry-potter-and-the-deathly-hallows-part-2/93-harry-potter-and-the-deathly-hallows-part-2.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991d_94-the-grapes-of-wrath-film/94-the-grapes-of-wrath-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991d_96-man-on-wire/96-man-on-wire.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991e_97-jaws-film/97-jaws-film.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991e_98-toy-story/98-toy-story.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991e_99-the-godfather-part-ii/99-the-godfather-part-ii.txt',
                     'https://d17h27t6h515a5.cloudfront.net/topher/2017/September/59ad991e_100-battleship-potemkin/100-battleship-potemkin.txt']

    for ebert_review in ebert_review_urls: # Iterate for the items (urls) in the ebert_review_urls list, one by one, and save the url each loop inside ebert_review variable
        response = requests.get(ebert_review) # send a request to the web server to return the contents of the file we requested and save it inside the response variable
        # Create and open a new file each loop, with the path of the new file, which consists of:
            # The folder name to create inside it the new file
            # The file's name which we select form the url of the file
        # and open the file in web binary mode, since the content of the file is returned in bytes format
        # and finally use the keyword 'file' to express the new file with it.
        with open(os.path.join( folder_name , ebert_review.split('/')[-1]) , mode = 'wb') as file:
            file.write(response.content) # use .write() method on the new file to write the content of the response we've received inside the new file

def import_ebert_reviews():
     """
     Gathering data from text files in Python means opening and reading from files. If you're using Pandas like we are here,
     then this also means storing the text data you just read in a Pandas data frame. We have 88 Roger Ebert reviews to open and read.
     We'll need a loop to iterate through all of the files in this folder to open and read each. There are two main ways of doing this.
     One using the OS library and the other using a library called glob.
     OS library is good if you're sure you want to open every file in the folder, like our case here.
     Every file in this folder is a Roger Ebert review text file. But I'll switch it up here and use glob instead.
     The glob library allows for Unix-style pathname pattern expansion, which is a fancy way of saying,
     using something called glob patterns to specify sets of filenames. These glob patterns use something called wildcard characters.
     glob.glob returns a list of path name that match pathname, i.e. this is where the glob pattern goes.
     How can we use this? We want all file names that end in.txt, which in this Ebert reviews folder, is all of them.
     And because glob.glob returns a list, we can loop through that directly here.

     In Python 3, when opening text to read, you should actually always use open with an explicit encoding,
     which comes after the encoding parameter. Doing so means you get correctly decoded Unicode, or an error right off the bat,
     What's the actual encoding?
     That depends on the source of the text. Let's use Roger Ebert's review for the movie Casablanca as a working example.
     If we inspect the review page's source, which we can do in various browsers by right clicking and selecting View page source or something of like,
     you'll find that the encoding is utf-8.
     """

     """
     We don't want all of text data in one big chunk though, which would be done with file.read()
     Instead, we want the first line (the movie title), the second line (the URL),
     and then everything from the third line onwards (the review text), as separate pieces of data,
     so we can't just use file.read() here. Since text files are separated by newline characters and the file object returned from with open,
     as file, is an iterator, we can read the file line by line.
     If we just want to read one line, you use.readline, like so, file.readline()
     There's actually a bit of white space below here, which is actually the \n, or the newline character.
     We can get rid of that by slicing it off at the end of these string.
     Next, we're going to grab the URL and the full review text.
     But before that, recall that we want all this data in a Pandas data frame, so we need to build one.
     The most computationally efficient way to do that is first to create an empty list then populate that list one by one as we iterate through this loop,
     and we'll fill this list with dictionaries. That list of dictionaries will later be converted to
     a Pandas data frame, all at once, once all of the data has been gathered.
     Your task is to grab the review URL, and then the full review text, and then append it to the list of dictionaries.

     The Jupyter Notebook below contains template code that:
     Creates an empty list, df_list, to which dictionaries will be appended. This list of dictionaries will eventually be converted to a pandas DataFrame (this is the most efficient way of building a DataFrame row by row).
     Loops through each movie's Roger Ebert review text file in the ebert_reviews folder.
     Opens each text file using a path generated by glob and passes it into a file handle called file.
     Creates a DataFrame called df by converting df_list using the pd.DataFrame constructor.
     Your task is to extract the movie title, Roger Ebert review URL, and the review in each text file and append each trio as a dictionary to df_list.

     The file methods required for this task are:

     readline()
     read()
    """
    df_list = []
    for ebert_review in glob.glob('ebert_reviews/*.txt'): # iterate over all the files in the 'ebret_reviews' folder that ends with .txt
        with open(ebert_review, encoding = 'utf-8') as file:
            title = file.readline()[:-1]
            review_url = file.readline()[:-1]
            review_text = file.read()
            df_list.append({'title' : title,
                            'review_url' : review_url,
                            'review_text' : review_text})

    df = pd.DataFrame(df_list, columns = ['title', 'review_url', 'review_text'])


def poster_images(): # Download movies poster

    # To access Wikipedia page data via the MediaWiki API with wptools, you need each movie's Wikipedia page title,
    # i.e., what comes after the last slash in en.wikipedia.org/wiki/ in the URL. So, we've gathered all of them in a list to iterate over them.
    title_list = [   'The_Wizard_of_Oz_(1939_film)',
                     'Citizen_Kane',
                     'The_Third_Man',
                     'Get_Out_(film)',
                     'Mad_Max:_Fury_Road',
                     'The_Cabinet_of_Dr._Caligari',
                     'All_About_Eve',
                     'Inside_Out_(2015_film)',
                     'The_Godfather',
                     'Metropolis_(1927_film)',
                     'E.T._the_Extra-Terrestrial',
                     'Modern_Times_(film)',
                     'It_Happened_One_Night',
                     "Singin'_in_the_Rain",
                     'Boyhood_(film)',
                     'Casablanca_(film)',
                     'Moonlight_(2016_film)',
                     'Psycho_(1960_film)',
                     'Laura_(1944_film)',
                     'Nosferatu',
                     'Snow_White_and_the_Seven_Dwarfs_(1937_film)',
                     "A_Hard_Day%27s_Night_(film)",
                     'La_Grande_Illusion',
                     'North_by_Northwest',
                     'The_Battle_of_Algiers',
                     'Dunkirk_(2017_film)',
                     'The_Maltese_Falcon_(1941_film)',
                     'Repulsion_(film)',
                     '12_Years_a_Slave_(film)',
                     'Gravity_(2013_film)',
                     'Sunset_Boulevard_(film)',
                     'King_Kong_(1933_film)',
                     'Spotlight_(film)',
                     'The_Adventures_of_Robin_Hood',
                     'Rashomon',
                     'Rear_Window',
                     'Selma_(film)',
                     'Taxi_Driver',
                     'Toy_Story_3',
                     'Argo_(2012_film)',
                     'Toy_Story_2',
                     'The_Big_Sick',
                     'Bride_of_Frankenstein',
                     'Zootopia',
                     'M_(1931_film)',
                     'Wonder_Woman_(2017_film)',
                     'The_Philadelphia_Story_(film)',
                     'Alien_(film)',
                     'Bicycle_Thieves',
                     'Seven_Samurai',
                     'The_Treasure_of_the_Sierra_Madre_(film)',
                     'Up_(2009_film)',
                     '12_Angry_Men_(1957_film)',
                     'The_400_Blows',
                     'Logan_(film)',
                     'All_Quiet_on_the_Western_Front_(1930_film)',
                     'Army_of_Shadows',
                     'Arrival_(film)',
                     'Baby_Driver',
                     'A_Streetcar_Named_Desire_(1951_film)',
                     'The_Night_of_the_Hunter_(film)',
                     'Star_Wars:_The_Force_Awakens',
                     'Manchester_by_the_Sea_(film)',
                     'Dr._Strangelove',
                     'Frankenstein_(1931_film)',
                     'Vertigo_(film)',
                     'The_Dark_Knight_(film)',
                     'Touch_of_Evil',
                     'The_Babadook',
                     'The_Conformist_(film)',
                     'Rebecca_(1940_film)',
                     "Rosemary%27s_Baby_(film)",
                     'Finding_Nemo',
                     'Brooklyn_(film)',
                     'The_Wrestler_(2008_film)',
                     'The_39_Steps_(1935_film)',
                     'L.A._Confidential_(film)',
                     'Gone_with_the_Wind_(film)',
                     'The_Good,_the_Bad_and_the_Ugly',
                     'Skyfall',
                     'Rome,_Open_City',
                     'Tokyo_Story',
                     'Hell_or_High_Water_(film)',
                     'Pinocchio_(1940_film)',
                     'The_Jungle_Book_(2016_film)',
                     'La_La_Land_(film)',
                     'Star_Trek_(film)',
                     'High_Noon',
                     'Apocalypse_Now',
                     'On_the_Waterfront',
                     'The_Wages_of_Fear',
                     'The_Last_Picture_Show',
                     'Harry_Potter_and_the_Deathly_Hallows_–_Part_2',
                     'The_Grapes_of_Wrath_(film)',
                     'Roman_Holiday',
                     'Man_on_Wire',
                     'Jaws_(film)',
                     'Toy_Story',
                     'The_Godfather_Part_II',
                     'Battleship_Potemkin'
                    ]

    folder_name = 'bestofrt_posters' # Folder name to save inside it the poster images
    # Make directory if it doesn't exist
    if not os.path.exists(folder_name): # Check if the directory DOESNOT exist
        os.makedirs(folder_name) # If not, create it as a new directory

    # List of dictionaries to build and convert to a DataFrame later
    df_list = [] # Create an empty list (of dictionaries) to hold all the dictionaries that we will create (a dictionary for each movie) then convert it into a DataFrame
    errors_list = [] # A list to hold all the errors when trying to download all the posters; to download them individually later.
    for title in title_list: # Iterate through all the title_list, to access each movie's page with wptools API
        try: # Since we already expect to get some errors in downloading the posters, we want to handle the errors and continue running the script
            ranking = title_list.index(title) + 1 # Since the title_list is saved with their ranking from 1 to 100, we will use their index in the list to save their actual ranking
            print(ranking) # print ranking to gauge time remaining
            page = wptools.page(title, silent = True) # Access the webpage of the movie via the API. Returns the JSON structue of all the webpages
            # silence attribute = True because Instance attributes echo automatically. You can turn that off with silent=True
            images = page.get().data['image'] # Access all the images in the webpage. Returns a list of all the images in the webpage (JSON structured)
            # First image is usually the poster
            first_image_url = images[0]['url'] # Access the poster image in the JSON structure. Returns the poster url
            r = requests.get(first_image_url) # Request to download the url from the webserver. Returns the server respone (Image content bytes)
            i = Image.open(BytesIO(r.content)) # Download movie poster image using the Image module from the Pillow package and
            image_file_format = first_image_url.split('.')[-1] # Return the image format (jpg, png) since it exists in the end of the poster url
            # This one was a big headache! 2 files was created but their size was 0 bytes and had errors!
            # After debugging, I found out the issue was that there is a column ':' in their title, and we the script tried to save the image
            # with a column in the title, it resulted in an error! So, before saving the image, we delete this character from the title
            title = title.replace(":","")
            i.save(folder_name + '/' + str(ranking) + '_' + title + '.' + image_file_format) # Save the new image. When we downloaded the image, it was saved in RAM.
            # Append to list of dictionaries
            df_list.append({'ranking' : ranking, # Save the rank of the movie
                            'title' : title, # Save the title of the movie
                            'poster_url' : first_image_url}) # Save the image URL

        # Not best practice to catch all exceptions but fine for this short script
        except Exception as e:
            print(str(ranking) + '_' + title + ':' + str(e)) # Print the rank and the title of the movie which was failed to download its image poster, and the error message
            errors_list.append(str(ranking) + '_' + title) # Append the rank and title of the movie in the list to download them individually later in the code

    # Once we have completed the above code requirements, print the errors to interpret their output.
    print("\nposter images that failed to download:")
    for rank_and_title in errors_list:
        print(rank_and_title) # print the title and rank of the movies that failed to download

    # Inspect unidentifiable images and download them individually
    # Rank over the dictionary of errors and return the key as a rank_title (since the key was the ranking concatenated with the movie title)
    # and return the value as images since
    for rank_title in errors_list: # Iterate through all the title in the errors list and return each title in rank_title variable
    # I provided the posters urls for the movies that failed to download. We iterate over them and check on each one to download its url
        if rank_title == "22_A_Hard_Day%27s_Night_(film)":
            url = "https://upload.wikimedia.org/wikipedia/en/4/47/A_Hard_Days_night_movieposter.jpg"
        if rank_title == "40_Argo_(2012_film)":
            url = "https://upload.wikimedia.org/wikipedia/en/e/e1/Argo2012Poster.jpg"
        if rank_title == "72_Rosemary%27s_Baby_(film)":
            url = "https://upload.wikimedia.org/wikipedia/en/thumb/e/ef/Rosemarys_baby_poster.jpg/220px-Rosemarys_baby_poster.jpg"

        title = rank_title[3:] # Since rank_title is the ranking and the title, remove the ranking (first 3 characters) then save the title in title variable
        # Append in the list of dictionaries: a new dictionary  consists of:
        df_list.append({'ranking' : int(title_list.index(title) + 1), # the ranking depending on its index in the original list of titles
                        'title' : title, # the title (after removing the ranking)
                        'poster_url' : url}) # the new url

        # Repeat the download process to download the new urls:
        r = requests.get(url)
        i = Image.open(BytesIO(r.content))
        image_file_format = url.split('.')[-1]
        i.save(folder_name + '/' + rank_title + '.' + image_file_format)

    print("\nIssue is resolved! We downloaded the previous poster images successfully!\n")
    # Create DataFrame from list of dictionaries
    df = pd.DataFrame(df_list, columns = ['ranking', 'title', 'poster_url'])
    # Sort the DataFrame based on the ranking and drop the pandas original index
    # drops the current index of the DataFrame and replaces it with an index of increasing integers. It never drops columns.
    df = df.sort_values('ranking').reset_index(drop = True)
    print(df.head())


def main():
    """ The main function """
    critic_reviews()
    movies_html()
    reading_html()
    web_scraping()
    download_ebert_reviews()
    import_txt()
    poster_images()

if __name__ == "__main__":
    main()
