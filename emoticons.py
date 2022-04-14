'''
/description: this program will open up a twitter document containing data regarding tweets which contained emoticons (E-mo-tih-KAhns) in order to sort them and print out a report of the top 5 most popular ones.
'''
def load_twitter_dicts_from_file(sF, dEtI, dItE): # builds the dictionaries by reading the data file and checking line by line if the emoticon or twttter ID is already in each dict, if not it will append a new entry.
    for line in open(sF):
        sAry = line.split()
        
        sID = sAry[2][1:-1] #removes the quotes
        sEm = sAry[0][1:-1] # same^
        
        if sEm in dEtI:
            dEtI[sEm].append(sID)
        else:
            dEtI[sEm] = []
            dEtI[sEm].append(sID)

        if sID in dItE:
            dItE[sID].append(sEm)
        else:
            dItE[sID] = []
            dItE[sID].append(sEm)
            
def find_most_common(d): # looks for the most common i.e. the longest list.
    sK = ""
    iL = 0
    for key in d: # for key in the dictionary, remember which has the longest list by assigning it to variable "sK"
        if len(d[key]) > iL:
            iL = len(d[key])
            sK = key
    return sK
        
def main():
    '''
    2 dictionaries are created, names are self-explanitory. 
    Next, the data file is opened from the directory. 
    main calles find_most_common with the emoticons_to_ids dictionary. 
    A for loop then prints out the top five most common emoticons by popping the previous #1
    '''
    emoticons_to_ids = {}
    ids_to_emoticons = {}

    load_twitter_dicts_from_file("twitter_emoticons.dat", emoticons_to_ids, ids_to_emoticons)
    print("Emoticons: " + str(len(emoticons_to_ids)))
    print("UserIDS: " + str(len(ids_to_emoticons)))

    for i in range(5): # to find the top five. run the find_most_common function but pop the winner after each iteration
        sKey = find_most_common(emoticons_to_ids)
        print(sKey + "           occurs     " + str(len(emoticons_to_ids[sKey])) + " times")
        emoticons_to_ids.pop(sKey)

if __name__ == '__main__':
    main() 
