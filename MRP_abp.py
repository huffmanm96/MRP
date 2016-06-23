import csv
import op_breakdown
import SMTPmail


m = open('MRP_PrimaryAVList.csv', 'r')
master = csv.reader(m)

c = open('/Users/maddiehuffman/Desktop/broken/MPC/MPC_Statewide_.csv', 'r')
copy = csv.reader(c)
head = next(copy)

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

all_daily = open('/Users/maddiehuffman/Desktop/broken/MPD/MPD_Statewide_.csv','w')
ad = csv.writer(all_daily, dialect='excel')
ad.writerow(head)
for a_list in diff_1:
    ad.writerow(a_list)


###############################################################################
nmpd = open('/Users/maddiehuffman/Desktop/broken/MPD/MPD_Statewide_.csv','r')
new_stuff = csv.reader(nmpd)
nmps = []
for line in new_stuff:
    nmps.append(line)
with open('/Users/maddiehuffman/Desktop/broken/MPC/MPC_Statewide_.csv','a') as copyfile:
    copyfile.write('\n')
    for a_list in nmps[1:]:
        wr = csv.writer(copyfile, dialect='excel')
        wr.writerow(a_list)


###############################################################################
og = open('MRP_PrimaryAVList.csv', 'r')
oginfo = csv.reader(og)


ph = open('/Users/maddiehuffman/Desktop/broken/PC/MRPphone.csv', 'r')
old_phone = csv.reader(ph)


all_phone_info = []
for row in oginfo:
    phone_stuff = (list( row[i] for i in [36, 37, 38, 39, 40, 52, 53, 1, 2, 3, 5, 24, 25, 43, 44] ))
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
newfile.write("LastName,FirstName,MiddleName,Address,PrimaryPhone,PhoneReliabilityCode,ClientID,StateVoterID,CD,LD,SD,County,Precinct,Township,County Commissioner District \n")
for each_list in diff_1:
    nr.writerow(each_list)
newfile.close()
og.close()
ph.close()

##################################################################################
np = open('/Users/maddiehuffman/Desktop/broken/PD/MRPphoneNEW.csv','r')
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
all = open('MRP_PrimaryAVList.csv', 'r')
allinfo = csv.reader(all)


ml = open('/Users/maddiehuffman/Desktop/broken/MC/MRPmail.csv', 'r')
old_mail = csv.reader(ml)


all_mail_info = []
for a_row in allinfo:
    mail_stuff = (list( a_row[m] for m in [36, 37, 38, 39, 40, 52, 53, 1, 2, 3, 10, 12, 13, 14, 6, 7, 8, 43, 44] ))
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
new_m_file.write("LastName,FirstName,MiddleName,HouseNumber,StreetPrefix,StreetName,StreetType,City,State,ZipCode,ClientID,StateVoterID,CD,LD,SD,County,Precinct,Township,County Commissioner District \n")
for each_mlist in diff_m:
    nmr.writerow(each_mlist)
new_m_file.close()
all.close()
ml.close()

##################################################################################
nm = open('/Users/maddiehuffman/Desktop/broken/MD/MRPmailNEW.csv','r')
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

print (('%s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second))

 
 ####################################################################


j_defs = {'CD':0,'LD':1,'SD':2,'County':3,'Precinct':4,'Township':5,'CountyCommissioner':6}
# # alt_defs = {'CD':36,'LD':37,'SD':38,'County':39,'Precinct':40,'Township':52,'CountyCommissioner':53}
# 
print('Working on cumulative mail file')
for c in j_defs.keys():
    op_breakdown.breakdown('/Users/maddiehuffman/Desktop/broken/MC/MRPmail.csv', 'MC', c, j_defs.get(c), False)
print('Cumulative mail file finished')

print('Working on cumulative phone file')
for e in j_defs.keys():
    op_breakdown.breakdown('/Users/maddiehuffman/Desktop/broken/PC/MRPphone.csv', 'PC', e, j_defs.get(e), False)
print('c_files finished')

print('Working on mail daily file')
for d in j_defs.keys():
    op_breakdown.breakdown('/Users/maddiehuffman/Desktop/broken/MD/MRPmailNEW.csv', 'MD', d, j_defs.get(d), True)
print('d_files finished')

print('Working on phone daily file')
for f in j_defs.keys():
        op_breakdown.breakdown('/Users/maddiehuffman/Desktop/broken/PD/MRPphoneNEW.csv', 'PD', f, j_defs.get(f), True)
print('d_files finished')

# print('Working on cumulative mail and phone')
# for a in alt_defs.keys():
#         op_breakdown.breakdown('/Users/maddiehuffman/Desktop/broken/MPC/MPC_Statewide_.csv', 'MPC', a, alt_defs.get(a), False)
# print('Cumulative mail and phone finished')
# 
# print('Working on new mail and phone')
# for b in alt_defs.keys():
#         op_breakdown.breakdown('/Users/maddiehuffman/Desktop/broken/MPD/MPD_Statewide_.csv', 'MPD', b, alt_defs.get(b), True)
# print('New mail and phone finished.')

####################################################################
print('Starting mailing process')
r = open('Responses.csv','r')
responses = csv.reader(r)
r_list = []
for line in responses:
    r_list.append(line)
cl_r_list = []
for item in r_list[1:]:
    cl_r_list.append(item)

from datetime import datetime
now = datetime.now()

for a_list in cl_r_list:
    if a_list[5] == 'Mail list - daily updates only':
        filetype = 'MD'
        SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,str(a_list[6]),filetype,str(a_list[6]),str(a_list[7])))])
    elif a_list[5] == 'Mail list - cumulative with daily updates':
        filetype = 'MC'
        SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,str(a_list[6]),filetype,str(a_list[6]),str(a_list[7])))])
    elif a_list[5] == 'Phone list - daily updates only':
        filetype = 'PD'
        SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,str(a_list[6]),filetype,str(a_list[6]),str(a_list[7])))])
    elif a_list[5] == 'Phone list - cumulative with daily updates':
        filetype = 'PC'
        SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,str(a_list[6]),filetype,str(a_list[6]),str(a_list[7])))])
    elif a_list[5] == 'Phone & Mail daily updates only':
        filetype = 'MPD'
        SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,str(a_list[6]),filetype,str(a_list[6]),str(a_list[7])))])
    elif a_list[5] == 'Phone & Mail - cumulative and daily updates':
        filetype = 'MPC'
        SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,str(a_list[6]),filetype,str(a_list[6]),str(a_list[7])))])

print('Mailing process finished')




