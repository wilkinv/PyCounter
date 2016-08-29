import click, string

@click.command()
@click.option('--highest', is_flag=True, help='Shows you the word with the highest word count.')
@click.argument('out', type=click.File('r'), default='Paragraph.txt', required=False)

def main(out, highest):
    """Shows the number of occurences of each word in a text file"""
    map = {}
    max = -1
    maxKey = ""
    #This reads in the text, removes all punctuation, and stores the string
    words = out.read().translate(string.maketrans("", ""), string.punctuation)
    click.echo("The number of occurences for each word is:")
    #Makes all characters lowercase and splits the string by space to separate words
    #Loops through each word in the resulting array
    for word in words.lower().split():
    	#Add the word in the dictionary and set count to 1
    	if word not in map:
    		map[word] = 1
    	#Increment word count if found
    	else:
            map[word] = map[word] + 1
    for key in map:
    	#maxKey is the word with the most occurences
    	if map[key] > max:
    		max = map[key]
    		maxKey = key
    	click.echo(key + ": %d" % map[key])
    #Check if highest option has been set
    if highest:
        click.echo("The word that appears most is: " + maxKey)
