filedict = {
    "2014_Yellow_Taxi_Trip_Data.csv": "taxipickup2014totals.csv",
    "2015_Yellow_Taxi_Trip_Data.csv": "taxipickup2015totals.csv",
    "2016_Yellow_Taxi_Trip_Data.csv": "taxipickup2016totals.csv",
    "2017_Yellow_Taxi_Trip_Data.csv": "taxipickup2017totals.csv",
    "2018_Yellow_Taxi_Trip_Data.csv": "taxipickup2018totals.csv",
    "2019_Yellow_Taxi_Trip_Data.csv": "taxipickup2019totals.csv",
    "2020_Yellow_Taxi_Trip_Data.csv": "taxipickup2020totals.csv",
    "2021_Yellow_Taxi_Trip_Data.csv": "taxipickup2021totals.csv",
}

for file in filedict.keys():
    print(file)
    print(filedict[file])
    print()

    infile = open(file, "r")
    outfile = open(filedict[file], "w")

    for line in infile:
        try:
            pickuplongitude = line.split(",")[5]
            pickuplatitude = line.split(",")[6]
            if pickuplongitude != "0" and pickuplatitude != "0":
                print(infile)
                print(f"{pickuplongitude}, {pickuplatitude}")
                print(f"{pickuplongitude}, {pickuplatitude}", file=outfile)
                print()
        except:
            print("Error!")
            print("Problem with the following line")
            print(line)

    infile.close()
    outfile.close()
