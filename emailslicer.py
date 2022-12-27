input1=int(input("Enter the number of Emails you want: "))
email_list=[]
for i in range(0, input1):
    email_list.append(input("Enter the email: ").strip())
for i in range(0, input1):
    email = email_list[i]
    username = email[:email.index('@')+ 1 :]
    domain =  email[email.index('@')+ 1 :]
    domain2= domain.upper()
    print(f"username: {username} & domain: {domain2}")



