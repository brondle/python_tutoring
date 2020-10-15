import random

#ballad stanza aabccb

new_string = 'this is my new string, it isnt long or short or flat or thin, it is just right'
print('new string: ', new_string)

class EraseWordGenerator:
    #only runs once, at startup
    def __init__(self, text):
        self.text = text
        self.list = text.split()
        self.number = len(self.list)/2

    def list_to_str(self, input_seq):
    # Join all the strings in list
        final_str = ' '.join(input_seq)
        return final_str

    def random_l(self, length, rn):
        num = random.sample(range(length), rn)
        return num

    def random_erase_replace(self):
        new_list = []
        list_length = len(self.list)
        min = round(list_length/2)
        max = round(list_length/1.33)
        rn = random.randint(min, max)
        random_list = self.random_l(list_length, rn)
        print(list_length, rn, random_list)

        for i in range(list_length):
            if i in random_list:
                char_length = len(self.list[i])
                em = ' '
                self.list[i] = self.list[i].replace(self.list[i], em*char_length)
        erased_string = self.list_to_str(self.list)
        return erased_string

    def seq_of_sents(self, sentence, num_of_sents):
        dont_exceed = len(sentence)-num_of_sents
        r_choice = random.randint(0, dont_exceed)
        return sentence[r_choice:r_choice+(num_of_sents)]

    def erase_words(self, all_but_n):
        sent_length = len(self.list)
        print('word list', self.list)
        num_to_erase = sent_length - all_but_n
        print('sent length:', sent_length)
        erase_list = random.sample(self.list, num_to_erase)
        print(sent_length,num_to_erase,'\n', erase_list)
        for i in range(len(self.list)):
            if self.list[i] in erase_list:
                char_length = len(self.list[i])
                em = ' '
                self.list[i] = em*char_length
            else:
                self.list[i] = self.list[i]
                # print(self.list[i])
        erased_string = self.list_to_str(self.list)
        return erased_string

    def erase_sentence(self, list_of_strings):
        for i in range(len(list_of_strings)):
            new_erase_list = list_of_strings[i].split()
            rn = random.randint(1, 5)
            erasure = self.erase_words(new_erase_list, rn)
            print(self.erase_words(new_erase_list, rn))
    # return erasure

replace = EraseWordGenerator(new_string)

print(replace.random_erase_replace())
#two models of dealing with lists of multiple strings - in-class method
replace.erase_sentence(whatever)
#out of class method
for i in whatever :
    replace = EraseWordGenerator(i)

    print(replace.random_erase_replace())

print(replace.list)
