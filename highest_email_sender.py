fname = input("Insert file name: ")
if len(fname) < 1 :
    fname = "email_data.txt"
fopen = open(fname)
count = dict()

for lines in fopen:

    if lines.startswith("From:"):
        data = lines.split()
        email = data[1]
        #print(email)

        if email not in count :
            count[email] = 0
        count[email] = count[email] + 1
        #max_email = count.values()
        #f_email = max(max_email)

        largest = -1
        highest_email = None
        for k, v in count.items():
            #print(k, v)
            if v > largest:
                largest = v
                highest_email = email
print(highest_email, largest)