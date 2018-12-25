import argparse

keyword = "mackerel"

words = [keyword]

def get_words(args):
	w = words
	if args.dictionary:
		try:
			with open(args.dictionary, 'r', encoding="utf8", errors='ignore') as f:
				content = f.readlines()
				w = [x.strip() for x in content] 
		except Exception as e:
			print(e)
			print("Could not open dictionary")
	return w

def get_mackerel_words(args):
	try:
		with open(args.text_file, 'r', encoding="utf8", errors='ignore') as f:
			content = f.readlines()
	except Exception as e:
		print(e)
		print("Could not open text_file")
		return []
	content = [x.strip() for x in content]
	words = get_words(args)
	mackerel_words = []
	for word in words:
		counter = 0
		letter_set = set([c for c in word.lower()])
		rearrange = []
		for entry in content:
			ent_set = set([c for c in entry.lower()])
			if ent_set.isdisjoint(letter_set):
				counter += 1
				rearrange.append(entry)
		if counter == 1:
			mackerel_words.append((rearrange[0], word))
	return mackerel_words

def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--text-file', type=str, default='states.txt',
	                    help='an integer for the accumulator')
	parser.add_argument('--dictionary', 
	                    help='Words to look for mackerel words from.')

	args = parser.parse_args()
	mackerel_words = get_mackerel_words(args)
	for word, mackerel in mackerel_words:
		print("{} is the only word which shares no letters with the word {}.".format(word, mackerel))

	print("Script finished.")
if __name__ == "__main__":
	main()