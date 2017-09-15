print("Enter HTML Text Below")
while True:
    
    import bs4

    txt = input("")
    soup = bs4.BeautifulSoup(txt, "html.parser")

    def cleaner(soup):
        for p_tag in soup.find_all("p"):
            del p_tag["align"]
            del p_tag["class"]     
        for span_tag in soup.find_all("span"):
            span_tag.unwrap()
        #for strong_tag in soup.find_all("strong"):
            #strong_tag.unwrap()       
        return soup

    #def hreplacer(soup):
        #for p_tag in soup.find_all("p", string=["Molina Healthcare | Technical How-To", "Molina Healthcare | Technical Reference", "Molina Healthcare | Process Reference", "Molina Healthcare | Process How-To"]):
           # p_tag.name = "h1"
        #for b_tag in soup.find_all("p", string="Molina Healthcare | Technical Reference"):
            #b_tag.name = "h1"
        #for c_tag in soup.find_all("p", string="Molina Healthcare | Process Reference"):
            #c_tag.name = "h1"
        #for d_tag in soup.find_all("p", string="Molina Healthcare | Process How-To"):
            #d_tag.name = "h1" 
            #return soup
            
        



        #p_tag = soup.p
        #h1_tag = soup.h1_tag("h1")
        #h1_tag.string = soup.string
        #soup.replace_with(h1_tag)
        

    #if p element contains Molina Healthcare | Technical How-To OR ""
    #insert <br /> before and after <img />
    #check wrap() method for changing to H1, H2, etc. 
    print((cleaner(soup)).prettify())
#https://stackoverflow.com/questions/22496822/removing-span-tags-from-soup-beautifulsoup-python
    
    


