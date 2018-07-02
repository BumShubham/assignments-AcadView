import re
#Q1
emails = "zuck26@facebook.com" " page33@google.com" " jeff42@amazon.com"
pattern = (r'[\w]+')
print(re.findall(pattern, emails))


#Q2
aa = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
l = re.findall(r'[bB]\w+',aa)
print(l)

#Q3
sentence = "A, very very; irregular_sentence"
output = " ".join(re.split('[;,\s_]+', sentence))                                      #Removal of extra special characters from the irregular string
print(output)

#Q$
