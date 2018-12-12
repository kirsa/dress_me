# dress_me.py

-----------------What is it?---------------------------

Python script to check weather in your loaction and generate an outfit for the day from your wardrobe


-----------------How to use it?------------------------
- Structure

dress_me.py     : Main python script
dress_me_lib.py : Functions used in dress_me.py
wardrobe.yaml   : Contents of your wardrobe

- Behaviour

The script reads in a yaml file (pass location of file to function that reads yaml) that has all the
contents of your wardrobe, checks the weather in the given location and randomly generates an outfit.

- Yaml structure

[Tops]
  -[OuterLayer]
    - [Knit]
    - [Sweatshirts]
  -[InnerLayer]
    - [Tshirts]
    - [Longsleeves]
    - [Shirts]
 [Bottoms]
 [Socks]
 [Shoes]
 
 - Weather data
 
 The script reads the minimum temperature for the day from the bbc's weather page for a location.
 Locations are specified using the 7-digit url page number of the location's bbc weather data page.
 
 - Outfit generation
 
 The weather data is used in the outfit generation function to work out whether to wear heavier or lighter layers.
 Along with some constraints on combinations for aestheic reasons. Customise the function as desired.

