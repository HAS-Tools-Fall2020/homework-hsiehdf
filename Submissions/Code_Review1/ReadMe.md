# Assignment 7
Diana Hsieh

HAS Tools

10/9/2020

- - -

Welcome Gillian! Please make yourself at home.  
**Thank you, I made a sandwich and grabbed a beer from the fridge  - Jill**

## Steps to Run my code

I hope all you need to do to run my code is to hit "run me" in each section of code. You will see comments in the code on what I would like you to predict for me!
The data (streamflow_week7) has already been downloaded and placed into my repo with the following path: homework-hsiehdf-git --> Submissions --> Code_Review1 --> data

Thanks!

Table 1. My Predictions

|Model |  Week 1 Prediction | Week 2 Prediction |
|--- | --- | ---|
|My Autoregressive Forecast| 161.0572702072062 | 206.02509172431473 |
|My **Actual** Forecast | 58 | 57 |


### Written Assessment

Hi Diana!

First of all, it would be very hard for me to score anyone else who tried their very best and got a working script that was decently neat and organized anything less than all 3's.  All being in the same boat, we know how much of a challenge and work this can be and I commend you for your hard work, determination, overall intelligence and, of course, a successful final code!!  That said, I will give you a detailed written assessment to the best of my capability because I know the feedback is also so valuable and will be needed for revising your code and discussing changes in the Week 8 assignment......


**On to your code review:**

*Is the script easy to read and understand?*  
  - Yes.  But the 'for' loops hurt my brain a little bit initially....not your fault though, likely just my brain.  &#x1F609;  I did however get what they were doing after some ponderance and playing around with running and printing and likely have a better understanding of for loops after this for it!  Interesting approach!

*Are variables and functions named descriptively when useful?*
  - Yes. There is little to suggest to update or correct from my viewpoint - so a small suggestion might be to name the 'this_week' and 'next_week' pred variables with an "AR" indicator to set them apart from the 'week1_pred' and 'week2_pred' for your actual prediction from the other code approach?

*Are the comments helpful?*  
  - Yes, they were descriptive of what each section of code is accomplishing and what I needed to pull out.

*Can you run the script on your own easily?*  
  - Yes, just went through each code block successively as instructed.  But also works when just "run all below" is selected.  If any small improvement could be made, it might be just adding a comment block above the AR predictions so that one can just "Run below" at top of code, scroll down and see the final 4 values printed out at bottom with comments indicating. (Code goals for me for sure)

*Are the doc-strings useful?*  
 - Yes, the doc string was useful to understand what the function is doing before even seeing the function code.   
**Notes:**  
  - Firstly - typo - what's a Fuction?  LOL &#x1F640;
  - I do think there might be a carryover old variable name in this statement ("two_week_mean is an int or float").  There are no other instances of the variable "two_week_mean" in the code.
  - Also would recommend clearly stating the Parameter and the Return values as in the example in the EDS course material:

https://www.earthdatascience.org/courses/intro-to-earth-data-science/write-efficient-python-code/intro-to-clean-code/expressive-variable-names-make-code-easier-to-read/   

**example from online tutorial:**

  def fahr_to_kelvin(fahr):  
      """Convert temperature in Fahrenheit to kelvin.

      Parameters:
      -----------
      fahr: int or float
          The tempature in Fahrenheit.

      Returns:
      -----------
      kelvin : int or float
          The temperature in kelvin.
      """
      kelvin = ((fahr - 32) * (5 / 9)) + 273.15
      return kelvin

*Does the code follow PEP8 style consistently?*  
 - It seems to follow it perfectly based on the '0' issues identified by the Flake8 Linter as well as what i recall of the training material description of PEP8.

*If not are there specific instances where the script diverges from this style?*
  - I do not notice any.  Looks clean, does not repeat itself, etc.

*Is the code written succinctly and efficiently?*  
  - Yes, I like how you did the 'for' loop on row 55 to both shift your data and add columns.  That seemed very efficient to me.  
  One suggestion perhaps - can combine these two lines to one line:  
  week1_pred = get_mean(14)  
  week1_pred_rounded = int(week1_pred)  
  to -  
  week1_pred = int(get_mean(14))  

*Are there superfluous code sections?*  
  - No, each section has a purpose and an output.  

*Is the use of functions appropriate?*
  - Yes, the function produces the final prediction values and can be utilized in a flexible manner for any time period of 'tail' data.

*Is the code written elegantly without decreasing readability?*
  - yes 


**Other Comments:**  
I was wondering what your basis was for subtracting 1cfs for the 2 week forecast.   Maybe add a comment or some code basis as to why?

P.S. ....Not too sure you're going to win the one-week forecast for this week as I saw an upward trend last week of ~10% in my model -  Taking a week off from winning might be a nice change for you though.  Come and see how the rest of us are living! LOL  &#x1F61D;   

P.P.S. Join me in my emoji game!  I know you like emojis!!
&#x1F929;  
https://www.unicode.org/emoji/charts-13.1/emoji-list.html

Table 2. Numeric Score For My Code

|Criteria |  Score |
|--- | --- |
|Readability| 3 |
|Style | 3 |
| Code Awesome| 3|
