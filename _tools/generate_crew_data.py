#!/usr/bin/env python2

import random

cap_list = [
    "",
    "Cap NCO",
    "Cap NCO 02",
    "Cap 06 Red",
    "Cap 06 Black",
    "Cap 06 Alternate",
    "Cap 05 Yellow",
    "Cap 05 Red",
    "Cap 05 Black",
    "Cap 03 Stripes",
    "Cap 03 Gray",
    "Cap 03 Black",
    "Cap 02 Red",
    "Cap 02 Blue",
    "Cap 02 Black",
    "Cap 01 Stripes",
    "Cap 01 Green",
    "Cap 01 Blue"]

shirt_list = [
    "Sweater",
    "Shirt 04 Red",
    "Shirt 04 Gray",
    "Shirt 04 Blue",
    "Shirt 03 Gray",
    "Shirt 03 Brown",
    "Shirt 03 Blue",
    "Shirt 03 Black",
    "Shirt 02 Gray",
    "Shirt 02 Blue-White",
    "Shirt 02 Black",
    "Shirt 02 Black-Blue",
    "Shirt 01",
    "Jacket 06",
    "Jacket 05",
    "Jacket 04 Gray",
    "Jacket 04 Black",
    "Jacket 03",
    "Jacket 02",
    "Jacket 01",
    "Cotton Shirt 04 Stripes",
    "Cotton Shirt 04 Red",
    "Cotton Shirt 04 Red 2",
    "Cotton Shirt 04 Green",
    "Cotton Shirt 04 Blue",
    "Cotton Shirt 04 Blue 2",
    "Cotton Shirt 03 Red",
    "Cotton Shirt 03 Red 2",
    "Cotton Shirt 03 Orange",
    "Cotton Shirt 03 Brown",
    "Cotton Shirt 03 Blue",
    "Cotton Shirt 03 Blue 2",
    "Cotton Shirt 02 Green",
    "Cotton Shirt 02 Gray",
    "Cotton Shirt 02 Brown",
    "Cotton Shirt 01 Turquise",
    "Cotton Shirt 01 Red",
    "Cotton Shirt 01 Red 2",
    "Cotton Shirt 01 Gray",
    "Cotton Shirt 01 Burgundy",
    "Cotton Shirt 01 Blue",
    "Cotton Shirt 01 Blue 3",
    "Cotton Shirt 01 Blue 2"]

pants_list = [
    "Pants 02",
    "Pants 01"]

hairstyle_list = [
    "Hair 06",
    "Hair 05",
    "Hair 04",
    "Hair 03",
    "Hair 02",
    "Hair 01",
    "Bald"]

haircolor_list = [
    [0.37254902720451357, 0.2235294133424759, 0.0235294122248888], #brown
    [0.7686274647712708, 0.4313725531101227, 0.0941176488995552], #red
    [0.8745098114013672, 0.786928117275238, 0.6117647290229797]] #black


complexion_list = [
    "Complexion VIII",
    "Complexion VII",
    "Complexion VI",
    "Complexion V",
    "Complexion IV",
    "Complexion III",
    "Complexion II",
    "Complexion I"]

minbeardsize_list = [
    0,
    random.random()]

facetype_list = [
    "Type XIII",
    "Type XII",
    "Type XI",
    "Type X",
    "Type VIII",
    "Type VII",
    "Type VI",
    "Type V",
    "Type IX",
    "Type IV",
    "Type III",
    "Type II",
    "Type I"]

with open('sailor_data.json', 'r') as file:
    json = file.read()
    json = json.replace('\t', '  ')
    json = json.replace('$(cap)', random.choice(cap_list))
    json = json.replace('$(shirt)', random.choice(shirt_list))
    json = json.replace('$(pants)', random.choice(pants_list))
    json = json.replace('$(accessory1)', "")
    json = json.replace('$(accessory2)', "")
    json = json.replace('$(pants)', random.choice(pants_list))
    json = json.replace('$(hairstyle)', random.choice(hairstyle_list))
    haircolor = random.choice(haircolor_list)
    json = json.replace('$(haircolor_r)', str(haircolor[0]))
    json = json.replace('$(haircolor_g)', str(haircolor[1]))
    json = json.replace('$(haircolor_b)', str(haircolor[2]))
    json = json.replace('$(complexion)', random.choice(complexion_list))
    json = json.replace('$(minimum_beard_size)', str(random.choice(minbeardsize_list)))
    json = json.replace('$(face_type)', random.choice(facetype_list))
    print(json)
