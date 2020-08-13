import csv
import codecs


def drop_blank(rows: list):
    """ Removes blank rows and cells

    Args:
        rows (list): list of rows

    Returns:
        list: A list of rows that aren't empty
    """
    return [x for x in [[cell for cell in row if len(cell)] for row in rows] if x]


def parse_rows(reader: list):
    """ Parses the list of rows

    Args:
        reader (list): list of rows to be parsed

    Returns:
        list: list of parsed rows
    """
    parsed_rows = [*reader[:2]]
    current = None
    for row in reader[2:]:
        # Save the department name for use later
        if row[0] == "Department:":
            department = row[1]
        # If current is None, it's a new person
        elif not current:
            current = [row[0].split(": ")[1], row[-1], department]
        else:
            current.append(row[0].split(":")[1])
            parsed_rows.append(current)
            current = None
    return parsed_rows


# Open in utf-16 encoding to handle NULL byte
with codecs.open("input.csv", "rU", "utf-16") as csvfile:
    csvReader = parse_rows(drop_blank(csv.reader(csvfile, delimiter="|")))

with open("output.csv", "w", newline="", encoding="utf-16") as csvfile:
    writer = csv.writer(csvfile)
    for row in csvReader:
        writer.writerow(row)
