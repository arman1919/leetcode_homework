def correct_mail(str):

    mail=''

    for i in str[:str.index("@")]:
        if i != ".":
            mail += i

    mail += str[str.index("@"):]

    mail2 = mail[:mail.index("+")] + mail[mail.index("@"):]

    return mail2

def check_mail(emails):

    ls = []
    for i in  emails:
        ls.append(correct_mail(i))

    for i in ls.copy():
        while ls.count(i) != 1:
            ls.remove(i)

    return len(ls)


emails = ["test.email+alex@leetcode.com",
         "test.e.mail+bob.cathy@leetcode.com",
         "testemail+david@lee.tcode.com",
          "test.emali+kevin@mail.ru",
          "test.email+david@lee.tcode.com"]

print(check_mail(emails))
