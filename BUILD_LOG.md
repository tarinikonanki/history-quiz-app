# Build Log — US History Quiz

## Task 1 - Scaffold Repo and write CLAUDE.md
- Brief: Create a CLAUDE.md along with setting up app structure/basic project files for a quiz app over american history.
- What Claude proposed: Claude proposed an app which offered multiple-choice US history questions that would provide explanations for each incorrect/correct answer and give feedback at the end over what the user struggled with.
- What I changed before approving: In order to keep it simple, I took out the feature for explanations and final feedback.
- Verification: I checked Github to see if ClAUDE.md and app project files existed and they did.
- One thing I learned: I learned how to continuously prompt Claude Code to change things I didn't like/want and get my desired final product for the plan/CLAUDE.md
.
## Task 2 - Design App Layout
- Brief: Design the layout for the app with title page explaining quiz and start button. The layout should be simple, with there being a title at the top that is always present and a brief explanation of the app's purpose below it. Below this will be a start button. Keep the layout shades of blue and visually pleasing.
- What Claude proposed: Claude proposed a simple page layout with the title centered and a short paragraph of text below it, with a start button below that.
- What I changed before approving: To make it more specific, I requested that the start button was also centered.
- Verification: I looked at the app to check if it had a title, a brief description, and start button in the layout I specified, which it did.
- One thing I learned: I learned how to be specific in my briefs and make sure Claude followed what I wanted by prompting it.

## Task 3 - Question List
- Brief: Write multiple-choice American history questions and add them to a list and put them in a file, making sure to include multiple wrong option choices and a correct option choice. There should be four total answer choices for each question, with 3 wrong choices and 1 correct choice. Make 10 questions.
- What Claude proposed: Claude proposed making 10 questions with 3 wrong answers and 1 right answer, with each entry being a dict with three keys: a question, choices, and answer. It also provided a list of topics it covered.
- What I changed before approving: To make it more specific to my needs, I changed some of the topics the questions covered such as going over the American Revolution.
- Verification: I looked at the file on github to see if it had the list of questions and was committed properly.
- One thing I learned: I learned how to analyze given plans to identify needed changes.

## Task 4 - Question Display
- Brief: Create a display for each question, calling each question from the list and presenting each answer choice below it (with 2 options positioned on left side and 2 options positioned on the right side). Make the question and answer choices be within a box.
- What Claude proposed: Claude proposed making the page with the quiz questions appear in the same style as the title page, with a submit button appearing after an answer choice is clicked.
- What I changed before approving: I made the submit button always visible.
- Verification: I looked at the running app to check if there was a box with a question, 4 answer choices, and a submit button always visible, which it was.
- One thing I learned: I learned how to look carefully at the details and decide based on given information what would make the best functionality choice for my app.

## Task 5 - Answer Choice Wrong or Right
- Brief: Let the user click an answer and be told it was either right or wrong, with that button they clicked turning green if it was right or red if it was wrong. The user can only click one answer and are given only one attempt at answering the question. They can only submit one answer essentially. Createa plan but don't implement it yet.
- What Claude proposed: Claude proposed making 2 answer choices have color when the user chooses incorrectly (that being the user's chosen answer and the right answer). It additionally makes sure right answers are green and wrong answers are red.
- What I changed before approving: I specified it to make sure the other choices would stay the normal color to not confuse the user.
- Verification: I ran the app, checking if the colors were correct when a wrong answer was chosen and when a right answer was chosen.
- One thing I learned: I learned how to make specific decisions for my app choices and ensure it functioned based on user needs such as by making the interface less confusing.

## Task 6 - Answer Choice Wrong or Right
- Brief: Create a "next" button for the user to click after they attempt each question one time and only one time, and when the "next" button is pressed, the user goes to the next question in order. The "next" button is positioned below the answer choices on the right side.
- What Claude proposed: Claude proposed making the next button the right side and below the answer choices as I specified.
- What I changed before approving: I decided to change it to make the submit button be replaced by the next button. I further prompted Claude afterwards to change the color of the next button to show a change.
- Verification: I ran the app, checking if the next button showed up, was a different color than the submit button, and took the user to the next page.
- One thing I learned: I learned how to look at what Claude offered me and decide on the go how I wanted to change my app.


# AI Workflow

For planning, I used Claude as it helped come up with ideas that I typically wouldn't think of right off the bat and expand on the ideas I came up with so I could create a more cohesive and fully-formed plan. I then used Claude Code to execute this plan by putting it in plan mode and then giving it a brief for each feature. I was then able to change it based on what I wanted to implement differently and then let Claude Code implement these ideas. For polishing, I used Copilot to change variable names and overall make the code more readable. For reviewing, I used Claude to make sure everything was cohesive, and the plan was good/made sense.

For polishing, Copilot definitely outperformed other AI tools in making small fixes and making the code more readable. It was generally faster in this and more suited to this task compared to other AI tools.

Initially, I actually tried using Claude to make the code readable in the instructions itself, but I switched to Copilot as I realized it would work better after finishing the rest of the app.


# Reflection

The agentic workflow helped build the actual code based off the instructions I gave it while making it look complete and visually appealing. This would not be possible for me to do in just 4 hours as I would take much longer to create the frontend and make it look nice, especially as I don't have much experience with this.

Sometimes, I would have to step in and override Claude when I gave it a brief and asked it for a plan. It would sometimes present ideas or features that didn't align with what I wanted or weren't specific enough, so I would add extra prompting and information to achieve what I wanted my app to be like. For instance, Claude wanted to make the submit button only visible after a person clicks an answer choice, but I thought it would make more sense and personally be more useful to me if the submit button was always present so I knew I could change my answer before I ultimately submitted. In cases like this, I understand my needs better than Claude does so I need to prompt it further to meet it.

In general, the project made me make more decisions especially as I had to override Claude a lot to make the app fit my specifications. I also got more experience in deciding functionalities for apps and making it more user-friendly as I had to figure out which specific features to create, how to arrange/style them, and what would be the most clear for the user. Additionally, the project made me see which gaps in knowledge I still had to overcome, such as my knowledge of testing. I could do simple tests, but with some of the more complicated features I have, I didn't know how to create tests for them, so that is still something I have to work on. I also still have to work on making my plans more specific.

I will bring this workflow into my internship by asking my manager their expectations for me in regards to AI use and then utilizing what I've learned to fit those expectations. For instance, if permitted, I will be able to ship code faster with Claude depending on what type of project it is. My goal on Day 1 is to outline expectations and find out how I may apply what I learn.

