# MailGen
<h1>Motivation</h1>
This python script was created for a friend of mine. He was working for his sister's startup. His task was to read data from the company spreadsheet and then send personalized emails to all clients and respond to their queries. This took a lot of time. This repo solves the issue and now this python file automates the process once you run it on your shell. If implemented on a cloud, another feature can be added which will send the answer to client queries as soon as the customers put their request. <br><br><br>


<h1>Setup</h1>
<ol>
  <li>Go to the directory where-ever you wish and use git clone "......"</li>
  <li>Open command prompt or your terminal and use cd MailGen</li>
  <li>make sure you have python installed</li>
  <li>run: python -m venv ./venv</li>
  <li>run: venv\Scripts\activate</li>
  <li>Now that you have activated your virtual environment you can install the dependencies for this repository</li>
  <li>run: pip install -r requirements.txt</li>
  <li>Now you need to create a .env file. create a file named .env</li>
  <li>
  Now you need to add two environment variables to this file
  <ul>
    <li>SENDER_EMAIL = your email id  </li>
    <li>SENDGRID_API_KEY = sendgrid api key</li>
  </ul>
  </li>
  <li>Now you are ready to use the code. The jupyter notebook is merely for reference purpose and you can direcly use it to test your code</li>
  <li>You would have to edit the template.py file as per your need</li>

</ol>
