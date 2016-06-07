import csv

m = open('MRP_PrimaryAVList.csv', 'rU')
master = csv.reader(m)

c = open('/Users/maddiehuffman/Desktop/broken/MPC/MRP_PrimaryAVListCopy.csv', 'rU')
copy = csv.reader(c)

master_info = []
for row in master:
    mi = (list( row[i] for i in range(len(row) )))
    master_info.append(mi)

copy_info = []
for line in copy:
    ci = (list( line[i] for i in range(len(line) )))
    copy_info.append(ci)

first_set = set(map(tuple, master_info))
secnd_set = set(map(tuple, copy_info))

diff_set = first_set.symmetric_difference(secnd_set) 
diff_1 = [list(item) for item in set(tuple(row) for row in diff_set)]

all_daily = open('/Users/maddiehuffman/Desktop/broken/MPD/MRPmailandphoneNEW.csv','w')
ad = csv.writer(all_daily, dialect='excel')
all_daily.write("BALLOTID,VOTERID,SPOILEDIND,REJECTED,BALLOTNUMBER,BALLOTTYPE,DATESENT,DATERETURNED,APPRETURNED,COUNTY,JURISDICTION,CBPRECINCT,LASTNAME,FIRSTNAME,ADDRESES1,ADDRESS2,ADDRESS3,ADDRESS4,ADDRESS5,SPOILED_BALLOTS,YOB,UOCAVASTATUS \n")
for a_list in diff_1:
    ad.writerow(a_list)
all_daily.close()
m.close()
c.close()

###############################################################################
nmpd = open('/Users/maddiehuffman/Desktop/broken/MPD/MRPmailandphoneNEW.csv','rU')
new_stuff = csv.reader(nmpd)
nmps = []
for line in new_stuff:
    nmps.append(line)
with open('/Users/maddiehuffman/Desktop/broken/MPC/MRP_PrimaryAVListCopy.csv','a') as copyfile:
    copyfile.write('\n')
    for a_list in nmps[1:]:
        wr = csv.writer(copyfile, dialect='excel')
        wr.writerow(a_list)


###############################################################################
og = open('MRP_PrimaryAVList.csv', 'rU')
oginfo = csv.reader(og)


ph = open('/Users/maddiehuffman/Desktop/broken/PC/MRPphone.csv', 'rU')
old_phone = csv.reader(ph)


all_phone_info = []
for row in oginfo:
    phone_stuff = (list( row[i] for i in [1, 9, 10, 12, 19, 20] ))
    all_phone_info.append(phone_stuff)


old_phone_info = []
for line in old_phone:
    old_phone_info.append(line)


first_set = set(map(tuple, all_phone_info))
secnd_set = set(map(tuple, old_phone_info))


diff_set = first_set.symmetric_difference(secnd_set) 
diff_1 = [list(item) for item in set(tuple(row) for row in diff_set)]

newfile = open('/Users/maddiehuffman/Desktop/broken/PD/MRPphoneNEW.csv','w')
nr = csv.writer(newfile, dialect='excel')
newfile.write("VOTERID,COUNTY,JURISDICTION,LASTNAME,FIRSTNAME,YOB,UOCAVASTATUS,PHONE#,SECONDARY# \n")
for each_list in diff_1:
    nr.writerow(each_list)
newfile.close()
og.close()
ph.close()

##################################################################################
np = open('/Users/maddiehuffman/Desktop/broken/PD/MRPphoneNEW.csv','rU')
new_phone_stuff = csv.reader(np)
nps = []
for a_line in new_phone_stuff:
    nps.append(a_line)
with open('/Users/maddiehuffman/Desktop/broken/PC/MRPphone.csv','a') as phonefile:
    phonefile.write('\n')
    for a_list in nps[1:]:
        wr = csv.writer(phonefile, dialect='excel')
        wr.writerow(a_list)


##################################################################################
all = open('MRP_PrimaryAVList.csv', 'rU')
allinfo = csv.reader(all)


ml = open('/Users/maddiehuffman/Desktop/broken/MC/MRPmail.csv', 'rU')
old_mail = csv.reader(ml)


all_mail_info = []
for a_row in allinfo:
    mail_stuff = (list( a_row[m] for m in [1, 6, 9, 10, 12, 13, 14, 19, 20] ))
    all_mail_info.append(mail_stuff)


old_mail_info = []
for each_line in old_mail:
    old_mail_info.append(each_line)



first_m_set = set(map(tuple, all_mail_info))
secnd_m_set = set(map(tuple, old_mail_info))


diff_m_set = first_m_set.symmetric_difference(secnd_m_set) 
diff_m = [list(k) for k in set(tuple(r) for r in diff_m_set)]

new_m_file = open('/Users/maddiehuffman/Desktop/broken/MD/MRPmailNEW.csv','w')
nmr = csv.writer(new_m_file, dialect='excel')
new_m_file.write("VOTERID,DATESENT,COUNTY,JURISDICTION,FULLNAME,ADDRESS1,ADDRESS2,YOB,UOCAVASTATUS \n")
for each_mlist in diff_m:
    nmr.writerow(each_mlist)
new_m_file.close()
all.close()
ml.close()

##################################################################################
nm = open('/Users/maddiehuffman/Desktop/broken/MD/MRPmailNEW.csv','rU')
new_mail_stuff = csv.reader(nm)
nms = []
for m_line in new_mail_stuff:
    nms.append(m_line)
with open('/Users/maddiehuffman/Desktop/broken/MC/MRPmail.csv','a') as mailfile:
    mailfile.write('\n')
    for m_list in nms[1:]:
        mr = csv.writer(mailfile, dialect='excel')
        mr.writerow(m_list)



from datetime import datetime
now = datetime.now()

print ('%s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)

 
 ####################################################################