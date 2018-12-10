""" Functions used in dress_me script """
# Imports
import random
import yaml
import feedparser

def read_yaml(file_name, file_path):
    """ Function to read a yaml file """
    yaml_file = open(file_path + file_name)
    yaml_content = yaml.load(yaml_file)
    yaml_file.close()
    return yaml_content

def print_yaml(yaml_file):
    """ Print yaml using yaml dump """
    print(yaml.dump(yaml_file))

def extract_celcius(rss_title_string):
    """ Extract the celcius value from the rss title string that has weather information """
    celcius_index = rss_title_string.find('°C')
    celcius = rss_title_string[celcius_index-2]+rss_title_string[celcius_index-1]
    return int(celcius)

def get_sheff_temp_tmr():
    """ Returns tomorrow's minimum temperature prediction for Sheffield from BBC """
    sheff_bbc_rss = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2638077'
    sheff_forecast = feedparser.parse(sheff_bbc_rss)
    # Index 1 gives tomorrow, 0 gives today, and 2 gives day after
    temp_forecast = extract_celcius(sheff_forecast.entries[1].title)
    return temp_forecast

def gen_tmr_outfit(wardrobe):
    """ Generate tomorrow's outfit """
    outfit = []
    if get_sheff_temp_tmr() < 10:
        outfit.append(random.choice(wardrobe['Tops']['Inner_layer']['Longsleeves']))
    if get_sheff_temp_tmr() > 9:
        outfit.append(random.choice(wardrobe['Tops']['Inner_layer']['Tshirts']))
    if get_sheff_temp_tmr() < 6:
        outfit.append(random.choice(wardrobe['Tops']['Outer_layer']['Knit']))
    if get_sheff_temp_tmr() > 5:
        outfit.append(random.choice(wardrobe['Tops']['Outer_layer']['Sweatshirts']))
    if 'Caramel_mix_Folk' in outfit:
        outfit.append('Black_Reiss')
    if 'Caramel_mix_Folk' not in outfit:
        outfit.append(random.choice(wardrobe['Bottoms']))
    if 'Caramel_mix_Folk' in outfit or 'Fair_isle_Scallpers' in outfit:
        outfit.append(random.choice(wardrobe['Socks']))
    if 'Caramel_mix_Folk' not in outfit and 'Fair_isle_Scallpers' not in outfit:
        outfit.append(random.choice(wardrobe['Chup_socks']))
    outfit.append(random.choice(['Black_1461_DrMartens', 'Brown_101_DrMartens']))
    return outfit
