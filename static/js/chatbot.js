var questionNum = 0;													// keep count of question, used for IF condition.
var question = '<h1>what is your name?</h1>';				  // first question

var output = document.getElementById('output');				// store id="output" in output variable
output.innerHTML = question;													// ouput first question

function bot() {
  var input = document.getElementById("input").value;
  console.log(input);

  if (questionNum == 0) {
  output.innerHTML = '<h1>hello ' + input + '</h1>';// output response
  document.getElementById("input").value = "";   		// clear text box
  question = '<h1>how old are you?</h1>';			    	// load next question
  setTimeout(timedQuestion, 2000);									// output next question after 2sec delay
  }

  else if (questionNum == 1) {
  output.innerHTML = '<h1>Good to know!</h1>';
  document.getElementById("input").value = "";
  question = '<h1>What do you feel about wars?</h1>';
  setTimeout(timedQuestion, 2000);
  }
 else if(questionNum == 2) {
  output.innerHTML = '<h1>Well yeah it we all can feel it!</h1>';
  document.getElementById("input").value = "";
  question = '<h1>What do you suffer like nightmaress, insomnia etc?</h1>';
  setTimeout(timedQuestion, 2000);
  }
 else if(questionNum == 3) {
  output.innerHTML = '<h1>Well I got your point. Let me suggest you a counsellor. what do you think?(Y/N)</h1>';
  document.getElementById("input").value = "";
   question = '<h1>Thank you for your response!</h1>';
  setTimeout(timedQuestion, 2000);
  }
else if(questionNum == 4) {
  output.innerHTML = '<h1>Here is your doctor. Type Y for confirmation.</h1>';
  document.getElementById("input").value = "";
  question = '<h1>Dr Aran Bhatia. You can book a appointment via our site. Thankyou !</h1>';
  setTimeout(timedQuestion, 4000);
  }
}



function timedQuestion() {
  output.innerHTML = question;
}

//push enter key (using jquery), to run bot function.
$(document).keypress(function(e) {
if (e.which == 13) {
  bot();																						// run bot function when enter key pressed
  questionNum++;																		// increase questionNum count by 1
}
});
