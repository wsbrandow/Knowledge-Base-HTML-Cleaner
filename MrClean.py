print("Enter HTML Text Below")	    
while True:
    
    from bs4 import BeautifulSoup
    import re
    
    inputdata = input("")
    soup = BeautifulSoup(inputdata, "html.parser")      

    def cleaner(soup):
        for p_tag in soup.find_all("p"):
            del p_tag["align"]
            del p_tag["class"]
            del p_tag["style"]
        for span_tag in soup.find_all("span"):        
            span_tag.unwrap()
        for p1 in soup.find_all("p", string=re.compile("Issue:")):
            p1.name = "h1"         
        for p2 in soup.find_all("p", string=["Impacted Applications", "Impacted Applications:"]):
            p2.name = "h2"
        for p222 in soup.find_all("p", string=["Context:"]):
            p222.name = "h2"
        for p22 in soup.find_all("p", string=["Keywords:"]):
            p22.name = "h2"
        for strong2_tag in soup.find_all("strong", string=["Impacted Applications", "Impacted Applications:"]):
            strong2_tag.unwrap()
        for p3 in soup.find_all("p", string=[" Molina Healthcare | Technical How-To ", " Molina Healthcare | Technical Reference ", " Molina Healthcare | Process Reference ", " Molina Healthcare | Process How-To ", "Molina Healthcare | Technical How-To", "Molina Healthcare | Technical Reference", "Molina Healthcare | Process Reference", "Molina Healthcare | Process How-To"]):
            p3.name = "h3"
        for p33 in soup.find_all("p", string=[" Molina Healthcare | Technical How-To ", " Molina Healthcare | Technical Reference ", " Molina Healthcare | Process Reference ", " Molina Healthcare | Process How-To ", "Molina Healthcare | Technical How-To", "Molina Healthcare | Technical Reference", "Molina Healthcare | Process Reference", "Molina Healthcare | Process How-To"]):
            p33.name = "h3"
        for strong3_tag in soup.find_all("strong", string=["How to Resolve"]):
            strong3_tag.unwrap()
        for h33 in soup.find_all("p", string=["How to Resolve"]):
            h33.name = "h3"
        for li_tag in soup.find_all("li"):
            del li_tag["class"]
            del li_tag["span"]
            del li_tag["style"]
            del li_tag["align"]
        for img_tag in soup.find_all("img"):
            soup.img.wrap(soup.new_tag("br"))
        return soup

    print(cleaner(soup))


