# Frankie's Notebook
This is a project for a beginner hack in Hack-or-Treat 2026.

## Inspiration
Frankenstein’s monster is a classic Halloween character, famous for its grotesque appearance and isolation from society. Due to a lack of social interaction, Frankenstein had to learn how to communicate by observing humans and reading classical books. We took this idea to create a flashcard review app designed to help him organize vocabulary, track his learning progress, and review words at his own pace.

## What it does
Frankie's Notebook is a customizable flashcard application that allows users to create their own vocabulary lists by adding words and definitions. Users can organize flashcards into collections by topic, with a default “Favourites” collection for tricky words. Inside collections, you can test your knowledge by going over all the flashcards, and as you go over them, you can select the tough ones so you can revise them later. At any point, you can add, delete, or edit your flashcards and collections.

## How we built it
To make development easier, we separated the project into UI development, data loading, and data management, with each group member responsible for building one and ensuring they worked together when combined. We used Python as the main language, combined it with Tkinter (Python’s library) to develop the user interface, and JSON to store data.

## Challenges we ran into
The main challenge we faced was connecting different parts of the project and managing shared data. Initially, we considered maintaining separate data structures for flashcards and collections, with each being saved to permanent storage (JSON files) independently. However, since flashcards and collections are closely related, we realized this approach could lead to data inconsistencies and make synchronization difficult. We eventually decided to store the application's data in one shared dictionary, allowing different managers to access and modify the same underlying data.

## Accomplishments that we're proud of
We’re proud that we could complete our first hackathon together and create this software in the limited amount of time. We also liked how this idea tied to the theme, while remaining very useful in university students’ daily lives. 

## What we learned
We didn’t all know how to do UI in Python, so we learned Tkinter along the way with the help of AI. We also learned how to define project structures and to divide up the work. 

## What's next for Frankie’s Notebook
We could easily extend this project to connect to a free dictionary API, which could provide additional phonetic pronunciations, example sentences, synonyms, and antonyms. This could make the learning process even more efficient. We could also build additional features such as viewing different stats, exporting and importing collections to share between users, and sound effects to enhance engagement. 

## Working Demo
Screenshots demonstrating current functionality
<img width="960" height="725" alt="image" src="https://github.com/user-attachments/assets/05dff263-6aae-47d3-a3b4-07b43a48ad2a" />
<img width="960" height="731" alt="image" src="https://github.com/user-attachments/assets/fab07a75-2cf4-4bd0-9907-c75032d5049d" />
<img width="960" height="735" alt="image" src="https://github.com/user-attachments/assets/b3b8b357-bde7-4f15-b154-808589f89dd9" />
<img width="960" height="729" alt="image" src="https://github.com/user-attachments/assets/0b87cebb-5181-41a1-b773-694097742638" />


