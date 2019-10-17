import time

# start timing
t1 = time.time()

# open files
filereader = open('data/adult.data', 'r')

filewriter = open('data/converted_data.mat', 'w')

# define arraies for conversion
workclass = ['?', 'Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay',
             'Never-worked']

education = ['?', 'Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th',
             '7th-8th', '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool']

marital_status = ['?', 'Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed',
                  'Married-spouse-absent', 'Married-AF-spouse']

occupation = ['?', 'Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
              'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving',
              'Priv-house-serv', 'Protective-serv', 'Armed-Forces']

relationship = ['?', 'Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried']

race = ['?', 'White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black']

sex = ['?', 'Female', 'Male']

native_country = ['?', 'United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany',
                  'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran',
                  'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland',
                  'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary',
                  'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago',
                  'Peru', 'Hong', 'Holand-Netherlands']

isover5K = ['?', '>50K', '<=50K']

# define a 2-dimension array
items = [workclass, education, marital_status, occupation, relationship, race, sex, native_country, isover5K]

# read file from lines
for eachline in filereader:

    # iterate arraies
    for item in items:

        count = 0

        # iterate strings and replace them with integers
        for element in item:
            # replace strings with integers
            eachline = eachline.replace(element, str(count))

            count += 1

    # write to file
    filewriter.write(eachline)

# close files
filereader.close()
filewriter.close()

# end timing
t2 = time.time()

print('done')
print(str(t2 - t1))