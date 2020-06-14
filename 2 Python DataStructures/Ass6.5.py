text = "X-DSPAM-Confidence:    0.8475";
inds = text.find('0.8475')
print('inds=',inds)
string = text[inds:]
print('string',string)
fno = float(string)
print(fno)
