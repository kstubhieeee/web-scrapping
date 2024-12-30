from bs4 import BeautifulSoup

with open('scraping-using-local-files/home.html','r') as html_file:
    content = html_file.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # courses_html_tags = soup.find_all('h5')
    # print(courses_html_tags)

    # for course in courses_html_tags:
    #     print(course.text)

    course_cards = soup.find_all('div',class_="card")
    # print(course_cards)

    for course in course_cards :
        course_name =course.h5.text
        course_desc =course.p.text
        course_price =course.a.text.split()[2]
        print(f'{course_name} costs {course_price}')

    

