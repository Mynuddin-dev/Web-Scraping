from bs4 import BeautifulSoup

with open("home.html","r") as html_file:
    
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")
    
    # print(content)
    # print(soup.prettify())
    
    # tags = soup.find("h5")
    # tags = soup.find_all("h5")
    # print(tags)
    # for tagsss in tags:
    #     print(tagsss.text)
    
    course_cards = soup.find_all("div" , class_='card' )
    
    for course in course_cards:
        
        # print(course.a) 
        
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(course_name ,":" , course_price)

html_file.close()