from datetime import datetime
from .models import Person



def clean_data(row):
    list_row = row.rstrip("\n").split(";")
    return list_row


def parse_name(full_name):
    try:
        if full_name:
            return [d.strip() for d in full_name.split()]
        else:
            return full_name
    except:
        return full_name


def parse_birth_date(date):
    date_format = "%Y-%m-%d"
    try:
        clean_data_string = date.strip()[:10]
        return datetime.strptime(clean_data_string, date_format)
    except:
        return None


with open('/Volumes/Extreme SSD/alfa/alfa.txt', 'r', encoding='utf-16') as file:
    next(file)  # skip first row as database was created and row do not correspond actual database columns
    check_value = 500
    count = 0  # count the number of records
    for f in file:  # looping throw the database records
        count += 1
        (ClientOwner,
        FullName,
        BirthDate,
        ClientContact,
        CardCodeNumber,
        ExpireDate) = (clean_data(f))
        data = parse_name(FullName)
        if len(data) == 1:
            first_name = data[0]
            last_name = None
            patronym = None
            otherinfo = None
        elif len(data) == 2:
            first_name = data[0]
            last_name = data[1]
            patronym = None
            otherinfo = None
        elif len(data) == 3:
            first_name = data[0]
            last_name = data[1]
            patronym = data[2]
            otherinfo = None
        elif len(data) > 3:
            first_name = data[0]
            last_name = data[1]
            patronym = data[2]
            otherinfo = " ".join(data[3:])
        else:
            first_name = data[0] if data else None
            last_name = None
            patronym = None
            otherinfo = None
        if count == check_value:
            print(first_name, last_name, patronym)
            print("Count: {}".format(count))
            check_value += 500
        Person.objects.create(ClientOwner=ClientOwner,
                            FirstName=first_name,
                            LastName=last_name,
                            Patronym=patronym,
                            OtherInfo=otherinfo,
                            BirthDate=parse_birth_date(BirthDate),
                            ClientContact=ClientContact)
