while True: 

  import re

  HTMLTxt = input("Enter your HTML Text here: ")
  
  def p1cleaner(raw_html):
    cleanp1 = re.compile('<p.*?>')
    cleantextp1 = re.sub(cleanp1, '<p>', raw_html)
    return p2cleaner(cleantextp1)

  def p2cleaner(cleantextp1):
    cleanp2 = re.compile('<.*?/p>')
    cleantextp2 = re.sub(cleanp2, '</p>', cleantextp1)
    print(cleantextp2)

  #def s1cleaner(y):
    #cleantextsp1 = re.sub('<span.*?>', '', y)
    #return s2cleaner(cleantextsp1)

  #def s2cleaner(z):
    #cleantextsp2 = re.sub('<.*?/span>', '', z)
    #print(cleantextsp2)

  
  p1cleaner(HTMLTxt)



    
    
    
