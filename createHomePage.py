import requests
from random import choice


def createHomePage(emailuserName):
    """Write an example web page to a file.
    Args:
    fileName (str): Name of the file to write HTML to.


    """
    firstname, lastname = emailuserName.split(".")
    file = open(emailuserName+".html", 'w')
    
    file.write(createDocType())
    
    file.write(startHTML())
    
    file.write(createHead())

    file.write(createTitle(f'{firstname}\'s Home Page'))

    file.write(endHead())
    
    file.write(startBody())
    file.write(createParagraph(findTemperatureLive2()))
    
    file.write(createHeading(f"Welcome to {firstname}'s Home Page"))
    file.write(createParagraph(findTemperatureLive()))
    

    file.write(createParagraph(f'Hi! I am {firstname}. This is my home page! \nHere is my picture.'))
    file.write(createImage(emailuserName))
    file.write(createParagraph(sentence()))
# ---- REMAINDER OF PAGE OMITTED ----
    file.write(endBody())
    
    
    file.write(endHTML())
    
    file.close()


def createHead():


    return '<head>\n'
def endHead():
    return '</head>\n'

def createTitle(text):
    """Retrun html title tag string."""
    return "<title>" + text + "</title>\n"


def createDocType():
    """Return standard html5 DOCTYPE string."""
    
    return '<!DOCTYPE html>\n'
def startHTML():
    """Return html start tag."""

    return '<html>\n'
def endHTML():
    """Return html end tag."""

    return '</html>\n'
def startBody():
    """Return body start tag."""

    return '<body>\n'

def endBody():
    return '</body>\n'

def createParagraph(text):
    return '<p>\n'+text+'\n</p>\n'

def createHeading(text):
    return '<h1>'+ text + '</h1>\n'

def createImage(emailuserName):
    return f'<img src="{emailuserName}.jpg" alt="Picture of an aardvark" />\n'

# ---- OTHER HTML-GENERATING FUNCTIONS OMITTED ----




def findTemperatureLive():  
    """Print the current temperature in Wenham using data from localconditions.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!
    """

    # Get the weather page
    weather = requests.get("https://www.localconditions.com/weather-boston-massachusetts/01984/").text

    # The temperature can be found near the top of the page after the word "Wenham" and
    # immediately before the HTML code &deg; (the degree symbol)
    curLoc = weather.find("Wenham")
    if curLoc != -1:
        # Now, find the degree symbol ("&deg;") following the temperature
        degLoc = weather.find("&deg;", curLoc)
        # The temperature number is preceded by a pipe
        tempLoc = weather.rfind("|", 0, degLoc)
        # Temperature value is everything between the pipe (and space) and the degree symbol
        print("Current temperature in Wenham is",weather[tempLoc+2:degLoc], "degrees")
        return "Current temperature in Wenham is " + weather[tempLoc+2:degLoc] + " degrees"
    else:
        print("Page format has changed; cannot find the temperature")

def sentence():
    """Generate a random sentence from a select set."""
    nouns = [
        "Mark",
        "Adam",
        "Angela",
        "Larry",
        "Jose",
        "Matt",
        "Jim"
        ]
    verbs = [
        "runs",
        "skips",
        "sings",
        "leaps",
        "jumps",
        "climbs",
        "fires a Civil War cannon",
        "swims",
        "argues",
        "giggles"
        ]
    phrases = [
        "in a tree",
        "through every room in the house",
        "very loudly",
        "around the bush",
        "while reading the newspaper",
        "very badly",
        "while skipping",
        "instead of grading",
        "while programming Python"
        ]
    
    print(choice(nouns), choice(verbs), choice(phrases)+".")
    return (choice(nouns) + ' ' + choice(verbs) + ' ' + choice(phrases)+".")

def findTemperatureLive2():  
    """Print the current temperature in Wenham using data from localconditions.com.
  
    This function depends on knowledge of the page structure - if they change
    the page structure, the program will not work!
    """

    # Get the weather page
    weather = requests.get("https://www.localconditions.com/weather-los-angeles-california/90071/").text

    # The temperature can be found near the top of the page after the word "Wenham" and
    # immediately before the HTML code &deg; (the degree symbol)
    curLoc = weather.find("Los")
    if curLoc != -1:
        # Now, find the degree symbol ("&deg;") following the temperature
        degLoc = weather.find("&deg;", curLoc)
        # The temperature number is preceded by a pipe
        tempLoc = weather.rfind("|", 0, degLoc)
        # Temperature value is everything between the pipe (and space) and the degree symbol
        print("Current temperature in Los_Angeles is",weather[tempLoc+2:degLoc], "degrees")
        return "Current temperature in Los_Angeles is " + weather[tempLoc+2:degLoc] + " degrees"
    else:
        print("Page format has changed; cannot find the temperature")



if __name__ == "__main__":
    createHomePage("Tianze.pan")
