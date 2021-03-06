# Introduction about the app. 

Comparing 2 texts to get a similarity score. This is a program that takes as inputs two texts and uses a metric to determine how similar they are. The metric being used to compare teh 2 texts is the Cosine Similarity Score.

## Description of how app works
This app will calculate the TF-IDF of the corpus, then it will calculate the cosine similarity between the 2 text samples. This cosine similarity is what will be used to determine how similar the Sample Texts are. 

## Instructions on running the APP using Python

[Go go this link to play with the live hosted app](https://text-similarity-comparison.herokuapp.com)

*If you wish to clone this repo and execute the code and get a comparison using the command line, follow the instructions below*

If you want to use the inputed **default text** to do comparisons, 

- Navigate to text_similarity folder.
- type `python text_similarity.py` to get a comparison score. 

To provide your own sample text, you have **2 options**. 

**Option 1:**
 
Open the `text_similarity.py` app under `app/api`, 

Under "if __name__ == "__main__" " command, change the sample text and repeat the above process by `python text_similarity.py`

**Option 2:**

* Open the command line
* navigate to `text_similarity/app/api`
* type in `Python` to enter a python shell
* type `import text_similarity` to import the python file into the python shell
* Define your 2 text inputs like this
* sample3 = "text string"
* sample4 = "new text string"
* after defining the text, type
* `text_similarity.similarity_comparison(sample3, sample4)` to get a score
* Repeat the above process as many times as you wish
* type `exit()` to exit the python shell

## Instructioins on running the APP using Docker

* navigate to "text_similarity" folder from your command line
* make sure you have docker running first
* type `docker-compose build` to build the docker image
* type `docker-compose up` to run the web application
* go to `localhost` to see the app. The localhost url given by docker by default may not work, so just go to `localhost` to see the app. 