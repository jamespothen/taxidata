infilelist = ['2011_Yellow_Taxi_Trip_Data.csv',
              '2012_Yellow_Taxi_Trip_Data.csv',
              '2013_Yellow_Taxi_Trip_Data.csv',
              '2014_Yellow_Taxi_Trip_Data.csv',
              '2015_Yellow_Taxi_Trip_Data.csv',
              '2016_Yellow_Taxi_Trip_Data.csv',
              '2017_Yellow_Taxi_Trip_Data.csv',
              '2018_Yellow_Taxi_Trip_Data.csv',
              '2019_Yellow_Taxi_Trip_Data.csv',
              '2020_Yellow_Taxi_Trip_Data.csv',
              '2021_Yellow_Taxi_Trip_Data.csv']

outfile = open('taxiridetotals.csv', 'w')

yearcountdict = {'2011':0,
                 '2011':0,
                 '2012':0,
                 '2013':0,
                 '2014':0,
                 '2015':0,
                 '2016':0,
                 '2017':0,
                 '2018':0,
                 '2019':0,
                 '2020':0,
                 '2021':0,}

for filename in infilelist:
    infile = open(filename, 'r')
    year = filename[0:4]

    for line in infile:
        yearcountdict[year] += 1
        print(f"{year}: {yearcountdict[year]}")
    infile.close()

for year in yearcountdict.keys():
    print(f"{year}, {yearcountdict[year]}", file = outfile)

outfile.close()
