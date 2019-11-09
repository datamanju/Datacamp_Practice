#1. Ployglot supports different languages, able to translate text
# Spanish NER with ployglot example
from polyglot.text import Text
text = """El presidente de la Generalitat de Cataluña,
                  Carles Puigdemont, ha afirmado hoy a la alcaldesa 
                  de Madrid, Manuela Carmena, que en su etapa de 
                  alcalde de Girona (de julio de 2011 a enero de 2016) 
                  hizo una gran promoción de Madrid."""
ptext = Text(text)
ptext.entities

#2. French NER with polyglot
# Create a new text object using Polyglot's Text class: txt
txt = Text(article)

# Print each of the entities found
for ent in txt.entities:
    print(ent)
    
# Print the type of each entity
print(type(ent))

# Create the list of tuples: entities
entities = [(ent.tag, ' '.join(ent)) for ent in txt.entities]

# Print the entities
print(entities)

#3. Spanish NER with polyglot
# Initialize the count variable: count
count = 0

# Iterate over all the entities
for ent in txt.entities:
    # Check whether the entity contains 'Márquez' or 'Gabo'
    if "Márquez" in ent or "Gabo" in ent:
        # Increment count
        count += 1

# Print count
print(count)

# Calculate the percentage of entities that refer to "Gabo": percentage
percentage = count * 1.0 / len(txt.entities)
print(percentage)