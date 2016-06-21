import csv


def breakdown(filepath, filetype, j_def, column, keep_headers):

    """ 
    filepath = path for one of the four files that you will be opening
    column = the column in the spreadsheet that you will be looking to
    filetype = the type of file that you are opening to work through:
                MC? MD? PC? PD?
    j_def = the jurisdictional definition that you are iterating for:
                Statewide? CD? LD? County? County Commissioner? MCD? Circuit Court?
    keep_headers = do you want the header in the new files?:
                True or False
                
    """
    
    
    open_file = open(filepath,'r')
    read_file = csv.reader(open_file)
    base_path = '/Users/maddiehuffman/Desktop/broken'

    values = []
    clean = []
    for row in read_file:
        if row:
            values.append(row[column])
    for item in values[1:]:
        if item in clean:
            pass
        else:
            clean.append(item)  
    r_file = open(filepath,'r')
    repeat_file = csv.reader(r_file) 
    rows = []
    for val in clean:
        print(val)
#         for a_row in repeat_file:
#             if a_row:
#                 if val == a_row[column]:
#                     with open('%s/%s/%s/%s_%s_%s.csv' % (base_path, filetype, j_def, filetype, j_def, val), 'a') as _ap:
#                         if keep_headers == True:
#                             headers = csv.reader.next()
#                             h = csv.writer(_ap, dialect='excel')
#                             h.writerow(headers)
#                             h.writerow(a_row)
#                         else:
#                             l = csv.writer(_ap, dialect='excel')
#                             l.writerow(a_row)
#                 else:
#                     pass


print(breakdown('/Users/maddiehuffman/Desktop/broken/MC/MRPmail.csv', 'MC', 'County', 3, False))

    
