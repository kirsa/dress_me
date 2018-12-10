""" Dress me script """

# Imports
import dress_me_lib

WARDROBE = dress_me_lib.read_yaml('wardrobe.yaml', '/Users/Home/dress_me/')

print(dress_me_lib.gen_tmr_outfit(WARDROBE))
