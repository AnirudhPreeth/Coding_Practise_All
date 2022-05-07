"""
Logical Operators. 
"""
#We use this when we have multiple conditions. 

"""
if applicant has high income AND good credit
   Elligible for loan
And operator. 

if applicant has high income OR good credit
   Elligible for loan
OR operator. 

if applicant has good credit AND doesn't have a criminal record
   Elligible for loan

"""
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Elligible for loan")
#And operator. 

has_high_income = False
has_good_credit = True
if has_high_income and has_good_credit:
    print("Elligible for loan")
#Message does not print.

has_high_income = False
has_good_credit = True
if has_high_income or has_good_credit:
    print("Elligible for loan")

has_high_income = True
has_good_credit = True
if has_high_income or has_good_credit:
    print("Elligible for loan")

has_high_income = False
has_good_credit = False
if has_high_income or has_good_credit:
    print("Elligible for loan")
#Or operator. Message will print even if one is false. Both false, message does not print.

has_good_credit = True
has_criminal_record = False
if has_good_credit and not has_criminal_record: 
    print("Elligible for loan")

has_good_credit = True
has_criminal_record = True
if has_good_credit and not has_criminal_record: 
    print("Elligible for loan")
#NOT operator.

#AND : Both should be true.
#OR : At least one should be true.
#NOT : Changes the boolean value. True changes to False. False changes to True. 

