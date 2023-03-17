library(readxl)
library(tidyverse)
Question <- read_excel("R/datasets/Jeopardy.xlsx")
Answer <- read_excel("R/datasets/Jeopardy.xlsx",sheet = "answers")

#make tible of qustion tidy
Question_tidy <- Question %>% 
  pivot_longer(cols = c("Short answer","Fill in the blank","Factual questions", "Disability/accessibility knowledge"), 
               names_to = "Topic",
               values_to = "Question") %>% 
  rename(Points = QUESTIONS);#View(Question_tidy)

#make tible of answer tidy
Answer_tidy <- Answer %>% 
  pivot_longer(cols = c("Short answer","Fill in the blank","Factual questions", "Disability/accessibility knowledge"), 
               names_to = "Topic",
               values_to = "Answer") %>% 
  rename(Points = ANSWERS);#View(Answer_tidy)

#combine two tables to make it more superior
Jeopardy <- merge(Question_tidy, Answer_tidy, by = c("Topic", "Points"));# View(Jeopardy)

#get each topic and point value
Topic <- tibble(unique(Jeopardy$Topic)) %>% 
  rename(Topic = `unique(Jeopardy$Topic)`); #View(Topic)

Points <- tibble(unique(Jeopardy$Points)) %>% 
  rename(Points = `unique(Jeopardy$Points)`); #View(Points)

write.csv(Jeopardy, "R/datasets/Jeopardy.csv")
write.csv(Topic, "R/datasets/Topic.csv")
write.csv(Points, "R/datasets/Points.csv")
