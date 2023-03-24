
# MIT License
# Copyright (C) 2023 Leo O. Pratt-Thomas
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. # nolint
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# install.packages(c('readxl', 'tidyverse'))

library("readxl")
library("tidyverse")

question <- read_excel("R/datasets/Jeopardy.xlsx",sheet = "qustions")
print("Question Imported: R/datasets/Jeopardy.xlsx")

answer <- read_excel("R/datasets/Jeopardy.xlsx",sheet = "answers")
print("Answer Imported: R/datasets/Jeopardy.xlsx")

color <- read_excel("R/datasets/Jeopardy.xlsx",sheet = "hex")
print("color Imported: R/datasets/Jeopardy.xlsx")

#make tible of question tidy
question_tidy <- question %>% 
  pivot_longer(cols = c("Short answer","Fill in the blank","Factual questions", "Disability/accessibility knowledge"),  # nolint
               names_to = "Topic",
               values_to = "Question") %>% 
  rename(Points = QUESTIONS)#; View(question_tidy)

#make tibble of answer tidy
answer_tidy <- answer %>%
  pivot_longer(cols = c("Short answer", "Fill in the blank", "Factual questions", "Disability/accessibility knowledge"),  # nolint: line_length_linter.
               names_to = "Topic",
               values_to = "Answer") %>%
  rename(Points = ANSWERS)#; View(answer_tidy)

color_tidy <- color %>%
  pivot_longer(cols = c("Short answer","Fill in the blank","Factual questions", "Disability/accessibility knowledge"),  # nolint
               names_to = "Topic",
               values_to = "Color") %>%
  rename(Points = HEX)#; View(color_tidy)

#combine two tables to make it more superior
jeopardy <- merge(question_tidy, answer_tidy, by = c("Topic", "Points"))
jeopardy <- merge(jeopardy,color_tidy, by = c("Topic", "Points"))

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