from dotenv import load_dotenv
import os
load_dotenv()
emotifyPath = os.getenv("EMOTIFY_PATH")
fp = open(emotifyPath+r"\new.html","w")
f2 = open(emotifyPath+r"\new.txt","r")
p=f2.read()
f2.close()
fp.write('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
  
    <title>HTML 5 Boilerplate</title>
  </head>
  <body background="'''+emotifyPath+'''\songRecommender\data\bg.jpg">
  
	<script src="index.js"></script>
    <iframe style="border-radius:12px" src="https://open.spotify.com/embed/playlist/'''+p+'''?utm_source=generator" width="75%" height="500" frameBorder="0" allow="autoplay; clipboard-write; encrypted-media; picture-in-picture" loading="lazy"></iframe>

  </body>
</html>''')

fp.close()
os.system(emotifyPath+r"\new.html")
