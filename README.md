What is published here is primarily a proof of concept that the tech stack is installed and working. 

There are two primary test cases

1) A negative test case based against a basic, static localhost site with no popups. This case is designed to fail cleanly as the specified element does not exist on the page, with no stacktrace elements to confuse the error message
2) A postiive test case against a dynamic modern website with both cookie and marketing popups. The test is designed to pass cleanly, even though dynamic re-rendering of the page means the selected element will re-order the parts of its name frequently.

3) The third test case is an example of different types of test, which I am incorporating into future test cases as appropriate. I will be publishing additional examples shortly.

Outstanding tasks
Move URLs under test to central config rather than in individual test cases. That way we can switch two tests down to one. 
incorporate test cases which more directly mimic user behaviour, as the click element piece is designed to find the element whether or not a popup has been dismissed or not.  
