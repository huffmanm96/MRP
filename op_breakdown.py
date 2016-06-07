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
    
    
    open_file = open(filepath,'rU')
    read_file = csv.reader(open_file)
    base_path = '/Users/maddiehuffman/Desktop/broken'

    values = []
    clean = []
    for row in read_file:
        if row:
            values.append(row[column])
    for item in values:
        if item in clean:
            pass
        else:
            clean.append(item)
    for val in clean:
        for row in read_file:
            if row:
                if row[column] == j_def:
                    with open('%s/%s/%s/%s_%s_%s.csv' % (base_path, filetype, j_def, filetype, j_def, val), 'rU') as _read:
                        for a_row in _read:
                            if a_row:
                                with open('%s/%s/%s/%s_%s_%s.csv' % (base_path, filetype, j_def, filetype, j_def, val), 'a') as _ap:
                                    _ap.write(row)
                            else:
                                with open('%s/%s/%s/%s_%s_s.csv' % (base_path, filetype, j_def, filetype, j_def, val), 'w') as _wr:
                                    if keep_headers:
                                        headers = csv.reader.next()
                                        _wr.writerow(headers)
                                        _wr.write(row)
    _wr.close()
    _ap.close()
    _read.close()
    open_file.close()
    
    