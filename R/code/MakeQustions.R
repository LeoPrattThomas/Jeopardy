library(tidyverse)

jeopardy <- read.csv("R/datasets/random_questions/JEOPARDY_QUESTIONS1.csv")

topics <- tibble(unique(jeopardy$Topics)) %>% 
  rename(Topic = `unique(jeopardy$Topics)`)

points <- tibble(unique(jeopardy$Points)) %>% 
  rename(Points = `unique(jeopardy$Points)`)

write.csv(topics, "R/datasets/random_questions/AllTopics.csv")
print("write R/datasets/Topic.csv")

write.csv(points, "R/datasets/random_questions/AllPoints.csv")
print("write R/datasets/Points.csv")

