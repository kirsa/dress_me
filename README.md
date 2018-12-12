# dress_me.py

-----------------Why?----------------------------------

Decision fatigue is slow wearing down of our mental willpower and energy to make well considered decisions 
as the day progresses. It is a natural consequence of constantly making decisions thorughout the day, and
every single decison we make contributes to this fatigue.

Some have sought to minimize the number of decisions by completely removing mundane ones, ones like the
crippling "What do I wear today?", and have done so with success. Take for example one late turtle neck and
sneaker sporting silicon valley icon. While some of us can commit to wearing the same thing everyday the rest 
of us might want a well put together outfit everyday without the hassle of putting one together everyday.

Short of an on-call personal stylist this script is the next best thing. It aims to reduce daily 
decision fatigue while making sure you still look good!

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

Must be named 'wardrobe.yaml' and be located in same directory as dress_me.py
Tops
  OuterLayer
    Knit   
    Sweatshirts
  InnerLayer
    Tshirts
    Longsleeves
    Shirts   
 Bottoms
 Socks
 Shoes
 
 - Weather data
 
 The script reads the minimum temperature for the day from the bbc's weather page for a location.
 Locations are specified using the 7-digit url page number of the location's bbc weather data page.
 
 - Outfit generation : gen_outfit(wardrobe, location)
 
 wardrobe = yaml
 location = 7-digit string
 
 The weather data is used in the outfit generation function to work out whether to wear heavier or lighter layers.
 Along with some constraints on combinations for aestheic reasons. Customise the function as desired.

