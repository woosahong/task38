# Task 38.2

import spacy

# Load the spaCy md language model.
nlp = spacy.load('en_core_web_md')

# Function to recommend the next movie to watch.
def next_movie(description):
    # Open and load file contents.
    movies = open("movies.txt", "r")
    # Read the file contents, strip the white spaces and split the sentences at every new line.
    movies_list = movies.read().strip().split("\n")
    # Declare and initialize a list to store the movie titles and another to store the movie descriptions.
    movie_title = []
    movie_desc = []

    # Iterate as many times as the number of movies in the text file. 
    for i in range (len(movies_list)):
        # Split movies into title and description and store it into the appropriate lists.
        title, desc = movies_list[i].split(" :")
        movie_title.append(title)
        movie_desc.append(desc)

    # Index counter.
    index = 0
    # Declare and initialize a list to store similarity values of the movies.
    similarity_list = []
    # Call the loaded nlp object on description.
    model_sentence = nlp(description)

    # Iterate as many times as the number of movies in the text file.
    for sentence in movie_desc:
        # Check similarity between the movie description with the recently watched movie description.
        similarity = nlp(sentence).similarity(model_sentence)
        # Store the similarity output to the similarity list.
        similarity_list.append(similarity)
        # Prints the movie title and the similarity to the recently watched movie.
        print(f"{movie_title[index]} - {similarity}")
        # Add 1 to the index.
        index += 1

    # Get the maximum similarity value.
    max_similarity = max(similarity_list)
    # Get the index of highest similarity value.
    max_similarity_index = similarity_list.index(max_similarity)
    # Return the movie title that is similar to the recently watched movie.
    return movie_title[max_similarity_index]

# The movie description that is used to be compared with.
hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

# Prints out the recommended movie to watch next by calling the function.
print(f"\nThe movie recommended to watch next is: {next_movie(hulk_description)}")