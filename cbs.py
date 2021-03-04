import os
import urllib.request
from pyctr.type.cia import CIAReader, CIASection, CIAError


def get_db():
    db_path = "3dsreleases.xml"
    db_url = "http://3dsdb.com/xml.php"

    print("searching for {}".format(db_path))
    if not os.path.exists(db_path):
        print("No release database detected, downloading database")
        urllib.request.urlretrieve(db_url, db_path)
    else:
        print("{} found".format(db_path))
    return db_path


def search_for_cia(search_dir=".", extension=".cia"):
    found = []
    extension = extension.lower()
    for dirpath, dirnames, files in os.walk(search_dir):
        for fname in files:
            if extension and fname.lower().endswith(extension):
                found.append(os.path.join(dirpath, fname))
    return found


def main():
    # initialize
    db_path = get_db()
    files = search_for_cia()
    print(files)


if __name__ == "__main__":
    main()
