
#################################################################
#
#Preprocessing the Data
#
#################################################################

import glob 
import os
import re
import string 
import os.path
import random
random.seed(36)


#Remove all files except transcripts from the House
path_name="./output/2014/*/__text/*.txt"
all_files= glob.glob(path_name)    

for file in all_files:
    with open(file, 'r') as f:
        words=f.read()
        if words.find('[House]') < 0:
            os.remove(file)


#List of States
state_list=['Alabama','Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia',
'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire',
'New Jersey', 'New Mexico','New York','North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 
'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah','Vermont','Virginia', 'West Virginia', 'Wisconsin', 'Wyoming']

#Create a dictionary of speakers that point to a list of all their text 
path_name="./output/2014/*/__text/*.txt"
all_files= glob.glob(path_name)   

speaker_dict={}

for file in all_files:
    with open(file, 'r') as f:
        words=f.read()
        pattern=r'\n  ((?:Mr.|Mrs.|Ms.|The) [A-Z]+[c]*[A-Z]*[^/S][-]*[A-Z]{3,60}(Speaker)?)'

        speakers = re.findall(pattern, words, re.DOTALL)
        parsed = re.split(pattern, words)
        #print parsed[0]
        #iterate through every other element of parsed to pull out names and text
        successful=0.0
        unsuccessful=0.0
        for i in range(1,len(parsed),4):
            speaker=parsed[i]
            try:
                successful+=1
                speaker=speaker.strip('Mr.')
                speaker=speaker.strip('Mrs.')
                speaker=speaker.strip('Ms.')
                speaker=speaker.lstrip().upper()
                text=parsed[i+2]
                text = ''.join(ch for ch in text if ch not in set(string.punctuation)) #Strip punctuation characters from the string. In Python, this happens to be usually done with a .join on the string object, but don't be thrown if you're used to other languages and this looks weird (hell, it looks weird to me), all we're doing is stripping punctuation.
                text=text.replace('\n','')
                for  state in state_list:
                    text=text.replace(state,'')
            except Exception as exc:
                unsuccessful+=1
 
            if speaker in speaker_dict:
                speaker_blurbs=speaker_dict.get(speaker)
                speaker_blurbs=speaker_blurbs.append(text)
            else:
                new_speaker_list=[]
                new_speaker_list.append(text)
                speaker_dict[speaker]=new_speaker_list



#Import list of the most liberal and conservative members of the House of Representatives
dw={}
dw['LEE']=-.746
dw['CONYERS']=-0.707
dw['MCDERMOT']=-.707
dw['WATERS']=-.707
dw['FILNER']=-.682
dw['STARK']=-.674
dw['CLARKE']=-.648
dw['SCHAKOWS']=-.643
dw['GRIJALVA']=-.639
dw['PAYNE']=-.639
dw['KUCINICH']=-.627
dw['LEWIS']=-.624
dw['ELLSON']=-.619
dw['CAPUANO']=-.618
dw['OLVER']=-.613
dw['EDWARDS']=-.613
dw['FUDGE']=-.607
dw['HINCHEY']=-.605
dw['WOOLSEY']=-.600
dw['BALDWIN']=-.594
dw['HASTINGS']=-.593
dw['MILLER']=-.592
dw['JACKSON']=-.592
dw['VELAZQUEZ']=-.588
dw['BASS']=-.579
dw['MOORE']=-.578
dw['HONDA']=-.576
dw['MCGOVERN']=-.572

dw['WATT']=-.568
dw['NADLER']=-.558
dw['CHU']=-.557
dw['FLAKE']=.988
dw['PAUL']=.970
dw['BROUN']=.941
dw['MASSIE']=.918
dw['GRAVES']=.906
dw['MULVANEY']=.895
dw['AMASH']=.867
dw['STUTZMAN']=.795
dw['CAMPBELL']=.784
dw['MCCLINTOCK']=.780
dw['FRANKS']=.775
dw['DUNCAN']=.773
dw['LABRADOR']=.751
dw['HUELSKAMP']=.749
dw['HENSARLIN']=.745
dw['WALSH']=.741
dw['WOODALL']=.737
dw['GOWDY']=.730
dw['LAMBORN']=.728
dw['QUALYE']=.728
dw['CHAFFETZ']=.722
dw['ROYCE']=.714
dw['POMPEO']=.707
dw['GARRETT']=.704
dw['SCOTT']=.703
dw['WESTMORE']=.697
dw['JORDAN']=.690
dw['HUIZENGA']=.688
dw['SCHWIKERT']=.682
dw['PENCE']=.677
dw['FOXX']=.671


#Go through speaker list and through out all entries not found in dw_dict
for speaker, speeches in speaker_dict.items():
    if speaker not in dw.keys():
        del speaker_dict[speaker]
        #print speaker



#Perform some counts on speaker_dict


def generate_bucket(fold_num):
    return random.randint(1,fold_num)

def write_to_file(category, speaker, speeches):
    fold_num=5  
    test_path='./congress_data_rand/test/'+category
    train_path='./congress_data_rand/train/'+category
    
    counter=0
    for speech in speeches:
        
        bucket=generate_bucket(fold_num)
        if bucket==2:
            complete_path=os.path.join(test_path, speaker+"_"+str(counter)+'.txt')
        else:
            complete_path=os.path.join(train_path, speaker+"_"+str(counter)+'.txt')
            
        with open(complete_path,'w') as f: 
            f.write(speech)
        
        counter+=1
    
    return len(speeches)

def write_to_file_random(category, speaker, speeches):
    fold_num=5  
    counter=0

    for speech in speeches:
        bucket=generate_bucket(fold_num)
        category=generate_bucket(2)

        if bucket==3:
            test_path='./congress_data2/test/'+category
            complete_path=os.path.join(test_path, speaker+"_"+str(counter)+'.txt')

        else:
            train_path='./congress_data2/train/'+category
            complete_path=os.path.join(train_path, speaker+"_"+str(counter)+'.txt')
            
        with open(complete_path,'w') as f: 
            f.write(speech)
        
        counter+=1

    return len(speeches)

    

total_liberal_count=0.0
total_cons_count=0.0
for speaker,speeches in speaker_dict.items():
    if speaker in dw.keys():
        orientation = dw.get(speaker)
        if orientation < 0: 
            liberal_count=write_to_file('liberal', speaker, speeches)
            total_liberal_count+=liberal_count
        elif orientation > 0: #conservative
            cons_count=write_to_file('conservative', speaker, speeches)  
            total_cons_count+=cons_count

print total_liberal_count
print total_cons_count
try:
    print total_liberal_count / (total_liberal_count+total_cons_count)
except:
    print "0"
