import csv
import op_breakdown
import SMTPmail


m = open('MRP_PrimaryAVList.csv', 'r')
master = csv.reader(m)

c = open('/Users/maddiehuffman/Desktop/broken/MPC/MRP_PrimaryAVListCopy.csv', 'r')
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
all_daily.write("HHName,LastName,FirstName,MiddleName,SuffixName,PrimaryAddress1,PrimaryCity,PrimaryState,PrimaryZip,PrimaryOddEvenCode,PrimaryHouseNumber,PrimaryHouseHalf,PrimaryStreetPre,PrimaryStreetName,PrimaryStreetType,PrimaryStreetPost,PrimaryUnit,PrimaryUnitNumber,SecondaryAddress1,SecondaryCity,SecondaryState,SecondaryZip,SecondaryUnit,SecondaryUnitNumber,PrimaryPhone,TelephoneReliabilityCode,EMail,DOB,Gender,ObservedParty,RegistrationDate,GeneralFrequency,PrimaryFrequency,OverAllFrequency,GeneralAbsenteeStatus,PrimaryAbsenteeStatus,CDName,LDName,SDName,CountyName,PrecinctNumber,VoterKey,JurisdictionalVoterId,ClientId,StateVoterId,Latitude,Longitude,MapCode,CellularPhone,HomePhone,OtherPhone,WorkPhone,Township,County Commissioner District \n")
for a_list in diff_1:
    ad.writerow(a_list)
all_daily.close()
m.close()
c.close()

###############################################################################
nmpd = open('/Users/maddiehuffman/Desktop/broken/MPD/MRPmailandphoneNEW.csv','r')
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

c_files = {'MC':'MRPmail','PC':'MRPphone'}
d_files = {'MD':'MRPmailNEW','PD':'MRPphoneNEW'}
cdf = 'MPC'
ddf = 'MPD'
j_defs = {'CD':1,'LD':2,'SD':3,'County':4,'Precinct':5,'Township':6,'CountyCommissioner':7}
alt_defs = {'CD':36,'LD':37,'SD':38,'County':39,'Precinct':40,'Township':52,'CountyCommissioner':53}

print('Working on c_files')
for each_file in c_files.keys():
    for c in j_defs.keys():
        op_breakdown.breakdown((('/Users/maddiehuffman/Desktop/broken/%s/%s.csv') % (each_file, c_files.get(each_file))), each_file, c, j_defs.get(c), False)
print('c_files finished')

print('Working on d_files')
for a_file in d_files.keys():
    for d in j_defs.keys():
        op_breakdown.breakdown((('/Users/maddiehuffman/Desktop/broken/%s/%s.csv') % (a_file, d_files.get(a_file))), a_file, d, j_defs.get(d), True)
print('d_files finished')

print('Working on cumulative mail and phone')
for a in alt_defs.keys():
        op_breakdown.breakdown((('/Users/maddiehuffman/Desktop/broken/%s/MRP_PrimaryAVListCopy.csv') % (cdf)), cdf, a, alt_defs.get(a), False)
print('Cumulative mail and phone finished')

print('Working on new mail and phone')
for b in alt_defs.keys():
        op_breakdown.breakdown((('/Users/maddiehuffman/Desktop/broken/%s/MRPmailandphoneNEW.csv') % (ddf)), ddf, b, alt_defs.get(b), True)
print('New mail and phone finished.')
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
    elif a_list[5] == 'Mail list - cumulative with daily updates':
        filetype = 'MC'
    elif a_list[5] == 'Phone list - daily updates only':
        filetype = 'PD'
    elif a_list[5] == 'Phone list - cumulative with daily updates':
        filetype = 'PC'
    elif a_list[5] == 'Phone & Mail daily updates only':
        filetype = 'MPD'
    elif a_list[5] == 'Phone & Mail - cumulative and daily updates':
        filetype = 'MPC'
    SMTPmail.send_mail( 'dnormile@migop.org', a_list[3], (('Absentee Distribution List %s/%s/%s %s:%s:%s') % (now.month, now.day, now.year, now.hour, now.minute, now.second)), "", [(('/Users/maddiehuffman/Desktop/broken/%s/%s/%s_%s_%s.csv') % (filetype,a_list[6],filetype,a_list[6],a_list[7]))])

print('Mailing process finished')

