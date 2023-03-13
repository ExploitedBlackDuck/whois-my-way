from ipwhois import IPWhois

#this module is core networking module in Python, 
#can be used to resolve IP address.

sourcefile = 'sourcefile.txt' #file with IP address
outfile = 'results.csv' #file to write the IP addresses

with open(sourcefile, 'r') as inputf: 
    #This opens the sourcefile in read mode to see what are the domains


    with open(outfile, 'a') as outputf: 
        #This opens the outfile in append mode to write the results


        addresses = inputf.readlines() 
        #This reads all the IP addresses in sourcefile line by line


        for address in addresses: 
            #This for loop will go one by one on addresses.

            address = address.strip("\n") 
                #as the every address in the file are in newline,
                #the socket function will have trouble, so strip off the newline char

            try:
                ipwhois = IPWhois(address)
                result = ipwhois.lookup_rdap()
                #print(result)
                #print("Country:",result["asn_country_code"])
                #print("CIDR:", result["asn_cidr"])
                initObjKey = list(result['objects'].keys())[0]
                print(address, " : ", result['objects'][initObjKey]['contact']['name'])
                outputf.write(address + "," + result["asn_country_code"] + "," +  result["asn_cidr"] + "," + result['objects'][initObjKey]['contact']['name'] + "\n")
            except:
                outputf.write(address + "," + "Unknown\n")
                print('Could not resolve ' + address)