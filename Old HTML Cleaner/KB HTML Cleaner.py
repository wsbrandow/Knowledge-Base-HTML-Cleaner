while True: #makes code loop

  import re
  print("Enter HTML Text Below")
  original = input("")
 
  
  def cleaner(raw_html):
    cleantextp = re.sub('<p.*?>', '<p>', raw_html, flags=re.DOTALL)
    cleantextspan1 = re.sub('<span.*?>', '', cleantextp, flags=re.DOTALL)
    cleantextspan2 = re.sub('<.*?/span>', '', cleantextspan1, flags=re.DOTALL)
    cleantextH1_1 = re.sub('<h1.*?>', '<h1>', cleantextspan2, flags=re.DOTALL)
    cleantextH1_2 = re.sub('<.*?/h1>', '</h1>', cleantextH1_1, flags=re.DOTALL)
    cleantextH2_1 = re.sub('<h2.*?>', '<h2>', cleantextH1_2, flags=re.DOTALL)
    cleantextH2_2 = re.sub('<.*?/h2>', '</h2>', cleantextH2_1, flags=re.DOTALL)
    cleantextH3_1 = re.sub('<h3.*?>', '<h3>', cleantextH2_2, flags=re.DOTALL)
    cleantextH3_2 = re.sub('<.*?/h3>', '</h3>', cleantextH3_1, flags=re.DOTALL)
    cleantextStrong1 = re.sub('<strong.*?>', '', cleantextH3_2, flags=re.DOTALL)
    cleantextStrong2 = re.sub('<.*?/strong>', '', cleantextStrong1, flags=re.DOTALL)
    cleantextItalic1 = re.sub('<i.*?>', '', cleantextStrong2, flags=re.DOTALL)
    cleantextItalic2 = re.sub('<.*?/i>', '', cleantextItalic1, flags=re.DOTALL)
    return cleantextItalic2



  if len(original) > 0:

    print(cleaner(original))

  else:
    print("Please try again")
    
    
