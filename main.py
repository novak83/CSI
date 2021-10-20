import json

with open("dna.txt", "r") as dna_file:
    dna_sample = dna_file.read()

# charateristic
# hair
black_hair = "CCAGCAATCGC"
brown_hair = "GCCAGTGCCG"
blonde_hair = "TTAGCTATCGC"

# facial shape
square_face = "GCCACGG"
round_face = "ACCACAA"
oval_face = "AGGCCTCA"

# eye color
blue_eyes = "TTGTGGTGGC"
green_eyes = "GGGAGGTGGC"
brown_eyes = "AAGTAGTGAC"

# gender
female = "TGAAGGACCTTC"
male = "TGCAGGAACTTC"

# race
white = "AAAACCTCA"
black = "CGACTACAG"
asian = "CGCGGGCCG"

def hair():
    for hair_color in dna_sample:
        if black_hair in dna_sample:
            hair_color = "black hair"
        if brown_hair in dna_sample:
            hair_color = "brown hair"
        if blonde_hair in dna_sample:
            hair_color = "blonde hair"
        return hair_color

def facial_shape():
    for facial_shape in dna_sample:
        if square_face in dna_sample:
            facial_shape = "square_face"
        if round_face in dna_sample:
            facial_shape = "round_face"
        if oval_face in dna_sample:
            facial_shape ="oval_face"
        return facial_shape

def eye_color():
    for eye_color in dna_sample:
        if blue_eyes in dna_sample:
            eye_color = "blue_eyes"
        if green_eyes in dna_sample:
            eye_color = "green_eyes"
        if brown_eyes in dna_sample:
            eye_color = "brown_eyes"
        return eye_color

def gender():
    for gender in dna_sample:
        if female in dna_sample:
            gender = "female"
        if male in dna_sample:
            gender = "male"
        return gender

def race():
    for race in dna_sample:
        if white in dna_sample:
            race = "white"
        if black in dna_sample:
            race = "black"
        if asian in dna_sample:
            race = "asian"
        return race

def suspects():
    global suspect
    if (dna_sample.find(female and white and blonde_hair and blue_eyes and oval_face) !=-1):
        suspect = "Eva"
    if (dna_sample.find(female and white and brown_hair and brown_eyes and oval_face) !=-1):
        suspect = "Larisa"
    if (dna_sample.find(male and white and black_hair and blue_eyes and oval_face) !=-1):
        suspect = "Matej"
    if (dna_sample.find(male and white and brown_hair and green_eyes and square_face) !=-1):
        suspect = "Miha"
    return suspect

hair()
facial_shape()
eye_color()
gender()
race()
suspects()

dna_results = "Analysis show that dna sample is from {}.".format(suspect)
print(dna_results)