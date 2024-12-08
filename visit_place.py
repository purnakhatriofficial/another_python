district_visited_place_in_nepal = {
    "Kathmandu": ["Thamel", "Zoo", "Buddha", "Pasupati Tempale", "Darbar Square"],
    "Pokhare": ["Fewa Lake", "Lake Side", "Tal Brahi Temple", "Gupteshwor Mahadev Cave", "Devis Fall", "World Peace pagoda"],
    "Rukum": ["Shital Pokhari", "Kankre Bihar", "Sahit Smirti Park", "Digree Temple", "Viral Bridge", "Kamal Pokhari"],
    "Mustang": ["Shree mukthinath temple", "Kagbeni", "Jomson", "Lo Manthang", "Kaligandagi Raiver", "Dhakmar", "Marpha Monastery", "Marpha"],
    "Lumbini": ["World peaces pagoda", "Maya devi temple", "Bardiya national park", "Thai monestry", "Birth place of gautambudha", "Maynmar golden temple", "Bageswari mandir"],
    "Ilam": ["Seti devi temple", "Singabahini temple", "sandakpur", "chhinatapu", "phikal bazzar"],
    "Dolpa": ["Shay phoksundo national park", "Shay Gump", "Putha Hiuchuli", "Great Himalay", "Churen Himal", "Dho", "Tinje", "Chaakra"]
}

#Adding the District

district_visited_place_in_nepal ["Jhapa"] = ["Birtamod", "Sunkharri"]
district_visited_place_in_nepal["Solukhumbu"] =["Sagarmatha neational parka", "Everest based ccamp", "Tongboche Everest"]

#delete 

del district_visited_place_in_nepal["Jhapa"]

#updating 

district_visited_place_in_nepal["Solukhumbu"] = ["Sagarmaths"]

district_place_name = input("Enter The Your Favourit Tourisim District : ").capitalize()

if district_place_name in district_visited_place_in_nepal:
    print(f"Visiting Place in {district_place_name} are :")

    for place_district in district_visited_place_in_nepal[district_place_name]:
        print(place_district)
else:
    print("Sorry district not avilable now")
