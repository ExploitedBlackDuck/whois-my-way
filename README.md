# whois-my-way

This Python script uses the ipwhois module to perform a RDAP lookup on IP addresses from a file, and writes the results to a CSV file.

The script first specifies the name of the source file and the output file, which should be customized to match the filenames and paths of the actual files being used. It then opens the source file in read mode and the output file in append mode, using the with statement to ensure that the files are properly closed when the code block is finished executing.

Next, the script reads all of the IP addresses in the source file using the readlines() method, which returns a list of strings containing each line of the file. The script then loops over each IP address in the list, stripping off any newline characters that may be present using the strip() method.

Inside the loop, the script uses the IPWhois class of the ipwhois module to perform a RDAP lookup on the IP address. If the lookup is successful, the script extracts various pieces of information from the returned dictionary, including the country code, CIDR range, and name of the contact associated with the IP address. The script then prints the IP address and the name of the contact to the console and writes them to the output file in comma-separated format. If the lookup is not successful, the script writes the IP address and the string "Unknown" to the output file and prints an error message to the console.

Note that the script may take some time to execute, especially if many IP addresses are being looked up, and may generate errors or produce unexpected results if the input file contains malformed or invalid IP addresses. Additionally, some RDAP servers may not allow repeated queries from the same IP address, so it is possible that the script may encounter rate limiting or other issues if used excessively.
