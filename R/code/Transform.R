#install.packages(c('readxl', 'tidyverse'))

library("readxl")
library("tidyverse")

question <- read_excel("R/datasets/Jeopardy.xlsx")
print("Question Imported: R/datasets/Jeopardy.xlsx")
answer <- read_excel("R/datasets/Jeopardy.xlsx",sheet = "answers")
print("Answer Imported: R/datasets/Jeopardy.xlsx")


#make tible of qustion tidy
question_tidy <- question %>% 
  pivot_longer(cols = c("Short answer","Fill in the blank","Factual questions", "Disability/accessibility knowledge"),  # nolint
               names_to = "Topic",
               values_to = "question") %>% 
  rename(Points = QUESTIONS)#; View(question_tidy)

#make tible of answer tidy
answer_tidy <- answer %>% 
  pivot_longer(cols = c("Short answer","Fill in the blank","Factual questions", "Disability/accessibility knowledge"),  # nolint: line_length_linter.
               names_to = "Topic",
               values_to = "answer") %>% 
  rename(Points = ANSWERS)#; View(answer_tidy)



#combine two tables to make it more superior
jeopardy <- merge(question_tidy, answer_tidy, by = c("Topic", "Points"))#; View(Jeopardy)

#get each topic and point value
topic <- tibble(unique(jeopardy$Topic)) %>% 
  rename(Topic = `unique(jeopardy$Topic)`)#; View(Topic)

points <- tibble(unique(jeopardy$Points)) %>% 
  rename(Points = `unique(jeopardy$Points)`)#; #View(Points)
print("All data is Tidy")


write.csv(jeopardy, "R/datasets/Jeopardy.csv")
print("write R/datasets/Jeopardy.csv")

write.csv(topic, "R/datasets/Topic.csv")
print("write R/datasets/Topic.csv")

write.csv(points, "R/datasets/Points.csv")
print("write R/datasets/Points.csv")