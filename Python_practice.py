print("wagmi")
counties=["Arapahoe","Denver","Jefferson"]
print("counties")
if counties[1]=='Denver':
    print(counties[1])

if "El Paso" in counties:
    print("El Paso in da house")
else:
    print("El Paso AFK")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe and El paso present")
else:
    print("Arapahoe or El paso not present")

for county in counties:
    print(county)

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
    